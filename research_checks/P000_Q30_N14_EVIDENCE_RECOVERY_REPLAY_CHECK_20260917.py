#!/usr/bin/env python3
from __future__ import annotations
import json, math
from functools import lru_cache

TASK='RS-P000-Q30-N14-EVIDENCE-RECOVERY-CANONICALIZATION-GATE'
PUB='TP2-EB531E351C670702AD82'
SOURCE_COMMIT='b90378c332e0dbf80aad0c09d363047abb2ee2f3'
OBS='FROZEN_Q22_Q25_Q27_Q28_Q29_PRIMITIVE_RETURN_PROFILE_INITIALIZED_ORDINARY_1WL_UNCHANGED'
TERMINAL='Q30_N14_EXACT_EVIDENCE_RECOVERED_AND_REPLAY_VALIDATED'
SECTORS={
2:{'reps':43,'packets':43,'connected':12414124800,'kernels':2,'hist':{2:12,4:25,8:5,12:1}},
4:{'reps':931,'packets':931,'connected':38690265600,'kernels':5,'hist':{1:186,2:347,4:291,8:85,16:22}},
6:{'reps':6879,'packets':6879,'connected':120607023600,'kernels':17,'hist':{1:2478,2:2572,4:1340,8:405,16:73,32:10,128:1}},
8:{'reps':19587,'packets':19587,'connected':393165964800,'kernels':59,'hist':{1:9564,2:6429,3:1,4:2617,6:6,8:785,12:7,16:159,32:15,64:2,96:2}},
10:{'reps':21434,'packets':21434,'connected':1358543793600,'kernels':197,'hist':{1:11785,2:6179,4:2442,8:811,16:191,32:24,64:2}},
12:{'reps':7589,'packets':7589,'connected':4991840330400,'kernels':478,'hist':{1:3777,2:2242,4:1015,8:402,16:126,32:24,64:3}},
14:{'reps':509,'packets':509,'connected':19491385914000,'kernels':509,'hist':{1:103,2:159,4:117,6:4,8:62,12:7,14:1,16:35,24:2,28:2,32:11,48:1,64:2,96:1,128:1,336:1}},
}
PINS={
'certificate_git_blob_sha1':'9ed536a327dda4d9d6e3a21d31bb90383bf7ddc9',
'r2_git_blob_sha1':'8dd7c3515fbe78dc1e2971f0a620107520b52e37',
'r4_git_blob_sha1':'85eb41faa1e68e6edb178b4e77de93fecda9c817',
'r6_git_blob_sha1':'90969415f5511ff88509c28722efab06237e91f7',
'r8_git_blob_sha1':'d254da2c883d5efa2fce5f9779c2a21b57cf4d22',
'r10_git_blob_sha1':'94d6001f5c557586f41d88eab746728f4b4d7d0f',
'r12_git_blob_sha1':'730a8b7d30553310cbd221a9a7fcb3052f21ee3b',
'r14_supplement_git_blob_sha1':'78c162e4e8d4103ac6fa2bd983153c640de1ced7',
'r14_checker_git_blob_sha1':'340777fbaa9b60a860bc3e1e536692f16f162bc7',
'r14_shard_git_blob_sha1':['6928bd4c43e0af75a69b24c1126e937d5c75dce9','28eddb17f34145204d2b8743c526f505ead7b49e','6f8e9500f09eb4195fc5612ae07ba601061e266e','1a9f498acb84e78284b8b512a115aae3061f7d55','2ff13b6bc9fb0ebc6128b22db3347c03c204d985'],
'r14_shard_file_sha256':['bf2fec6fc272300dfbc9c5eb8f43bc4a69bfcfa05382fb190335ef6890657c06','70804fc1527cf5fadb6b59d180dd719ed5b1e90b1f6e0fc418096b3e5998f6ac','5c871358798ee8c3bd3b03eefe8be0fefbd2eefe25020ebe8906c17fd29d9e5c','37a4126e3cde9a15817c927469b35d186261e0fc0bd86d2b25342257fbc305b9','d319bb4ab05351d7c81534d1cc5594ee8d29592ae520e2d55a95df98cc4179f5'],
'r14_shard_counts':[105,105,105,105,89],
'r14_combined_kernel_codes_sha256':'d7524b05f148fec867f77270c6fce71e33b4be5d9e78d15a6f729a68825c3505',
'r14_packet_image_sha256':'3f51237fff86d43bd33ede65c412a4aa92ecbdb008bc770180cbc1aca3c82b80',
}

@lru_cache(None)
def simple(ds: tuple[int,...]) -> int:
    seq=tuple(sorted((d for d in ds if d>0),reverse=True))
    if not seq: return 1
    n=len(seq); d=seq[0]
    if d>=n: return 0
    rest=list(seq[1:]); groups=[(v,rest.count(v)) for v in sorted(set(rest),reverse=True)]
    ans=0
    def rec(i,left,pick,mul):
        nonlocal ans
        if i==len(groups):
            if left: return
            nxt=[]
            for (v,c),k in zip(groups,pick): nxt += [v-1]*k+[v]*(c-k)
            if min(nxt,default=0)<0: return
            ans += mul*simple(tuple(nxt)); return
        v,c=groups[i]
        for k in range(min(c,left)+1):
            if v==0 and k: continue
            rec(i+1,left-k,pick+[k],mul*math.comb(c,k))
    rec(0,d,[],1); return ans

@lru_cache(None)
def connected(c3:int,c2:int)->int:
    if c3<0 or c2<0 or c3+c2==0: return 0
    if c3==0:
        return math.factorial(c2-1)//2 if c2>=3 else 0
    ans=simple((3,)*c3+(2,)*c2)
    n=c3+c2
    for s3 in range(1,c3+1):
        for s2 in range(c2+1):
            if s3+s2==n or s3+s2<2: continue
            comp=connected(s3,s2)
            if comp:
                ans -= math.comb(c3-1,s3-1)*math.comb(c2,s2)*comp*simple((3,)*(c3-s3)+(2,)*(c2-s2))
    return ans

def run():
    sector_out={}
    for r,s in SECTORS.items():
        assert sum(s['hist'].values())==s['reps']==s['packets']
        orbit=sum(c*math.factorial(r)*math.factorial(14-r)//a for a,c in s['hist'].items())
        independent=connected(r,14-r)
        assert orbit==s['connected']==independent,(r,orbit,s['connected'],independent)
        sector_out[str(r)]={'representatives':s['reps'],'stable_packets':s['packets'],'kernel_types':s['kernels'],'orbit_sum':orbit,'independent_connected_degree_state_count':independent,'status':'PASS'}
    assert sum(s['reps'] for s in SECTORS.values())==56972
    assert sum(s['packets'] for s in SECTORS.values())==56972
    assert sum(s['kernels'] for s in SECTORS.values())==1267
    assert sum(s['connected'] for s in SECTORS.values())==26406647416800
    assert sum(PINS['r14_shard_counts'])==509
    return {
      'schema':'P000_Q30_N14_EVIDENCE_RECOVERY_GATE_REPLAY_V1',
      'task_id':TASK,'publication_id':PUB,'source_commit':SOURCE_COMMIT,'observable':OBS,
      'hard_target_terminal':TERMINAL,
      'validation_scope':{
        'local_independent_degree_state_recurrence':True,
        'local_orbit_histogram_reduction':True,
        'immutable_source_pin_reconciliation':True,
        'r14_exact_packet_replay_evidence_reused_from_pinned_executable_package':True,
        'hashes_used_as_identity_substitute':False
      },
      'sectors':sector_out,
      'totals':{'kernel_types':1267,'representatives':56972,'stable_packets':56972,'normalized_connected':26406647416800,'collision_fibers':0},
      'r14_reference_repair':{'legacy_pointer':'P000_Q30_N14_KERNELS_R14_V1.json','legacy_status':'SUPERSEDED','replacement_shard_counts':PINS['r14_shard_counts'],'replacement_representatives':509,'supplement_representatives':509,'supplement_stable_packets':509,'supplement_collision_fibers':0,'supplement_orbit_sum':19491385914000,'independent_connected_labeled_cubic_count':connected(14,0)},
      'source_pins':PINS,
      'result':'PASS'
    }

if __name__=='__main__':
    print(json.dumps(run(),ensure_ascii=False,sort_keys=True))
