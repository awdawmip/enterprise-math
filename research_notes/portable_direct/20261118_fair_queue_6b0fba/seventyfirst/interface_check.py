from pathlib import Path
import contextlib,io,runpy,itertools,json,hashlib
import argparse
ap=argparse.ArgumentParser(); ap.add_argument('--repo',type=Path,required=True); root=ap.parse_args().repo
n30=root/'experiments/x6_network_event_ledger_v29_20260906/check_event_order_holonomy.py'
n43=root/'experiments/x6_nonfcc_observer_switch_v42_20260906/check_nonfcc_observer_switch.py'
ntriad=root/'experiments/x6_triadic_atomic_scatter_v1_20260906/check_triadic_atomic_scatter.py'
nrot=root/'experiments/x6_triadic_rotation_v1_20260906/check_triadic_rotation.py'
nclock=root/'experiments/x6_native_event_time_v1_20260906/check_event_time_markov.py'
nbrc=root/'experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py'
closure_spec=root/'research_notes/X6_TRIADIC_INNER_C12_RELATION_CLOCK_V2_20260906.md'
assert hashlib.sha256(closure_spec.read_bytes()).hexdigest()=='34c42b94713411a16ba74e1f557fdb4580f9a954c4c63e9446f22b1db9612064'
assert [hashlib.sha256(x.read_bytes()).hexdigest() for x in (n30,n43,ntriad,nrot,nclock,nbrc)]==['184c5954d9211f8c2c1ee55972008d6b5b324b60e4c7c64a7ca3fef6046673d4', 'b00d3a283b84bf2082eeb0e69b4d750eaf18fd38b90c36f6e1d711eca15763d2', '6e843f505807d9d68d9847a9e55e575e7663b6321151a08b8c4fcc7cdf45e579', '42a04380e294281e56fca8c26cb278bfdcd0c2d668b119f25a29dc9ec6f9c477', '1474c65dba67c6eecfd6aabb54181f686bd6ce20b370614c60b0123daa8b2d91', '6f0d79a519c53fed1300b3fabf500c34e30aa46cdd63b409fa6ecc115071ecb4']
with contextlib.redirect_stdout(io.StringIO()):
 r=runpy.run_path(str(n30));s=runpy.run_path(str(n43)); tri=runpy.run_path(str(ntriad)); rot=runpy.run_path(str(nrot)); clock=runpy.run_path(str(nclock))
S=r['S0']; lift=s['edge_lift']; comp=s['compose']; mm=s['matS']; V=s['V']
ops=[]
for order in [(r['A'],r['B']),(r['B'],r['A'])]:
 ret=r['run'](order);path=ret[3];f=s['ID']
 for a,b in zip(path,path[1:]):f=comp(lift(a,b),f)
 t=path[-1];perm=tuple(S.index(f.index(j)) for j in t)
 assert perm==ret[5]
 def block(x,t=t,f=f):
  return s['mv'](mm(t),[x[S.index(f.index(j))] for j in t])
 ops.append((block,path,perm,f))
def decode(out):
 x,y,z=out
 assert y-x==z # V3=(1,0,-1),V4=(0,1,1), giving z=y-x

 return (x,y)

f,g=(z[0] for z in ops)
basis=[(1,0,0),(0,1,0),(0,0,1)]
for a,b,c in itertools.product(range(-6,7),repeat=3):
 x=(a,b,c);u,v=decode(f(x));u2,w=decode(g(x))
 assert u==u2==a+c and v==b+c and w==a+b
 assert (u+w-v,v+w-u,u+v-w)==(2*a,2*b,2*c)
mod_counts={}
for q in range(2,17):
 fibers={}
 for x in itertools.product(range(q),repeat=3):
  a=decode(f(x));b=decode(g(x))
  key=tuple(y%q for y in (a[0],a[1],b[1])); fibers[key]=fibers.get(key,0)+1
 assert set(fibers.values())==({2} if q%2==0 else {1})
 mod_counts[q]=[len(fibers),max(fibers.values())]
qS=tri['q_triad'](S); qT=tri['q_triad'](ops[0][1][-1])
tau=clock['succ']; frames=clock['cycle']
assert qS==rot['q_triad'](S) and qT==rot['q_triad'](ops[0][1][-1])
o=tri['power'];compose=tri['compose']; brc=tri['brc']
checks=0
for (fun,path,perm,up),orient in zip(ops,(1,-1)):
 signed=tuple(z+1 for z in up)
 for t in range(6):
  assert compose(signed,o(qS,t))==compose(o(qT,(orient*t)%6),signed)
  for i in S:
   z=tri['unit'](i)
   lhs=tri['act'](signed,tri['act'](o(qS,t),z))
   rhs=tri['act'](o(qT,(orient*t)%6),tri['act'](signed,z))
   assert lhs==rhs
   checks+=1
 def reflect(x):
  kind,j=x
  if orient>0: return x
  return (kind,(-j-int(kind=='Kappa'))%6)
 tauinv={v:k for k,v in tau.items()}
 for x in frames:
  assert reflect(tau[x])==(tau if orient>0 else tauinv)[reflect(x)]
# V2's decorated closure records the directed port matching, even when all
# branches have the same pivot. Keep token names 0,1,2 in source-frame order.
def apply_frame(operator, frame):
    return tuple(tri['act'](operator, pos) for pos in frame)

def closure(frame, target):
    assert len(set(frame)) == len(set(target)) == 3
    return (tri['ZERO'], frame, target, tuple(zip(range(3), frame, target)))

def reverse_closure(event):
    pivot, src, dst, matching = event
    return pivot, dst, src, tuple((name, end, start) for name, start, end in matching)

def transport_closure(operator, event):
    pivot, src, dst, matching = event
    return (tri['act'](operator,pivot), apply_frame(operator,src), apply_frame(operator,dst),
            tuple((name,tri['act'](operator,start),tri['act'](operator,end))
                  for name,start,end in matching))

source_frame = tuple(tri['unit'](i) for i in S)
fixed_frame = tuple(tri['unit'](i) for i in ops[0][1][-1])
fixed_shells = [apply_frame(o(qT,k),fixed_frame) for k in range(6)]
decorated_checks = {}
for label, (_, _, _, up), orient in zip(('AB','BA'), ops, (1,-1)):
    transport = tuple(x+1 for x in up)
    target_zero = apply_frame(transport,source_frame)
    target_shells = [apply_frame(o(qT,k),target_zero) for k in range(6)]
    phase_on_fixed_frame = [k for k,frame in enumerate(fixed_shells) if target_zero == frame]
    assert phase_on_fixed_frame == ([4] if orient == 1 else [])
    forward = [closure(target_shells[k],target_shells[(k+1)%6]) for k in range(6)]
    directly_forward = 0
    after_duality = 0
    for r_index in range(6):
        before = apply_frame(o(qS,r_index),source_frame)
        after = apply_frame(qS,before)
        transported = transport_closure(transport,closure(before,after))
        k = (orient*r_index)%6
        assert transported == closure(target_shells[k],target_shells[(k+orient)%6])
        if orient == 1:
            assert transported == forward[k]
            directly_forward += 1
        else:
            assert transported not in forward
            assert reverse_closure(transported) == forward[(k-1)%6]
            after_duality += 1
    decorated_checks[label] = {
        "fixed_target_initial_phases": phase_on_fixed_frame,
        "directed_matches_with_transport_orientation": 6,
        "direct_positive_closure_matches": directly_forward,
        "reversed_matching_matches_with_positive_closure": after_duality}
# Compare actual atomic shortest options and INNER closure before/after the two paths.
cases=0
for _,path,_,up in ops:
 signed=tuple(z+1 for z in up)
 for signs in itertools.product((-1,1),repeat=3):
  starts=[tri['unit'](i,sign) for i,sign in zip(S,signs)]
  targets=[tri['act'](qS,x) for x in starts]
  opts=[tri['midpoint_options'](x,y) for x,y in zip(starts,targets)]
  transported=[tri['midpoint_options'](tri['act'](signed,x),tri['act'](signed,y)) for x,y in zip(starts,targets)]
  assert all(tuple(tri['act'](signed,z) for z in a)==b for a,b in zip(opts,transported))
  assert [mid for mid in itertools.product(*transported) if mid[0]==mid[1]==mid[2]]==[(tri['ZERO'],)*3]
  cases+=1
print(json.dumps(dict(abstract_clock_reversal_certified=True,directed_closure_comparisons=decorated_checks,axes_conjugacy_checks=checks,transported_signed_scatter_cases=cases,raw_hashes=[hashlib.sha256(p.read_bytes()).hexdigest() for p in (n30,n43,ntriad,nrot,nclock,Path(brc.__file__),closure_spec)],source_axes=S,paths=[z[1] for z in ops],slot_maps=[z[2] for z in ops],full_A6=[z[3] for z in ops],ABC_raw_FCC=[[fun(x) for x in basis] for fun in (f,g)],cube_signed_trials=13**3,reciprocal_moduli=mod_counts),indent=2))
