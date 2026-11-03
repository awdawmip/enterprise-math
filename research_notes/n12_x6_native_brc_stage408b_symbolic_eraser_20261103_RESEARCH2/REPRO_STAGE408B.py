"""Stage408-B exact finite cross-check, standard-library integer arithmetic."""
from itertools import product
from collections import defaultdict,Counter,deque
from functools import lru_cache
import json
D=(1,-1)

def J(w): return tuple(Counter(zip(w,w[1:])).get(e,0) for e in product(D,repeat=2))
def O(p,q):return (len(p),len(q),sum(p),sum(q),J(p),J(q),sum(a==b for a,b in zip(p,q)))

def analyze(p,q,r,s,shield):
    if O(p,q)!=O(r,s):raise ValueError('not same observer')
    todo=deque([(p,q,r,s,0,0,0)])
    seen={(p,q,r,s,0,0,0)}
    checks=0
    while todo:
        p,q,r,s,pp,cc,run=todo.popleft()
        if run>=shield:continue
        for a,b in product(D,repeat=2):
            x,y=p+(a,),q+(b,);u,v=r+(a,),s+(b,)
            checks+=1
            if O(x,y)!=O(u,v):return False,len(seen),checks,'APP'
            t=(x,y,u,v,pp,cc,run+1)
            if t not in seen:seen.add(t);todo.append(t)
        if not pp:
            if bool(q)!=bool(s):return False,len(seen),checks,'POP-enabled'
            if q:
                x,y=p,q[:-1];u,v=r,s[:-1]
                checks+=1
                if O(x,y)!=O(u,v):return False,len(seen),checks,'POP'
                t=(x,y,u,v,1,cc,0)
                if t not in seen:seen.add(t);todo.append(t)
        if not cc:
            ep=len(p)>=2 and len(q)>=2 and p[-1]==-p[-2] and q[-1]==-q[-2]
            er=len(r)>=2 and len(s)>=2 and r[-1]==-r[-2] and s[-1]==-s[-2]
            if ep!=er:return False,len(seen),checks,'CAN-enabled'
            if ep:
                x,y=p[:-2],q[:-2];u,v=r[:-2],s[:-2]
                checks+=1
                if O(x,y)!=O(u,v):return False,len(seen),checks,'CAN'
                t=(x,y,u,v,pp,1,0)
                if t not in seen:seen.add(t);todo.append(t)
    return True,len(seen),checks,None

def canon(seq):
    axes={};n=1;out=[]
    for v in seq:
        axis=abs(v)
        if axis==1:out.append(v);continue
        if axis not in axes:
            n+=1;axes[axis]=(n, 1 if v>0 else -1)
        idx,first_sign=axes[axis]
        out.append(idx if (1 if v>0 else -1)==first_sign else -idx)
    return tuple(out)

@lru_cache(None)
def orbit_dp(k,slots):
    if not slots:return 1
    return (2+2*k)*orbit_dp(k,slots-1)+(orbit_dp(k+1,slots-1) if k<5 else 0)

def main():
    cases=[('fiber-01',(1,)*6,(1,1,-1,1,-1,1),(1,)*6,(1,-1,1,1,-1,1)),('fiber-02',(1,)*6,(1,1,-1,1,-1,1),(1,)*6,(1,-1,1,-1,1,1)),('fiber-03',(1,)*6,(1,-1,1,1,-1,1),(1,)*6,(1,-1,1,-1,1,1))]
    res=[]
    for name,p,q,r,s in cases:
        a=analyze(p,q,r,s,3);b=analyze(p,q,r,s,4)
        res.append({'case':name,'shield3':a,'shield4':b})
        assert a[0]==b[0]
    fibers=defaultdict(list)
    for n in range(0,5):
        words=list(product(D,repeat=n))
        for p in words:
            for q in words:fibers[O(p,q)].append((p,q))
    pairs=0;states3=states4=checks3=checks4=0;different=[]
    for f in fibers.values():
        for i in range(len(f)):
            for j in range(i+1,len(f)):
                pairs+=1
                p,q=f[i];r,s=f[j]
                t=analyze(p,q,r,s,3);u=analyze(p,q,r,s,4)
                states3+=t[1];states4+=u[1];checks3+=t[2];checks4+=u[2]
                if t[0]!=u[0]:different.append([p,q,r,s,t,u])
    assert not different
    full=tuple(i for i in range(-6,7) if i)
    orbit_exact={i:orbit_dp(0,2*i) for i in (1,2,3)}
    assert orbit_exact=={1:11,2:257,3:10298}
    for k in (1,2):
        assert len({canon(x) for x in product(full,repeat=2*k)})==orbit_exact[k]
    p=(1,)*6;q=(1,1,-1,1,-1,1);s=(1,-1,1,1,-1,1)
    conditional=analyze(p,q,p,s,2)
    assert conditional[0]
    print(json.dumps({'status':'STAGE408B_THREE_APP_SHIELD_FINITE_PASS','cases':res,'n_leq_4_observer_fibers':len(fibers),'paired_histories_checked':pairs,'states_shield3':states3,'states_shield4':states4,'transitions_shield3':checks3,'transitions_shield4':checks4,'mismatches':different,'old_action_bound':11,'new_action_bound':8,'old_APP_bound':9,'new_APP_bound':6,'one_axis_orbits':orbit_exact,'conditional_2_APP_fiber':conditional},sort_keys=True))
if __name__=='__main__':main()
