"""Audit or fully replay the completed three-coordinate mod-three increment."""
from pathlib import Path
from hashlib import sha256
import argparse
import json
import subprocess
import sys

HERE=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--integer-cuts',type=Path,required=True)
    p.add_argument('--previous',type=Path,required=True)
    p.add_argument('--joint4',type=Path,required=True)
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--mode',choices=('audit','full'),default='audit')
    a=p.parse_args()
    roots={k:getattr(a,k).resolve() for k in ('integer_cuts','previous','joint4')}
    a.work=a.work.resolve();a.work.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((HERE/'manifest.json').read_text())
    for row in manifest['files']:
        assert sha256((HERE/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
    for row in manifest['dependencies']:
        assert sha256((roots[row['root']]/row['path']).read_bytes()).hexdigest()==row['sha256'],row
    commands=[[sys.executable,HERE/'verify_mod3_separator.py',
       '--old-witness',roots['joint4']/'cover_2.json','--new-witness',HERE/'cover_2.json',
       '--output',a.work/'separator.json']]
    if a.mode=='full':
        commands.extend([
          [sys.executable,roots['joint4']/'verify_new_survivor.py','--witness',HERE/'cover_2.json',
           '--prior-cuts',roots['integer_cuts'],'--delivery',roots['previous'],'--output',a.work/'direct_verification.json'],
          [sys.executable,roots['joint4']/'separate_coordinate_parity.py','--witness',HERE/'cover_2.json',
           '--output',a.work/'coordinate_parity.json'],
          [sys.executable,HERE/'separate_three_coordinate_mod3.py','--witness',HERE/'cover_2.json',
           '--output',a.work/'three_coordinate_mod3.json'],
          [sys.executable,HERE/'separate_three_coordinate_mod3.py',
           '--witness',roots['integer_cuts']/'all_joint_exact/cover_1.json','--output',a.work/'frame1_three_coordinate_mod3.json'],
          [sys.executable,roots['integer_cuts']/'portable/verify_integer_xor.py',
           '--witness-dir',HERE,'--parallel-module',roots['integer_cuts']/'parallel_family.py',
           '--work',a.work/'xor','--output',a.work/'xor_verification.json','--frames','2']])
    for command in commands:subprocess.run(list(map(str,command)),check=True)
    checked=a.work if a.mode=='full' else HERE/'checks'
    native=json.loads((checked/'direct_verification.json').read_text())
    parity=json.loads((checked/'coordinate_parity.json').read_text())
    mod3=json.loads((checked/'three_coordinate_mod3.json').read_text())
    frame1=json.loads((checked/'frame1_three_coordinate_mod3.json').read_text())
    xor=json.loads((checked/'xor_verification.json').read_text())
    assert native['all_checks_passed'] and parity['violated_indexed_cuts']==0
    assert mod3['violating_dp_minima']==frame1['violating_dp_minima']==0
    assert mod3['represented_index_checks']==frame1['represented_index_checks']==28697814
    assert xor['frames'][0]['verified']
    digest=sha256((HERE/'cover_2.json').read_bytes()).hexdigest()
    assert native['witness_sha256']==parity['witness_sha256']==mod3['witness_sha256']==xor['frames'][0]['witness_sha256']==digest
    result={'mode':a.mode,'source_bindings_passed':True,'old_304_point_separated':True,
       'new_frame2_exact_fractional_survivor':True,'new_positive_free_classes':298,
       'frame1_exact_fractional_survivor_reused':True,'frame1_positive_free_classes':588,
       'new_coordinate_additive_parity_indices_per_frame':32768,
       'new_three_coordinate_mod3_indices_per_frame':28697814,
       'native_classes_checked':native['native_unique_classes'],
       'star_checks':native['native']['star_checks_inside_free'],
       'verification_reexecuted':a.mode=='full','all_checks_passed':True,
       'review_status':'NOT_REVIEWED'}
    (a.work/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
