#!/usr/bin/env python3
"""One new q2-1 unit, exact int/Fraction; no old checker/census imports.
Preparation constructs the affine input only. Feasibility requires the actual
own native winning claim/open and fully read-back Source scope evidence.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
INPUT=HERE/'source-inputs/exact-source/research_artifacts/T6_P17_ORDER1_SUPPORT_20260923'
TASK='RS-T6-P17-ORDER2-PORTABLE-CERTIFICATE-20260923'
PUB='TP2-33BFE7DD84657DAB803C'
ACTOR='EM-T6-B4F89F'
SID='MCP-2b2adc7725e84b0c90908ba5db66a17f'
PORTABLE_SHA='7060ee638986a5c71a9775093e6b7f03ff3d5ff205ed438e3f5fa5aa93ca62ce'
PROBLEM_SHA='a16356adfd5c1763ed0c0426b381d89f70f0c51736335687578f1b9a5c63db0d'
P=17
N=16
R2=8450730
POS=1737
NEG=2331

def require(c,m):
    if not c: raise ValueError(m)
def nofloat(x):
    raise ValueError('Scientific floating arithmetic is forbidden')
def integer(x):
    require(isinstance(x,str) and x and (x.isdecimal() or x[0]=='-' and x[1:].isdecimal()),'Bad decimal integer')
    return int(x)
def rat(x):
    require(isinstance(x,list) and len(x)==2,'Bad rational pair')
    a,b=map(integer,x);require(b>0,'Nonpositive denominator');return Fraction(a,b)
def pair(x):
    x=Fraction(x);return [str(x.numerator),str(x.denominator)]
def read(path,sha=None):
    raw=Path(path).read_bytes()
    require(sha is None or hashlib.sha256(raw).hexdigest()==sha,'Source input SHA mismatch')
    return json.loads(raw,parse_float=nofloat)
def write(path,x):
    Path(path).write_text(json.dumps(x,indent=2)+'\n')
def dot(a,b):
    require(len(a)==len(b),'Wrong vector dimension')
    return sum((x*y for x,y in zip(a,b)),Fraction(0))
def det(matrix):
    a=[r[:] for r in matrix];n=len(a);prev=1;sign=1
    for k in range(n-1):
        pivot=next((j for j in range(k,n) if a[j][k]),None)
        if pivot is None:return 0
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign=-sign
        v=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                q,r=divmod(v*a[i][j]-a[i][k]*a[k][j],prev)
                require(r==0,'Nonexact Bareiss division');a[i][j]=q
            a[i][k]=0
        prev=v
    return sign*a[-1][-1]
def modular_solve(a,rhs,m):
    n=len(a);w=[[x%m for x in row]+[rhs[i]%m] for i,row in enumerate(a)]
    for k in range(n):
        row=next((i for i in range(k,n) if w[i][k]%P),None)
        require(row is not None,'Missing unit pivot')
        w[k],w[row]=w[row],w[k]
        inv=pow(w[k][k],-1,m);w[k]=[(x*inv)%m for x in w[k]]
        for i in range(n):
            if i!=k:
                factor=w[i][k];w[i]=[(x-factor*y)%m for x,y in zip(w[i],w[k])]
    x=[w[i][-1] for i in range(n)]
    require(all((sum(u*v for u,v in zip(row,x))-b)%m==0 for row,b in zip(a,rhs)),'Modular solve failed')
    return x

def prepare():
    portable=read(INPUT/'portable_input.json',PORTABLE_SHA)
    problem=read(INPUT/'order2_problem.json',PROBLEM_SHA)
    require(problem['common_basis_sha256']==PORTABLE_SHA,'Basis join failed')
    require(len(problem['cases'])==272 and all(x['status']=='INPUT_ONLY_NOT_SOLVED' for x in problem['cases']),'Original problem state mismatch')
    case=next(x for x in problem['cases'] if x['id']=='q2-1')
    require(case['positive_atoms']==[['2','1']] and not case['negative_atoms'],'Wrong vertical pattern')
    require(integer(case['q0_positive_budget'])==POS and integer(case['q0_negative_budget'])==NEG,'Wrong signed budgets')
    require(integer(case['radius_squared'])==R2==POS**2+NEG**2,'Wrong necessary sphere')
    weights=[P*j-1 for j in range(1,N+1)]
    require(list(map(integer,portable['weights']))==weights==list(map(integer,problem['weights'])),'Wrong weights')
    moduli=[P**k for k in range(1,7)]
    coefficients=[[pow(j,-k,P**k) for j in range(1,N+1)] for k in range(1,7)]
    require(list(map(integer,problem['moduli']))==moduli,'Wrong moduli')
    require([[integer(x) for x in row] for row in problem['coefficients']]==coefficients,'Wrong mixed coefficients')
    rhs=[(-pow(35,-k,P**k))%(P**k) for k in range(1,7)]
    require(rhs==list(map(integer,case['mixed_targets'])),'Wrong atom targets')
    U=[[integer(x) for x in row] for row in portable['unweighted_basis']]
    B=[[integer(x) for x in row] for row in portable['weighted_basis']]
    require(len(U)==len(B)==N and all(len(row)==N for row in U+B),'Wrong basis dimension')
    require(B==[[x*w for x,w in zip(row,weights)] for row in U],'Weighting failed')
    determinant=det(U);require(abs(determinant)==P**21,'Wrong full kernel index')
    require(all(sum(u*a for u,a in zip(row,coefficients[k]))%moduli[k]==0 for row in U for k in range(6)),'Basis outside mixed kernel')
    minor=det([[coefficients[k][j]%P for j in range(6)] for k in range(6)])%P
    require(minor!=0,'Mixed-modulus map not saturated')
    D=list(map(rat,portable['gram_schmidt_squared']))
    mu=[[rat(x) for x in row] for row in portable['mu']]
    require(len(D)==len(mu)==N and all(len(row)==N for row in mu),'Wrong GS dimensions')
    require(all(mu[i][i]==1 and all(mu[i][j]==0 for j in range(i+1,N)) for i in range(N)),'Wrong unit lower triangular mu')
    require(all(d>R2 for d in D),'Two-choice lemma is unavailable')
    for i in range(N):
        for j in range(N):
            require(dot(B[i],B[j])==sum(mu[i][k]*mu[j][k]*D[k] for k in range(N)),'Exact Gram identity failed')
    # Strong modulus is used ONLY to build one representative.
    # The searched homogeneous basis is the FULL mixed kernel of index17^21.
    M=P**6
    a=[[pow(j,-k,M) for j in range(1,7)] for k in range(1,7)]
    target=[(-pow(35,-k,M))%M for k in range(1,7)]
    first=modular_solve(a,target,M)
    particular=first+[0]*(N-6)
    for k in range(6):
        require(sum(x*a for x,a in zip(particular,coefficients[k]))%moduli[k]==rhs[k],'Particular fails true mixed moduli')
    weighted=[w*x for w,x in zip(weights,particular)]
    # Recover orthogonal inner products from the certified triangular Gram data.
    inner=[]
    for i in range(N):
        inner.append(dot(weighted,B[i])-sum(mu[i][j]*inner[j] for j in range(i)))
    centers=[inner[i]/D[i] for i in range(N)]
    require(dot(weighted,weighted)==sum(D[i]*centers[i]**2 for i in range(N)),'Affine orthogonal identity failed')
    for i in range(N):
        require(dot(weighted,B[i])==sum(mu[i][j]*D[j]*centers[j] for j in range(N)),'Affine center reconstruction failed')
    projection={'schema':'T6_Q2_1_EXACT_AFFINE_INPUT_V1','task_id':TASK,'publication_id':PUB,
      'pattern_id':'q2-1','original_pattern_status':case['status'],
      'particular_q0':list(map(str,particular)),'weighted_particular':list(map(str,weighted)),
      'affine_centers':list(map(pair,centers)),'mixed_targets':list(map(str,rhs)),
      'moduli':list(map(str,moduli)),'coefficients':[[str(x) for x in row] for row in coefficients],
      'weights':list(map(str,weights)),'q0_positive_budget':str(POS),'q0_negative_budget':str(NEG),
      'radius_squared':str(R2),'vertical_atom':{'q':'2','r':'1','cofactor':'35','denominator':'595','mass':'594','factorization':['5','7'],'maximal_prime':'17'},
      'common_input_sha256':PORTABLE_SHA,'order2_problem_sha256':PROBLEM_SHA,
      'kernel_determinant':str(determinant),'unit_minor_mod17':str(minor),
      'all_D_gt_radius':True,'all_D_gt_twice_radius':all(d>2*R2 for d in D),
      'at_most_one_nonpreferred_if_all_D_gt_twice_radius':True,
      'feasibility_search_executed_by_input_preparation':False}
    return projection,weights,U,B,D,mu,centers,particular,coefficients,rhs,moduli

def authorize(context_path):
    context=read(context_path)
    require(context['task_id']==TASK and context['publication_id']==PUB,'Wrong context task/publication')
    require(context['researcher_id']==ACTOR and context['session_id']==SID,'Wrong own identity')
    require(context['Source_session_RA_ER_publication_book_full_bytes_verified'] is True,'Native Source chain not read back')
    receipts=[read(HERE/'native'/('RECEIPT_%02d_FINAL.json'%i)) for i in (2,3,4)]
    require(all(x['bridge_receipt']['status']=='SUCCEEDED' for x in receipts),'Native admission not complete')
    prepared=receipts[0]['bridge_receipt']['receipt']['result']
    claimed=receipts[1]['bridge_receipt']['receipt']['result']
    opened=receipts[2]['bridge_receipt']['receipt']
    binding=opened['result']['execution_binding'];run=opened['run']
    require(opened['result']['authorized'] is True,'Actual open denied')
    require(opened['result']['authorization_authority']=='CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM','Wrong native authority')
    require(binding['executor_role']=='RESEARCHER' and binding['researcher_id']==ACTOR and binding['session_id']==SID,'Wrong typed executor')
    require(binding['claim_id']==prepared['intent']['claim_id']==context['claim_id'],'Claim chain mismatch')
    require(binding['execution_record_id']==prepared['intent']['execution_record_id']==context['execution_record_id'],'ER chain mismatch')
    require(binding['publication_id']==PUB and opened['result']['task_id']==TASK,'Wrong run task')
    require(run['run_id']==context['run_id'] and run['task_id']==TASK and run['publication_id']==PUB,'Run ID/binding mismatch')
    require(run['researcher_id']==ACTOR and run['session_id']==SID and run['claim_id']==context['claim_id'],'Run owner mismatch')
    require(run['fenced_by_claim_id'] is None,'Native run fenced')
    require(run['generation']==context['run_generation'],'Run generation mismatch')
    require(context['allowed_outputs']==binding['allowed_outputs'],'Allowed outputs mismatch')
    return context

def execute(context_path):
    context=authorize(context_path)
    start=time.perf_counter_ns()
    prepared,weights,U,B,D,mu,alpha,particular,coeff,rhs,moduli=prepare()
    # Actual run only: translate by one exact Babai nearest-plane lattice vector.
    original=particular[:];zshift=[0]*N;shift_trace=[]
    for i in range(N-1,-1,-1):
        c=alpha[i]+sum(mu[j][i]*zshift[j] for j in range(i+1,N))
        q,rem=divmod(c.numerator,c.denominator)
        z=-q-1 if 2*rem>=c.denominator else -q
        zshift[i]=z
        shift_trace.append({'index':i,'center':pair(c),'quotient':str(q),'remainder':str(rem),'denominator':str(c.denominator),'z':str(z)})
    particular=[original[j]+sum(zshift[i]*U[i][j] for i in range(N)) for j in range(N)]
    alpha=[alpha[i]+zshift[i]+sum(mu[j][i]*zshift[j] for j in range(i+1,N)) for i in range(N)]
    require(all(abs(c)<=Fraction(1,2) for c in alpha),'Translated center outside nearest-plane cell')
    require(all(sum(x*a for x,a in zip(particular,coeff[k]))%moduli[k]==rhs[k] for k in range(6)),'Translation lost mixed congruences')
    nodes=[];survivors=[];leaf_counts={'full_sphere_leaves':0,'budget_pruned':0}
    z=[0]*N
    def visit(i,partial):
        node_id=len(nodes)
        node={'id':node_id,'index':i,'suffix':[str(x) for x in z[i+1:]],'partial_norm':pair(partial),'edges':[]}
        nodes.append(node)
        c=alpha[i]+sum(mu[j][i]*z[j] for j in range(i+1,N))
        q,rem=divmod(c.numerator,c.denominator)
        require(c.numerator==q*c.denominator+rem and 0<=rem<c.denominator,'Bad Euclidean floor')
        node.update(center=pair(c),floor={'quotient':str(q),'remainder':str(rem),'denominator':str(c.denominator)})
        for value in (-q-1,-q):
            z[i]=value
            total=partial+D[i]*(value+c)**2
            edge={'z':str(value),'partial_norm':pair(total)}
            node['edges'].append(edge)
            if total>R2:edge['action']='NORM_PRUNED'
            elif i>0:
                edge['action']='CHILD';edge['child']=visit(i-1,total)
            else:
                leaf_counts['full_sphere_leaves']+=1
                u=[particular[j]+sum(z[t]*U[t][j] for t in range(N)) for j in range(N)]
                v=[w*x for w,x in zip(weights,u)]
                require(dot(v,v)==total,'Complete norm identity failed')
                residues=[sum(x*a for x,a in zip(u,coeff[k]))%moduli[k] for k in range(6)]
                require(residues==rhs,'Full leaf fails mixed affine equations')
                positive=sum(max(x,0) for x in v);negative=sum(max(-x,0) for x in v)
                edge.update(vector=list(map(str,u)),positive_mass=str(positive),negative_mass=str(negative),
                            mixed_residues=list(map(str,residues)),weighted_norm=pair(total))
                if positive>POS or negative>NEG:
                    edge['action']='BUDGET_PRUNED';leaf_counts['budget_pruned']+=1
                else:
                    edge['action']='SURVIVOR'
                    survivors.append({'q0':list(map(str,u)),'q0_positive_mass':str(positive),
                      'q0_negative_mass':str(negative),'total_positive_mass_with_atom':str(positive+594),
                      'total_negative_mass':str(negative),'mixed_residues':list(map(str,residues)),
                      'full_H0_lower_prime_completion':'OPEN_NOT_A_FULL_COLLISION'})
        return node_id
    root=visit(N-1,Fraction(0))
    require(len(nodes)<=2**(N+1)-1,'Complete tree exceeds proved finite bound')
    outcome='LOCAL_KERNEL' if survivors else 'EMPTY'
    ledger={'schema':'T6_Q2_1_EXACT_TWO_CHOICE_SAVED_LEDGER_V1','task_id':TASK,'publication_id':PUB,
      'pattern_id':'q2-1','outcome':outcome,'scope':'ONE_PATTERN_PARTIAL_SCOPE_NOT_272_FAMILY_OR_GLOBAL_T6_COMPLETION',
      'particular_q0':list(map(str,particular)),'affine_centers':list(map(pair,alpha)),
      'original_particular_q0':list(map(str,original)),'lattice_translation':list(map(str,zshift)),
      'translation_divrem_trace':shift_trace,'root':root,'nodes':nodes,'survivors':survivors,
      'node_count':len(nodes),'edge_count':sum(len(n['edges']) for n in nodes),
      'pruned_edges':sum(e['action']=='NORM_PRUNED' for n in nodes for e in n['edges']),
      **leaf_counts,'complete_traversal':True,'resource_exhausted':False,
      'completed_pattern_ids':['q2-1'],'next_pattern':'q2-2','remaining_pattern_count':271,
      'family_hard_target_complete':False,'global_T6_complete':False,
      'domain':'MAXIMAL_P17_ADMISSIBLE_35_EQUALS_5_TIMES_7','radius_squared':str(R2),
      'q0_positive_budget':str(POS),'q0_negative_budget':str(NEG),
      'common_input_sha256':PORTABLE_SHA,'order2_problem_sha256':PROBLEM_SHA,
      'exact_scientific_arithmetic':'PYTHON_INT_AND_FRACTION_ONLY_WITH_SAVED_EUCLIDEAN_DIVREM',
      'elapsed_nanoseconds':time.perf_counter_ns()-start,
      'own_actual_control':{'researcher_id':ACTOR,'session_id':SID,'claim_id':context['claim_id'],
        'execution_record_id':context['execution_record_id'],'run_id':context['run_id'],'run_generation':context['run_generation']}}
    write(HERE/'Q2_1_EXACT_AFFINE_INPUT.json',prepared)
    write(HERE/'Q2_1_COMPLETE_NEW_LEDGER.json',ledger)
    print(json.dumps({k:ledger[k] for k in ['pattern_id','outcome','node_count','edge_count','pruned_edges','full_sphere_leaves','completed_pattern_ids','next_pattern','remaining_pattern_count']}))

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--execute',action='store_true')
    parser.add_argument('--context',type=Path)
    args=parser.parse_args()
    if args.execute:
        require(args.context is not None,'Actual own native context required')
        require(not (HERE/'Q2_1_COMPLETE_NEW_LEDGER.json').exists(),'Do not repeat completed bounded compute')
        execute(args.context)
    else:
        # This prepares an exact affine input only, without any feasibility nodes.
        prepared,*_=prepare()
        write(HERE/'Q2_1_PREPARATION_ONLY_AFFINE_INPUT.json',prepared)
        print(json.dumps({'prepared_input_only':True,'feasibility_nodes_visited':0,'pattern_id':'q2-1'}))
