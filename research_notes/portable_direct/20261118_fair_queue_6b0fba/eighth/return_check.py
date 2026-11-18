"""Return-defect audit, integer count checks and optional pinned BRC replay."""
import argparse
from collections import Counter
from fractions import Fraction as F
import gzip
import hashlib
import importlib
import json
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile

ARCHIVE_SHA='df9808c2bee3365d46e3f1c2b674245115cad457711c37a1c7ee1b2e88124e78'
KERNEL_BLOB='4e6b3132580e3cd70a20a0d8bd4d28792b961afb'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def pair_plan(L,R):
    q,ell=divmod(L,2*R)
    s=max(0,ell-R)
    B=min(ell,2*R-ell)
    a=2*q*R+s
    starts=[2*j*R+i for j in range(q) for i in range(R)]
    starts.extend(range(2*q*R,2*q*R+s))
    return a,B,starts


def public_checks():
    counts=Counter()
    for m in range(1,9):
        L=1<<m
        for R in range(1,L):
            a,B,starts=pair_plan(L,R)
            assert sorted(starts+[i+R for i in starts]+list(range(a,a+B)))==list(range(L))
            for r in range(1,R+1):
                if R%r: continue
                groups=Counter(i%r for i in starts)
                tails=Counter(i%r for i in range(a,a+B))
                q,ell=divmod(L,2*R)
                s=max(0,ell-R)
                assert max(groups.values())==q*(R//r)+(s+r-1)//r
                singles=sum(v==1 for v in tails.values())
                assert singles==(B if B<=r else max(0,2*r-B))
                counts['residue_multiplicity_checks']+=1
            counts['partitions']+=1
    L=4; R=3
    a,B,sel=pair_plan(L,R)
    signs=[1,-1,-1,1]
    assert sum(signs)==0 and sum(signs[a:a+B])==-2 and sum(signs[:B])==0
    Delta=sum((signs[i]+signs[i+R])**2 for i in range(L-R))
    mu=F(sum(signs[a:a+B])**2,L**2)
    assert mu==F(1,4) and len(sel)*Delta==L*L*mu
    # The common three-outcome basis measurement: the rare conditional TV
    # stays one even though the entire output TV tends to zero.
    t=F(1,100)
    pa=(1/(1+t*t),t*t/(1+t*t),F())
    pb=(1/(1+t*t),F(),t*t/(1+t*t))
    assert sum(abs(a-b) for a,b in zip(pa,pb))/2 == F(1,10001)
    assert pa[1]/sum(pa[1:]) - pb[1]/sum(pb[1:])==1
    return dict(counts,zero_parent_equal_budget=True,rare_conditional_tv='1')


def typed_tests(h):
    op=h.Ops()
    I,N,H,S=h.eye(),h.neg0(),h.hadamard4_fixture(),h.swap01()
    A={(1,0):F(1)}
    assert h.carry(op,[S],1,A)==1 and h.carry(op,[S],1,h.tr(A))==0
    words=[S,H,N]
    av=[h.alpha(op,words,i) for i in range(8)]
    queries=0
    for R in range(1,8):
        for k in range(4):
            for prefix in range(1<<k):
                fixed={(3-k+b):((prefix>>b)&1) for b in range(k)}
                J=h.carry_restricted(op,words,R,A,fixed)
                pairs=[f for f in range(8-R) if f>>(3-k)==prefix]
                lhs=op.obs('audit_direct_nonsymmetric',((op.dot(av[f+R],op.apply(A,av[f])),) for f in pairs))
                assert J==lhs
                queries+=1
    # O is globally different from -I but equals -I on the active source span.
    ar=h.alpha(op,[N],1)
    assert ar==op.apply(N,h.alpha(op,[N],0)) and N[(1,1)]==1 and ar=={0:-1}
    # An additional rational orthogonal test operator. Arithmetic on the
    # complete 61-coordinate carrier goes through the archived positive observer.
    U=I.copy()
    U.update({(0,0):F(399,401),(0,1):F(-40,401),(1,0):F(40,401),(1,1):F(399,401)})
    assert op.mul(h.tr(U),U)==I
    words=[I,N,I,U]
    L,R,mod,c=16,6,7,2
    assert pow(c,R,mod)==1 and pow(c,3,mod)==1 and c%mod!=1
    a,B,starts=pair_plan(L,R)
    vs=[h.alpha(op,words,i) for i in range(L)]
    deltas=[op.vadd(vs[f],vs[f+R]) for f in range(L-R)]
    DD=op.obs('audit_energy',((op.dot(d,d),) for d in deltas))
    J=h.carry(op,words,R,I)
    assert DD==op.obs('audit_norm_identity',((2,L-R),(2,J)))
    def grouped_norm(entries):
        labels={}
        for i,v in entries:
            lab=pow(c,i,mod)
            labels[lab]=op.vadd(labels.get(lab,{}),v)
        return op.obs('audit_grouped_norm',((op.dot(v,v),) for v in labels.values()))
    error=grouped_norm((f,deltas[f]) for f in starts)
    tail=grouped_norm((i,vs[i]) for i in range(a,a+B))
    mu=F(2,L*L)
    assert error<=2*DD and tail/(L*L)>=mu
    assert (DD,tail)==(F(22424,160801),F(328002,160801))
    old=6*DD/(L*L*mu); improved=2*DD/(L*L*mu)
    assert improved < F(1,4) < old
    return dict(nonsymmetric_prefix_queries=queries,global_O_correction=True,
                new_typed_kernel_calls=op.counts['actual_BRC_kernel_calls'],
                grouped_example=dict(L=L,R=R,B=B,a=a,P=len(starts),Pmax=2,
                    delta=str(DD),mu=str(mu),actual_tail_mass=str(tail/(L*L)),
                    true_error_squared=str(error/(L*L)),old_tv_bound_squared=str(old),
                    new_tv_bound_squared=str(improved),epsilon='1/2'))


def replay(p):
    data=p.read_bytes()
    assert len(data)==95202 and sha(data)==ARCHIVE_SHA
    with ZipFile(p) as z, TemporaryDirectory() as directory:
        root=Path(directory)
        man=json.loads(z.read('MANIFEST.json'))['files']
        assert set(z.namelist())==set(man)|{'MANIFEST.json'}
        for name,spec in man.items():
            b=z.read(name)
            blob=hashlib.sha1(('blob '+str(len(b))+'\0').encode()+b).hexdigest()
            assert len(b)==spec['bytes'] and sha(b)==spec['sha256'] and blob==spec['git_blob']
            if name.endswith('.py'):
                assert Path(name).name==name
                (root/name).write_bytes(b)
        assert man['brc_weighted_recurrent.py']['git_blob']==KERNEL_BLOB
        subprocess.run([sys.executable,'-B','check_return_defect.py'],cwd=root,
                       check=True,stdout=subprocess.DEVNULL)
        old=json.loads(z.read('TEST_RESULTS.json'))
        new=json.loads((root/'TEST_RESULTS.json').read_bytes())
        for d in (old,new): d.pop('elapsed_seconds_observed')
        assert old==new and new['checks']==217
        receipts=gzip.decompress(z.read('BRC_OBSERVER_RECEIPTS.json.gz'))
        assert receipts==gzip.decompress((root/'BRC_OBSERVER_RECEIPTS.json.gz').read_bytes())
        sys.path.insert(0,str(root))
        host=importlib.import_module('check_return_defect')
        addition=typed_tests(host)
        return dict(archive_sha256=sha(data),manifest_payloads=len(man),checks=new['checks'],
                    counts=new['counts'],test_records_agree_except_wall_time=True,
                    receipt_plain_bytes=len(receipts),receipt_plain_sha256=sha(receipts),
                    extra_interface=addition)


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--archive',type=Path,help='externally supplied frozen zip')
    args=parser.parse_args()
    summary={'public_checks':public_checks()}
    if args.archive: summary['archive_replay']=replay(args.archive)
    print(json.dumps(summary,indent=2))
