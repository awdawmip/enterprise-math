from t6_q11_split011_exact import *
import subprocess,pathlib
root=pathlib.Path(__file__).resolve().parent
assert B==13**6 and dmin>2*CAP**2 and all(abs(mu[j][i])<=F(1,2) for j in range(N) for i in range(j))
param=root/'t6_q11_split29_params.txt'
param.write_text('\n'.join([str(Q),*(' '.join(map(str,[L[i],T[i],*MM[i]])) for i in range(N)),*(' '.join(map(str,C[q,r])) for q in range(1,12) for r in range(1,13))])+'\n')
def run(length):
 rows=[]; start=time.perf_counter()
 for negpat in patterns(9,length):
  d={0:1}
  for m in Counter(negpat).values():
   g=Counter(sum(rs) for rs in combinations_with_replacement(range(1,P),m));h=Counter()
   for a,b in d.items():
    for t,n in g.items():h[a+t]+=b*n
   d=h
  for kind,pospat in enumerate(((2,),(1,1))):
   pp=list(rosters(pospat));s=subprocess.check_output([str(root/'t6_q11_split29_gmp'),str(param),str(kind),*map(str,negpat)],text=True);ws=[];row=None
   for line in s.splitlines():
    v=list(map(int,line.split()[1:]))
    if line.startswith('R '):raw,over,common,nodes,leaves=v;row=v;continue
    pos=pp[v[0]];neg=list(zip(negpat,v[1:1+length]));z=v[1+length:];assert len(z)==N
    u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
    cp=sum(P*(P*q+r)-1 for q,r in pos);cn=sum(P*(P*q+r)-1 for q,r in neg)
    residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)];assert residues==[0]*6
    norm=sum((w*x)**2 for w,x in zip(W,u));radius=(CAP-cp)**2+(CAP-cn)**2;assert norm<=radius
    c=[(sum(C[a][j] for a in neg)-sum(C[a][j] for a in pos))%B for j in range(N)];assert all((a-b)%B==0 for a,b in zip(z,c))
    masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
    ws.append(dict(pos=pos,neg=neg,u=u,masses=masses,residues=residues,norm_sq=norm,radius_sq=radius,budget_valid=max(masses)<=CAP))
   assert row is not None and len(ws)==leaves
   assert raw==len(pp)*sum(d.values()) and over==len(pp)*sum(n for t,n in d.items() if 1521+13*t-length>CAP)
   no_common=0
   for pos in pp:
    a=1
    for q,m in Counter(negpat).items():a*=comb(11-len({r for k,r in pos if k==q})+m,m)
    no_common+=a
   assert common==raw-no_common
   rows.append(dict(pos_pattern=pospat,neg_pattern=negpat,raw=raw,over=over,common_included=common,search=raw-over,nodes=nodes,leaves=leaves,valid=sum(w['budget_valid'] for w in ws),witnesses=ws));print(negpat,pospat,row,flush=True)
 out=dict(schema='T6_P13_Q11_SPLIT2_9_GMP_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',p=13,valuation=1,total_q=11,split=[2,9],budget=2331,negative_length=length,positive_patterns=[[2],[1,1]],gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,rows=rows,totals={k:sum(r[k] for r in rows) for k in ('raw','over','common_included','search','nodes','leaves','valid')},elapsed_s=time.perf_counter()-start,hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in ('t6_q11_split011_exact.py','t6_q11_split29_gmp.cpp','t6_q11_split29_gmp.py')},status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
 (root/f't6_q11_split29_gmp_len{length}.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n'); print('RESULT',length,out['totals'],out['elapsed_s'],flush=True)
if __name__=='__main__':
 for l in map(int,sys.argv[1:]):run(l)
