"""Audit complete original execution receipts; deliberately do not rerun51M nodes."""
from hashlib import sha256
from pathlib import Path
import argparse
import json

HERE=Path(__file__).resolve().parent


def digest(path):
    b=path.read_bytes();return {'bytes':len(b),'sha256':sha256(b).hexdigest()}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--D-proof',dest='d',type=Path,required=True)
    p.add_argument('--mixed-proof',type=Path,required=True)
    p.add_argument('--mother-proof',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    for directory in (HERE,a.d,a.mixed_proof,a.mother_proof):
        for r in json.loads((directory/'package_manifest.json').read_text())['files']:
            assert digest(directory/r['path'])=={k:r[k] for k in ('bytes','sha256')}
    saved=json.loads((HERE/'execution_bindings.json').read_text())['files']
    actual={'native_source':a.d/'sources/native_regional.cpp','obs':a.mixed_proof/'inputs/obs',
            'parent':a.mixed_proof/'inputs/parent','B11':a.mixed_proof/'inputs/B11','B12':a.mixed_proof/'inputs/B12',
            'frames':a.mixed_proof/'frames/frames_2_25.txt','options':a.d/'cost_defect_options.txt',
            'small_bank_verification':a.d/'small_bank_verification.json'}
    for key,path in actual.items():assert digest(path)=={k:saved[key][k] for k in ('bytes','sha256')}
    assert json.loads((a.d/'small_bank_verification.json').read_text())['proper_bank']=={k:saved['proper_bank'][k] for k in ('bytes','sha256')}
    profile=json.loads((HERE/'profile.json').read_text());row=profile['profile']
    assert row in json.loads((a.mother_proof/'plan_9995.json').read_text())['profiles']
    assert row['embedded_sizes']==[12,13] and row['proper_sizes']==[9,9]+[10]*7+[12]
    assert profile['budget']==9995 and row['minimum_total_cost']==9966
    assert profile['engine']=='regional' and profile['complete_profile_exclusion']
    assert profile['native_source_sha256']==saved['native_source']['sha256']
    frames=(actual['frames']).read_text().splitlines();assert len(frames)==6
    parents=[]
    for line in actual['parent'].read_text().splitlines()[:250]:
        lo,hi=map(int,line.split());parents.append(lo+(hi<<64))
    allowances=[]
    for line in frames:
        i,j=map(int,line.split());allowances.append((parents[i]|parents[j]).bit_count()-25)
    assert set(allowances)<=set((0,1))
    receipts=[]
    for index in range(6):
        state=json.loads((HERE/f'frame_{index:03d}.json').read_text())
        assert state['frame_index']==index and state['profile']==row and state['budget']==9995
        assert state['native_source_sha256']==saved['native_source']['sha256']
        assert state['frame_source_sha256']==saved['frames']['sha256']
        assert state['engine']=='regional' and state['complete_frame_exclusion']
        assert state['counts'][0]==1 and state['counts'][-1]==0 and state['stdout']==''
        cmd=state['command'];assert Path(cmd[0]).name=='native_regional'
        assert Path(cmd[4]).name=='frames_2_25.txt'
        assert cmd[5:14]==[','.join(map(str,row['proper_sizes'])),'12,13','2400','9995',str(index),str(index+1),'0','0',','.join(['0']*14)]
        assert Path(cmd[14]).name=='cost_defect_options.txt' and Path(cmd[15]).name=='small_proper'
        lines=state['stderr'].splitlines();assert len(lines)==4
        assert list(map(int,lines[0].split()))==state['counts']
        for i,name,key in [(1,'marginal','marginal_test_prune_counts'),(2,'capacity','capacity_test_prune_counts'),(3,'smallbank','small_bank_node_candidate_counts')]:
            parts=lines[i].split();assert parts[0]==name and list(map(int,parts[1:]))==state[key]
        receipts.append(state)
    assert [sum(r['counts'][i] for r in receipts) for i in range(5)]==profile['counts']==[6,51672395,51672389,0,0]
    for key in ('marginal_test_prune_counts','capacity_test_prune_counts','small_bank_node_candidate_counts'):
        assert [sum(r[key][i] for r in receipts) for i in range(2)]==profile[key]
    result={'all_bindings_and_receipts_verified':True,'new_complete_E2_profiles':1,'total_E2_completed_with_C_and_D':7,
            'frames':6,'original_search_nodes':51672395,'found':0,'full_search_rerun':False,
            'inside_allowances':allowances,
            'scope':'Same validated regional engine and complete candidate bank as D. Completeness additionally uses C\'s complete six mother-pair frames, the original outside-point condition, and the explicitly checked d=0/1 candidate-set replacement.'}
    a.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
