from run import *
from itertools import combinations_with_replacement,product
from concurrent.futures import ThreadPoolExecutor

def verify(pp,np,pl,nl,z):
 pos=tuple(zip(pp,pl));neg=tuple(zip(np,nl));assert len(z)==N
 u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
 cp=sum(P*(P*q+r)-1 for q,r in pos);cn=sum(P*(P*q+r)-1 for q,r in neg)
 if max(cp,cn)>CAP:return None
 norm=sum((w*x)**2 for w,x in zip(W,u));radius=(CAP-cp)**2+(CAP-cn)**2
 if norm>radius:return None
 residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)];assert residues==[0]*6
 c=[(sum(C[a][j] for a in neg)-sum(C[a][j] for a in pos))%B for j in range(N)];assert all((a-b)%B==0 for a,b in zip(z,c))
 masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
 return dict(pos=pos,neg=neg,z=z,u=u,residues=residues,norm_sq=norm,radius_sq=radius,masses=masses,budget_valid=max(masses)<=CAP)

def run_fiber(pp,np,lo,hi):
 path=root/('fiber_' +'_'.join(map(str,pp))+'__'+'_'.join(map(str,np))+f'_range{lo}_{hi}.json')
 if path.exists():return json.loads(path.read_text())
 p_raw,p_count=count_dp(pp,(CAP-169*sum(pp)+len(pp))//13);n_raw,n_count=count_dp(np,(CAP-169*sum(np)+len(np))//13)
 ps=list(feasible(pp,(CAP-169*sum(pp)+len(pp))//13));ns=list(feasible(np,(CAP-169*sum(np)+len(np))//13));assert (len(ps),len(ns))==(p_count,n_count)
 assert 0<=lo<=hi<=n_count; full_n_count=n_count; ns=ns[lo:hi]; n_count=len(ns)
 sets=Counter(frozenset(a) for a in ps);common=sum(n*sum(bool(p.intersection(a)) for a in ns) for p,n in sets.items())
 sets_non1=Counter(frozenset(a for a in p if a[1]!=1) for p in ps)
 reps=p_count*n_count-sum(n*sum(bool(p.intersection(a)) for a in ns) for p,n in sets_non1.items())
 ls=subprocess.check_output([str(root/'exact_fiber_shard'),str(params),str(lo),str(hi),*map(str,pp),'--',*map(str,np)],text=True).splitlines()
 a,b,search,cf,nodes,leaves,nrep=map(int,ls[-1].split()[1:]);assert (a,b,search,cf,nrep)==(p_count,n_count,p_count*n_count,common,reps) and len(ls)==leaves+1
 ws=[];seen=set();rep_witness=[]
 for line in ls[:-1]:
  assert line.startswith('W ');v=list(map(int,line.split()[1:]));pl=v[:len(pp)];nl=v[len(pp):len(pp)+len(np)];z=v[len(pp)+len(np):]
  w=verify(pp,np,pl,nl,z);assert w is not None
  p,n=Counter(w['pos']),Counter(w['neg']);j=p&n;assert all(t==1 for a,t in j)
  pd=p-j;nd=n-j;orders=sorted(Counter({a:k for (a,t),k in j.items()}).items())
  k=0
  for assignment in product(*(combinations_with_replacement(range(1,13),m) for a,m in orders)):
   common_atoms=Counter((a,t) for (a,m),ts in zip(orders,assignment) for t in ts)
   newp=tuple(sorted((pd+common_atoms).elements()));newn=tuple(sorted((nd+common_atoms).elements()));assert (tuple(a for a,t in newp),tuple(a for a,t in newn))==(pp,np)
   w2=verify(pp,np,[t for a,t in newp],[t for a,t in newn],z)
   if w2 is None:continue
   key=(newp,newn,tuple(z));assert key not in seen;seen.add(key);ws.append(w2);k+=1
  assert k>=1;rep_witness.append({'pos':w['pos'],'neg':w['neg'],'u':w['u'],'fiber_size':k})
 row=dict(pos_pattern=pp,neg_pattern=np,full_raw=p_raw*n_raw,full_feasible=p_count*full_n_count,negative_roster_count=full_n_count,negative_roster_range=[lo,hi],search_domain=search,common_feasible=common,representative_search=reps,nodes=nodes,representative_leaves=leaves,leaves=len(ws),valid=sum(w['budget_valid'] for w in ws),witnesses=ws,rep_witness=rep_witness)
 tmp=path.with_suffix('.tmp');tmp.write_text(json.dumps(row,separators=(',',':'))+'\n');tmp.replace(path);print('FIBER',pp,np,search,reps,nodes,leaves,len(ws),row['valid'],flush=True);return row

if __name__=='__main__':
 lo,hi=map(int,sys.argv[1:3]); pp=tuple(map(int,sys.argv[3:])); np=(1,1,1,1,2,4)
 run_fiber(pp,np,lo,hi)
