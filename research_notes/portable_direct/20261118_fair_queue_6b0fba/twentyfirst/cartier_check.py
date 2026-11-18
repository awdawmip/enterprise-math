"""Cartier coefficients of the homogeneous ordered shear-word BRC, modulo p^k."""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
from math import comb
import sys

PIN='7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'
ONE={(0,0):1}
X={(1,0):1};Y={(0,1):1}


def import_core(repo):
    path=repo/'src/enterprise_math/brc_weighted_recurrent.py'
    assert hashlib.sha256(path.read_bytes()).hexdigest()==PIN
    spec=importlib.util.spec_from_file_location('cartier_frozen_core',path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module.recurrent_mass_power


class Residues:
    def __init__(self,core,m):
        self.m=m;self.plus=[[0]*m for _ in range(m)];self.times=[[0]*m for _ in range(m)]
        trace=hashlib.sha256()
        for a in range(m):
            for b in range(m):
                # Two independently labelled positive paths add; one two-edge path multiplies.
                gs=([0,a,b,0],[0,0,0,1],[0,0,0,1],[0,0,0,0])
                gp=([0,a,0],[0,0,b],[0,0,0])
                z=core(gs,2)[0][3];w=core(gp,2)[0][2]
                assert z.denominator==w.denominator==1
                self.plus[a][b]=z.numerator%m;self.times[a][b]=w.numerator%m
                trace.update(f'{a},{b},{z},{w};'.encode())
        self.ledger=trace.hexdigest()

    def add(self,*polys):
        out={}
        for poly in polys:
            for j,v in poly.items():out[j]=self.plus[out.get(j,0)][v]
        return {j:v for j,v in out.items() if v}

    def scale(self,c,poly):
        return {j:w for j,v in poly.items() if (w:=self.times[c%self.m][v])}

    def mul(self,P,Q):
        out={}
        for (a,b),v in P.items():
            for (c,d),w in Q.items():
                idx=(a+c,b+d)
                out[idx]=self.plus[out.get(idx,0)][self.times[v][w]]
        return {j:v for j,v in out.items() if v}

    def power(self,P,n):
        result=ONE
        while n:
            if n&1:result=self.mul(result,P)
            n//=2
            if n:P=self.mul(P,P)
        return result

    def raw_moments(self,x,y):
        t=self.times
        return (1,x,y,t[x][x],t[x][y],t[y][y])


def polynomials(R):
    s=R.add(ONE,R.scale(-1,X),R.scale(-1,Y));u=R.add(ONE,R.scale(-1,Y));v=R.add(ONE,R.scale(-1,X))
    xy=R.mul(X,Y)
    d1=R.add(R.mul(s,s),R.scale(-1,xy))
    d2=R.add(R.power(s,3),R.scale(-3,R.mul(xy,s)),R.scale(-2,xy))
    return [(s,[ONE]),(d1,[u,v]),(d2,[R.mul(u,R.add(u,X)),R.mul(u,v),R.mul(v,R.add(v,Y))])]


class Sections:
    def __init__(self,R,p,k,den,nums):
        self.R=R;self.p=p;K=p**(k-1);self.limit=max(sum(j) for j in den)*K
        frob={(i*p,j*p):v for (i,j),v in den.items()}
        assert R.power(den,p*K)==R.power(frob,K)
        self.nums=[R.mul(P,R.power(den,K-1)) for P in nums]
        twist=R.power(den,(p-1)*K)
        self.sort={}
        for (i,j),v in twist.items():self.sort.setdefault((i%p,j%p),[]).append((i,j,v))
        self.memo={};self.stats=Counter()

    def read(self,a,b):
        polys=self.nums; R=self.R;p=self.p
        while a or b:
            a,i=divmod(a,p);b,j=divmod(b,p);new=[]
            for P in polys:
                key=(tuple(sorted(P.items())),i,j)
                self.stats['digit_state_requests']+=1
                if key not in self.memo:
                    result={}
                    for (u,v),w in P.items():
                        for s,t,z in self.sort.get(((i-u)%p,(j-v)%p),()):
                            self.stats['selected_scalar_products']+=1
                            idx=((u+s)//p,(v+t)//p)
                            result[idx]=R.plus[result.get(idx,0)][R.times[w][z]]
                    result={j:v for j,v in result.items() if v}
                    assert all(sum(j)<=self.limit for j in result)
                    self.memo[key]=result
                new.append(self.memo[key])
            polys=new
        return [P.get((0,0),0) for P in polys]


def exhaustive(R,maxlen):
    M={}
    def visit(a,b,x,y):
        at=(a,b)
        vals=R.raw_moments(x,y)
        M[at]=tuple(R.plus[s][t] for s,t in zip(M.get(at,(0,)*6),vals))
        if a+b<maxlen:
            visit(a+1,b,R.plus[x][y],y)
            visit(a,b+1,x,R.plus[x][y])
    visit(0,0,1,1)
    return M


def rectangle(R,side):
    # Independent endpoint recurrence, appending a last letter in its true time order.
    table={}
    add=R.plus
    zero=(0,0,0,0,0,0)
    for a in range(side+1):
        for b in range(side+1):
            if (a,b)==(0,0):table[a,b]=(1,)*6;continue
            count,u,v,uu,uv,vv=table.get((a-1,b),zero)
            wa=(count,add[u][v],v,add[add[uu][vv]][add[uv][uv]],add[uv][vv],vv)
            count,u,v,uu,uv,vv=table.get((a,b-1),zero)
            wb=(count,u,add[u][v],uu,add[uu][uv],add[add[uu][vv]][add[uv][uv]])
            table[a,b]=tuple(add[i][j] for i,j in zip(wa,wb))
    return table


def single_B(R,a):
    # Word U^i V U^(a-i) in temporal notation, counted once for every 0<=i<=a.
    m=R.m;result=(0,)*6
    for i in range(m):
        count=(a-i)//m+1
        if count<=0:continue
        v=(i+2)%m
        u=R.plus[(i+1)%m][R.times[(a-i)%m][v]]
        result=tuple(R.plus[x][R.times[count%m][y]] for x,y in zip(result,R.raw_moments(u,v)))
    return result


def run(core,p,k):
    R=Residues(core,p**k); sec=[Sections(R,p,k,D,N) for D,N in polynomials(R)]
    read=lambda a,b:tuple(x for s in sec for x in s.read(a,b))
    small=exhaustive(R,10)
    for (a,b),z in small.items():assert read(a,b)==z
    grid=rectangle(R,24)
    for (a,b),v in grid.items():assert read(a,b)==v
    big=(p**101-1)//(p-1)
    pairs=((big,big),(p**100+4,p**91+7),(p**131+123456789,1))
    outputs=[]
    for a,b in pairs:
        v=read(a,b);sw=read(b,a)
        assert sw==(v[0],v[2],v[1],v[5],v[4],v[3])
        if b==1:assert v==single_B(R,a)
        outputs.append({'a':str(a),'b':str(b),'totals':v,'axis_swap_check':True,
                        'verified_all_one_B_words_by_residue_classes':b==1})
    return {'p':p,'k':k,'modulus':R.m,'BRC_scalar_table_kernel_calls':2*R.m**2,'BRC_table_sha256':R.ledger,
          'independent_grid_endpoints':len(grid),'direct_words':2**11-1,'small_endpoints':len(small),'huge_endpoints':outputs,
          'Cartier_by_degree':[{'j':j,'numerator_total_degree_bound':s.limit,'distinct_digit_transitions':len(s.memo),
                    **s.stats} for j,s in enumerate(sec)]}


def binary_certificate(core):
    R=Residues(core,2)
    den,nums=polynomials(R)[1]
    sec=Sections(R,2,1,den,nums)
    assert sec.read(3,3)==[1,1]
    transitions={}
    for name,P in [('u',nums[0]),('v',nums[1]),('one',ONE)]:
        key=(tuple(sorted(P.items())),1,1)
        assert sec.memo[key]==ONE
        transitions[name]='one'
    for m in range(1,13):
        a=2**m-1;mass=comb(2*a,a)
        assert (mass&-mass).bit_length()-1==m and sec.read(a,a)==[1,1]
    return {'mod2_denominator_terms':[list(j) for j in sorted(den)],
            'section_11_transitions':transitions,'binomial_mass_valuation_checks_m':list(range(1,13))}


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--repo',type=Path,required=True);a=ap.parse_args()
    core=import_core(a.repo)
    print(json.dumps({'core_sha256':PIN,'initial':[1,1],'weights':'unit for every positive A,B branch',
       'observation':'endpoint-conditioned unnormalized (mass,u,v,u²,uv,v²) modulo p^k',
       'binary_infinite_family_certificate':binary_certificate(core),'cases':[run(core,p,k) for p,k in ((3,2),(2,3))]},indent=1,sort_keys=True))
