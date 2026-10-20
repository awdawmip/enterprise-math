from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
import hashlib, json
from pathlib import Path
from typing import Iterable

Point=tuple[int,int]
State=frozenset[Point]
DIRS=((1,0),(0,1),(-1,1),(-1,0),(0,-1),(1,-1))
MASK64=(1<<64)-1

def add(p:Point,q:Point)->Point: return (p[0]+q[0],p[1]+q[1])
def sub(p:Point,q:Point)->Point: return (p[0]-q[0],p[1]-q[1])
def Q(p:Point)->int:
    a,b=p; return a*a+a*b+b*b

def L(p:Point,q:Point)->int:
    a,b=p; c,d=q
    return 2*a*c+a*d+b*c+2*b*d

def sum_point(C:Iterable[Point])->Point:
    a=b=0
    for x,y in C: a+=x; b+=y
    return a,b

def energy_fast(C:Iterable[Point])->int:
    pts=list(C); n=len(pts); S=sum_point(pts)
    return n*sum(Q(p) for p in pts)-Q(S)

def energy_pairwise(C:Iterable[Point])->int:
    pts=list(C); total=0
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            total += Q(sub(pts[i],pts[j]))
    return total

def delta_g(C:State,u:Point,v:Point)->int:
    n=len(C); S=sum_point(C); d=sub(v,u)
    return n*(Q(v)-Q(u))-(L(S,d)+Q(d))

def neighbors(p:Point):
    for d in DIRS: yield add(p,d)

def connected(C:State)->bool:
    if not C: return False
    start=next(iter(C)); seen={start}; stack=[start]
    while stack:
        p=stack.pop()
        for q in neighbors(p):
            if q in C and q not in seen:
                seen.add(q); stack.append(q)
    return len(seen)==len(C)

def hole_free(C:State)->bool:
    if not C: return True
    aa=[p[0] for p in C]; bb=[p[1] for p in C]
    amin,amax=min(aa)-1,max(aa)+1; bmin,bmax=min(bb)-1,max(bb)+1
    def in_box(p): return amin<=p[0]<=amax and bmin<=p[1]<=bmax
    exterior=set(); dq=deque()
    for a in range(amin,amax+1):
        for b in (bmin,bmax):
            p=(a,b)
            if p not in C and p not in exterior: exterior.add(p); dq.append(p)
    for b in range(bmin,bmax+1):
        for a in (amin,amax):
            p=(a,b)
            if p not in C and p not in exterior: exterior.add(p); dq.append(p)
    while dq:
        p=dq.popleft()
        for q in neighbors(p):
            if in_box(q) and q not in C and q not in exterior:
                exterior.add(q); dq.append(q)
    amin0,amax0=min(aa),max(aa); bmin0,bmax0=min(bb),max(bb)
    for a in range(amin0,amax0+1):
        for b in range(bmin0,bmax0+1):
            p=(a,b)
            if p not in C and p not in exterior:
                return False
    return True

def boundary(C:State)->tuple[Point,...]:
    return tuple(sorted(p for p in C if any(q not in C for q in neighbors(p))))

def frontier(C:State)->tuple[Point,...]:
    if not C: return tuple()
    f=set()
    for p in C:
        for q in neighbors(p):
            if q not in C: f.add(q)
    return tuple(sorted(f))

def frontier_neighbor_counts(C:State)->dict[Point,int]:
    out={}
    for v in frontier(C): out[v]=sum((q in C) for q in neighbors(v))
    return out

def normalize_translation(C:Iterable[Point])->tuple[Point,...]:
    pts=list(C)
    if not pts: return tuple()
    ma=min(a for a,b in pts); mb=min(b for a,b in pts)
    return tuple(sorted((a-ma,b-mb) for a,b in pts))

def rot60(p:Point)->Point:
    a,b=p; return (-b,a+b)

def reflect(p:Point)->Point:
    a,b=p; return (a+b,-b)

def transform_point(p:Point,idx:int)->Point:
    q=reflect(p) if idx>=6 else p
    k=idx%6
    for _ in range(k): q=rot60(q)
    return q

def transform_state(C:Iterable[Point],idx:int)->tuple[Point,...]:
    return normalize_translation(transform_point(p,idx) for p in C)

def canonical_state(C:Iterable[Point])->tuple[Point,...]:
    return min(transform_state(C,i) for i in range(12))

def canonical_state_with_indices(C:Iterable[Point]):
    reps=[transform_state(C,i) for i in range(12)]
    best=min(reps)
    return best,[i for i,r in enumerate(reps) if r==best]

def pure_translation_equiv(A:Iterable[Point],B:Iterable[Point])->bool:
    return normalize_translation(A)==normalize_translation(B)

def canonical_move_key(Cprime:State,u:Point,v:Point)->tuple:
    best,idxs=canonical_state_with_indices(Cprime)
    keys=[]
    for idx in idxs:
        tpts=[transform_point(p,idx) for p in Cprime]
        ma=min(a for a,b in tpts); mb=min(b for a,b in tpts)
        tu=transform_point(u,idx); tv=transform_point(v,idx)
        keys.append(((tu[0]-ma,tu[1]-mb),(tv[0]-ma,tv[1]-mb)))
    return min(keys)

def current_orientation_move_key(C:State,u:Point,v:Point)->tuple:
    ma=min(a for a,b in C); mb=min(b for a,b in C)
    return ((u[0]-ma,u[1]-mb),(v[0]-ma,v[1]-mb))

def centroid_class(C:State)->dict:
    n=len(C); S=sum_point(C); r=(S[0]%n,S[1]%n)
    orbit=sorted(set((transform_point(r,i)[0]%n,transform_point(r,i)[1]%n) for i in range(12)))
    canon=orbit[0]
    return {'residue':[r[0],r[1]],'canonical_residue':[canon[0],canon[1]],'denominator':n,'d6_orbit_size':len(orbit),'d6_stabilizer_size':12//len(orbit)}

def p_edge(C:State)->int:
    return sum(1 for p in C for q in neighbors(p) if q not in C)

def direction_counts(C:State)->tuple[int,...]:
    return tuple(sum(1 for p in C if add(p,d) not in C) for d in DIRS)

def frac_obj(f:Fraction):
    return {'num':f.numerator,'den':f.denominator,'float':float(f)}

def anisotropy_A2(C:State):
    n=len(C); S=sum_point(C)
    vals=[]
    for a,b in C:
        A=n*a-S[0]; B=n*b-S[1]
        vals.append((A,B))
    X=sum((2*A+B)**2 for A,B in vals)
    Y3=3*sum(B*B for A,B in vals)
    cross=sum((2*A+B)*B for A,B in vals)
    den=(X+Y3)**2
    if den==0: return frac_obj(Fraction(0,1))
    num=(X-Y3)**2+12*cross*cross
    return frac_obj(Fraction(num,den))

def radial_sq_dispersion(C:State):
    n=len(C); S=sum_point(C); bd=boundary(C)
    rs=[]
    for a,b in bd:
        A=n*a-S[0]; B=n*b-S[1]
        rs.append(Q((A,B)))
    if not rs or sum(rs)==0: return frac_obj(Fraction(0,1))
    m=len(rs); sm=sum(rs); ss=sum(r*r for r in rs)
    return frac_obj(Fraction(m*ss-sm*sm,sm*sm))

def dir_imbalance(C:State):
    c=direction_counts(C); P=sum(c)
    if P==0:return frac_obj(Fraction(0,1))
    return frac_obj(Fraction(6*sum(x*x for x in c)-P*P,P*P))

def diagnostics(C:State)->dict:
    return {'G':energy_fast(C),'P_edge':p_edge(C),'A2':anisotropy_A2(C),'boundary_squared_radius_dispersion':radial_sq_dispersion(C),'direction_counts':list(direction_counts(C)),'six_direction_boundary_imbalance':dir_imbalance(C),'centroid_class':centroid_class(C)}

@dataclass(frozen=True)
class Move:
    u:Point
    v:Point
    delta:int
    next_state:State
    next_canonical:tuple[Point,...]

def legal_moves(C:State,dynamics:str,strict_desc=True)->list[Move]:
    G=energy_fast(C); fnc=frontier_neighbor_counts(C); out=[]
    for u in boundary(C):
        if dynamics=='D1':
            vs=[]
            for v in neighbors(u):
                if v in C: continue
                if fnc.get(v,0)-1 >= 1: vs.append(v)
        elif dynamics=='D2':
            vs=[v for v,cnt in fnc.items() if v!=u and cnt-(1 if u in set(neighbors(v)) else 0)>=1]
        else: raise ValueError(dynamics)
        for v in vs:
            d=delta_g(C,u,v)
            if strict_desc and d>=0: continue
            Cp=frozenset((C-{u})|{v})
            if len(Cp)!=len(C): continue
            if pure_translation_equiv(C,Cp): continue
            if not connected(Cp): continue
            if not hole_free(Cp): continue
            Gp=energy_fast(Cp)
            if Gp-G!=d: raise AssertionError(('delta mismatch',C,u,v,G,Gp,d))
            if strict_desc and not (Gp<G): raise AssertionError('strict descent mismatch')
            out.append(Move(u,v,d,Cp,canonical_state(Cp)))
    return out

def select_move(C:State,dynamics:str,tie_id:str)->Move|None:
    moves=legal_moves(C,dynamics,True)
    if not moves:return None
    bestd=min(m.delta for m in moves)
    cand=[m for m in moves if m.delta==bestd]
    if tie_id=='T0_CANONICAL_MIN':
        return min(cand,key=lambda m:(m.next_canonical,canonical_move_key(m.next_state,m.u,m.v)))
    if tie_id=='T1_CANONICAL_MAX':
        return max(cand,key=lambda m:(m.next_canonical,canonical_move_key(m.next_state,m.u,m.v)))
    if tie_id=='T2_ORIENTATION_MOVE_LEX':
        return min(cand,key=lambda m:current_orientation_move_key(C,m.u,m.v))
    raise ValueError(tie_id)

def relax(C0:State,dynamics:str,tie_id:str,max_steps=100000,record_moves=True)->dict:
    if not connected(C0) or not hole_free(C0): raise ValueError('invalid initial state')
    C=C0; n=len(C); G=energy_fast(C); S=sum_point(C)
    initial=list(map(list,sorted(C)))
    moves_out=[]; gseq=[G]; centroid_sums=[list(S)]
    for step in range(max_steps):
        mv=select_move(C,dynamics,tie_id)
        if mv is None: break
        Cp=mv.next_state
        if len(Cp)!=n or not connected(Cp) or not hole_free(Cp): raise AssertionError('postcondition')
        Gp=energy_fast(Cp)
        if not Gp<G: raise AssertionError('not descending')
        Sp=sum_point(Cp)
        if record_moves:
            moves_out.append({'step':step+1,'u':list(mv.u),'v':list(mv.v),'delta_G':mv.delta,'G_before':G,'G_after':Gp,'centroid_sum_after':list(Sp)})
        C,G,S=Cp,Gp,Sp
        gseq.append(G); centroid_sums.append(list(S))
    else: raise RuntimeError('max_steps exceeded')
    dS=sub(S,sum_point(C0)); net_disp_sq=Fraction(Q(dS),n*n)
    return {
      'N':n,'dynamics':dynamics,'tie_break':tie_id,'initial_state':initial,'initial_canonical':[list(x) for x in canonical_state(C0)],
      'initial_G':gseq[0],'moves':moves_out,'move_count':len(moves_out),'G_sequence':gseq,'centroid_sum_sequence':centroid_sums,
      'final_state':[list(x) for x in sorted(C)],'final_canonical':[list(x) for x in canonical_state(C)],'terminal_G':G,
      'terminal_diagnostics':diagnostics(C),'net_centroid_displacement_squared':frac_obj(net_disp_sq),
      'status':'D1_LOCAL_MINIMUM' if dynamics=='D1' else 'D2_RELOCATION_MINIMUM'
    }

def hex_shell_growth(N:int)->State:
    pts=[(0,0)]; r=1
    walk_dirs=((-1,1),(-1,0),(0,-1),(1,-1),(1,0),(0,1))
    while len(pts)<N:
        p=(r,0); ring=[]
        for d in walk_dirs:
            for _ in range(r):
                if p not in ring: ring.append(p)
                p=add(p,d)
        if len(ring)!=6*r: raise AssertionError((r,len(ring)))
        for p in ring:
            if len(pts)>=N:break
            pts.append(p)
        r+=1
    C=frozenset(pts)
    assert len(C)==N and connected(C) and hole_free(C)
    return C

def elongated_strip(N:int)->State:
    C=frozenset((a,0) for a in range(N)); assert connected(C) and hole_free(C); return C

def six_arm_star(N:int)->State:
    C={(0,0)}; lengths=[0]*6; k=0
    while len(C)<N:
        i=k%6; lengths[i]+=1; d=DIRS[i]; C.add((d[0]*lengths[i],d[1]*lengths[i])); k+=1
    C=frozenset(C); assert len(C)==N and connected(C) and hole_free(C); return C

def l_shape(N:int)->State:
    h=(N+2)//2
    C={(a,0) for a in range(h)}|{(0,b) for b in range(1,N-h+1)}
    C=frozenset(C); assert len(C)==N and connected(C) and hole_free(C); return C

def splitmix64_next(state:int):
    state=(state+0x9E3779B97F4A7C15)&MASK64
    z=state
    z=((z^(z>>30))*0xBF58476D1CE4E5B9)&MASK64
    z=((z^(z>>27))*0x94D049BB133111EB)&MASK64
    z=z^(z>>31)
    return state,z&MASK64

def eden_seeded(N:int,base_seed:int)->State:
    C=frozenset({(0,0)}); state=(base_seed ^ ((N*0x9E3779B97F4A7C15)&MASK64))&MASK64
    while len(C)<N:
        F=list(frontier(C)); state,r=splitmix64_next(state); start=r%len(F)
        chosen=None
        for j in range(len(F)):
            v=F[(start+j)%len(F)]; Cp=frozenset(set(C)|{v})
            if connected(Cp) and hole_free(Cp): chosen=v; break
        if chosen is None: raise RuntimeError('no Eden admissible frontier')
        C=frozenset(set(C)|{chosen})
    return C

def compact_bfs_alt(N:int)->State:
    C=frozenset({(0,0)})
    while len(C)<N:
        F=frontier(C)
        def gd(p): a,b=p; return max(abs(a),abs(b),abs(a+b))
        v=min(F,key=lambda p:(-sum(q in C for q in neighbors(p)),gd(p),p[1],p[0]))
        C=frozenset(set(C)|{v})
        if not hole_free(C): raise AssertionError('compact growth made hole')
    return C

def initial_states(N:int)->dict[str,State]:
    return {
      'HEX_SHELL_GROWTH':hex_shell_growth(N),'ELONGATED_STRIP':elongated_strip(N),'SIX_ARM_STAR':six_arm_star(N),
      'L_SHAPE_OR_WEDGE':l_shape(N),'EDEN_SEEDED_seed_550001':eden_seeded(N,550001),
      'EDEN_SEEDED_seed_550021':eden_seeded(N,550021),'EDEN_SEEDED_seed_550057':eden_seeded(N,550057),
      'COMPACT_BFS_ALT_TIE':compact_bfs_alt(N),
    }

def enumerate_connected_classes(max_n:int=12)->dict[int,set[tuple[Point,...]]]:
    levels={1:{((0,0),)}}
    for n in range(2,max_n+1):
        nxt=set()
        for enc in levels[n-1]:
            C=frozenset(enc)
            for v in frontier(C):
                nxt.add(canonical_state(set(C)|{v}))
        levels[n]=nxt
    return levels

def sha256_file(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def json_dump(path:Path,obj):
    path.write_text(json.dumps(obj,ensure_ascii=False,sort_keys=True,indent=2,separators=(',', ': '))+'\n',encoding='utf-8')

def state_id(enc:tuple[Point,...])->str:
    s=';'.join(f'{a},{b}' for a,b in enc)
    return hashlib.sha256(s.encode()).hexdigest()[:16]

@dataclass(frozen=True)
class RawMove:
    u:Point
    v:Point
    delta:int

def raw_descending_candidates(C:State,dynamics:str)->list[RawMove]:
    S=sum_point(C); n=len(C); occ=C; out=[]
    for u in boundary(C):
        if dynamics=='D1':
            vs=[]
            for v in neighbors(u):
                if v in occ: continue
                if any(q in occ and q!=u for q in neighbors(v)):
                    vs.append(v)
        elif dynamics=='D2':
            rem=frozenset(occ-{u})
            vs=[v for v in frontier(rem) if v not in occ and v!=u]
        else: raise ValueError(dynamics)
        for v in vs:
            d=delta_g(C,u,v)
            if d<0: out.append(RawMove(u,v,d))
    return out

def select_move_fast(C:State,dynamics:str,tie_id:str)->Move|None:
    raws=raw_descending_candidates(C,dynamics)
    raws.sort(key=lambda m:(m.delta,m.u,m.v))
    i=0; G=energy_fast(C)
    while i<len(raws):
        d=raws[i].delta; j=i
        legal=[]
        while j<len(raws) and raws[j].delta==d:
            rm=raws[j]
            Cp=frozenset((C-{rm.u})|{rm.v})
            if len(Cp)==len(C) and not pure_translation_equiv(C,Cp) and connected(Cp) and hole_free(Cp):
                Gp=energy_fast(Cp)
                if Gp-G!=d: raise AssertionError(('delta mismatch fast',G,Gp,d,rm))
                if not Gp<G: raise AssertionError('strict descent mismatch fast')
                legal.append(Move(rm.u,rm.v,d,Cp,canonical_state(Cp)))
            j+=1
        if legal:
            if tie_id=='T0_CANONICAL_MIN':
                return min(legal,key=lambda m:(m.next_canonical,canonical_move_key(m.next_state,m.u,m.v)))
            if tie_id=='T1_CANONICAL_MAX':
                return max(legal,key=lambda m:(m.next_canonical,canonical_move_key(m.next_state,m.u,m.v)))
            if tie_id=='T2_ORIENTATION_MOVE_LEX':
                return min(legal,key=lambda m:current_orientation_move_key(C,m.u,m.v))
            raise ValueError(tie_id)
        i=j
    return None

def relax_fast(C0:State,dynamics:str,tie_id:str,max_steps=100000,record_moves=True)->dict:
    if not connected(C0) or not hole_free(C0): raise ValueError('invalid initial state')
    C=C0; n=len(C); G=energy_fast(C); S=sum_point(C); S0=S
    initial=list(map(list,sorted(C)))
    moves_out=[]; gseq=[G]; centroid_sums=[list(S)]; step_count=0
    for step in range(max_steps):
        mv=select_move_fast(C,dynamics,tie_id)
        if mv is None: break
        Cp=mv.next_state
        if len(Cp)!=n or not connected(Cp) or not hole_free(Cp): raise AssertionError('postcondition')
        Gp=energy_fast(Cp)
        if not Gp<G: raise AssertionError('not descending')
        Sp=sum_point(Cp)  # mandatory full N-cell centroid recompute
        step_count += 1
        if record_moves:
            moves_out.append({'step':step_count,'u':list(mv.u),'v':list(mv.v),'delta_G':mv.delta,'G_before':G,'G_after':Gp,'centroid_sum_after':list(Sp)})
        C,G,S=Cp,Gp,Sp
        gseq.append(G); centroid_sums.append(list(S))
    else: raise RuntimeError('max_steps exceeded')
    dS=sub(S,S0); net_disp_sq=Fraction(Q(dS),n*n)
    return {
      'N':n,'dynamics':dynamics,'tie_break':tie_id,'initial_state':initial,'initial_canonical':[list(x) for x in canonical_state(C0)],
      'initial_G':gseq[0],'moves':moves_out,'move_count':step_count,'G_sequence':gseq,'centroid_sum_sequence':centroid_sums,
      'final_state':[list(x) for x in sorted(C)],'final_canonical':[list(x) for x in canonical_state(C)],'terminal_G':G,
      'terminal_diagnostics':diagnostics(C),'net_centroid_displacement_squared':frac_obj(net_disp_sq),
      'status':'D1_LOCAL_MINIMUM' if dynamics=='D1' else 'D2_RELOCATION_MINIMUM'
    }

# Exact fast selector preserving the frozen/legal_moves enumeration order as the final deterministic fallback
# when two candidates share the same declared canonicalized tie key.
def raw_descending_candidates_exact_order(C:State,dynamics:str)->list[RawMove]:
    out=[]
    fnc=frontier_neighbor_counts(C)
    for u in boundary(C):
        if dynamics=='D1':
            vs=[]
            for v in neighbors(u):
                if v in C: continue
                if fnc.get(v,0)-1 >= 1: vs.append(v)
        elif dynamics=='D2':
            vs=[v for v,cnt in fnc.items() if v!=u and cnt-(1 if u in set(neighbors(v)) else 0)>=1]
        else: raise ValueError(dynamics)
        for v in vs:
            d=delta_g(C,u,v)
            if d<0: out.append(RawMove(u,v,d))
    return out

def select_move_fast(C:State,dynamics:str,tie_id:str)->Move|None:
    raws=raw_descending_candidates_exact_order(C,dynamics)
    if not raws:return None
    G=energy_fast(C)
    for d in sorted({m.delta for m in raws}):
        legal=[]
        for rm in raws:
            if rm.delta!=d: continue
            Cp=frozenset((C-{rm.u})|{rm.v})
            if len(Cp)!=len(C) or pure_translation_equiv(C,Cp) or not connected(Cp) or not hole_free(Cp): continue
            Gp=energy_fast(Cp)
            if Gp-G!=d: raise AssertionError(('delta mismatch fast',G,Gp,d,rm))
            if not Gp<G: raise AssertionError('strict descent mismatch fast')
            legal.append(Move(rm.u,rm.v,d,Cp,canonical_state(Cp)))
        if legal:
            if tie_id=='T0_CANONICAL_MIN':
                return min(legal,key=lambda m:(m.next_canonical,canonical_move_key(m.next_state,m.u,m.v)))
            if tie_id=='T1_CANONICAL_MAX':
                return max(legal,key=lambda m:(m.next_canonical,canonical_move_key(m.next_state,m.u,m.v)))
            if tie_id=='T2_ORIENTATION_MOVE_LEX':
                return min(legal,key=lambda m:current_orientation_move_key(C,m.u,m.v))
            raise ValueError(tie_id)
    return None
