"""Integer block-sum/edge-difference quotients. Python standard library."""
from collections import Counter
from itertools import combinations, product
from math import comb, gcd, prod
import json


def identity(n):
    return [[int(i==j) for j in range(n)] for i in range(n)]


def mv(A,x):
    return [sum(a*b for a,b in zip(row,x)) for row in A]


def smith(matrix, cols):
    """Return diagonal, left/right change of basis and reverse row operations."""
    A=[row[:] for row in matrix]; h=len(A)
    U=identity(h); V=identity(cols); row_log=[]
    def swap_rows(i,j):
        for a in (A,U):a[i],a[j]=a[j],a[i]
        row_log.append(('swap',i,j,0))
    def add_row(i,j,t):
        for a in (A,U):
            a[i]=[x+t*y for x,y in zip(a[i],a[j])]
        row_log.append(('add',i,j,t))
    def swap_cols(i,j):
        for a in (A,V):
            for row in a:row[i],row[j]=row[j],row[i]
    def add_col(i,j,t):
        for a in (A,V):
            for row in a:row[i]+=t*row[j]
    diag=[]
    for k in range(min(h,cols)):
        entry=next(((i,j) for i in range(k,h) for j in range(k,cols) if A[i][j]),None)
        if entry is None:break
        i,j=entry;swap_rows(k,i);swap_cols(k,j)
        while True:
            i=next((i for i in range(k+1,h) if A[i][k]),None)
            if i is not None:
                add_row(i,k,-(A[i][k]//A[k][k]))
                if A[i][k]:swap_rows(k,i)
                continue
            j=next((j for j in range(k+1,cols) if A[k][j]),None)
            if j is not None:
                add_col(j,k,-(A[k][j]//A[k][k]))
                if A[k][j]:swap_cols(k,j)
                continue
            bad=next(((i,j) for i in range(k+1,h) for j in range(k+1,cols) if A[i][j]%A[k][k]),None)
            if bad is None:break
            add_row(k,bad[0],1)
        if A[k][k]<0:
            for a in (A,U):a[k]=[-x for x in a[k]]
            row_log.append(('neg',k,k,0))
        diag.append(A[k][k])
    assert all(v==0 for i,row in enumerate(A) for j,v in enumerate(row) if i!=j)
    assert all(b%a==0 for a,b in zip(diag,diag[1:]))
    return diag,U,V,row_log


def undo_rows(y,log):
    z=y[:]
    for op,i,j,v in reversed(log):
        if op=='swap':z[i],z[j]=z[j],z[i]
        elif op=='add':z[i]-=v*z[j]
        else:z[i]=-z[i]
    return z


class Chart:
    def __init__(self,blocks,edges):
        self.b=list(blocks);self.E=list(edges);n=len(blocks);self.k=max(blocks, default=-1)+1
        adj=[[] for _ in blocks]
        for i,(u,v) in enumerate(edges):
            adj[u].append((v,i,-1));adj[v].append((u,i,1))
        self.comp=[-1]*n;self.orders=[];tree=set();self.c=0
        for root in range(n):
            if self.comp[root]>=0:continue
            self.comp[root]=self.c;self.c+=1;stack=[root]
            while stack:
                u=stack.pop()
                for v,edge,sign in adj[u]:
                    if self.comp[v]>=0:continue
                    self.comp[v]=self.comp[u];tree.add(edge)
                    self.orders.append((u,v,edge,sign));stack.append(v)
        self.chords=[i for i in range(len(edges)) if i not in tree]
        self.M=[[0]*self.c for _ in range(self.k)]
        for b,c in zip(self.b,self.comp):self.M[b][c]+=1
        self.diag,self.U,self.V,self.log=smith(self.M,self.c)
        self.free=len(self.chords)+self.k-len(self.diag)
        self.tor=[d for d in self.diag if d>1]

    def D(self,x):
        return [x[u]-x[v] for u,v in self.E]

    def sums(self,x):
        tot=[0]*self.k
        for b,v in zip(self.b,x):tot[b]+=v
        return tot

    def section(self,b):
        x=[0]*len(self.b)
        for i,v in enumerate(b):x[self.b.index(i)]=v
        return x

    def integrate(self,y):
        x=[0]*len(self.b)
        for u,v,edge,sign in self.orders:x[v]=x[u]+sign*y[edge]
        return x

    def normal(self,y):
        x=self.integrate(y); dx=self.D(x)
        coarse=mv(self.U,self.sums(x))
        for i,d in enumerate(self.diag):coarse[i]%=d
        return tuple(y[e]-dx[e] for e in self.chords),tuple(coarse)

    def lift(self,label):
        cycles,b=label
        y=self.D(self.section(undo_rows(list(b),self.log)))
        for i,e in enumerate(self.chords):y[e]+=cycles[i]
        return y

    def hidden_witness(self,y):
        t=self.integrate(y)
        if self.D(t)!=y:return None
        ub=mv(self.U,self.sums(t));r=len(self.diag)
        if any(ub[i]%d for i,d in enumerate(self.diag)) or any(ub[r:]):return None
        coef=mv(self.V,[ub[i]//self.diag[i] if i<r else 0 for i in range(self.c)])
        x=[w-coef[c] for w,c in zip(t,self.comp)]
        assert self.D(x)==y and not any(self.sums(x))
        return x


def parts(n):
    for a in product(range(n),repeat=n):
        if a[0]==0 and all(a[i]<=max(a[:i])+1 for i in range(1,n)):
            yield a


def graph_checks():
    count=0
    for n in range(1,5):
        all_edges=list(combinations(range(n),2))
        for mask in range(1<<len(all_edges)):
            edges=[e for j,e in enumerate(all_edges) if mask>>j&1]
            for partition in parts(n):
                chart=Chart(partition,edges);basis=[]
                for i,b in enumerate(partition):
                    root=partition.index(b)
                    if i==root:continue
                    h=[0]*n;h[i]=1;h[root]=-1;basis.append(chart.D(h))
                actual,_u,_v,_rows=smith([list(row) for row in zip(*basis)] if basis else [[] for _ in edges],len(basis))
                assert [d for d in actual if d>1]==chart.tor
                assert len(edges)-len(actual)==chart.free
                y=[i%5-2 for i in range(len(edges))]
                tag=chart.normal(y);back=chart.lift(tag)
                assert chart.normal(back)==tag
                assert chart.hidden_witness([v-w for v,w in zip(y,back)]) is not None
                count+=1
    return count


def finite_case(blocks,edges,q):
    c=Chart(blocks,edges);coarse=[0]*c.k
    hist=Counter(tuple(t%q for t in c.D(x)) for x in product(range(q),repeat=len(blocks))
                 if [v%q for v in c.sums(x)]==coarse)
    mod_classes=q**c.free*prod(gcd(q,d) for d in c.tor)
    multiplicity=q**(c.c-len(c.diag))*prod(gcd(q,d) for d in c.tor)
    assert len(hist)*mod_classes==q**len(edges) and set(hist.values())=={multiplicity}
    return {'modulus':q,'report_classes':mod_classes,'hidden_edge_reports':len(hist),'fine_lifts':multiplicity}


def ceildiv(a,b):
    return -((-a)//b)


def band_count(size,S,edges,R):
    neighbors=[[] for _ in S]
    for i,j in edges:neighbors[i].append(j);neighbors[j].append(i)
    def box(u,t,lo,hi):
        h=hi-lo+1;t-=u*lo
        if h<=0 or t<0:return 0
        return sum((-1)**k*comb(u,k)*comb(t-k*h+u-1,u-1) for k in range(min(u,t//h)+1))
    boxes=[];profiles=[]
    for i,u in enumerate(size):
        lo=max(ceildiv(S[j],size[j])-R for j in neighbors[i])
        hi=min(S[j]//size[j]+R for j in neighbors[i])
        rows=[]
        for a in range(lo,hi+1):
            for b in range(a,hi+1):
                mass=box(u,S[i],a,b)-box(u,S[i],a+1,b)-box(u,S[i],a,b-1)+box(u,S[i],a+1,b-1)
                if mass:rows.append((a,b,mass))
        profiles.append(rows);boxes.append((lo,hi))
    count=sum(prod(c for _,_,c in profile) for profile in product(*profiles)
              if all(max(profile[i][1]-profile[j][0],profile[j][1]-profile[i][0])<=R for i,j in edges))
    direct=[]
    for u,Sj,(lo,hi) in zip(size,S,boxes):
        direct.append([x for x in product(range(lo,hi+1),repeat=u) if sum(x)==Sj])
    assert count==sum(all(abs(x-y)<=R for i,j in edges for x in values[i] for y in values[j]) for values in product(*direct))
    minR=max(max(ceildiv(S[i],size[i])-S[j]//size[j],ceildiv(S[j],size[j])-S[i]//size[i]) for i,j in edges)
    assert (count>0)==(R>=minR)
    return count


def extremal():
    total=0; distinct=0
    maximum={}
    for n in range(1,7):
        partitions=list(parts(n)); seen=set()
        for a in partitions:
            for c in partitions:
                mat=[[0]*(max(c)+1) for _ in range(max(a)+1)]
                for i,j in zip(a,c):
                    mat[i][j]+=1
                key=tuple(tuple(row) for row in mat)
                seen.add(key); total+=1
        for mat in seen:
            ds,*_=smith([list(row) for row in mat],len(mat[0]))
            rank=len(ds); q,t=divmod(n,rank)
            bound=q**(rank-t)*(q+1)**t
            tor=prod(ds)
            assert tor<=bound
            shape=len(mat)==rank==len(mat[0]) and all(sum(v>0 for v in row)==1 for row in mat)
            balanced=max(map(sum,mat))-min(map(sum,mat))<=1
            assert (tor==bound)==(shape and balanced)
            maximum[n,rank]=max(maximum.get((n,rank),0),tor)
        distinct+=len(seen)
    for (n,k),v in maximum.items():
        q,t=divmod(n,k)
        assert v==q**(k-t)*(q+1)**t
    return {'labelled_partition_pairs':total,'distinct_tables_by_size':distinct,
            'N6_maximum_by_rank':[maximum[6,k] for k in range(1,7)]}


def run():
    empty=Chart([],[])
    assert empty.normal([])==((),()) and empty.lift(((),()))==[] and empty.hidden_witness([])==[]
    small=graph_checks()
    source=Chart([0,0,1,1],[(0,2),(0,3),(1,2),(1,3)])
    assert source.tor==[2] and source.free==2
    valid=[5,5,5,5];invalid=[0,10,0,10]
    assert source.sums(valid)==source.sums(invalid)==[10,10]
    assert source.D(valid)==[0]*4 and source.D(invalid)==[0,-10,10,0]
    # M=[[2,1],[1,2]], with two path components.  Add a parallel oriented edge and loop.
    b3=[0,0,1,0,1,1]; e3=[(0,1),(1,2),(3,4),(4,5)]
    mix=Chart(b3,e3+[(1,0),(4,4)])
    assert mix.M==[[2,1],[1,2]] and (mix.free,mix.tor)==(2,[3])
    diag=Chart([0]*2+[1]*6,[(0,1)]+[(i,i+1) for i in range(2,7)])
    assert (diag.free,diag.tor)==(0,[2,6])
    btests=0
    for size,es in [([2,3],[(0,1)]),([1,2,2],[(0,1),(1,2)]),([2,2,2],[(0,1),(1,2),(0,2)])]:
        for S in product((-2,0,1,3),repeat=len(size)):
            for R in range(3):
                band_count(size,S,es,R);btests+=1
    return {'empty_graph_round_trip':True,'sharp_torsion_inequality':extremal(),'all_simple_graph_partition_checks_n_1to4':small,'source_quotient':{'free':source.free,'torsion':source.tor,
            'equal_total_distinct_fine_guards':[source.D(valid),source.D(invalid)]},
            'mixed_component_matrix':mix.M,'mixed_component_with_loop_and_parallel':{'free':mix.free,'torsion':mix.tor},
            'forest_diag_2_6_modular_class_counts':{str(q):prod(gcd(q,d) for d in diag.tor) for q in (2,4,8,3,9,6)},
            'direct_modular_examples':[finite_case(source.b,source.E,q) for q in (2,3,4,8)]+[finite_case(b3,e3,q) for q in (2,3,4)],
            'band_profiles_vs_complete_enumeration':btests}


if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
