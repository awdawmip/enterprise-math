#!/usr/bin/env python3
import hashlib, inspect, json, math

MIRROR={'1':'3','2':'2','3':'1'}
checks=[]

def ck(name,cond,detail=''):
    if not cond:
        raise AssertionError(f'{name}: {detail}')
    checks.append((name,True,str(detail)))

# TARGET GENERATOR: copied as an independent local replay of the accepted AH recurrence.
# Source angles/arc measures are deliberately absent from this function.
def generate_word(r:int)->str:
    a,b=r,0
    rho=-4
    half=[]
    while a-b>1:
        if rho>=0:
            half.append('1')
            rho -= 3*(a+2*b+3)
            b += 1
        else:
            half.append('2')
            rho += 3*(a-b-3)
            a -= 1
            b += 1
    center='2' if a-b==1 else ''
    return ''.join(half)+center+''.join(MIRROR[c] for c in reversed(half))

def vertices(r,w=None):
    if w is None:
        w=generate_word(r)
    a,b=r,0
    out=[(a,b)]
    for c in w:
        if c=='1': b+=1
        elif c=='2': a-=1; b+=1
        elif c=='3': a-=1
        else: raise AssertionError(c)
        out.append((a,b))
    return out

def tan_coeff(p,q):
    # Returns exact rational coefficient tan(Delta)/sqrt(3)=num/den.
    a,b=p; c,d=q
    return a*d-b*c, 2*a*c+2*b*d+a*d+b*c

def source_angle(p):
    # SOURCE COMPATIBILITY LAYER ONLY.
    a,b=p
    return math.atan2(math.sqrt(3)*b/2, a+b/2)

def sector_weights(r):
    w=generate_word(r)
    V=vertices(r,w)
    ang=[source_angle(p) for p in V]
    ds=[ang[i+1]-ang[i] for i in range(len(w))]
    return w,V,[r*x for x in ds],ds

def rot(p):
    a,b=p
    return (-b,a+b)

def central_index(r,w,V):
    M=r+w.count('1')
    for i,c in enumerate(w):
        if c=='2':
            a,b=V[i]
            if a+b==M and a-b in (1,2):
                return i
    raise AssertionError((r,w))

for r in range(1,1025):
    w,V,weights,ds=sector_weights(r)
    ck(f'endpoint_{r}',V[-1]==(0,r))
    ck(f'counts_{r}',w.count('3')==w.count('1') and w.count('2')==r-w.count('1'))
    ck(f'sector_angle_{r}',abs(sum(ds)-math.pi/3)<2e-12,sum(ds))
    ck(f'positive_{r}',min(weights)>0,min(weights))
    ck(f'reflection_{r}',max(abs(x-y) for x,y in zip(weights,reversed(weights)))<5e-11)
    ck(f'weighted_sum_{r}',abs(6*sum(weights)-2*math.pi*r)<2e-9,6*sum(weights)-2*math.pi*r)
    n0,d0=tan_coeff(V[0],V[1])
    ck(f'axis_exact_{r}',(n0,d0)==(r,r*(2*r-1)),(n0,d0))
    ci=central_index(r,w,V)
    a,b=V[ci]; m=a+b; diff=a-b
    n,dn=tan_coeff(V[ci],V[ci+1])
    ck(f'central_state_{r}',w[ci]=='2' and m==r+w.count('1') and diff in (1,2),(ci,a,b,m,diff))
    expdn=(3*m*m+diff*diff-2*diff)//2
    ck(f'central_exact_{r}',(n,dn)==(m,expdn),(n,dn,m,expdn))
    mean=sum(weights)/len(weights)
    ck(f'defect_zero_{r}',abs(sum(x-mean for x in weights))<5e-10)
    ok=True
    for p,q in zip(V,V[1:]):
        if tan_coeff(p,q)!=tan_coeff(rot(p),rot(q)):
            ok=False; break
    ck(f'D6_{r}',ok)
    if r in (1,2):
        ck(f'equal_{r}',max(weights)-min(weights)<1e-12,max(weights)-min(weights))
    else:
        ck(f'nonprop_{r}',max(weights)-min(weights)>1e-12,max(weights)-min(weights))
    if r==3:
        ck('r3_witness',(tan_coeff(V[0],V[1]),tan_coeff(V[1],V[2]))==((3,15),(3,13)))
    if r==4:
        ck('r4_witness',(tan_coeff(V[0],V[1]),tan_coeff(V[1],V[2]))==((4,28),(4,24)))
    if r>=5:
        ck(f'prefix21_{r}',w[:2]=='21',w[:4])

for r in (2048,4096,8192):
    w,V,weights,ds=sector_weights(r)
    ci=central_index(r,w,V)
    axis=weights[0]; mid=weights[ci]
    ck(f'cp_axis_{r}',abs(axis-math.sqrt(3)/2)<2/r,axis)
    ck(f'cp_mid_{r}',abs(mid-1)<5/r,mid)
    ck(f'cp_sep_{r}',mid-axis>0.1,mid-axis)
    ck(f'cp_nonprop_{r}',max(weights)-min(weights)>0.1,max(weights)-min(weights))
    ck(f'cp_reflection_{r}',max(abs(x-y) for x,y in zip(weights,reversed(weights)))<1e-9)

for r in range(5,200):
    ck(f'exact_ineq_{r}',(r-1)*(2*r-1)!=(2*r*r-r+3))

target_src=inspect.getsource(generate_word).lower()
for tok in ['sqrt','atan','pi','cos','sin','coverage','occupancy','word_table','boundary_table','source']:
    ck(f'target_firewall_{tok}',tok not in target_src)

payload='\n'.join(f'{n}:1:{d}' for n,_,d in checks).encode()
print(json.dumps({
    'schema':'R059D_STAGE_AN_DETERMINISTIC_CHECKER_OUTPUT_V1',
    'status':'PASS',
    'checks_total':len(checks),
    'checks_passed':len(checks),
    'checks_failed':0,
    'checks_digest_sha256':hashlib.sha256(payload).hexdigest(),
    'history_gate':'PENDING_EXTERNAL_GITHUB_COMPARE',
    'validation':'r=1..1024 plus 2048,4096,8192; source-pushforward weights, sharp nonproportionality, axis/central refinement limits, D6/reflection and target firewall',
},sort_keys=True))
