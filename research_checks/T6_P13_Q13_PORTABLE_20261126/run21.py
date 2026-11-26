from run_exact import *
from concurrent.futures import ThreadPoolExecutor

def run21(pp,np):
    p_raw,p_count=count_dp(pp,(CAP-169*2+len(pp))//13)
    n_raw,n_count=count_dp(np,(CAP-169*11+len(np))//13)
    ps=list(feasible(pp,(CAP-169*2+len(pp))//13));ns=list(feasible(np,(CAP-169*11+len(np))//13));assert (len(ps),len(ns))==(p_count,n_count)
    # Independent histogram of the shared atoms; pair counts from grouped multiset DP.
    sets=Counter(frozenset(a) for a in ps)
    common=sum(n*sum(bool(p.intersection(a)) for a in ns) for p,n in sets.items())
    ls=subprocess.check_output([str(root/'exact21'),str(params),*map(str,pp),'--',*map(str,np)],text=True).splitlines()
    a,b,search,cf,nodes,leaves=map(int,ls[-1].split()[1:]);assert ls[-1].startswith('R ') and (a,b,search,cf)==(p_count,n_count,p_count*n_count,common) and len(ls)==leaves+1
    ws=[]
    for line in ls[:-1]:
        assert line.startswith('W ');v=list(map(int,line.split()[1:]));pos=tuple(zip(pp,v[:len(pp)]));neg=tuple(zip(np,v[len(pp):len(pp)+len(np)]));z=v[len(pp)+len(np):];assert len(z)==N
        u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
        cp=sum(P*(P*q+r)-1 for q,r in pos);cn=sum(P*(P*q+r)-1 for q,r in neg);assert max(cp,cn)<=CAP
        residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)];assert residues==[0]*6
        norm=sum((w*x)**2 for w,x in zip(W,u));radius=(CAP-cp)**2+(CAP-cn)**2;assert norm<=radius
        c=[(sum(C[a][j] for a in neg)-sum(C[a][j] for a in pos))%B for j in range(N)];assert all((a-b)%B==0 for a,b in zip(z,c))
        masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
        ws.append(dict(pos=pos,neg=neg,z=z,u=u,residues=residues,norm_sq=norm,radius_sq=radius,masses=masses,budget_valid=max(masses)<=CAP))
    row=dict(pos_pattern=pp,neg_pattern=np,raw=p_raw*n_raw,over=p_raw*n_raw-search,search=search,common_feasible=common,nodes=nodes,leaves=leaves,valid=sum(w['budget_valid'] for w in ws),witnesses=ws)
    path=root/('split21_'+'_'.join(map(str,pp))+'__'+'_'.join(map(str,np))+'.json');tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(row,separators=(',',':'))+'\n');tmp.replace(path)
    print('ROW',pp,np,search,nodes,leaves,row['valid'],flush=True);return row
if __name__=='__main__':
    lengths=list(map(int,sys.argv[1:])) or [1,2,3]
    jobs=[(pp,np) for l in lengths for np in patterns(11) if len(np)==l for pp in patterns(2)]
    with ThreadPoolExecutor(max_workers=4) as pool:rows=list(pool.map(lambda v:run21(*v),jobs))
    keys=('raw','over','search','common_feasible','nodes','leaves','valid');totals={k:sum(r[k] for r in rows) for k in keys}
    out=dict(schema='T6_P13_Q13_SPLIT2_11_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',source_initializer_blob='1097ff3a84242ea2c9347912697205f9681d8448',prior_driver_blob='32dd6b472cc6936505eb6b5e7e849e72e18690dd',p=P,valuation=1,total_q=13,split=[2,11],budget=CAP,negative_lengths=lengths,gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,rows=rows,totals=totals,program_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),kernel_sha256=hashlib.sha256((root/'exact21.cpp').read_bytes()).hexdigest(),status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED',scope='Six mixed congruences and both independent budgets; H0 and lower prime completion not implied; no formal claim or protected progress.')
    (root/'T6_P13_Q13_SPLIT2_11_LEN1_3_CERT.json').write_text(json.dumps(out,separators=(',',':'))+'\n');print('TOTAL',totals,flush=True)
