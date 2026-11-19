from math import log,sqrt
from scipy.integrate import quad
from explore_rectangle import kernel2,kernel3

def k2direct(A,R,S):
 D=A/(R*S); h=1-D
 # y permutation 0,s,1; 1,s,0; then four product cases with reparameterization.
 p1=2*h*(1-(R+S)/2)
 p6=quad(lambda t: 1-(max(R,S)-t*R-(h-t)*S)/2,0,h)[0]*2
 p2=quad(lambda t:(1-max(t*R+S,R+h*S/t)/2)/t,h,1,epsabs=1e-12)[0]
 p5=quad(lambda t:(1-(max(S,R+(1-h/t)*S)-min(S,t*R))/2)/t,h,1,epsabs=1e-12)[0]
 return p1+p6+2*p2+2*p5

def k3direct(A,R,S):
 D=A/(R*S); h=1-D; e=2*D-1
 pp=2*h*(1-(R+S)/2)
 mm=2*quad(lambda u: 1-(abs(R*(u+D)-S*u)+abs(R*(1-u-D)-S*(1-u)))/2,0,h)[0]
 pm=quad(lambda x: (1-(abs(R*(1+x)/2-S*(1-e/x)/2)+R*(1-x)/2+S*(1+e/x)/2)/2)/(2*x),e,1)[0]
 pm+=quad(lambda x: (1-(abs(R*(1-x)/2-S*(1+e/x)/2)+R*(1+x)/2+S*(1-e/x)/2)/2)/(2*x),e,1)[0]
 return pp+mm+2*pm

for A in [.52,2/3,.8,.98]:
 for R,S in [(.95,.9),(.95,.8),(.99,.99),(.81,.95),(.999,.7)]:
  if R*S>A:
   z=R+S;d=abs(R-S)
   print(A,R,S, k2direct(A,R,S)-kernel2(A,z,d), k3direct(A,R,S)-kernel3(A,z,d))
