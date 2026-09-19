from __future__ import annotations
import json, math, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'tools/nollm_visual_toolkit'))
from nollm_visual_toolkit import multiplication_lab as lab


def spf_list(count:int):
    s=list(range(count)); s[0]=s[1]=0
    for p in range(2,math.isqrt(count-1)+1):
        if s[p]==p:
            for n in range(p*p,count,p):
                if s[n]==n:s[n]=p
    return s


def build_phase(N:int,bits:int,kind:str='inverse'):
    M=1<<bits; s=spf_list(N); ps=[p for p in range(2,N) if s[p]==p]
    if kind=='inverse':
        table={p:(M//8 if p==2 else pow(p,-1,M)) for p in ps}
    elif kind=='golden_rank':
        table={}
        for rank,p in enumerate(ps,1):
            a=rank*M; table[p]=((3*a-math.isqrt(5*a*a)-1)//2)%M
    elif kind=='golden_prime':
        table={}
        for p in ps:
            a=p*M; table[p]=((3*a-math.isqrt(5*a*a)-1)//2)%M
    else: raise ValueError(kind)
    phi=[None,0]+[0]*(N-2)
    for n in range(2,N):
        p=s[n]; phi[n]=(phi[n//p]+table[p])%M
    return phi,s,table


def metrics(phi,bits:int,bins:int=64,cells:bool=True):
    M=1<<bits; N=len(phi); counts=[0]*bins; cellmap={}
    for n in range(1,N): counts[phi[n]*bins//M]+=1
    mean=(N-1)/bins
    cv=math.sqrt(sum((x-mean)**2 for x in counts)/bins)/mean
    out={'N':N,'bits':bits,'M':M,'cv':cv,'iid_cv':math.sqrt((bins-1)/(N-1)),
         'cv_over_iid':cv/math.sqrt((bins-1)/(N-1)),'angular_counts':counts}
    if cells:
        for n in range(N):
            if n:
                a=2*math.pi*phi[n]/M; r=math.sqrt(n)
                cell=lab.rounded_hex(r*math.cos(a),r*math.sin(a))
            else: cell=(0,0)
            cellmap[cell]=cellmap.get(cell,0)+1
        out.update(occupied=len(cellmap),occupied_ratio=len(cellmap)/N,
                   collision_groups=sum(v>1 for v in cellmap.values()),
                   excess=N-len(cellmap),maxload=max(cellmap.values()))
    return out


def windows(phi,bits:int,block:int,bins:int=64):
    M=1<<bits;cvs=[]
    for lo in range(1,len(phi),block):
        hi=min(len(phi),lo+block); c=[0]*bins
        for n in range(lo,hi): c[phi[n]*bins//M]+=1
        mu=sum(c)/bins;cvs.append(math.sqrt(sum((x-mu)**2 for x in c)/bins)/mu)
    return {'block':block,'blocks':len(cvs),'min':min(cvs),'mean':sum(cvs)/len(cvs),'max':max(cvs),
            'iid_reference':math.sqrt((bins-1)/block)}


def main():
    base={}
    for kind in ('inverse','golden_rank','golden_prime'):
        phi,_,_=build_phase(65536,16,kind); base[kind]=metrics(phi,16)
    inv=build_phase(65536,16,'inverse')[0]
    base['inverse']['windows_4096']=windows(inv,16,4096)
    base['inverse']['distinct_ticks']=len(set(inv[1:]))

    scaling=[]
    for m in range(8,17):
        phi,_,_=build_phase(1<<m,m,'inverse'); x=metrics(phi,m); x.pop('angular_counts'); scaling.append(x)

    precision=[]
    for N in (4096,16384,65536,262144,1000001):
        predicted=math.ceil(math.log2(2*math.pi*math.sqrt(N)))
        for bits in range(max(6,predicted-2),predicted+3):
            phi,_,_=build_phase(N,bits,'inverse'); x=metrics(phi,bits); x.pop('angular_counts')
            x['predicted_bits']=predicted;x['outer_arc_spacing']=2*math.pi*math.sqrt(N)/(1<<bits);precision.append(x)

    phi13,_,_=build_phase(1000001,13,'inverse')
    million13=metrics(phi13,13); million13['windows_10000']=windows(phi13,13,10000)
    phi16,_,_=build_phase(1000001,16,'inverse'); million16=metrics(phi16,16)

    lifts=[]
    s16=spf_list(65536); primes16=[p for p in range(3,65536,2) if s16[p]==p]
    for m in range(8,16):
        M=1<<m; common=[p for p in primes16 if p<M]; b0=b1=bad=0
        for p in common:
            u=pow(p,-1,M); v=pow(p,-1,2*M)
            if v==u:b0+=1
            elif v==u+M:b1+=1
            else:bad+=1
        lifts.append({'m':m,'odd_primes':len(common),'b0':b0,'b1':b1,'failures':bad})

    lam=math.sqrt(3)/(2*math.pi); cells=2*math.pi*65536/math.sqrt(3)
    ref={'lambda':lam,'occupied_ratio':(1-math.exp(-lam))/lam,
         'occupied_cells':65536*(1-math.exp(-lam))/lam,
         'collision_groups':cells*(1-math.exp(-lam)*(1+lam))}
    result={'schema':'NOLLM_RECIPROCAL_PHASE_VERIFICATION_V1','status':'FINITE_NOT_THEOREM',
            'candidate':'a2=M/8; ap=inverse(p) mod M for odd primes','base':base,
            'power2_scaling':scaling,'precision_scan':precision,'million_bits13':million13,
            'million_bits16':million16,'inverse_lifts':lifts,'poisson_area_reference':ref}
    out=Path(__file__).with_name('results.json');out.write_text(json.dumps(result,indent=2)+'\n')
    assert all(x['failures']==0 for x in lifts)
    assert base['inverse']['cv'] < base['golden_prime']['cv'] < base['golden_rank']['cv']
    assert base['inverse']['occupied'] > base['golden_prime']['occupied'] > base['golden_rank']['occupied']
    assert million13['occupied_ratio'] > .87
    print(json.dumps({'PASS':True,'base_inverse_cv':base['inverse']['cv'],'base_inverse_occupied':base['inverse']['occupied'],
                      'million13_cv':million13['cv'],'million13_occupied_ratio':million13['occupied_ratio']},indent=2))

if __name__=='__main__':main()
