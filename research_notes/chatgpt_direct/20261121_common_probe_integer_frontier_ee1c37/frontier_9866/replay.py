"""Audit a partial 9866 search checkpoint and its exact missing set."""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys

HERE=Path(__file__).resolve().parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mother',type=Path,default=HERE.parent/'integer_cuts/mother12')
    p.add_argument('--defect',type=Path,default=HERE.parent/'mother_sublevels_D')
    p.add_argument('--lower',type=Path,default=HERE.parent/'lower')
    p.add_argument('--previous',type=Path,default=HERE.parent/'previous')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();args.output.mkdir(parents=True,exist_ok=True)
    b=json.loads((HERE/'bindings.json').read_text())
    for item in b['dependencies']:
        assert sha256((getattr(args,item['root'])/item['path']).read_bytes()).hexdigest()==item['sha256'],item
    assert sha256((HERE/'original_driver.py').read_bytes()).hexdigest()==b['driver_sha256']
    subprocess.run([sys.executable,'-B',HERE/'exact_price_frontier.py','--cost','9866',
                    '--mother-proof',args.mother,'--defect-catalog',args.defect/'cost_defect_catalog.json',
                    '--output',args.output/'typed_frontier.json'],check=True,stdout=subprocess.DEVNULL)
    typed=json.loads((args.output/'typed_frontier.json').read_text())
    target={r['tag'] for r in typed['survivors']}
    assert len(target)==117
    rows=[json.loads(line) for line in (HERE/'receipts.jsonl').read_text().splitlines()]
    done={r['tag'] for r in rows};assert len(done)==len(rows) and done<=target
    assert target-done==set((HERE/'pending_profiles.txt').read_text().splitlines())
    assert target==set((HERE/'selected_profiles.txt').read_text().splitlines())
    for r in rows:
        assert r['cost']==9866 and r['found']==0
        for key in ('source_sha256','bank_sha256','driver_sha256'):
            assert r[key]==b[key]
    result=json.loads((HERE/'expected.json').read_text())
    assert result['completed_profiles']==len(rows)
    assert result['pending_profiles']==len(target-done)
    assert result['whole_cost_layer_complete']==(target==done)
    for key in ('search_nodes','geometric_nodes','leaf_nodes'):
        assert result[key]==sum(r[key] for r in rows)
    for e,expected in result['by_embedded_count'].items():
        group={r['tag'] for r in typed['survivors'] if r['embedded_count']==int(e)}
        actual=[r for r in rows if r['tag'] in group]
        assert expected=={'required':len(group),'completed':len(actual),'complete':group<=done,
                          'search_nodes':sum(r['search_nodes'] for r in actual)}
    result['audit_passed']=True
    result['search_rerun']=False
    (args.output/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,sort_keys=True))


if __name__=='__main__':
    main()
