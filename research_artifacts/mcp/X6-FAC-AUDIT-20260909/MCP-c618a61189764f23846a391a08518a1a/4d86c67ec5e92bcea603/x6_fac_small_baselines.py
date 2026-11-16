import json, math
from sympy import primerange

def fermat(N):
    a=math.isqrt(N)
    if a*a<N:a+=1
    tests=0
    while True:
        delta=a*a-N; tests+=1
        b=math.isqrt(delta)
        if b*b==delta:
            p=a-b; q=a+b
            assert p*q==N
            return {'sqrt_tests':tests,'factors':[p,q]}
        a+=1

def rho(N):
    # Deterministic Floyd x^2+1 with x0=y0=2; may cycle trivially.
    x=2;y=2;mods=0;gcds=0
    for k in range(1,100000):
        x=(x*x+1)%N;mods+=1
        y=(y*y+1)%N;mods+=1
        y=(y*y+1)%N;mods+=1
        g=math.gcd(abs(x-y),N);gcds+=1
        if 1<g<N:return {'success':True,'modular_squares':mods,'gcd_calls':gcds,'found_factor':g}
        if g==N:return {'success':False,'modular_squares':mods,'gcd_calls':gcds,'failure_reason':'CYCLE_EQUALS_N'}
    return {'success':False,'modular_squares':mods,'gcd_calls':gcds,'failure_reason':'BUDGET'}

ns=[]
for p in (11,13,17,19):
 for g in (6,12,18,24):
  q=next(primerange(p+g,p+g+100));N=p*q
  ns.append({'N':N,'p':p,'q':q,'gap':q-p,'fermat':fermat(N),'rho':rho(N)})
with open('/mnt/data/x6_fac_small_baselines.json','w') as f:json.dump(ns,f,indent=2);f.write('\n')
print('cases',len(ns),'rho successes',sum(a['rho']['success'] for a in ns),'fermat median sqrt tests', sorted(a['fermat']['sqrt_tests'] for a in ns)[8], 'rho median squares', sorted(a['rho']['modular_squares'] for a in ns)[8]); print(ns[:3])
