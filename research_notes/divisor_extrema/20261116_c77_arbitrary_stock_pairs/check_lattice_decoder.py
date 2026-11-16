"""Compile and independently replay the exact 72M inversion at its threshold."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
from lattice_decoder import decode
from check_far_decoder import _native


def main():
    c,n=100,7200
    here=Path(__file__).resolve().parent
    checks=[]
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/"lll"
        subprocess.run(["c++","-O3","-std=c++17",str(here/"kernel_lll.cpp"),"-lgmpxx","-lgmp","-o",str(exe)],check=True)
        for v,w in ((37,23),(100,3),(100,100),(2,2)):
            observed=_native(n,v,w)
            cert={}
            result=decode(c,n,observed,executable=exe,certificate=cert)
            assert result==(v,w)
            checks.append(cert)
    return dict(outer_stock=n,cap=c,physical_cases=checks)


if __name__=="__main__":
    print(json.dumps(main(),indent=2))
