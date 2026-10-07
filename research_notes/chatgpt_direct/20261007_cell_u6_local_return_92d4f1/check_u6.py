#!/usr/bin/env python3
"""U6 exact BRC certificates: clock elimination, escape and local exposure.
All statements are conditional on the unchanged U5 response circuit.
No native force, physical probability/time, or prime assertion is made.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import hashlib, importlib.util, sys, json, gzip
ROOT=Path(__file__).resolve().parent
SRC=ROOT/'lifecycle.py'
if not SRC.exists():
    SRC=ROOT.parent/'20261007_cell_u5_lifecycle_3e72b9'/'lifecycle.py'
b=SRC.read_bytes()
if hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()!='389bd51a2a71a62a4c533ef781920bef00783bc3':
    raise RuntimeError('U5 source pin mismatch')
spec=importlib.util.spec_from_file_location('u6_pinned_u5',SRC)
u=importlib.util.module_from_spec(spec);sys.modules[spec.name]=u;spec.loader.exec_module(u)
c,r,o=u.c,u.r,u.o
checks=0

def ck(ok,label):
    global checks
    checks+=1
    if not ok: raise AssertionError(label)

def put(dst,key,value):
    dst[key]=r.merge(dst.get(key,r.brc.CWM_ZERO),value)

def scale(value,weight):
    return r.serial(value,r.edge(weight)) if weight else r.brc.CWM_ZERO

def phi(z):
    # An auxiliary comparison observer, NOT energy, a number shell, or a force.
    return Q(1,1+sum(x*x for x in z))

def potential(z,cells):
    return r.total(r.edge(phi(tuple(x-y for x,y in zip(z,a)))) for a in cells).total

rho=Q(1,4);eps=Q(1,8);transport=c.RetainedField(rho)
normalizer=r.edge(1/rho)
mat={p:tuple((q,r.serial(v,normalizer)) for q,v in transport.material[p]) for p in r.PORTS}
bulk=tuple((q,r.serial(v,normalizer)) for q,v in transport.bulk)
for p,col in mat.items():
    ck(r.total(v for q,v in col).total==1,'spatial jump column mass')
    for q,v in col:
        ck(v.total==(Q(1,3) if p==q else Q(1,15)),'unchanged default incidence')

# Representative absolute-coordinate partitions; the all-X6 proof is symbolic.
# Each signed permutation has the same bulk potential average.
potential_cases=0
for z in combinations_with_replacement(range(5),6):
    S=sum(x*x for x in z)
    avg=r.total(scale(r.edge(phi(r.advance(z,q))),Q(1,12)) for q in r.PORTS).total
    bound=(5*Q(1,S+2)+Q(S+2,S*S+4))/6
    gap=Q((S-1)**2+11,3*(S+1)*(S+2)*(S*S+4))
    ck(avg<=bound,'convex rational upper bound')
    ck(phi(z)-bound==gap and gap>0,'symbolic superharmonic comparison identity')
    potential_cases+=1

z=r.ZERO;e1=r.direction(0);e2=r.direction(2)
def plus(a,b): return tuple(x+y for x,y in zip(a,b))
layouts={'adjacent_pair':(z,e1),'gap_pair':(z,plus(e1,e1)),
         'square_221':(z,e1,plus(e1,e2),e2)}

# A normalized spatial ray is a device for total-response bounds, not matter.
# First hits are kept in a separate positive sector, not discarded.
def first_return_prefix(cells,anchor,port,steps=4):
    occupied=set(cells);layer={(anchor,port):r.brc.CWM_ONE};hits={};history=[]
    for n in range(1,steps+1):
        nxt={};row={}
        for (cell,p),v in sorted(layer.items()):
            for q,w in mat[p] if cell in occupied else bulk:
                key=(r.advance(cell,q),q^1);vv=r.serial(v,w)
                put(row if key[0] in occupied else nxt,key,vv)
        hit=r.total(row.values());hits[n]=hit;layer=nxt
        ck(r.total(hits.values()).total+r.total(layer.values()).total==1,'first-hit/survivor partition')
        future_bound=r.total(scale(v,min(Q(1),potential(cell,cells)))
                             for (cell,p),v in sorted(layer.items())).total
        history.append({'jumps':n,'new_hit':hit,'hit_prefix':r.total(hits.values()).total,
                        'survivor_total':r.total(layer.values()).total,
                        'all_future_hit_upper':min(Q(1),r.total(hits.values()).total+future_bound),
                        'survivor_states':len(layer)})
    return history

# Explicit disjoint escape paths, followed by a proved infinite no-return bound.
def escape_certificate(cells):
    unused=[j for j in range(6) if len({a[j] for a in cells})==1]
    steps=2 if len(cells)==4 else 1
    bounds=[];records=[]
    for anchor in cells:
        for p in r.PORTS:
            value=r.brc.CWM_ZERO
            for q,w in mat[p]:
                if r.axis(q) not in unused: continue
                state=w;cell=r.advance(anchor,q);path=[anchor,cell]
                ck(cell not in cells,'escape leaves all material cells')
                for _ in range(steps-1):
                    state=r.serial(state,dict(bulk)[q]);cell=r.advance(cell,q);path.append(cell)
                    ck(cell not in cells,'escape path has no premature material return')
                psi=potential(cell,cells)
                ck(psi<1,'infinite exterior escape probability lower bound positive')
                value=r.merge(value,scale(state,1-psi))
                records.append({'anchor':anchor,'incoming':p,'path':path,
                                'path_CWM':state,'potential_upper':psi})
            bounds.append(value.total)
    delta=min(bounds)
    r.CALLS['one_state_recurrent_cwm']+=1
    visits=r.brc.one_state_recurrent_cwm([1-delta])
    ck(visits.total_mass_stable,'return budget series converges')
    visit_bound=visits.total_mass_closure
    # Active visits at a spatial vertex have expected count 1/rho.
    local_bound=scale(r.edge(visit_bound),Q(len(cells))/rho).total
    return {'escape_lower':delta,'return_upper':1-delta,'jump_visit_bound':visit_bound,
            'local_active_exposure_bound':local_bound,'all_port_bounds':bounds,'paths':records}

certs={name:escape_certificate(cells) for name,cells in layouts.items()}
ck(certs['adjacent_pair']['escape_lower']==Q(1,9),'adjacent exact uniform escape certificate')
ck(certs['gap_pair']['escape_lower']==Q(2,9),'gap exact uniform escape certificate')
ck(certs['square_221']['escape_lower']==Q(68,4725),'square exact uniform escape certificate')
returns={}
for name,cells in layouts.items():
    returns[name]={}
    for p in (0,1,4):
        h=first_return_prefix(cells,cells[0],p)
        for row in h:
            ck(row['hit_prefix']<=certs[name]['return_upper'],'finite return below all-future bound')
        returns[name][p]=h

# Exact finite waiting words and their unchanged spatial distribution.
# A->D and D->A stay at the exact old key; only A->jump uses the spatial table.
clocks=[]
for epsilon in (Q(1,8),Q(1,4),Q(3,4)):
    for p in r.PORTS:
        A=r.brc.CWM_ONE;D=r.brc.CWM_ZERO;out={};active_visits=[]
        for n in range(1,33):
            active_visits.append(A)
            for q,w in mat[p]: put(out,q,r.serial(scale(A,rho),w))
            A,D=scale(D,epsilon),r.merge(scale(A,1-rho),scale(D,1-epsilon))
            moved=r.total(out.values()).total
            ck(moved+A.total+D.total==1,'waiting or already moved, all budget retained')
            for q,w in mat[p]: ck(out[q].total==moved*w.total,'waiting leaves spatial law unchanged')
        r.CALLS['one_state_recurrent_cwm']+=1
        active_series=r.brc.one_state_recurrent_cwm([1-rho])
        ck(active_series.total_mass_closure==1/rho,'all-waiting-words active exposure')
        ck(r.total(active_visits).total<=1/rho,'finite exposure bounded by exact full clock sum')
        clocks.append({'epsilon':epsilon,'incoming':p,'survival_at32':A.total+D.total,
                       'active_exposure_prefix32':r.total(active_visits).total,
                       'active_exposure_all':active_series.total_mass_closure})

# Original U5 circuit at fixed layouts. No artificial wall/reset or new injection.
# These finite local measurements illustrate; they do not prove infinite escape.
fields={}
for name in ('gap_pair','square_221'):
    cells=layouts[name];seed=r.edge(Q(1,12));N=len(cells)
    A={(b,cell,p):seed for b,cell in enumerate(cells) for p in r.PORTS};D={};rows=[]
    cumulative=r.brc.CWM_ZERO
    for n in range(7):
        local=r.total(v for (s,cell,p),v in A.items() if cell in cells)
        cross=r.total(v for (s,cell,p),v in A.items() if cell in cells and cells.index(cell)!=s)
        dormant_local=r.total(v for (s,cell,p),v in D.items() if cell in cells)
        cumulative=r.merge(cumulative,local)
        ck(c.total_readout(A)+c.total_readout(D)==N,'full response conservation')
        ck(c.total_readout(A)==Q(N,7)+Q(6*N,7)*Q(1,8)**n,'inherited sector recurrence')
        ck(cumulative.total<=certs[name]['local_active_exposure_bound'],'local exposure certificate')
        rows.append({'stage':n,'global_active':c.total_readout(A),'local_active':local,
                     'local_cross_source':cross,'local_dormant':dormant_local,
                     'local_active_cumulative':cumulative.total,'active_keys':len(A),'dormant_keys':len(D)})
        if n<6: A,D,part=u.local_release_step(A,D,cells,n+1,transport,eps)
    fields[name]={'rows':rows,'final_active':A,'final_dormant':D}

# Uniform controlled escape from a finite region: symbolic all-schedule bound.
# These path checks do not enumerate all time-dependent occupancy histories.
bounded={}
for name,cells in layouts.items():
    B=set(cells);R=max(abs(v) for a in cells for v in a);m=2*R+len(B)+1
    K=2*m+1;endpoint_max=Q(0)
    for a in B:
        for p in r.PORTS:
            q0=0 if (p^1)!=0 else 2
            pos=a;incoming=p
            for j in range(2*m):
                q=q0 if j%2==0 else (2 if q0==0 else 0)
                wm=dict(transport.material[incoming]).get(q,r.brc.CWM_ZERO)
                wb=dict(transport.bulk)[q]
                ck(wm.total>=rho/15 and wb.total>=rho/15,'uniform material-or-bulk escape edge')
                pos=r.advance(pos,q);incoming=q^1
            psi=potential(pos,cells);endpoint_max=max(endpoint_max,psi)
            ck(pos not in B and psi<Q(1,2),'finite-region endpoint exterior certificate')
    path=r.brc.CWM_ONE
    for j in range(2*m): path=r.serial(path,r.edge(rho/15))
    eta=scale(scale(path,eps),Q(1,2)).total
    r.CALLS['one_state_recurrent_cwm']+=1
    blocks=r.brc.one_state_recurrent_cwm([1-eta])
    C=scale(r.edge(blocks.total_mass_closure),Q(K)).total
    ck(eta>0 and C==Q(K)/eta,'uniform local occupation comparison constant')
    bounded[name]={'region_size':len(B),'m':m,'block_length':K,'escape_lower':eta,
                   'max_endpoint_potential':endpoint_max,'per_unit_local_exposure_upper':C,
                   'proof_scope':'ANY_SCHEDULE_WITH_MATERIAL_CELLS_IN_THIS_REGION'}

# Missing waiting clock invalidates transient stationary localization.
# Symbolic certificate, not a numerical eigensolver: D=(1-rho)/epsilon F,
# F=rho P F+epsilon D => F=P F. Finite local exposure rules out nonzero l1 F.

summary={'status':'CONDITIONAL_U5_NO_LOCALIZATION_CERTIFICATE',
 'event_id':'EM-20261007-CELL-U6-LOCAL-RETURN-92D4F1','checks':checks,
 'BRC_calls':dict(r.CALLS),'potential_representatives':potential_cases,
 'parameters':{'rho':str(rho),'epsilon':str(eps)},
 'certificates':{name:{k:str(v) for k,v in row.items() if k not in ('paths','all_port_bounds')}
                 for name,row in certs.items()},
 'bounded_region_certificates':c.encode(bounded),
 'first_return_prefixes':c.encode(returns),
 'local_prefixes':{name:c.encode(v['rows']) for name,v in fields.items()},
 'holding_preserves_spatial_jump_chain':True,
 'fixed_finite_material_local_active_sum_finite':True,
 'fixed_finite_material_local_active_and_dormant_tend_zero':True,
 'nonzero_finite_mass_stationary_response_impossible':True,
 'bounded_material_schedule_extension':'PROVED_SYMBOLICALLY_NOT_ENUMERATED',
 'stopped_at_region_exit_trajectory_TV_bound':'min(1,C_B*(active_l1+dormant_l1)/kappa)',
 'unbounded_comoving_localization':'UNRESOLVED',
 'native_force':False,'prime_claim':False,'physical_time':False,'independent_review':False}
trace={'escape_certificates':certs,'first_returns':returns,'holding_clocks':clocks,'bounded_regions':bounded,'fields':fields}
raw=(json.dumps(c.encode(trace),sort_keys=True,separators=(',',':'))+'\n').encode()
compressed=gzip.compress(raw,mtime=0)
summary['trace_sha256']=hashlib.sha256(raw).hexdigest();summary['trace_bytes']=len(raw)
summary['trace_compressed_sha256']=hashlib.sha256(compressed).hexdigest()
ev=ROOT/'evidence';ev.mkdir(exist_ok=True)
(ev/'full_trace.json.gz').write_bytes(compressed)
(ev/'results.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k not in ('first_return_prefixes','local_prefixes')},indent=2))
for name,v in fields.items():
    print(name,[(x['stage'],str(x['local_active'].total),str(x['local_cross_source'].total)) for x in v['rows']])
