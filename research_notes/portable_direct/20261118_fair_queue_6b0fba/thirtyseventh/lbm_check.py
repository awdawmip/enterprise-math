"""D2Q9 exact invariants and actual FP64 lbmpy kernels (Python 3.12+).
Install lbmpy==2.1.1, pystencils==2.1, sympy==1.14.0, numpy==2.5.5.
--cost also profiles three CPU kernels on a shared host. --emit-c saves their C.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as F
import hashlib
from itertools import combinations, combinations_with_replacement, product
import json
from math import lcm, prod
import os
from pathlib import Path
import platform
import random
import resource
import subprocess
import sys
from time import perf_counter
from tempfile import TemporaryDirectory


def report(x):
    return json.dumps(x,indent=2,sort_keys=True)


def rank(rows):
    if not rows:return 0
    if len(rows)==1:return 1
    x0,y0=rows[0]
    x1,y1=rows[1]
    return 3 if any((x1-x0)*(y-y0)!=(y1-y0)*(x-x0) for x,y in rows[2:]) else 2


def universal_modes(V):
    checked={}
    for nx,ny in ((1,1),(1,6),(2,2),(3,4),(4,3),(4,4),(5,6),(7,8),(8,9),(10,11)):
        d=lcm(nx,ny)
        modes=[]
        for k,l in product(range(nx),range(ny)):
            e=[(k*x*(d//nx)+l*y*(d//ny))%d for x,y in V]
            for z in set(e):
                dim=3-rank([v for v,t in zip(V,e) if t!=z])
                if dim:
                    modes.append([k,l,z,dim])
        expected=[[0,0,0,3]]
        if nx%2==0: expected.append([nx//2,0,d//2,1])
        if ny%2==0: expected.append([0,ny//2,d//2,1])
        assert sorted(modes)==sorted(expected)
        checked[f"{nx}x{ny}"]=sorted(modes)
    return checked


def connected_graphs(m):
    edges=list(combinations(range(m),2))
    histogram=Counter()
    for bits in product((0,1),repeat=len(edges)):
        components=[{i} for i in range(m)]
        for (i,j),present in zip(edges,bits):
            if present:
                left=next(c for c in components if i in c)
                right=next(c for c in components if j in c)
                if left!=right:
                    components.remove(right)
                    left.update(right)
        if len(components)==1:
            histogram[sum(bits)]+=1
    return dict(sorted(histogram.items()))


def markov_basis(V):
    pairs=defaultdict(list)
    for i,j in combinations_with_replacement(range(9),2):
        c,d=V[i],V[j]
        pairs[c[0]+d[0],c[1]+d[1]].append((i,j))
    assert len(pairs)==25
    trees=[(p[0],v) for p in pairs.values() for v in p[1:]]
    sizes=Counter(map(len,pairs.values()))
    assert len(trees)==20 and sizes=={1:12,2:8,3:4,5:1}
    complete_moves=sum(len(p)*(len(p)-1)//2 for p in pairs.values())
    counts={}
    for mass in range(2,7):
        states=list(combinations_with_replacement(range(9),mass))
        parent={s:s for s in states}
        def root(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        for x in states:
            for a,b in trees:
                ys=list(x)
                if a[0] not in ys:continue
                ys.remove(a[0])
                if a[1] not in ys:continue
                ys.remove(a[1]); ys.extend(b)
                parent[root(x)]=root(tuple(sorted(ys)))
        cells={}
        for x in states:
            key=tuple(sum(V[i][j] for i in x) for j in range(2))
            assert cells.setdefault(key,root(x))==root(x)
        assert len(set(cells.values()))==len(cells)==(2*mass+1)**2
        counts[mass]={"populations":len(states),"moment_fibers":len(cells)}
    graph_counts={m:connected_graphs(m) for m in sizes}
    valid_rule_sets=prod(sum(graph_counts[m].values())**n for m,n in sizes.items())
    assert valid_rule_sets==186368
    return {"all_binary_generating_systems":valid_rule_sets,"connected_graphs_by_edges":graph_counts,
            "pair_fiber_sizes":dict(sizes),"primitive_unordered_binary_moves":complete_moves,
            "every_minimal_basis_size":len(trees),"minimal_basis_count":prod(max(1,t**max(0,t-2))**m for t,m in sizes.items()),
            "star_tree_connectivity_checked":counts}


def moments(f,V):
    return tuple(sum(fi*c for fi,c in zip(f,coeff)) for coeff in ([1]*9,[x for x,y in V],[y for x,y in V]))


def collide(f,V,w):
    rho,jx,jy=moments(f,V)
    ux,uy=jx/rho,jy/rho
    omega=F(5,4)
    return [a+omega*(rho*b*(1+3*z+F(9,2)*z*z-F(3,2)*(ux*ux+uy*uy))-a)
            for a,b,z in zip(f,w,[x*ux+y*uy for x,y in V])]


def scalar_reference(src,V,w,wall):
    nx,ny=len(src),len(src[0])
    inv=[V.index((-x,-y)) for x,y in V]
    out=[[None]*ny for _ in range(nx)]
    wall_j=[F(0),F(0)]
    for x,y in product(range(nx),range(ny)):
        f=[]
        for i,(cx,cy) in enumerate(V):
            sx,sy=x-cx,y-cy
            if wall and not (0<=sx<nx and 0<=sy<ny):
                reflected=src[x][y][inv[i]]
                f.append(reflected)
                wall_j[0]+=2*cx*reflected
                wall_j[1]+=2*cy*reflected
            else:
                f.append(src[sx%nx][sy%ny][i])
        out[x][y]=collide(f,V,w)
        assert moments(out[x][y],V)==moments(f,V)
    def macro(grid):
        m=[moments(row,V) for col in grid for row in col]
        return [sum(p[j] for p in m) for j in range(3)]
    a,b=macro(src),macro(out)
    assert [b[i]-a[i] for i in range(3)]==[0,*wall_j]
    for axis,N in enumerate((nx,ny)):
        if wall or N%2==0:
            def checkerboard(field):
                return sum((-1)**((x,y)[axis])*moments(field[x][y],V)[axis+1]
                           for x,y in product(range(nx),range(ny)))
            assert checkerboard(src)==-checkerboard(out)
    return out,wall_j


def irregular_bounces(V):
    # Per-link test on an odd box with a hole and a missing corner.
    sites=set(product(range(5),range(3)))-{(2,1),(0,0)}
    transitions=[]
    for j,c in enumerate(V):
        for p in sites:
            q=p[0]+c[0],p[1]+c[1]
            k=j
            if q not in sites:
                q=p
                k=V.index((-c[0],-c[1]))
            transitions.append((q,k))
            for axis in range(2):
                assert (-1)**q[axis]*V[k][axis]==-(-1)**p[axis]*c[axis]
    assert len(set(transitions))==len(transitions)==len(sites)*9
    return {"sites":len(sites),"population_links":len(transitions),"alternating_momenta_tested":2}


def halo_plan(nx,ny,V,np):
    groups=[]
    for i,(cx,cy) in enumerate(V):
        sites=set()
        if cx:
            x=1 if cx==1 else nx
            sites.update((x,y) for y in range(1,ny+1))
        if cy:
            y=1 if cy==1 else ny
            sites.update((x,y) for x in range(1,nx+1))
        if sites:
            xy=np.array(sorted(sites),dtype=np.intp)
            x,y=xy.T
            groups.append((x-cx,y-cy,i,x,y,V.index((-cx,-cy))))
    return groups


def fill(a,plan=None):
    if plan is not None:
        for sx,sy,i,x,y,opp in plan:
            a[sx,sy,i]=a[x,y,opp]
    else:
        a[0,1:-1,:]=a[-2,1:-1,:]
        a[-1,1:-1,:]=a[1,1:-1,:]
        a[:,0,:]=a[:,-2,:]
        a[:,-1,:]=a[:,1,:]


def array(np,nx,ny):
    return np.empty((9,ny+2,nx+2),dtype=np.float64).transpose(2,1,0)


def generate(np,sp,emit):
    from pystencils import Field
    from lbmpy.fieldaccess import StreamPullTwoFieldsAccessor
    from lbmpy import LBMConfig,LBMOptimisation,create_lb_update_rule,create_lb_ast
    from lbmpy.stencils import LBStencil
    from lbmpy.enums import Method,Stencil
    stencil=LBStencil(Stencil.D2Q9)
    V=[tuple(map(int,c)) for c in stencil]
    funcs={}
    records={}
    builds={}
    for name in ("auto","builtin_global_cse","stream_only"):
        start=perf_counter()
        cfg=LBMConfig(stencil=stencil,method=Method.SRT,relaxation_rate=sp.Rational(5,4),
                      compressible=True,zero_centered=False,equilibrium_order=2,
                      kernel_type="stream_pull_only" if name=="stream_only" else "stream_pull_collide")
        opt=LBMOptimisation(cse_global=(name=="builtin_global_cse"),field_layout="fzyx")
        rule=create_lb_update_rule(lbm_config=cfg,lbm_optimisation=opt)
        reads=set().union(*(a.rhs.atoms(Field.Access) for a in rule.all_assignments))
        writes={a.lhs for a in rule.all_assignments if isinstance(a.lhs,Field.Access)}
        source=next(iter(reads)).field
        target=next(iter(writes)).field
        accessor=StreamPullTwoFieldsAccessor()
        assert reads==set(accessor.read(source,stencil)) and writes==set(accessor.write(target,stencil))
        assert source.name=="src" and target.name=="dst"
        indices=sorted((int(r.index[0]),*map(int,r.offsets)) for r in reads)
        assert indices==[(i,-x,-y) for i,(x,y) in enumerate(V)]
        ast=create_lb_ast(update_rule=rule,lbm_config=cfg,lbm_optimisation=opt)
        code=ast.get_c_code()
        if emit:
            emit.mkdir(parents=True,exist_ok=True)
            (emit/(name+".c")).write_text(code)
        generated=perf_counter()
        funcs[name]=ast.compile()
        builds[name]={"construct_and_emit_s":generated-start,"compile_and_load_s_with_empty_run_cache":perf_counter()-generated}
        records[name]={"operation_counts_from_symbolic_rule":{str(k):int(v) for k,v in rule.operation_count.items()},
                       "inplace":False,"source_offset_x_y_lane":[[dx,dy,i] for i,dx,dy in indices]}
        builds[name]["emitted_c_sha256"]=hashlib.sha256(code.encode()).hexdigest()
        builds[name]["emitted_c_utf8_bytes"]=len(code.encode())
    return V,funcs,records,builds


def validate(np,V,w,fn):
    nx,ny=6,4
    raw=[[[wi*(1+F((13*x+7*y+3*i)%17-8,1000)) for i,wi in enumerate(w)]
          for y in range(ny)] for x in range(nx)]
    results={}
    for boundary in ("periodic","wall"):
        wall=boundary=="wall"
        plan=halo_plan(nx,ny,V,np) if wall else None
        exact,impulse=scalar_reference(raw,V,w,wall)
        expected=np.array(exact,dtype=np.float64)
        f=array(np,nx,ny); f[1:-1,1:-1]=np.array(raw,dtype=np.float64)
        fill(f,plan)
        err={}
        for name in ("auto","builtin_global_cse"):
            dst=array(np,nx,ny);dst[:]=np.nan
            fn[name](src=f,dst=dst)
            err[name]=float(np.max(np.abs(dst[1:-1,1:-1]-expected)))
            assert err[name]<3e-15 and np.isnan(dst[0]).all()
        # A second test detects repeated steps and halo updates, independently of one-step rational arithmetic.
        fields=[]
        for name in ("auto","builtin_global_cse"):
            src=array(np,nx,ny);src[1:-1,1:-1]=np.array(raw,dtype=np.float64)
            dst=array(np,nx,ny)
            for _ in range(19):
                fill(src,plan)
                fn[name](src=src,dst=dst)
                src,dst=dst,src
            fields.append(src[1:-1,1:-1].copy())
        err["between_generated_variants_after_19"]=float(np.max(abs(fields[0]-fields[1])))
        assert err["between_generated_variants_after_19"]<3e-14
        results[boundary]={"measured_max_errors":err,"exact_wall_impulse":list(map(str,impulse))}
    return results


def benchmark(np,V,w,fn):
    rng=random.Random(907322)
    info={}
    for n,reps in ((96,30),(512,4),(1536,1)):
        s,d=array(np,n,n),array(np,n,n)
        for i,wi in enumerate(w):
            s[:,:,i]=float(wi)*(1+0.0003*((np.arange(n+2)[:,None]+np.arange(n+2)[None,:]+i)%5))
        d.fill(0)
        def group(name,count):
            start=perf_counter()
            for _ in range(count):
                fill(s)
                fn[name](src=s,dst=d)
            return (perf_counter()-start)/count
        for name in fn:
            group(name,1)
        times={name:[] for name in fn}
        for _ in range(5):
            order=list(fn);rng.shuffle(order)
            for name in order:
                times[name].append(group(name,reps))
        info[n]={name:{"seconds_per_step_repetitions":ts,"median_MLUPS":n*n/float(np.median(ts))/1e6,
                       "median_effective_GBps_144_payload_bytes":144*n*n/float(np.median(ts))/1e9}
                 for name,ts in times.items()}
    return info


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cost",type=Path)
    ap.add_argument("--emit-c",type=Path)
    args=ap.parse_args()
    import numpy as np
    import sympy as sp
    import lbmpy,pystencils
    assert (lbmpy.__version__,pystencils.__version__)==("2.1.1","2.1")
    affinity=sorted(os.sched_getaffinity(0)) if hasattr(os,"sched_getaffinity") else []
    if affinity and args.cost: os.sched_setaffinity(0,{affinity[0]})
    V,funcs,records,builds=generate(np,sp,args.emit_c)
    w=[F(4,9) if x==y==0 else (F(1,36) if x*y else F(1,9)) for x,y in V]
    verify=validate(np,V,w,funcs)
    eq=[a*36 for a in w]
    delta=[int(y==0 and abs(x)==1)-2*int(x==y==0) for x,y in V]
    other=[x+y for x,y in zip(eq,delta)]
    assert moments(eq,V)==moments(other,V)==(36,0,0)
    diff=[b-a for a,b in zip(collide(eq,V,w),collide(other,V,w))]
    assert diff==[-F(x,4) for x in delta]
    stable={"lbmpy":lbmpy.__version__,"pystencils":pystencils.__version__,"stencil":V,
            "weights":list(map(str,w)),"omega":"5/4","kernel_cases":records,
            "binary_collision_lattice":markov_basis(V),"periodic_character_modes":universal_modes(V),"irregular_wall":irregular_bounces(V),
            "moment_only_counterexample":{"pre_collision_delta":delta,"post_collision_delta":list(map(str,diff))},
            "checks":{k:{"exact_global_wall_impulse":v["exact_wall_impulse"],"one_step_fp64_max_error_lt":"3e-15",
                         "variant_max_difference_at_19_lt":"3e-14"} for k,v in verify.items()}}
    if args.cost:
        times=benchmark(np,V,w,funcs)
        cost={"python":platform.python_version(),"numpy":np.__version__,"sympy":sp.__version__,
              "platform":platform.platform(),"affinity_for_timed_run":affinity[:1],
              "cxx_compiler_available":subprocess.check_output(["c++","--version"],text=True).splitlines()[0],
              "build":builds,"floating_checks":verify,"measurements":times,
              "peak_rss_KiB_linux":resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "cost_scope":"five shuffled timing groups, one CPU affinity; fixed input, periodic halo plus FP64 kernel; payload floor excludes cache, RFO and halo"}
        args.cost.write_text(report(cost)+"\n")
    print(report(stable))


if __name__=="__main__":
    # Use fresh per-run symbolic and machine-code caches without disturbing user caches.
    with TemporaryDirectory() as cache:
        os.environ["XDG_CACHE_HOME"]=cache
        os.environ["PYSTENCILS_CACHE_DIR"]=str(Path(cache)/"symbolic")
        main()
