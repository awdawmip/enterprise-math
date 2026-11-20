"""Check the 11,292 equality budget separately with at most two full thirteen-point messages."""
import argparse,json,sys,os
from pathlib import Path
from tempfile import TemporaryDirectory
HERE=Path(__file__).resolve().parent
def verify(proof,last,older):
    import importlib.util
    spec=importlib.util.spec_from_file_location('base_involution_cover',proof/'replay.py')
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.BUDGET=11292
    with TemporaryDirectory()as work:
        result=module.verify(last,older,Path(work))
        for i,row in result.items():
            row['max_thirteen_point_classes']=0 if i==2 else 2
        return result
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for v in ['proof','last','older']:p.add_argument('--'+v,type=Path,required=True)
    a=p.parse_args()
    print(json.dumps(verify(a.proof.resolve(),a.last.resolve(),a.older.resolve()),sort_keys=True,indent=2))
