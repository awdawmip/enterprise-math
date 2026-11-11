"""Compute positive hidden-word masses using the C62 native histogram carrier."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from zipfile import ZipFile

def check(archive, fiber_module):
    sys.path.insert(0, str(fiber_module.resolve()))
    from verify_fibers import inversion_count, words, likelihood_of_block_and_pair
    with tempfile.TemporaryDirectory() as tmp, ZipFile(archive) as z:
        root=Path(tmp)/'prime_quantum_schedule_extrema_c62'
        for name in z.namelist():
            if name.startswith(root.name+'/') and name.endswith('.py'):
                dest=(Path(tmp)/name).resolve()
                if not dest.is_relative_to(root):
                    raise ValueError('Unrecognised archive member')
                dest.parent.mkdir(parents=True,exist_ok=True)
                dest.write_bytes(z.read(name))
        sys.path.insert(0,str(root))
        import schedule_extrema as old
        native=old.old.prior.inherited.old.old.inherited.native
        raw=Path(native.__file__).read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert blob=='9a3962ec095095f14e63a91cfe6b7ebf07d9a1d1'
        serial=merged=0
        counts=[]
        for r,c,d,a,b,x in [(1,2,6,2,5,4),(2,10,8,7,5,23)]:
            members=[v for v in words(a,b) if inversion_count(v)==x]
            counts.append(len(members))
            for rate in [Q(1,4),Q(1),Q(4)]:
                observed=native.weight_histogram([])
                expected=Q(0)
                for word in members:
                    f,g=c,d
                    hist=native.weight_histogram([1])
                    for p in word:
                        total=2*r+rate*f+g
                        w=(rate*f if p=='5' else g)/total
                        hist=native.histogram_serial(hist,native.weight_histogram([w]))
                        serial+=1
                        f-=int(p=='5')
                        g-=int(p=='7')
                    next_rate=1 if rate==Q(1,4) else 4
                    for w in (r/(2*r+rate*f+g),Q(r,2*r-1+next_rate*f+g)):
                        hist=native.histogram_serial(hist,native.weight_histogram([w]))
                        serial+=1
                    mass=likelihood_of_block_and_pair(word,r,c,d,rate)
                    assert hist.total_mass==mass
                    expected+=mass
                    observed=native.histogram_recoalesce(observed,hist)
                    merged+=1
                assert observed.total_mass==expected and observed.count==len(members)
        return dict(fiber_sizes=counts,serial=serial,recoalescences=merged,native_git_blob=blob)

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('c62_zip',type=Path)
    args=parser.parse_args()
    print(json.dumps(check(args.c62_zip,Path(__file__).resolve().parents[1]/'fiber'),indent=2))
