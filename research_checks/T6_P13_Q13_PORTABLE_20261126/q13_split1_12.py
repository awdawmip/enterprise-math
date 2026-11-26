#!/usr/bin/env python3
# Reuse the executed q13 initializer without executing its split(0,13) work.
import pathlib,hashlib
root=pathlib.Path(__file__).resolve().parent
source=root/'q13_split0_13.py'
assert hashlib.sha256(source.read_bytes()).hexdigest()=='5fabe0e6ae4f6e2961e09f6f77c4dcac790de9d4a4235ce76f3cf7d4df411f01'
exec(compile(source.read_text().split('start=time.perf_counter();rows=[]',1)[0],str(source),'exec'))
import sys

def search_signed(pos,neg,cp,cn,cnvec):
    radius=(CAP-cp)**2+(CAP-cn)**2;bound=Q*radius
    c=[(x-y)%B for x,y in zip(cnvec,C[pos[0]])];z=c.copy();nodes=0;witness=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
            residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)];assert residues==[0]*6
            norm=sum((w*x)**2 for w,x in zip(W,u));assert norm<=radius and all((a-b)%B==0 for a,b in zip(z,c));assert spent==Q*norm
            masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            witness.append(dict(pos=pos,neg=neg,z=z.copy(),u=u,residues=residues,norm_sq=norm,radius_sq=radius,masses=masses,budget_valid=max(masses)<=CAP));return
        nodes+=1
        h=L[i]*c[i]+sum(a*b for a,b in zip(MM[i],z[i+1:]));step=B*L[i];near=(-h)//step
        for n in (near,near+1):
            e=spent+T[i]*(h+step*n)**2
            if e<=bound:z[i]=c[i]+B*n;descend(i-1,e)
        z[i]=c[i]
    descend(N-1,0);return nodes,witness

def run(length):
    rows=[];start=time.perf_counter()
    for pat in patterns(12):
        if len(pat)!=length:continue
        limit=(CAP-169*12+length)//13
        nraw,n=count_dp(pat,limit);ws=[];nodes=0;seen=0;common_feasible=0
        counts=Counter(pat);m=counts.get(1,0)
        no_common=comb(10+m,m)
        for q,k in counts.items():
            if q!=1:no_common*=comb(11+k,k)
        common=12*(nraw-no_common)
        for neg in feasible(pat,limit):
            seen+=1;cn=sum(P*(P*q+r)-1 for q,r in neg);assert cn<=CAP
            cnvec=[sum(C[a][i] for a in neg)%B for i in range(N)]
            labels={r for q,r in neg if q==1};common_feasible+=len(labels)
            for s in range(1,13):
                pos=((1,s),);cp=P*(P+s)-1
                nn,ww=search_signed(pos,neg,cp,cn,cnvec);nodes+=nn;ws.extend(ww)
        assert seen==n
        row=dict(pos_pattern=[1],neg_pattern=pat,raw=12*nraw,over=12*(nraw-n),search=12*n,common_included=common,common_feasible=common_feasible,nodes=nodes,leaves=len(ws),valid=sum(w['budget_valid'] for w in ws),witnesses=ws)
        rows.append(row)
        print('ROW',pat,row['search'],nodes,row['leaves'],row['valid'],flush=True)
    totals={k:sum(r[k] for r in rows) for k in ('raw','over','search','common_included','common_feasible','nodes','leaves','valid')}
    out=dict(schema='T6_P13_Q13_SPLIT1_12_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',source_initializer_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),program_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),p=P,valuation=1,total_q=13,split=[1,12],budget=CAP,negative_length=length,gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,rows=rows,totals=totals,status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED',scope='Six mixed congruences and both independent budgets; H0 and lower prime completion not implied; no formal claim or protected progress.')
    (root/f'T6_P13_Q13_SPLIT1_12_LEN{length}_AUTHOR_EXACT_CERT_20261126.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print('RESULT',length,totals,'seconds',time.perf_counter()-start,flush=True)
if __name__=='__main__':
    for length in map(int,sys.argv[1:]):run(length)
