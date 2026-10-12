#!/usr/bin/env python3
"""New q4 canonical M17^6 exact producer; default is LOCAL_NOT_ADMITTED.

Construction author EM-T6-B4F89F, directed/nonblind UNKNOWN helpers. Root FBF
static/canonical-codec direction and Driver4CF input/Task credits retained.
No native transport. Actual own new Task/claim/open and Source input/code
review guard must succeed before the first common/case scientific operation.
"""
import argparse,hashlib,json,os,time
from datetime import datetime,timezone
from fractions import Fraction
from pathlib import Path
from order4_exact_math_and_input import (require,load_inputs,validate_static_input,establish_operator,
                                       canonical_particular,pair,digest,blob,INPUT_SHA,COMMON_SHA)
from q4_dfs_wire import header,encode_actions
from q4_native_admission_guard import authorize,check_lease,SCOPE,SOURCE_AUTHORS

def pin(path):
    raw=Path(path).read_bytes()
    return {'path':str(Path(path).resolve()),'bytes':len(raw),'sha256':digest(raw),'git_blob_sha1':blob(raw)}

def write_json_new(path,data):
    raw=(json.dumps(data,indent=2)+'\n').encode()
    with Path(path).open('xb') as handle:handle.write(raw)
    return pin(path)

def leaf_obligations(case,vector,positive,negative):
    """Retain genuine local witnesses and all unresolved H0/lower-prime obligations."""
    residual=[case['budgets'][0]-positive,case['budgets'][1]-negative]
    moments=[Fraction(len(case['positive_atoms'])-len(case['negative_atoms'])+sum(vector))]
    for k in range(1,7):
        moment=sum((Fraction(1,(17*(17*q+r))**k) for q,r in case['positive_atoms']),Fraction(0))
        moment-=sum((Fraction(1,(17*(17*q+r))**k) for q,r in case['negative_atoms']),Fraction(0))
        moment+=sum((Fraction(x,(17*j)**k) for j,x in enumerate(vector,1)),Fraction(0))
        require(moment.denominator%17!=0,'Uncancelled p17 pole in local witness')
        moments.append(moment)
    return {'remaining_positive_budget':str(residual[0]),'remaining_negative_budget':str(residual[1]),
            'moments_M0_to_M6':[pair(x) for x in moments],
            'necessary_completion_cuts':[{'k':k,'M_k':pair(x),
                'lower':pair(-Fraction(residual[0],2**k)),'upper':pair(Fraction(residual[1],2**k)),
                'passes':-Fraction(residual[0],2**k)<=x<=Fraction(residual[1],2**k)}
                for k,x in enumerate(moments)],
            'lower_prime_completion_equations':'sum t_a/a^k = -M_k, k=0..6, a>=2 and17-free; separate weighted residual side masses',
            'maximal_p17_carrier_applicable':case['domain']=='ADMISSIBLE',
            'full_H0_or_composite_collision_established':False,'global_goal_status':'OPEN'}

def produce_case(operator,case):
    """Fresh canonical particular and complete DFS; no relaxed vector spoofing."""
    a=canonical_particular(operator,case)
    centers=[sum((x*v for x,v in zip(a[:6],row)),Fraction(0)) for row in operator['center_linear']]
    D,mu,U,w=operator['D'],operator['mu'],operator['U'],operator['weights']
    require(sum(c*c*d for c,d in zip(centers,D))==sum((x*y)**2 for x,y in zip(a,w)),
            'Full affine norm decomposition')
    require(all(d>(4 if case['quarter'] else 2)*case['radius'] for d in D),'Strict omitted-integer/path-count bound')
    actions=[];z=[0]*16;witnesses=[]
    stats={'nodes':0,'edges':0,'strict_norm_prunes':0,'sphere_leaves':0,'budget_pruned':0,'kernels':0}
    def descend(i,partial):
        stats['nodes']+=1
        center=centers[i]+sum((z[h]*mu[h][i] for h in range(i+1,16)),Fraction(0))
        f=center.numerator//center.denominator
        for choice in (-f-1,-f):
            stats['edges']+=1;z[i]=choice
            norm=partial+D[i]*(choice+center)**2
            if norm>case['radius']:
                actions.append(0);stats['strict_norm_prunes']+=1
            elif i>0:
                actions.append(1);descend(i-1,norm)
            else:
                stats['sphere_leaves']+=1
                vector=[a[j]+sum(z[h]*U[h][j] for h in range(16)) for j in range(16)]
                require(sum((x*y)**2 for x,y in zip(vector,w))==norm,'Leaf exact norm identity')
                residues=[sum(x*c for x,c in zip(vector,row))%17**k
                          for k,row in enumerate(operator['coeff'],1)]
                require(residues==case['targets'],'Leaf all six mixed congruences fail-hard')
                positive=sum(max(x,0)*weight for x,weight in zip(vector,w))
                negative=sum(max(-x,0)*weight for x,weight in zip(vector,w))
                if positive>case['budgets'][0] or negative>case['budgets'][1]:
                    actions.append(2);stats['budget_pruned']+=1
                else:
                    actions.append(3);stats['kernels']+=1
                    witnesses.append({'q0_vector':list(map(str,vector)),
                        'basis_coefficients':list(map(str,z)),
                        'signed_masses':[str(positive),str(negative)],'six_congruence_residues':list(map(str,residues)),
                        'H0_lower_prime_obligations':leaf_obligations(case,vector,positive,negative)})
            require(len(actions)<=case['action_bound'],'Uniform justified action bound exceeded')
    descend(15,Fraction(0))
    require(len(actions)==stats['edges'] and len(actions)==2*stats['nodes'],'Complete two-candidate grammar')
    return encode_actions(actions),{'case_index':case['index'],'case_id':case['id'],
        'domain':case['domain'],'outcome':'LOCAL_KERNEL' if witnesses else 'EMPTY',
        'canonical_particular':list(map(str,a)),'stats':stats,'local_witnesses':witnesses}

def execute(context_path,output_root):
    context,evidence,paths=authorize(context_path) # before every mathematical operation
    require(Path(context['producer_path']).resolve()==Path(__file__).resolve(),'Reviewed producer path mismatch')
    out=Path(output_root);require(not out.exists(),'Never overwrite a prior scientific unit')
    out.mkdir(parents=True)
    start=datetime.now(timezone.utc).isoformat();began=time.monotonic()
    write_json_new(out/'SCIENCE_INVOCATION_START.json',{'start':start,'actual_context':pin(context_path),
        'actual_run_id':context['run_id'],'actual_run_generation':context['run_generation'],
        'scope':SCOPE,'authority_evidence':evidence,'new_scientific_invocation':True})
    common,problem=load_inputs(paths['portable_path'],paths['order4_input_path'])
    cases=validate_static_input(problem);operator=establish_operator(common)
    raw_path=out/'INCOMPLETE_PARTIAL_DFS_PREFIX.bin'
    summaries=[];counts={key:0 for key in ('nodes','edges','strict_norm_prunes','sphere_leaves','budget_pruned','kernels')}
    reason=None;completed=0
    with raw_path.open('xb') as sink:
        sink.write(header(COMMON_SHA,INPUT_SHA));sink.flush();os.fsync(sink.fileno())
        try:
            for case in cases:
                check_lease(context)
                record,summary=produce_case(operator,case)
                # Complete a case in memory; partial interrupted case never enters the durable prefix.
                sink.write(record);sink.flush();os.fsync(sink.fileno())
                summaries.append(summary);completed+=1
                for key,value in summary['stats'].items():counts[key]+=value
                if summary['outcome']=='LOCAL_KERNEL':reason='FIRST_EXACT_LOCAL_KERNEL';break
        except KeyboardInterrupt:reason='RESOURCE_INTERRUPT_NOT_EMPTY'
        except Exception as error:
            reason='UNRESOLVED_FAIL_HARD_'+type(error).__name__
            write_json_new(out/'FAIL_HARD_ERROR.json',{'error_type':type(error).__name__,'message':str(error),
                'next_case_index':completed,'case_NOT_classified':True,'no_failure_as_EMPTY':True})
    complete=completed==30992 and reason is None
    if complete:
        raw_path.rename(out/'COMPLETE_FULL30992_T6Q4DFS1.bin');raw_path=out/'COMPLETE_FULL30992_T6Q4DFS1.bin'
    finish=datetime.now(timezone.utc).isoformat()
    write_json_new(out/'CASE_CLASSIFICATION_SUMMARIES.json',summaries)
    result={'schema':'T6_Q4_EXACT_PRODUCER_SCIENTIFIC_FRONTIER_V1','complete_family':complete,
        'finished_case_count':completed,'completed_pattern_ids':[c['id'] for c in cases[:completed]],
        'remaining_case_count':30992-completed,'next_pattern':cases[completed]['id'] if completed<30992 else None,
        'stop_reason':reason,'stats':counts,'proof_pin':pin(raw_path),'scientific_start':start,'scientific_end':finish,
        'scientific_seconds':time.monotonic()-began,'actual_run_id':context['run_id'],
        'actual_run_generation':context['run_generation'],'scope':SCOPE,'source_author_ids':sorted(SOURCE_AUTHORS),
        'local_helper_native_identity':'UNKNOWN','source_exposure':'NONBLIND_DISCLOSED',
        'all_literal_outsiders_retained':True,'method_reuse':'EXTEND_EXISTING_TOOL_AND_COMPOSE_APPLIED',
        'native_mathematical_acceptance':False,'global_goal_status':'OPEN',
        'complete_proof_consumer_required':True,'genuine_separate_nonauthor_review_required':True}
    write_json_new(out/'SCIENTIFIC_FRONTIER.json',result)
    return result

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute',action='store_true');parser.add_argument('--context');parser.add_argument('--output')
    args=parser.parse_args()
    if not args.execute:
        print(json.dumps({'status':'LOCAL_PREPARATION_NOT_ADMITTED','scientific_feasibility_executed':False,
                          'scope':SCOPE,'actual_new_Task_claim_run_required':True}));return
    require(args.context and args.output,'Actual context and fresh output directory required')
    result=execute(args.context,args.output)
    print(json.dumps({k:result[k] for k in ('complete_family','finished_case_count','remaining_case_count','stop_reason','stats')}))

if __name__=='__main__':main()
