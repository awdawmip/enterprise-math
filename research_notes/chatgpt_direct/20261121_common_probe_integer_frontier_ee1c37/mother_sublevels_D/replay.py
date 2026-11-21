"""Portable replay of the D mother-layer increment, with inherited C bindings.

Rebuilds the complete cheap bank, exact capacity options, two new E2 profiles,
and the two residual E3 exact9865 types. The previously certified four E2
profiles and exactly-three-core theorem are bound as dependencies, not rerun.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import argparse
import importlib.util
import json
import shutil
import struct
import subprocess
import sys

import verify_e3
import verify_price_capacity

HERE=Path(__file__).resolve().parent


def digest(path):
    raw=path.read_bytes();return {'bytes':len(raw),'sha256':sha256(raw).hexdigest()}


def manifest(directory):
    recorded=json.loads((directory/'package_manifest.json').read_text())
    for row in recorded['files']:
        assert digest(directory/row['path'])=={k:row[k] for k in ('bytes','sha256')}


def compile_source(name,work):
    executable=work/Path(name).stem
    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',HERE/'sources'/name,'-o',executable],check=True)
    return executable


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--seeds',type=Path,required=True)
    p.add_argument('--mother-proof',type=Path,required=True)
    p.add_argument('--mixed-proof',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    a=p.parse_args();work=a.work.resolve();work.mkdir(parents=True,exist_ok=True)
    manifest(HERE);manifest(a.mother_proof);manifest(a.mixed_proof)
    dependencies=json.loads((HERE/'dependencies.json').read_text())
    for key,path in [('static_mother_package',a.mother_proof/'package_manifest.json'),
                     ('mixed_and_first_four_E2_package',a.mixed_proof/'package_manifest.json'),
                     ('mixed_bound',a.mixed_proof/'mixed_bound_verification.json'),
                     ('complete_seeds',a.seeds),('full_native_catalog',a.mother_proof/'catalog.txt'),
                     ('core_three_result',a.previous/'cores/core_three_result.json'),
                     ('core_three_replay',a.previous/'cores/verify_core_three.py'),
                     ('original_uniform_search',a.previous/'bias/weighted_native.cpp')]:
        assert digest(path)=={k:dependencies[key][k] for k in ('bytes','sha256')},key
    assert (HERE/'sources/native_original.cpp').read_bytes()==(a.previous/'bias/weighted_native.cpp').read_bytes()
    assert (HERE/'e3/core_three_dependency_result.json').read_bytes()==(a.previous/'cores/core_three_result.json').read_bytes()
    price=verify_price_capacity.verify(a.seeds,a.mother_proof,a.mixed_proof)
    e3=verify_e3.verify(a.mother_proof)
    print(json.dumps({'arithmetic_verified':price,'E3_capacity_survivors':e3['capacity_survivors']}),flush=True)
    bank_proof=json.loads((HERE/'small_bank_verification.json').read_text())
    assert bank_proof['caps']=={'9':598,'10':780,'8':443}
    assert digest(a.mixed_proof/'inputs/obs')==bank_proof['native_observer']
    assert digest(a.mixed_proof/'inputs/parent')==bank_proof['mothers']
    assert digest(HERE/'inputs/linear')==bank_proof['linear_actions']
    assert digest(HERE/'sources/genprof.cpp')==bank_proof['affine_expansion_source']
    portable_filter=(HERE/'sources/verify_filter.cpp').read_text()
    original_filter=portable_filter.replace('"native_original.cpp"','"../work_capacity/native.cpp"')
    assert sha256(original_filter.encode()).hexdigest()==bank_proof['native_validation_source']['sha256']
    seed_lines=a.seeds.read_bytes().splitlines();caps={8:443,9:598,10:780}
    selected=[]
    for line in seed_lines:
        n,c=map(int,line.split(None,2)[:2])
        if n in caps and c<=caps[n]:selected.append(line)
    assert len(selected)==5816
    assert b'\n'.join(selected)+b'\n'==(HERE/'inputs/small_needed').read_bytes()
    linear=[tuple(map(int,line.split())) for line in (HERE/'inputs/linear').read_text().splitlines()]
    assert len(linear)==96 and all(sorted(row)==list(range(125)) for row in linear)
    actual_maps=(a.mixed_proof/'inputs/maps').read_bytes()
    assert len(actual_maps)==12000*125
    expanded={bytes(25*((row[p]//25+d//25)%5)+5*((row[p]//5%5+d//5%5)%5)+(row[p]%5+d%5)%5 for p in range(125)) for row in linear for d in range(125)}
    assert expanded=={actual_maps[i:i+125] for i in range(0,len(actual_maps),125)}
    genprof=compile_source('genprof.cpp',work)
    generated=subprocess.check_output([genprof,HERE/'inputs/linear',HERE/'inputs/small_needed',HERE/'inputs/small_caps',work/'small_all'],text=True)
    (work/'small_all.log').write_text(generated)
    native_filter=compile_source('verify_filter.cpp',work)
    checked=subprocess.check_output([native_filter,a.mixed_proof/'inputs/obs',a.mixed_proof/'inputs/parent',work/'small_all',work/'small_proper',HERE/'inputs/small_caps'],text=True)
    expected_counts=''.join(f"{r['size']} {r['cost']} {r['legal_classes']} {r['proper_classes']}\n" for r in bank_proof['type_counts'])
    assert checked==expected_counts
    assert digest(work/'small_proper')==bank_proof['proper_bank']
    assert bank_proof['all_expanded_native_checks']==607500 and bank_proof['proper_classes']==566000
    capacity_check=compile_source('check_capacity.cpp',work)
    assert subprocess.check_output([capacity_check,HERE/'cost_defect_options.txt',HERE/'capacity_queries.txt'],text=True).strip()=='7773'
    candidates_check=compile_source('check_small_candidates.cpp',work)
    compared=subprocess.check_output([candidates_check,a.mixed_proof/'inputs/obs',a.mixed_proof/'inputs/parent',work/'small_proper',a.mixed_proof/'frames/frames_2_26.txt',a.mixed_proof/'frames/frames_2_25.txt'],text=True)
    candidate_proof=json.loads((HERE/'small_candidate_verification.json').read_text())
    assert [list(map(int,line.split())) for line in compared.splitlines()]==candidate_proof['cases']
    print(json.dumps({'complete_small_native_rows':607500,'proper_rows':566000,'candidate_sets_compared':4}),flush=True)
    native=compile_source('native_regional.cpp',work)
    summary=json.loads((HERE/'result.json').read_text())
    totals=Counter()
    for filename in summary['new_completed_E2_receipts']:
        receipt=json.loads((HERE/'receipts'/filename).read_text());row=receipt['profile']
        assert receipt['engine']=='regional' and receipt['complete_profile_exclusion'] and row['embedded_sizes']==[13,13]
        assert digest(HERE/'sources/native_regional.cpp')['sha256']==receipt['native_source_sha256']
        cmd=[native,a.mixed_proof/'inputs/obs',a.mixed_proof/'inputs/parent',a.mixed_proof/'inputs/B',
             a.mixed_proof/'frames/frames_2_26.txt',','.join(map(str,row['proper_sizes'])),'13,13','2592','9995','0','4','0','0',','.join(['0']*14),HERE/'cost_defect_options.txt',work/'small_proper']
        run=subprocess.run(cmd,text=True,capture_output=True,check=True)
        lines=run.stderr.splitlines();assert not run.stdout and len(lines)==4
        counts=list(map(int,lines[0].split()));assert counts==receipt['counts']
        for i,label,field in [(1,'marginal','marginal_test_prune_counts'),(2,'capacity','capacity_test_prune_counts'),(3,'smallbank','small_bank_node_candidate_counts')]:
            values=lines[i].split();assert values[0]==label and list(map(int,values[1:]))==receipt[field]
        assert counts[0]==4 and counts[-1]==0
        totals['frames']+=counts[0];totals['nodes']+=counts[1]
        print(json.dumps({'E2_replayed':filename,'counts':counts}),flush=True)
    assert totals['frames']==8 and totals['nodes']==12971519
    # Rebuild the complete typed E3 bank, but retain the frozen original
    # row order for exact comparison of deterministic native node counts.
    receipts=json.loads((HERE/'e3/integer_receipts.json').read_text())
    typed={tuple(map(int,part.split('-')[:2])) for r in receipts for part in r['tag'].split('_')}
    assert len(typed)==8
    required=[line for line in seed_lines if tuple(map(int,line.split(None,2)[:2])) in typed]
    ework=work/'e3';ework.mkdir(exist_ok=True)
    (ework/'needed').write_bytes(b'\n'.join(required)+b'\n')
    ceilings={}
    for n,c in typed:ceilings[n]=max(ceilings.get(n,0),c)
    (ework/'caps').write_text(' '.join(str(ceilings.get(n,0)) for n in range(14))+'\n')
    subprocess.run([genprof,HERE/'inputs/linear',ework/'needed',ework/'caps',ework/'generated_bank'],stdout=subprocess.DEVNULL,check=True)
    rebuilt=list(struct.iter_unpack('<QQII',(ework/'generated_bank').read_bytes()))
    original=list(struct.iter_unpack('<QQII',(HERE/'e3/bank.bin').read_bytes()))
    assert len(rebuilt)==len(original)==87500 and set(rebuilt)==set(original)
    # Expand the native validator's size range only; its observer-price and
    # forbidden-triple checks are unchanged and also cover the core classes.
    echeck_source=ework/'verify_e3_bank.cpp'
    echeck_source.write_text(portable_filter.replace('"native_original.cpp"','"'+str((HERE/'sources/native_original.cpp').resolve())+'"').replace('assert(s>=8&&s<=10);','assert(s>=8&&s<=13);'))
    subprocess.run(['c++','-std=c++20','-O3','-mpopcnt',echeck_source,'-o',ework/'verify_e3_bank'],check=True)
    subprocess.run([ework/'verify_e3_bank',a.mixed_proof/'inputs/obs',a.mixed_proof/'inputs/parent',HERE/'e3/bank.bin',ework/'proper_unused',ework/'caps'],stdout=subprocess.DEVNULL,check=True)
    third=a.previous/'previous/previous/previous/previous/previous'
    sys.path[:0]=[str(third/'low'),str(third/'previous/bounds')]
    from cores import orbits
    fixed,seen,reps=orbits(2);assert fixed==seen and len(reps)==6
    full=(1<<125)-1
    core_text=''
    for rows,centers in reps:
        free=full^sum(rows);core_text+=' '.join(map(str,[free%(1<<64),free>>64,*centers]))+'\n'
    assert core_text==(HERE/'e3/cores2.txt').read_text()
    (ework/'cores2.txt').write_text(core_text);shutil.copyfile(HERE/'inputs/linear',ework/'linear')
    punctures=sorted((lo,hi,int(s>=256)) for lo,hi,c,s in original if s%256==12 and c==1116)
    assert len(punctures)==3000
    (ework/'punct').write_text('1\n12 1116 3000\n'+''.join(f'{lo} {hi} {r}\n' for lo,hi,r in punctures))
    anchor=compile_source('anchor.cpp',work)
    for h in (0,1):
        raw=subprocess.check_output([anchor,'2',str(h),'1',ework/'punct',ework/'cores2.txt'],text=True)
        original_anchor=dependencies['E3_original_anchor_files'][h]
        assert sha256(raw.encode()).hexdigest()==original_anchor['sha256']
        compact=''.join(' '.join(line.split()[:2])+' 0\n' for line in raw.splitlines())
        assert compact==(HERE/'e3'/f'anchored2_{h}').read_text()
        (ework/f'anchored2_{h}').write_text(compact)
    exact=compile_source('front_orbit_min_witness.cpp',work)
    types=sorted(typed);requests=[]
    for r in receipts:
        assert digest(HERE/'sources/front_orbit_min_witness.cpp')['sha256']==r['source_sha256']
        count={tuple(map(int,part.split('-')[:2])):int(part.split('-')[2]) for part in r['tag'].split('_')}
        requests.append(' '.join(map(str,[9865]+[count.get(t,0) for t in types])))
    answer=subprocess.run([exact,HERE/'e3/bank.bin',ework,ework],input='\n'.join(requests)+'\n',text=True,capture_output=True,check=True)
    assert not answer.stderr
    responses=[list(map(int,line.split())) for line in answer.stdout.splitlines()]
    assert len(responses)==2
    for record,response in zip(receipts,responses):
        assert response==[record[k] for k in ('cost','geometric_nodes','leaf_nodes','search_nodes','found')]
    result={'schema':'MOTHER12_D_REPLAY_V1','all_verified':True,'price_capacity':price,
            'expanded_small_native_classes':607500,'complete_small_proper_classes':566000,
            'new_E2_complete_profiles':2,'new_E2_frames':8,'new_E2_search_nodes':12971519,
            'inherited_C_E2_complete_profiles':4,'total_E2_complete_profiles':6,'E2_profiles_pending_in_snapshot':8,
            'complete_E2_exclusion':False,'E3_arithmetic':e3,'E3_native_classes':87500,
            'E3_native_responses':responses,'E3_exact9865_excluded':True,
            'inherited_three_core_search_rerun':False,'review_status':'NOT_REVIEWED'}
    (work/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
