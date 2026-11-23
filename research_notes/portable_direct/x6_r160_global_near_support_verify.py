from x6_r159_global_six_witness_verify import *
# Strict near support: F_v < 3/2 eta iff 3 F_w > 2 F_v for all w in W.
C=[v for v,g in G.items() if not any(all(2*a>=3*b for a,b in zip(g,G[u])) for u in P)]
assert len(C)==20
support={}
for v in C:
    for j,n in enumerate(G[v]):
        if not n:continue
        R=T
        for k,m in enumerate(G[v]):R=clip(R,cmp(n,j,m,k))
        cells=[R] if area(R)>0 else []
        for w in W:
            new=[]
            for poly in cells:
                for k,m in enumerate(G[w]):
                    l=cmp(3*m,k,2*n,j)
                    if l==(0,0,0):continue
                    X=clip(poly,l)
                    if area(X)>0:new.append(X)
            cells=new
        if cells:
            # Vertex average lies in the interior of a full-dimensional convex polygon.
            poly=cells[0];b,d=(sum(p[i] for p in poly)/len(poly) for i in (0,1));t=1-b-d
            B,D=b/t,d/t
            s=(136+B,312,136+D,176+B,B+D,176+D)
            f={u:max(Q(a,b) for a,b in zip(g,s)) for u,g in G.items()};m=min(f.values())
            assert 2*f[v]<3*m
            support[v]=(B,D)
            break
print('STRICT NEAR SUPPORT',len(support))
for v,(B,D) in support.items():print(v,str(B),str(D))
print('NEVER STRICT NEAR',sorted(set(C)-set(support)))
assert len(support)==10
print('GLOBAL TEN-ROW NEAR SUPPORT PASS')
