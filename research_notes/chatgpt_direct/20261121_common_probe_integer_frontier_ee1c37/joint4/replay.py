"""Portable audit or full verification of the completed four-fiber increment."""
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
    p.add_argument('--work',type=Path,required=True)
    p.add_argument('--mode',choices=('audit','full'),default='audit')
    a=p.parse_args()
    a.integer_cuts=a.integer_cuts.resolve();a.previous=a.previous.resolve();a.work=a.work.resolve()
    a.work.mkdir(parents=True,exist_ok=True)
    manifest=json.loads((HERE/'manifest.json').read_text())
    for row in manifest['files']:
        assert sha256((HERE/row['path']).read_bytes()).hexdigest()==row['sha256'],row['path']
    for row in manifest['dependencies']:
        root=a.integer_cuts if row['root']=='integer_cuts' else a.previous
        assert sha256((root/row['path']).read_bytes()).hexdigest()==row['sha256'],row
    commands=[
        [sys.executable,HERE/'verify_four_fiber_separator.py',
         '--old-witness',a.integer_cuts/'all_joint_exact/cover_2.json',
         '--new-witness',HERE/'cover_2.json','--output',a.work/'separator.json']]
    if a.mode=='full':
        commands.extend([
          [sys.executable,HERE/'verify_new_survivor.py','--witness',HERE/'cover_2.json',
           '--prior-cuts',a.integer_cuts,'--delivery',a.previous,'--output',a.work/'direct_verification.json'],
          [sys.executable,HERE/'separate_coordinate_parity.py','--witness',HERE/'cover_2.json',
           '--output',a.work/'coordinate_parity.json'],
          [sys.executable,a.integer_cuts/'portable/verify_integer_xor.py',
           '--witness-dir',HERE,'--parallel-module',a.integer_cuts/'parallel_family.py',
           '--work',a.work/'xor','--output',a.work/'xor_verification.json','--frames','2']])
    for command in commands:subprocess.run(list(map(str,command)),check=True)
    checked=a.work if a.mode=='full' else HERE/'checks'
    native=json.loads((checked/'direct_verification.json').read_text())
    parity=json.loads((checked/'coordinate_parity.json').read_text())
    xor=json.loads((checked/'xor_verification.json').read_text())
    assert native['all_checks_passed'] and parity['violated_indexed_cuts']==0
    assert parity['indexed_cuts']==32768
    assert xor['frames'][0]['verified'] and xor['frames'][0]['indexed_cuts']==22371336
    digest=sha256((HERE/'cover_2.json').read_bytes()).hexdigest()
    assert native['witness_sha256']==parity['witness_sha256']==xor['frames'][0]['witness_sha256']==digest
    result={'mode':a.mode,'source_bindings_passed':True,'old_point_separated':True,
       'new_exact_fractional_survivor':True,'new_positive_free_classes':304,
       'new_coordinate_additive_parity_indexed_cuts':32768,
       'native_classes_checked':native['native_unique_classes'],
       'star_checks':native['native']['star_checks_inside_free'],
       'inherited_modular_family_indices':12413656,'xor_indices':22371336,
       'verification_reexecuted':a.mode=='full','all_checks_passed':True,
       'review_status':'NOT_REVIEWED'}
    (a.work/'result.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))


if __name__=='__main__':main()
