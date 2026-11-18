"""Python 3.10+, actual 61-mode operators only. Required inputs are documented in the note."""
import argparse
import hashlib
import json
import os
import sys
from collections import Counter
from fractions import Fraction as F
from math import lcm
from pathlib import Path

# All input programs, inspected prefixes, candidate rules and epsilon fixed before native generation.
FIXTURES=((15,2,4),(51,2,4),(21,2,4))
DEPTHS=(3,4)
EPS=F(1,2)
BANK='79491e65feec104f2cdc9de510263efef749d8a1174f9cab4c20146a0171615c'
SOURCE_PINS={'check_return_defect.py':'87239d347e2a52b2a2f145cbe12f0de62b9d7d5d80fa0d60dd7fbb3140caa1b2',
    'source_positive_observer.py':'92fdf2ecd6e154f6593e12a4073afe3a51950a82d89437abd7521e58f6cdb80b',
    'brc_weighted_recurrent.py':'7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26'}

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(',',':'),default=str).encode()

def digest(b):
    return hashlib.sha256(b).hexdigest()

def imports(repo,stage,audit):
    rec=repo/'research_notes/directed_recovery'; pkg=rec/'20260926_C6438C'
    prior=rec/'20260926_0C08F0'
    os.environ.update(BRC_STAGE87_SOURCE=str(stage),BRC_STREAMING_PREVIOUS=str(prior),
         BRC_ZERO_ENDPOINT_SOURCE=str(prior/'adversarial/zero_endpoint_extension.py'))
    for p in (stage,pkg/'optimization/collision_analysis',pkg/'optimization/streaming',
              pkg/'optimization/lazy_modular',rec/'20260927_C6438C/qft_row_queries/gram_research',audit):
        sys.path.insert(0,str(p))
    for n,sha in SOURCE_PINS.items():
        assert digest((audit/n).read_bytes())==sha
    from check_gram_sampler import load_bank
    from lazy_streaming import SelectedStreamingProgram
    from stage45.brc_loop_recheck import CALLS,verify_vendor
    from single_walker import PointRowOracle
    import check_return_defect as rd
    assert Path(rd.__file__).resolve()==audit/'check_return_defect.py'
    vendor=verify_vendor()
    bank,record=load_bank()
    assert record['payload_sha256']==BANK
    return SelectedStreamingProgram,PointRowOracle,CALLS,bank,rd,vendor

def raw_field(state,den):
    assert all(ctrl==spect==0 for (ctrl,_,spect),v in state.items() if any(v))
    return {label:{j:F(x,den) for j,x in enumerate(vec) if x}
            for (ctrl,label,spect),vec in state.items() if any(vec) and ctrl==spect==0}

def mass(op,field):
    return op.obs('sum_row_norms',((op.dot(v,v),) for v in field.values()))

def scale(op,rows,weight):
    return {g:{i:op.obs('declared_common_scale',((weight,x),)) for i,x in row.items()}
            for g,row in rows.items() if row and weight}

def combine(op,*fields):
    out={}
    for rows in fields:
        for g,v in rows.items():
            out[g]=op.vadd(out.get(g,{}),v)
    return {g:v for g,v in out.items() if v}

def bind_word(rd,op,program,h):
    ordered=[]
    for k,bit in enumerate(h):
        T=rd.eye()
        for j in range(k):
            if h[j]:
                gate=program.bank[k-j+1]
                A={(i,jj):F(v,gate.den) for jj,col in enumerate(gate.columns)
                   for i,v in enumerate(col) if v}
                T=op.mul(A,T)
        ordered.append({ij:-v if bit else v for ij,v in T.items()})
    return list(reversed(ordered))

def discover(program,m):
    L=1<<m
    schedule=[]
    for j in range(m):
        val=program.tables[m-1-j][1];schedule.append(val)
        if val==1:
            d=1<<j
            return d,True,schedule,0
    table=program.tables[m-1]
    y=1
    for i in range(1,L):
        y=table[y]
        if y==1:
            return i,False,schedule,i
    return None,False,schedule,L-1

def certify(program,m,R):
    y=1
    records=[]
    for j in range(m):
        if (R>>j)&1:
            z=program.tables[m-1-j][y]
            records.append([m-1-j,y,z])
            y=z
    return y==1,records

def labels_for_validation(program,m):
    a=[1];t=program.tables[m-1]
    for _ in range(1,(1<<m)+1):a.append(t[a[-1]])
    return a

def partition(L,R):
    q,ell=divmod(L,2*R)
    s=max(0,ell-R); start=2*q*R+s
    Fset=[2*i*R+j for i in range(q) for j in range(R)]+list(range(2*q*R,start))
    B=min(ell,2*R-ell)
    return Fset,start,B

def statuses(R,L,verified,delta,B,mu,zero_parent,ray,passes,retain=True):
    if R<=0 or R>=L: return 'NO_SHORTENING'
    if not verified:return 'INVALID_RETURN'
    if zero_parent:return 'NO_CERTIFIED_COMPRESSION'
    if delta==0:return 'EXACT_BOUNDARY'
    if B==0 or mu<=0:return 'NO_CERTIFIED_COMPRESSION'
    if ray or passes:return 'CERTIFIED_TRUNCATION'
    return 'RETAIN_RESIDUAL' if retain else 'NO_CERTIFIED_COMPRESSION'

def coeffs_and_rows(op,rd,words,zs):
    alpha=[rd.alpha(op,words,e) for e in range(len(zs)-1)]
    field=scale(op,combine(op,*({g:v} for g,v in zip(zs,alpha))),F(1,len(alpha)))
    return alpha,field

def cost(op):
    rec=op.observer.operations
    return {'kernel_calls':len(rec),'expression_requests':op.counts['expression_requests'],
        'peak_graph_states':max((r['states'] for r in rec),default=0),
        'peak_graph_edges':max((len(r['positive_edges']) for r in rec),default=0),
        'peak_numeric_bits':max((max(x.numerator.bit_length(),x.denominator.bit_length())
            for r in rec for x in [*(F(a) for t in r['terms'] for a in t),
            F(r['signed_observation']),F(r['positive_endpoint']),F(r['negative_endpoint'])]),default=0),
        'peak_single_dense_graph_slots':max((r['states']**2 for r in rec),default=0),
        'unique_graphs_and_use_record_bytes':len(canonical([rec,op.uses])),
        'graph_use_sha256':digest(canonical([rec,op.uses]))}

def serialize(rows):
    return {str(g):{str(i):str(x) for i,x in v.items()} for g,v in rows.items()}

def fixture(api,config):
    program_class,oracle_class,calls,bank,rd,_=api
    before=len(calls)
    p=program_class(*config,bank,61)
    admission=len(calls)-before
    discovery_start=len(calls)
    discoveries={m:discover(p,m) for m in DEPTHS}
    discovery_cost=len(calls)-discovery_start
    validations={}
    for m,(d,_,_,_) in discoveries.items():
        L=1<<m
        candidates=[d]+([3*d] if 3*d<L else [])
        validations[m]={r:certify(p,m,r) for r in [1,*candidates]}
        assert not validations[m][1][0] and all(validations[m][r][0] for r in candidates)
    shared_columns=[x.report_metrics() for x in p.lazy_factory.tables.values()]
    # Separate verifier, fresh program. No verifier outputs are used by the discovery rule.
    q=program_class(*config,bank,61)
    frontier={():q.initial()}
    output=[];totals=Counter(); layers={}; next_compare=0;nonzero_res=False;zero_controls=[];joint={};odd_signed_tail=[]
    for m in range(5):
        following={}
        if m in DEPTHS:
            d,dyadic,probes,linear=discoveries[m]
            assert d is not None
            zs=labels_for_validation(q,m); L=1<<m
            assert zs[d]==1 and all(zs[i]!=1 for i in range(1,d))
            candidates=[d] + ([3*d] if 3*d<L else [])
            assert all(zs[r]==1 for r in candidates)
            layers[m]={'square_schedule_columns_at_one':probes,'linear_discovery_steps':linear,
                       'first_return':d,'dyadic':dyadic,'candidates':candidates,
                       'modular_return_proofs':validations[m],
                       'invalid_or_out_of_range_control':[statuses(1,L,validations[m][1][0],0,0,0,False,False,False),
                       statuses(L,L,True,0,0,0,False,False,False)]}
        for h,(state,den) in frontier.items():
            if m<4:
                plan=q.branch_plan(state,den,h)
                for bit in (0,1):
                    if plan.masses[bit]:
                        following[h+(bit,)]=q.materialize(plan,bit)
                    elif m==0:
                        z,zd=q.materialize(plan,bit)
                        assert not raw_field(z,zd)
                        zero_controls.append({'h':str(bit),'parent_raw_mass':str(plan.masses[bit]),
                             'child_field':{},'subsequent_normalized_readouts':0,
                             'status':statuses(2,8,True,0,0,0,not bool(plan.masses[bit]),False,False)})
            if m not in DEPTHS: continue
            op=rd.Ops();words=bind_word(rd,op,q,h);word_cost=cost(op)
            alpha,field=coeffs_and_rows(op,rd,words,zs)
            assert field==raw_field(state,den)
            nonzero_res |= any(i>=2 for v in field.values() for i in v)
            if dyadic:
                assert not any(h[:m-(d.bit_length()-1)])
                assert all(alpha[e]==alpha[e%d] for e in range(L))
                unique={zs[i]:alpha[i] for i in range(d)}
                assert scale(op,unique,F(1,d))==field and mass(op,field)==F(1,d)
                if m==config[2]:
                    row_masses={str(g):op.dot(v,v) for g,v in field.items()}
                    assert set(row_masses.values())=={F(1,d*d)}
                    joint[''.join(map(str,h))]={g:str(x) for g,x in row_masses.items()}
            # Supplemental theorem check. This does not enter the predefined candidate count.
            if d>1 and d%2 and h==(0,)*(m-1)+(1,):
                whole,partial=divmod(L,d)
                odd_rows=partial if whole%2==0 else d-partial
                assert mass(op,field)==F(odd_rows,L*L)
                for R in range(d,L,d):
                    valid,proof=certify(q,m,R)
                    assert valid
                    fs,start,blen=partition(L,R)
                    left=L%(2*R)
                    sign=1 if R%2 or left<R else -1
                    assert left not in (0,R) and blen
                    w=scale(op,combine(op,*({zs[e]:alpha[e]} for e in range(start,start+blen))),F(1,L))
                    assert w==scale(op,field,sign)
                    jval=rd.carry(op,words,R,rd.eye())
                    delta=op.obs('odd_signed_tail_defect',((2,L-R),(2,jval)))
                    assert delta==(0 if R%2 else 4*(L-R))
                    descendants=0
                    if m<config[2]:
                        cd=lcm(*(v.denominator for row in w.values() for v in row.values()))
                        cs={(0,g,0):tuple(int(v.get(i,0)*cd) for i in range(61)) for g,v in w.items()}
                        cp=q.branch_plan(cs,cd,h)
                        assert cp.masses==plan.masses
                        for bit in (0,1):
                            sa,da=q.materialize(cp,bit);sb,db=q.materialize(plan,bit)
                            assert raw_field(sa,da)==scale(op,raw_field(sb,db),sign)
                            descendants+=1
                    odd_signed_tail.append({'h':''.join(map(str,h)),'R':R,'return_certificate':proof,
                        'd':d,'L':L,'J':str(jval),'Delta':str(delta),'tail_start':start,'B':blen,
                        'parent_mass':str(mass(op,field)),'actual_signed_tail_multiplier':sign,
                        'actual_descendant_fields_compared':descendants})
            for R in candidates:
                Fset,start,B=partition(L,R)
                # Differential cost: certificate-only carry call, before separate validation.
                co=rd.Ops()
                J=rd.carry(co,words,R,rd.eye())
                Delta=co.obs('defect_from_J',((2,L-R),(2,J)))
                delta_cost=cost(co)
                pairs=[op.vadd(alpha[i],alpha[i+R]) for i in range(L-R)]
                assert Delta==op.obs('direct_delta',((op.dot(v,v),) for v in pairs))
                if dyadic:assert J==L-R and Delta==4*(L-R)
                tail=scale(op,combine(op,*({zs[e]:alpha[e]} for e in range(start,start+B))),F(1,L))
                residual=scale(op,combine(op,*({zs[e]:pairs[e]} for e in Fset)),F(1,L))
                assert combine(op,tail,residual)==field
                mu=mass(op,tail);Pmax=max(Counter(zs[i] for i in Fset).values(),default=0)
                ok=bool(mu and Pmax*Delta<=EPS**2*L**2*mu)
                ray=bool(dyadic and B)
                if ray:
                    assert scale(op,field,F(B,L))==tail
                status=statuses(R,L,True,Delta,B,mu,False,ray,ok)
                totals[status]+=1
                if (ray or Delta==0) and m<4:
                    # Reconstruct raw child plan from tail only (same program/unchanged histories).
                    keys={g:tuple(v.get(i,F(0)) for i in range(61)) for g,v in tail.items()}
                    common=lcm(*(x.denominator for v in keys.values() for x in v))
                    st={(0,g,0):tuple(int(x*common) for x in v) for g,v in keys.items()}
                    tp=q.branch_plan(st,common,h)
                    scale_to_tail=F(B,L) if ray else F(1)
                    assert tp.masses==tuple(scale_to_tail**2*x for x in plan.masses)
                    for bit in (0,1):
                        cs,cd=q.materialize(tp,bit)
                        vs,vd=q.materialize(plan,bit)
                        assert raw_field(cs,cd)==scale(op,raw_field(vs,vd),scale_to_tail)
                    next_compare+=2
                # Locate at least one counterexample at every positive-defect history via actual pairs;
                # also run the independent audited restricted carry bisection once per (fixture,depth).
                witness=next((i for i,v in enumerate(pairs) if v),None)
                restricted=None
                if Delta and h==min(frontier) and R==d:
                    restricted=rd.locate_defect(op,words,R)
                    assert restricted and op.dot(pairs[restricted['f']],pairs[restricted['f']])>0
                output.append({'h':''.join(map(str,h)),'R':R,'J':str(J),'Delta':str(Delta),
                    'Pmax':Pmax,'tail_start':start,'B':B,'verified_tail_mu':str(mu),
                    'prefix_mass':str(mass(op,field)),'old_square_test':ok,'dyadic_ray':ray,
                    'status':status,'decision_path':('exact_signed_cancellation' if Delta==0 else
                    'proved_positive_ray' if ray else 'audited_squared_gate' if ok else 'retain_full_information'),
                    'mass_interval_width':'0','first_failed_pair':witness,
                    'restricted_carry_witness':restricted,'carry_only':delta_cost})
            # Separate exact point-row baseline on the same public labels and actual history.
            oracle=oracle_class(q,h,query_budget=1000)
            for g in set(zs[:-1]):
                rr=oracle.query(m,g)
                assert {i:F(x,rr.den) for i,x in enumerate(rr.values) if x}==field.get(g,{})
            output[-1]['ordered_feedback_word_construction']=word_cost
            metrics=oracle.report()
            output[-1]['point_row_check_same_labels']={
                k:metrics[k] for k in ('distinct_queries','query_requests','native_phase_vector_applications',
                    'actual_positive_path_observations','max_numerator_bits','max_denominator_bits','cached_row_scalar_slots')}
        frontier=following
    if discoveries[config[2]][1]:
        assert len(joint)==discoveries[config[2]][0]
    assert nonzero_res or config[0]==15
    return {'N_a_t':config,'full_dimension':61,'admission_core_calls_after_bank_load':admission,
            'shared_candidate_discovery_extra_core_calls':discovery_cost,'shared_modular_tables_after_discovery':[
            {k:v for k,v in t.items() if k in ('computed_columns','setup_adder_digit_replays',
                'column_adder_digit_replays','column_requests','peak_cached_columns')} for t in shared_columns],
            'supplemental_odd_order_signed_tails':odd_signed_tail,'terminal_dyadic_joint_masses':joint,'zero_mass_native_controls':zero_controls,'layers':layers,'cases':output,'status_counts':dict(totals),'next_branch_fields_compared':next_compare,
            'nonzero_outside_first_two':nonzero_res,'exact_full_field_verifier_metrics':q.report_metrics()}

def main():
    ap=argparse.ArgumentParser()
    for name in ('repo','stage','audit'):ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--ledger',type=Path,help='Also export the replayed data as an independent cost ledger')
    a=ap.parse_args()
    api=imports(a.repo.resolve(),a.stage.resolve(),a.audit.resolve())
    data=[fixture(api,c) for c in FIXTURES]
    assert set.union(*(set(c['status_counts']) for c in data))>={'EXACT_BOUNDARY','CERTIFIED_TRUNCATION','NO_CERTIFIED_COMPRESSION','RETAIN_RESIDUAL'}
    assert data[0]['zero_mass_native_controls'] and data[1]['zero_mass_native_controls']
    assert statuses(1,8,False,0,0,0,False,False,False)=='INVALID_RETURN'
    assert statuses(8,8,True,0,0,0,False,False,False)=='NO_SHORTENING'
    assert statuses(2,8,True,4,2,0,False,False,False)=='NO_CERTIFIED_COMPRESSION'
    if a.ledger:
        a.ledger.write_text(json.dumps(data,default=str,indent=1,sort_keys=True)+'\n')
    print(json.dumps({'baseline_inputs_and_budget':{'fixtures':FIXTURES,'depths':DEPTHS,'epsilon':'1/2',
        'discover':'first squared column at 1, else at most L-1 typed repeated columns',
        'candidates':'first return d and 3d if below L','production_samples':0,'retries':0,
        'assessment':'exact bounded fields, no statistical estimate or timing speedup'},
        'operator_source_hashes':SOURCE_PINS,'bank_payload_sha256':BANK,
        'native_vendor':api[-1],'cases':data},default=str,indent=1,sort_keys=True))

if __name__=='__main__':main()
