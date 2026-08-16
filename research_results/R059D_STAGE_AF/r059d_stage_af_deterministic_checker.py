#!/usr/bin/env python3
import json,base64,zlib,lzma,hashlib,math
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parent
checks=[]
def ck(name,cond,detail=''):
    checks.append((name,bool(cond),str(detail)))
    if not cond: raise AssertionError(f'{name}: {detail}')

def load(name):
    o=json.loads((ROOT/name).read_text())
    codec=o.get('codec') if isinstance(o,dict) else None
    if codec:
        raw=base64.b64decode(o['compressed_payload_b64'])
        if codec=='zlib+base64': raw=zlib.decompress(raw)
        elif codec=='lzma+base64': raw=lzma.decompress(raw)
        else: raise ValueError(codec)
        ck('sha_'+name,hashlib.sha256(raw).hexdigest()==o['uncompressed_sha256'])
        ck('bytes_'+name,len(raw)==o['uncompressed_bytes'])
        return json.loads(raw)
    return o

def n_j_candidate(R=512):
    j=0; out=[]
    for r in range(1,R+1):
        u=3*j+2; v=3*r
        if 3*u*u+6*u*v-v*v <= 0: j+=1
        out.append(j)
    return out

radius=load('R059D_STAGE_AF_RADIUS_LEDGER.json')
words=load('R059D_STAGE_AF_BOUNDARY_WORD_REGISTRY.json')
jump=load('R059D_STAGE_AF_JUMP_LEDGER.json')
skel=load('R059D_STAGE_AF_COMMON_SKELETON_AUDIT.json')
ident=load('R059D_STAGE_AF_INTEGER_CURVATURE_IDENTITY.json')
cand=load('R059D_STAGE_AF_GENERATOR_CANDIDATES.json')
hold=load('R059D_STAGE_AF_HOLDOUT_AUDIT.json')
prec=load('R059D_STAGE_AF_C_PRECISION_AUDIT.json')

RID='EM-R059D-AF-7E31C6'
ck('rid_radius',radius['researcher_id']==RID)
ck('ranges',radius['range']=={'discovery':[1,256],'holdout':[257,512]})
ck('rows_N',len(radius['N'])==512); ck('rows_C',len(radius['C'])==512)
ck('words_N',len(words['N'])==512); ck('words_C',len(words['C'])==512)
ck('precision_selected',prec['selected_sampling']==1024)
ck('precision_full_stable',prec['doubling_comparisons']['1024_vs_2048']['changed_radius_count']==0)
ck('precision_status',prec['status']=='FULL_MANDATORY_RANGE_SAMPLING_STABILITY_CERTIFIED')

ix={name:i for i,name in enumerate(radius['fields'])}
allseq={}
for arm in ('N','C'):
    B=[];J=[]
    for idx,row in enumerate(radius[arm],start=1):
        r,D,C,V,b,j,db,dj,d2b,d2j,sl,tc,pt,nt,nca,nja=row
        ck(f'r_{arm}_{r}',r==idx)
        ck(f'D_{arm}_{r}',D==2*r+1)
        ck(f'C_{arm}_{r}',C==6*r+6*j)
        ck(f'V_{arm}_{r}',V==1+3*r*(r+1)+6*b)
        B.append(b); J.append(j)
    dB=[B[0]]+[B[i]-B[i-1] for i in range(1,512)]
    dJ=[J[0]]+[J[i]-J[i-1] for i in range(1,512)]
    d2B=[dB[0]]+[dB[i]-dB[i-1] for i in range(1,512)]
    for i,row in enumerate(radius[arm]):
        ck(f'dB_{arm}_{i+1}',row[ix['DeltaB']]==dB[i])
        ck(f'dJ_{arm}_{i+1}',row[ix['DeltaJ']]==dJ[i])
        ck(f'd2B_{arm}_{i+1}',row[ix['Delta2B']]==d2B[i])
    allseq[arm]=(B,J,dB,dJ,d2B)
    wmap={int(r):w for r,w,t in words[arm]}
    ck(f'word_keys_{arm}',len(wmap)==512)
    for r in range(1,513):
        w=wmap[r]; b=B[r-1]; j=J[r-1]
        h=0; area=0; c1=c2=c3=0
        for ch in w:
            if ch=='1': h+=1; c1+=1
            elif ch=='2': area+=h; c2+=1
            elif ch=='3': area+=h; h-=1; c3+=1
            else: ck('bad_symbol',False,ch)
            ck(f'motzkin_nonneg_{arm}_{r}_{len(checks)}',h>=0)
        ck(f'motzkin_end_{arm}_{r}',h==0)
        ck(f'motzkin_counts_{arm}_{r}',c1==j and c3==j and c2==r-j,(c1,c2,c3,j))
        ck(f'motzkin_len_{arm}_{r}',len(w)==r+j)
        ck(f'motzkin_B_{arm}_{r}',area==b,(area,b))

for arm in ('N','C'):
    B,J,dB,dJ,d2B=allseq[arm]
    KB=[r for r in range(2,513) if d2B[r-1]!=0]
    KJ=[r for r in range(2,513) if dJ[r-1]!=0]
    ck('KB_count_'+arm,len(KB)==skel['K_B'][arm+'_count'])
    ck('KJ_count_'+arm,len(KJ)==skel['K_J'][arm+'_count'])
ck('KB_inter',len(set([r for r in range(2,513) if allseq['N'][4][r-1]!=0]) & set([r for r in range(2,513) if allseq['C'][4][r-1]!=0]))==393)
ck('KJ_inter',skel['K_J']['intersection_count']==60)
ck('delay_pairs_count',len(skel['K_J']['delay_pairs'])==19)
for a,b in skel['K_J']['delay_pairs']:
    ck(f'delay_{a}',allseq['N'][3][a-1]==1 and allseq['C'][3][a-1]==0 and allseq['C'][3][b-1]==1 and b==a+1)
ck('no_exact_common_skel',skel['common_exact_point_skeleton_established'] is False)
ck('J_scalar_counterexample',allseq['N'][1][14]==allseq['C'][1][14]==2 and allseq['N'][0][14]==23 and allseq['C'][0][14]==21)
ck('sameJ_diffB_count',sum(1 for i in range(512) if allseq['N'][1][i]==allseq['C'][1][i] and allseq['N'][0][i]!=allseq['C'][0][i])==412)

nj=n_j_candidate(512); JN=allseq['N'][1]
ck('cand_discovery',nj[:256]==JN[:256])
ck('cand_holdout',nj[256:]==JN[256:])
ck('holdout_frozen',hold['freeze_before_holdout'] is True)
ck('holdout_status',hold['AF-G1-N-J-ALGEBRAIC-BEATTY-001']['holdout_status']=='SURVIVES_EXACTLY_256_OF_256')
g1=next(x for x in cand['candidates'] if x['candidate_id']=='AF-G1-N-J-ALGEBRAIC-BEATTY-001')
ck('autonomous_J_only',g1['generator']['GENERATOR_IS_FORWARD_AUTONOMOUS'] is True and g1['target']=='J_N only')
ck('no_pi',g1['generator']['uses_pi'] is False)
ck('no_sqrt_runtime',g1['generator']['uses_classical_sqrt_runtime'] is False)
ck('no_Q_runtime',g1['generator']['uses_source_Q_runtime'] is False)
ck('proof_open',g1['status']=='SURVIVES_HOLDOUT__PROOF_OPEN')
ck('full_generator_absent',cand['full_BJ_generator_status']=='NO_FORWARD_AUTONOMOUS_FULL_BJ_GENERATOR_FOUND')
cg=next(x for x in cand['candidates'] if x['candidate_id']=='AF-G1-C-AFFINE-FLOOR-NOGO-001')
ck('C_floor_killed',cg['discovery_exact_feasibility']['strict_interval_nonempty'] is False and cg['discovery_exact_feasibility']['lower_alpha']==cg['discovery_exact_feasibility']['upper_alpha']=='13/84')
ck('N_transient_fail_11',allseq['N'][0][10] != 11-2)
ck('C_transient_fail_12',allseq['C'][0][11] != 12-2)
ck('identity_status',ident['theorem_name']=='SECTOR_MOTZKIN_INTEGER_CURVATURE_IDENTITY')

payload='\n'.join(f'{n}:{int(ok)}:{d}' for n,ok,d in checks).encode()
out={
 'schema':'R059D_STAGE_AF_DETERMINISTIC_CHECKER_OUTPUT_V1',
 'status':'PASS','checks_total':len(checks),'checks_passed':sum(ok for _,ok,_ in checks),
 'checks_failed':sum(not ok for _,ok,_ in checks),
 'checks_digest_sha256':hashlib.sha256(payload).hexdigest(),
 'history_gate':'PENDING_EXTERNAL_GITHUB_COMPARE',
 'summary':'All frozen radius/word rows, Motzkin integer-curvature identities, jump-skeleton certificates, scalar-state no-go, discovery/holdout isolation, N-only integer candidate and semantic firewalls pass.'
}
print(json.dumps(out,sort_keys=True,separators=(',',':')))
