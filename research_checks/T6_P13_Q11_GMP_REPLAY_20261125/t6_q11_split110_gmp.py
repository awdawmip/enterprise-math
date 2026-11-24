from t6_q11_split011_exact import *
import subprocess,pathlib
root=pathlib.Path(__file__).resolve().parent
param=root/'t6_q11_gmp_params.txt'
param.write_text('\n'.join([str(Q),*( ' '.join(map(str,[L[i],T[i],*MM[i]])) for i in range(N)),*(' '.join(map(str,C[q,r])) for q in range(1,12) for r in range(1,13))])+'\n')
length,index=map(int,sys.argv[1:]);pat=list(patterns(10,length))[index]
start=time.perf_counter();s=subprocess.check_output([str(root/'t6_q11_split110_gmp'),str(param),*map(str,pat)],text=True);elapsed=time.perf_counter()-start
ws=[];row=None
for line in s.splitlines():
 v=list(map(int,line.split()[1:]))
 if line.startswith('R '):raw,over,common,nodes,leaves=v;row=(raw,over,common,nodes,leaves);continue
 pr=v[0];neg=list(zip(pat,v[1:1+length]));pos=[(1,pr)];z=v[1+length:];assert len(z)==N
 u0=[sum(z[j]*Urows[j][t] for j in range(N)) for t in range(N)];assert all(x%B==0 for x in u0);u=[x//B for x in u0]
 cp=sum(P*(P*q+r)-1 for q,r in pos);cn=sum(P*(P*q+r)-1 for q,r in neg)
 residues=[(sum(x*h for x,h in zip(u,H[k-1]))-sum(pow(P*q+r,-k,P**k) for q,r in neg)+sum(pow(P*q+r,-k,P**k) for q,r in pos))%(P**k) for k in range(1,7)];assert residues==[0]*6
 norm=sum((w*x)**2 for w,x in zip(W,u));radius=(CAP-cp)**2+(CAP-cn)**2;assert norm<=radius
 c=[(sum(C[a][j] for a in neg)-sum(C[a][j] for a in pos))%B for j in range(N)];assert all((a-b)%B==0 for a,b in zip(z,c))
 masses=[cp+sum(w*max(0,x) for w,x in zip(W,u)),cn+sum(w*max(0,-x) for w,x in zip(W,u))]
 ws.append(dict(pos=pos,neg=neg,u=u,masses=masses,residues=residues,norm_sq=norm,radius_sq=radius,budget_valid=max(masses)<=CAP))
assert row is not None and leaves==len(ws)
expected=12;d={0:1}
for m in Counter(pat).values():
 expected*=comb(11+m,m);g=Counter(sum(rs) for rs in combinations_with_replacement(range(1,P),m));h=Counter()
 for a,b in d.items():
  for t,n in g.items():h[a+t]+=b*n
 d=h
assert raw==expected and over==12*sum(n for t,n in d.items() if 1690+13*t-length>CAP)
m=pat.count(1);assert common==expected*m//(11+m)
valid=sum(w['budget_valid'] for w in ws)
out=dict(schema='T6_P13_Q11_SPLIT1_10_GMP_AUTHOR_EXACT_INTEGER_V1',frozen_science='d84bd940cfb093cdc60e569f15cad58772a51dca',p=13,valuation=1,total_q=11,split=[1,10],budget=2331,length=length,index=index,pattern=pat,raw=raw,over=over,common_included=common,search=raw-over,nodes=nodes,leaves=leaves,valid=valid,witnesses=ws,elapsed_s=elapsed,gs_min_sq=str(dmin),coset_denominator=B,lattice_index='13^21',kernel_sha256=hashlib.sha256((root/'t6_q11_split011_exact.py').read_bytes()).hexdigest(),cpp_sha256=hashlib.sha256((root/'t6_q11_split110_gmp.cpp').read_bytes()).hexdigest(),wrapper_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),status='AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED')
path=root/f't6_q11_split110_gmp_len{length}_{index}.json';path.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n');print(json.dumps(out,separators=(',',':')),flush=True)
