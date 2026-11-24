from t6_q11_split011_exact import *
def signed_search(pos,neg):
    cp=sum(P*(P*q+r)-1 for q,r in pos)
    cn=sum(P*(P*q+r)-1 for q,r in neg)
    if cn>CAP or cp>CAP:return True,0,[]
    radius=(CAP-cp)**2+(CAP-cn)**2;assert radius<dmin;bound=radius*Q
    c=[(sum(C[a][j] for a in neg)-sum(C[a][j] for a in pos))%B for j in range(N)];z=c[:];nodes=0;leaves=[]
    def descend(i,spent):
        nonlocal nodes
        if i<0:
            uu=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)]
            assert all(x%B==0 for x in uu);u=[x//B for x in uu]
            masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
            residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)]
            assert residues==[0]*6
            norm=sum((w*x)**2 for w,x in zip(W,u));assert norm<=radius and norm*Q==spent
            leaves.append(dict(pos=pos,neg=neg,u=u,masses=masses,residues=residues,norm_sq=norm,radius_sq=radius,budget_valid=max(masses)<=CAP));return
        nodes+=1;center=L[i]*c[i]+sum(a*b for a,b in zip(MM[i],z[i+1:]));den=B*L[i];near=(-center)//den
        for ni in (near,near+1):
            sp=spent+T[i]*(center+den*ni)**2
            if sp<=bound:
                z[i]=c[i]+B*ni;descend(i-1,sp)
        z[i]=c[i]
    descend(N-1,0);return False,nodes,leaves

# Full signed Cartesian roster, both positive partitions of 2.
rows=[];witnesses=[];start=time.perf_counter()
for length in (1,2):
    for negpat in patterns(9,length):
        for pospat in ((2,),(1,1)):
            raw=over=nodes=leaves=valid=common=0;digest=hashlib.sha256();wsall=[]
            for neg in rosters(negpat):
                for pos in rosters(pospat):
                    raw+=1;common+=bool(set(pos)&set(neg))
                    digest.update((repr((pos,neg))+'\n').encode('ascii'))
                    skip,nd,ws=signed_search(pos,neg);over+=skip;nodes+=nd;leaves+=len(ws);valid+=sum(w['budget_valid'] for w in ws);wsall.extend(ws)
            def count(pat):
                result=1
                for m in Counter(pat).values():result*=comb(11+m,m)
                return result
            assert raw==count(pospat)*count(negpat) and over==0
            # Inclusion-exclusion across disjoint residue sets: negative atoms of each q multiplicity.
            no_common=0
            for pos in rosters(pospat):
                avoid=1
                for q,m in Counter(negpat).items():
                    available=12-len({r for a,r in pos if a==q})
                    avoid*=comb(available+m-1,m)
                no_common+=avoid
            assert common==raw-no_common
            row=dict(pos_pattern=pospat,neg_pattern=negpat,raw=raw,over=over,common_included=common,search=raw-over,nodes=nodes,leaves=leaves,valid=valid,roster_sha256=digest.hexdigest(),witnesses=wsall);rows.append(row);print(json.dumps(row),flush=True)
out=dict(schema='T6_P13_Q11_SPLIT2_9_LEN1TO2_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',p=13,valuation=1,total_q=11,split=[2,9],budget=2331,negative_length_range=[1,2],positive_patterns=[[2],[1,1]],gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,rows=rows,totals={k:sum(r[k] for r in rows) for k in ('raw','over','common_included','search','nodes','leaves','valid')},elapsed_s=time.perf_counter()-start,status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
with open('/mnt/data/t6_q11_split29_len1to2.json','w') as f:json.dump(out,f,sort_keys=True,indent=2);f.write('\n')
print('RESULT',json.dumps(out['totals']),out['elapsed_s'],flush=True)
