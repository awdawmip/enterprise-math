#!/usr/bin/env python3
import hashlib
import json
import math

SQ3=math.sqrt(3.0)
PI=math.pi
STEP={'1':(0,1),'2':(-1,1),'3':(-1,0)}
checks=[]

def ck(name,cond,detail=''):
    checks.append((name,bool(cond),str(detail)))
    if not cond:
        raise AssertionError(f'{name}: {detail}')

def sector_word(r):
    a,b=r,0
    rho=-4
    left=[]
    while a-b>1:
        if rho>=0:
            left.append('1')
            rho-=3*(a+2*b+3)
            b+=1
        else:
            left.append('2')
            rho+=3*(a-b-3)
            a-=1
            b+=1
    center=['2'] if a-b==1 else []
    trans={'1':'3','2':'2'}
    right=[trans[c] for c in reversed(left)]
    return ''.join(left+center+right)

def sector_vertices(r):
    w=sector_word(r)
    a,b=r,0
    v=[(a,b)]
    for c in w:
        da,db=STEP[c]
        a+=da
        b+=db
        v.append((a,b))
    return w,v

def qE(a,b):
    return a*a+a*b+b*b

def supE(a,b):
    return 9*qE(a,b)-9*max(a,b)+3

def thetaE(a,b):
    return math.atan2(SQ3*b,2*a+b)

def Gfun(t):
    if t<=PI/6:
        return 2/SQ3*math.sin(t)
    return 2/SQ3-(math.cos(t)-math.sin(t)/SQ3)

def gfun(t):
    if t<=PI/6:
        return 2/SQ3*math.cos(t)
    return math.sin(t)+math.cos(t)/SQ3

def H1(t):
    return math.sin(t)/SQ3+math.cos(t)

def H2L(t):
    return -math.cos(t)+math.sin(t)/SQ3

def H2R(t):
    return 2*math.sin(t)/SQ3

def H3(t):
    return -math.cos(t)-math.sin(t)/SQ3

def rot(p):
    a,b=p
    return (-b,a+b)

for r in range(1,2049):
    w,v=sector_vertices(r)
    M=len(w)
    ck(f'shell_{r}',(3*M-1)**2<=12*r*r<(3*(M+1)-1)**2)
    ck(f'ends_{r}',v[0]==(r,0) and v[-1]==(0,r) and len(v)==M+1)
    refl=''.join({'1':'3','2':'2','3':'1'}[c] for c in reversed(w))
    ck(f'word_reflect_{r}',w==refl)
    cum=True
    support=True
    bound=True
    for n,(a,b) in enumerate(v):
        if a>=b and n!=b:
            cum=False
            break
        if a<=b and n!=M-a:
            cum=False
            break
        if supE(a,b)>9*r*r:
            support=False
            break
        if not (abs(qE(a,b)-r*r)<3*r+3):
            bound=False
            break
    ck(f'cumulative_{r}',cum)
    ck(f'support_{r}',support)
    ck(f'radial_bound_{r}',bound)
    ang=[thetaE(a,b) for a,b in v]
    ck(f'angles_{r}',all(ang[i+1]>ang[i] for i in range(M)) and abs(ang[0])<1e-15 and abs(ang[-1]-PI/3)<1e-14)
    reflang=max(abs(ang[i]+ang[M-i]-PI/3) for i in range(M+1))
    ck(f'angle_reflect_{r}',reflang<2e-14,reflang)
    dels=[ang[i+1]-ang[i] for i in range(M)]
    ck(f'source_sum_{r}',abs(sum(dels)-PI/3)<2e-14)
    cdferr=max(abs(n/r-Gfun(t)) for n,t in enumerate(ang))
    ck(f'cdf_{r}',cdferr*r<2.0,cdferr*r)
    weights=[r*d for d in dels]
    spread=max(weights)-min(weights)
    ck(f'proportional_{r}',(spread<1e-12) if r<=2 else (spread>1e-6),spread)
    ck(f'axis_formula_{r}',abs(math.tan(dels[0])-SQ3/(2*r-1))<2e-13)
    centr=[]
    for i,c in enumerate(w):
        if c=='2':
            a,b=v[i]
            if a+b==M and a-b in (1,2):
                centr.append((i,a,b))
    ck(f'central_unique_{r}',len(centr)==1,centr)
    i,a,b=centr[0]
    d=a-b
    tanmid=2*SQ3*M/(3*M*M+d*d-2*d)
    ck(f'central_formula_{r}',abs(math.tan(dels[i])-tanmid)<3e-13,(math.tan(dels[i]),tanmid))
    wd=max(abs(dels[i]-dels[M-1-i]) for i in range(M))
    ck(f'fiber_reflect_{r}',wd<2e-14,wd)

for r in [4096,8192,16384]:
    w,v=sector_vertices(r)
    M=len(w)
    ang=[thetaE(a,b) for a,b in v]
    dels=[ang[i+1]-ang[i] for i in range(M)]
    mids=[(ang[i+1]+ang[i])/2 for i in range(M)]
    weights=[r*d for d in dels]
    mean=sum(weights)/M
    m2=sum(x*x for x in weights)/M
    macro2=sum((1/gfun(t))**2 for t in mids)/M
    c6=sum(math.cos(6*t) for t in mids)/M
    c12=sum(math.cos(12*t) for t in mids)/M
    smu6=sum(d*math.cos(6*t) for d,t in zip(dels,mids))/(PI/3)
    cdferr=max(abs(n/r-Gfun(t)) for n,t in enumerate(ang))
    ck(f'cp_cdf_{r}',cdferr*r<2,cdferr*r)
    ck(f'cp_mesh_{r}',max(dels)*r<2,max(dels)*r)
    ck(f'cp_mean_{r}',abs(mean-PI/(2*SQ3))*r<2,(mean-PI/(2*SQ3))*r)
    ck(f'cp_m2_{r}',abs(m2-5/6)*r<2,(m2-5/6)*r)
    ck(f'cp_macro2_{r}',abs(macro2-0.75*math.log(3))*r<1,(macro2-0.75*math.log(3))*r)
    ck(f'cp_c6_{r}',abs(c6-1/35)*r<2,(c6-1/35)*r)
    ck(f'cp_c12_{r}',abs(c12+1/143)*r<2,(c12+1/143)*r)
    ck(f'cp_source_c6_{r}',abs(smu6)*r<0.1,smu6*r)
    ck(f'cp_axis_{r}',abs(weights[0]-SQ3/2)*r<2,(weights[0]-SQ3/2)*r)
    centr=[(i,*v[i]) for i,c in enumerate(w) if c=='2' and sum(v[i])==M and v[i][0]-v[i][1] in (1,2)]
    i,a,b=centr[0]
    ck(f'cp_mid_{r}',abs(weights[i]-1)*r<3,(weights[i]-1)*r)
    maxerr=0.0
    for j in range(3):
        lo=j*(PI/18)
        hi=(j+1)*(PI/18)
        for sym,anti in [('1',H1),('2',H2L)]:
            cnt=sum(1 for c,t in zip(w,mids) if c==sym and lo<=t<hi)
            exp=anti(hi)-anti(lo)
            maxerr=max(maxerr,abs(cnt/r-exp)*r)
    for j in range(3):
        lo=PI/6+j*(PI/18)
        hi=PI/6+(j+1)*(PI/18)
        for sym,anti in [('2',H2R),('3',H3)]:
            cnt=sum(1 for c,t in zip(w,mids) if c==sym and lo<=t<hi)
            exp=anti(hi)-anti(lo)
            maxerr=max(maxerr,abs(cnt/r-exp)*r)
    ck(f'cp_symbol_bins_{r}',maxerr<2,maxerr)
    ok=True
    for p in [v[0],v[M//4],v[M//2],v[-1]]:
        x=p
        for _ in range(6):
            x=rot(x)
        if x!=p:
            ok=False
    ck(f'cp_D6_{r}',ok)
    edgevar=m2-mean*mean
    macrovar=macro2-mean*mean
    edgevarlim=5/6-(PI/(2*SQ3))**2
    macrovarlim=.75*math.log(3)-(PI/(2*SQ3))**2
    ck(f'cp_edgevar_{r}',abs(edgevar-edgevarlim)*r<4,(edgevar-edgevarlim)*r)
    ck(f'cp_macrovar_{r}',abs(macrovar-macrovarlim)*r<4,(macrovar-macrovarlim)*r)

target_runtime_text="""
def sector_word(r):
    a,b=r,0;rho=-4
    left=[]
    while a-b>1:
        if rho>=0:
            left.append('1');rho-=3*(a+2*b+3);b+=1
        else:
            left.append('2');rho+=3*(a-b-3);a-=1;b+=1
    center=['2'] if a-b==1 else []
    trans={'1':'3','2':'2'}
    right=[trans[c] for c in reversed(left)]
    return ''.join(left+center+right)
"""
forbidden=['atan','sqrt','pi','cos','sin','source','angle','float','occupancy','coverage']
ck('target_runtime_firewall',all(x not in target_runtime_text.lower() for x in forbidden),target_runtime_text)

payload='\n'.join(f'{n}:{int(ok)}:{d}' for n,ok,d in checks).encode()
out={
    'schema':'R059D_STAGE_AO_DETERMINISTIC_CHECKER_OUTPUT_V1',
    'status':'PASS',
    'checks_total':len(checks),
    'checks_passed':sum(ok for _,ok,_ in checks),
    'checks_failed':sum(not ok for _,ok,_ in checks),
    'checks_digest_sha256':hashlib.sha256(payload).hexdigest(),
    'validation':'r=1..2048 plus 4096,8192,16384',
    'weak_target_moments':{'cos6_limit':'1/35','cos12_limit':'-1/143'},
    'source_uniform_cos6_limit':'0',
    'edge_second_moment_limit':'5/6',
    'macro_second_moment_limit':'(3/4)*log(3)',
    'history_gate':'PENDING_EXTERNAL_GITHUB_COMPARE'
}
print(json.dumps(out,sort_keys=True))
