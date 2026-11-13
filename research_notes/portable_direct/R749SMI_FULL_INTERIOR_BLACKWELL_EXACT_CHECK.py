from fractions import Fraction as Q
from itertools import product
import json
S=list(product((1,-1),repeat=3))
G=[Q(-1),Q(-1,2),Q(0),Q(1,2),Q(1)]
def F(z,o,a,b,c):
 x,y,t=z;u,v,w=o
 return (2+a*u*x)*(2+b*v*(y if u==1 else t))*(2+c*w*y*t)/Q(64)
def P(z,o,a,b,c):
 x,y,t=z;u,v,w=o
 return (2+c*w*y*t)*sum((2+i*x)*(1+a*u*i)*(2+b*v*(y if i==1 else t)) for i in (1,-1))/Q(128)
def prior(z,k):
 x,y,t=z
 return (1+[Q(y,2),Q(t,2),Q(x*(y-t),4),-Q(x*(y-t),4)][k])/8
def mix(K,k,a,b,c):
 return [sum(prior(z,k)*K(z,o,a,b,c) for z in S) for o in S]
def TV(x,y):return sum(abs(v-w) for v,w in zip(x,y))/2
def run():
 for k in range(4):
  p=[prior(z,k) for z in S]
  assert sum(p)==1 and min(p)>=Q(1,16)
 n=0
 for a,b,c in product(G,repeat=3):
  for K in (F,P):
   for z in S:
    v=[K(z,o,a,b,c) for o in S]
    assert min(v)>=0 and sum(v)==1
  vals=(TV(mix(F,0,a,b,c),mix(F,1,a,b,c)),TV(mix(P,0,a,b,c),mix(P,1,a,b,c)),TV(mix(F,2,a,b,c),mix(F,3,a,b,c)),TV(mix(P,2,a,b,c),mix(P,3,a,b,c)))
  assert vals==(abs(b)/8,abs(a*b)/8,abs(a*b)/16,abs(b)/16)
  n+=1
 return {"status":"PASS","parameter_triples":n,"state_columns_per_kernel":n*8,"arithmetic":"Fraction","claim":"exact four TV identities and stochastic kernels"}
if __name__=="__main__":print(json.dumps(run(),indent=2))
