from t6_q12_exact_init import *
import subprocess,pathlib
root=pathlib.Path(__file__).resolve().parent
assert B==13**6 and dmin>2*CAP**2 and all(abs(mu[j][i])<=F(1,2) for j in range(N) for i in range(j))
param=root/'t6_q12_split39_params.txt'
param.write_text('\n'.join([str(Q),*(' '.join(map(str,[L[i],T[i],*MM[i]])) for i in range(N)),*(' '.join(map(str,C[q,r])) for q in range(1,13) for r in range(1,13))])+'\n')
def run(length):
 rows=[]; start=time.perf_counter()
 for negpat in patterns(9,length):
  d={0:1}
  for m in Counter(negpat).values():
   g=Counter(sum(rs) for rs in combinations_with_replacement(range(1,P),m));h=Counter()
   for a,b in d.items():
    for t,n in g.items():h[a+t]+=b*n
   d=h
  for kind,pospat in enumerate(((3,),(1,2),(1,1,1))):
   saved=root/f't6_q12_split39_len{length}_row{len(rows)}.json'
   if saved.exists():
    row=json.loads(saved.read_text());assert tuple(row['pos_pattern'])==pospat and tuple(row['neg_pattern'])==negpat and len(row['witnesses'])==row['leaves'];row['origin']='RECOVERED_PERSISTED_ROW_NO_REPLAY';rows.append(row);print('RECOVERED',negpat,pospat,row['raw'],row['nodes'],row['leaves'],flush=True);continue
   pp=list(rosters(pospat));parts=[]
   for t in range(1,13):
    sp=root/f't6_q12_split39_len{length}_row{len(rows)}_shard{t}.txt'
    if sp.exists(): part=sp.read_text()
    else:
     part=subprocess.check_output([str(root/'t6_q12'),str(param),str(t),'9',*map(str,pospat),'--',*map(str,negpat)],text=True)
     assert part.splitlines()[-1].startswith('R '); assert sum(x.startswith('W ') for x in part.splitlines())==int(part.splitlines()[-1].split()[-1])
     tmp=sp.with_suffix('.tmp');tmp.write_text(part);tmp.replace(sp)
    parts.append(part)
   summary=[sum(int(x.splitlines()[-1].split()[i]) for x in parts) for i in range(1,6)];s='\n'.join(x for part in parts for x in part.splitlines() if x.startswith('W '))+'\nR '+' '.join(map(str,summary));origin='EXECUTED_THIS_CALL'
   ws=[];row=None
   for line in s.splitlines():
    if not line:continue
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
   rows.append(dict(pos_pattern=pospat,neg_pattern=negpat,raw=raw,over=over,common_included=common,search=raw-over,nodes=nodes,leaves=leaves,valid=sum(w['budget_valid'] for w in ws),witnesses=ws,shards=[list(map(int,part.splitlines()[-1].split()[1:])) for part in parts],origin=origin)); (root/f't6_q12_split39_len{length}_row{len(rows)-1}.json').write_text(json.dumps(rows[-1],sort_keys=True,indent=2)+'\n');print(negpat,pospat,row,origin,flush=True)
 out=dict(schema='T6_P13_Q12_SPLIT3_9_SHARDED_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',p=13,valuation=1,total_q=12,split=[3,9],budget=2331,negative_length=length,positive_patterns=[[3],[1,2],[1,1,1]],gs_min_sq=str(dmin),lattice_index='13^21',coset_denominator=B,rows=rows,totals={k:sum(r[k] for r in rows) for k in ('raw','over','common_included','search','nodes','leaves','valid')},elapsed_s=time.perf_counter()-start,hashes={p:hashlib.sha256((root/p).read_bytes()).hexdigest() for p in ('t6_q12_exact_init.py','t6_q12_generic_shard.cpp','replay.py')},status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
 (root/f't6_q12_split39_gmp_len{length}.json').write_text(json.dumps(out,sort_keys=True,indent=2)+'\n'); print('RESULT',length,out['totals'],out['elapsed_s'],flush=True)
if __name__=='__main__':
 for l in map(int,sys.argv[1:]):run(l)
