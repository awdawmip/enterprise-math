#!/usr/bin/env python3
"""Independent Python reproduction of the original-input signed-root cancellation.
Run beside the preceding EC49FOK independent Python verifier, at its frozen
commit ba72605fed95280371a262362997e5aceee2564c. Requires the frozen master.
The trie DP is reconstructed in Python; no C++ cost/CSV result is imported.
"""
import importlib.util
import itertools
import sys
from pathlib import Path

ROOTS=(3,5,6,7)
IDS=(32318,32274,32287)
spec=importlib.util.spec_from_file_location(
    "fok_py", Path(__file__).with_name("VERIFY_EC49FOK_INDEPENDENT.py"))
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.IDS=IDS

def main(path):
    words,cases=mod.parse(path)  # includes frozen source SHA256 check
    prof={x:{r:mod.table(words,cases[x],r) for r in ROOTS} for x in IDS}
    dom={x:mod.domain(prof[x]) for x in IDS}
    assert dom[32318]==dom[32274]==dom[32287]
    choices=[dom[32318][l] for l in range(24)]
    assert __import__("math").prod(len(x) for x in choices)==648
    witness=(5,6,5,6,6,5,5,6,5,6,6,7,5,6,6,3,5,3,6,7,5,3,5,6)
    for target in (32274,32287):
        total=nonzero=canceled=mixed=0
        first=10**9
        samples=[]
        for assignment in itertools.product(*choices):
            local_delta=[];c1=c2=0
            for root in ROOTS:
                def cost(x):
                    labels,ix,dp=prof[x][root]
                    mask=sum(1<<ix[l] for l,r in enumerate(assignment) if r==root)
                    return dp[mask]
                a=cost(32318);b=cost(target)
                local_delta.append(b-a);c1+=a;c2+=b
            delta=sum(local_delta)
            total+=1
            if any(local_delta):
                nonzero+=1
                if delta==0:
                    canceled+=1
                    samples.append((assignment,c1,c2,tuple(local_delta)))
            if min(local_delta)<0 and max(local_delta)>0:mixed+=1
            if delta:first=min(first,c1,c2)
        assert (total,nonzero,canceled,mixed,first)==(648,244,2,2,156)
        assert any(a==witness and c1==c2==180 and d==(-1,0,0,1)
                   for a,c1,c2,d in samples)
        print(f"PY_INDEPENDENT_PASS 32318->{target} full_assignments={total} "
              f"nonzero_component={nonzero} exact_cancellations={canceled} first_sep={first}")
        for w,c1,c2,d in samples:
            print("CANCEL",target,"assignment="," ".join(map(str,w)),
                  "costs=",c1,c2,"rootdelta=",d)
    print("EC49FOL_INDEPENDENT_EXACT_PASS")
if __name__=="__main__":main(sys.argv[1])
