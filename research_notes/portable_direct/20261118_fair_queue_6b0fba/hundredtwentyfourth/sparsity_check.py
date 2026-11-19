"""Exact final-report and named-label tests for a one-positive-word approximation."""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from hashlib import sha256
import importlib.util
from itertools import product
import json
from math import gcd
from pathlib import Path


def edge_changes(counts, mask):
    # Scale the signed change in zero-report mass at this target by 4Q^2.
    return [(x*x+y*y)*int((mask >> i) & (mask >> ((i+1)%len(counts))) & 1) - 2*x*y
            for i,x in enumerate(counts) for y in (counts[(i+1)%len(counts)],)]


def schedule(d, Q):
    shift = pow(2,-1,d)
    return [Q//d+int(i*shift % d < Q%d) for i in range(d)]


def dense_predictions(Q, d):
    k, r = divmod(Q,d)
    j = min(r,d-r)
    h = k+int(r>d//2)
    C, S = 2*j, d-2*j
    wc, ws = 2*k*(k+1)+1, 2*h*h
    assert gcd(wc,ws)==1
    # The congruence directly returns all broken-same counts.
    v0 = (C * pow(ws,-1,wc)) % wc
    minima = {}
    for v in range(v0,min(S,C//ws)+1,wc):
        u = (C-ws*v)//wc
        if 0<=u<=C and u+v>=2:
            minima[2*(C-u)] = d-u-v+1
    return minima


def sparse_predictions(Q,d):
    H=max(0,2*Q-d)
    if H==0:
        return {0:0}
    if d-Q==1:
        return {0:H+1}
    return {4*b:H+b+1 for b in range(min(H,d-Q)+1)}


def portable():
    cases = masks = 0
    samples = {}
    for d in range(3,14,2):
        for t in range(1,8):
            Q=2**t
            counts=schedule(d,Q)
            optimal, joint_by_size = {}, {}
            for mask in range(1<<d):
                diff = edge_changes(counts,mask)
                joint = sum(map(abs,diff))
                size = mask.bit_count()
                joint_by_size[size] = min(joint_by_size.get(size,joint),joint)
                if sum(diff)==0:
                    optimal[joint] = min(optimal.get(joint,size),size)
            if Q>d:
                assert optimal==dense_predictions(Q,d)
                k,r=divmod(Q,d)
                j=min(r,d-r)
                h=k+int(r>d//2)
                benefits=sorted([2*k*(k+1)-1]*(2*j)+[2*h*h]*(d-2*j),reverse=True)
                base=2*k*(k+1)*2*j+2*h*h*(d-2*j)
                for n in range(d+1):
                    kept=d if n==d else max(0,n-1)
                    assert joint_by_size[n]==base-sum(benefits[:kept])
            else:
                assert optimal==sparse_predictions(Q,d)
            masks+=1<<d
            cases+=1
            if t==3:
                samples[d]={str(F(w,4*Q**2)):n for w,n in sorted(optimal.items())}
    dense_family=[]
    for t in range(5,18,2):
        Q=2**t
        d=3*Q//4+1
        r=Q-d
        minima=dense_predictions(Q,d)
        assert min(minima.values())==d-r+1
        assert minima[4*r]==d-r+1
        dense_family.append(dict(t=t,d=d,deleted=r-1,report_tv='0',joint_tv=str(F(r,Q**2))))
    return dict(direct_mask_cases=cases,direct_masks=masks,final_t3_exact_reports=samples,
                analytic_dense_family=dense_family)


def load_old():
    source=Path(__file__).resolve().parent.parent/'eightieth'/'gauge_check.py'
    assert sha256(source.read_bytes()).hexdigest()==OLD_SHA
    spec=importlib.util.spec_from_file_location('source80',source)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def actual(repo,stage):
    old=load_old()
    native,Oracle,normalize,calls=old.load_native(repo,stage)
    from single_walker import transition_plan
    results=[]
    for N,base,d in [(7,2,3),(31,2,5),(19,4,9),(23,2,11),(53,16,13)]:
        program=type(native)(N,base,4,native.bank,61)
        assert tuple(program.bank[2].apply_numer((1,)+(0,)*60)) == (0,-program.bank[2].den)+(0,)*59
        assert pow(base,d,N)==1 and all(pow(base,i,N)!=1 for i in range(1,d))
        tags=[pow(base,i,N) for i in range(d)]  # Next permutation is multiplication by base.
        labels=range(1<<(N-1).bit_length())
        counts=schedule(d,8)
        assert tags[0]==1
        begin=len(calls)
        src_queries=nonzero_histories=original_plans=0
        nonzero_replacement_epsilon=F(0)
        def probability(oracle,table,inverse,z):
            left=table[z]
            right=oracle.apply_feedback(len(oracle.history),table[inverse[z]])
            mass=oracle.norm_observation(left)+oracle.norm_observation(right)
            return (oracle.norm_observation(oracle.combine(left,right,halve=False))/(2*mass)
                    if mass else F(1,2))
        states={('',1):F(1)}
        final=None
        for i in range(4):
            new=defaultdict(F)
            for history in product((0,1),repeat=i):
                name=''.join(map(str,history))
                oracle=Oracle(program,history,query_budget=2000)
                inverse=oracle.inverse_table(i)
                table=[oracle.query(i,z) for z in labels]
                src_queries+=len(table)
                if any(history):
                    nonzero_histories+=1
                proposal={}
                p={}
                for z in labels:
                    mass=(states.get((name,z),F(0))+states.get((name,inverse[z]),F(0)))/2
                    proposal[z]=mass
                    p[z]=probability(oracle,table,inverse,z)
                    if name=='1':
                        assert not any(table[z].values[1:])
                        assert p[z]==F(1,2)
                        nonzero_replacement_epsilon+=sum(F(c,table[z].den)**2 for c in table[z].values)
                    if mass:
                        aux=int(states.get((name,z),F(0))==0)
                        latent=inverse[z] if aux else z
                        planned=transition_plan(oracle,latent,aux)
                        assert planned['candidate']==z and planned['bit_probability_given_proposed_label']==p[z]
                        original_plans+=1
                        new[name+'0',z]+=mass*p[z]
                        new[name+'1',z]+=mass*(1-p[z])
                if name=='000':
                    final=oracle,inverse,table,proposal,p
            states=new
            assert sum(states.values())==1
        oracle,inverse,table,proposal,p=final
        numeric={z:counts[i] for i,z in enumerate(tags)}
        for z in labels:
            assert list(map(lambda x:F(x,table[z].den),table[z].values))==[F(numeric.get(z,0),8)]+[0]*60
        words={}
        check_masks=[]
        for mask in range(1<<d):
            diff=edge_changes(counts,mask)
            if sum(diff)==0:
                joint=sum(map(abs,diff))
                if joint not in words or mask.bit_count()<words[joint].bit_count():
                    words[joint]=mask
        check_masks.extend(words.values())
        check_masks.extend([0,(1<<d)-1])
        output=[]
        for mask in dict.fromkeys(check_masks):
            forged=[normalize((0,)*61,8) for z in labels]
            for i,z in enumerate(tags):
                if mask>>i & 1:
                    forged[z]=normalize((1,)+(0,)*60,8)
            delta=[proposal[z]*(probability(oracle,forged,inverse,z)-p[z]) for z in labels]
            expected=edge_changes(counts,mask)
            # Edge i targets tag i+1, with wrap.
            assert all(delta[tags[(i+1)%d]]==F(v,256) for i,v in enumerate(expected))
            eps=sum(F((numeric.get(z,0)-int(z in tags and (mask>>tags.index(z))&1))**2,64)
                    for z in labels)
            output.append(dict(positive_slots=mask.bit_count(),initial_exponent_mask_hex=hex(mask),
                               raw_row_error=str(eps),report_tv=str(abs(sum(delta))),
                               named_joint_tv=str(sum(map(abs,delta)))))
        assert nonzero_replacement_epsilon==F(1,2)
        results.append(dict(N=N,base=base,order_checked=d,full_work_addresses=len(labels),
                            exact_transition_plan_calls=original_plans,
                            optional_history_one_zero_table_epsilon=str(nonzero_replacement_epsilon),
                            true_history_address_rows=src_queries,nonzero_feedback_histories=nonzero_histories,
                            source_brc_calls=len(calls)-begin,source_output_mass=str(sum(states.values())),
                            replacement_rows=output))
    return results


OLD_SHA='cde258c18b42104e0b01bc027ecab9aced4f03a579fb40ac285194e493f83240'


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--repo',type=Path)
    ap.add_argument('--stage',type=Path)
    ap.add_argument('--verify',type=Path)
    args=ap.parse_args()
    if bool(args.repo)!=bool(args.stage):
        ap.error('--repo and --stage must be supplied together')
    data=dict(portable=portable())
    if args.repo:
        data['native']=actual(args.repo.resolve(),args.stage.resolve())
    out=json.dumps(data,sort_keys=True,ensure_ascii=False,indent=2)+'\n'
    if args.verify:
        expected=json.loads(args.verify.read_text())
        assert all(expected[k]==v for k,v in json.loads(out).items())
        print('verified '+', '.join(data))
    else:
        print(out,end='')


if __name__=='__main__':
    main()
