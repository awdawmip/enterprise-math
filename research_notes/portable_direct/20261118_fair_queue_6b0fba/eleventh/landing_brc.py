"""Exact two-round landing tests, with positive signed endpoints and actual BRC transfer."""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from pathlib import Path
import sys

CORE="7520822074b8f29e1c54f57b9543c043202db8bd7c6e27f3f1d6176028ac4a26"
COMPILER="e8f7048e2e73292bda230a2adad4aaa76f0b3cd5525f8f0899628bd649d1d81d"
D=61
WIDTH=2
ZERO=(0,)*(2*D)
UNIT=(1,)+(0,)*(2*D-1)


class Positive:
    def __init__(self,repo):
        file=repo/'src/enterprise_math/brc_weighted_recurrent.py'
        assert sha256(file.read_bytes()).hexdigest()==CORE
        source=repo/'research_notes/directed_recovery/20260926_C6438C/new_word_compiler/certified_word_compiler.py'
        assert sha256(source.read_bytes()).hexdigest()==COMPILER
        assert "QUARTER_WORD = (('swap', 0, 1), ('neg', 1))" in source.read_text()
        spec=spec_from_file_location('frozen_positive_brc',file)
        mod=module_from_spec(spec);sys.modules[spec.name]=mod;spec.loader.exec_module(mod)
        self.core=mod;self.calls=Counter()
        self.swap=self.columns('swap_0_1', (2,3,0,1))
        self.neg1=self.columns('neg_coordinate_1',(0,1,3,2))
        self.sign=self.columns('readout_negation',(1,0))
        self.identity=self.columns('fixed_coordinate_identity',(0,1))
        # Rows are source-to-destination; quarter is applied in time order.
        assert self.neg1[self.swap[0]]==3
        assert self.neg1[self.swap[2]]==0

    def power(self,name,graph,depth):
        self.calls[name]+=1
        return self.core.recurrent_mass_power(graph,depth)

    def columns(self,name,permutation,depth=1):
        n=len(permutation)
        graph=[[int(permutation[i]==j) for j in range(n)] for i in range(n)]
        actual=self.power(name,graph,depth)
        assert all(sum(row)==1 and max(row)==1 for row in actual)
        return tuple(row.index(1) for row in actual)

    @lru_cache(None)
    def plus(self,a,b):
        graph=[[0,a,b,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]
        return int(self.power('positive_fan_in',graph,2)[0][3])

    @lru_cache(None)
    def times(self,a,b):
        graph=[[0,a,0],[0,0,b],[0,0,0]]
        return int(self.power('positive_path_product',graph,2)[0][2])

    @lru_cache(None)
    def square(self,pos,neg):
        # Parallel sign endpoints of all two-walk products; xor combines signs.
        count=self.power('signed_endpoint_self_product',((pos,neg),(neg,pos)),2)[0]
        return int(count[0]-count[1])

    def add(self,x,y):
        return tuple(self.plus(a,b) for a,b in zip(x,y))

    def norm(self,row):
        s=0
        for i in range(D):
            s=self.plus(s,self.square(row[2*i],row[2*i+1]))
        return s

    def destination(self,src,quarter,negative):
        # The remaining 59 coordinates belong to the fixed two-sign blocks.
        mid=self.neg1[self.swap[src]] if quarter and src<4 else 2*(src//2)+self.identity[src%2]
        return (mid//2)*2+self.sign[mid%2] if negative else mid

    def action(self,row,quarter,negative):
        out=[0]*(2*D)
        for src,value in enumerate(row):
            out[self.destination(src,quarter,negative)]=value
        return tuple(out)


def test(N,brc):
    w=N.bit_length()
    assert N==(1<<w)-1
    # Native bit line i goes to i+1 (mod w); packing returned wires is decoding.
    # All-ones is a padded fixed label and is never a live modular residue.
    wire=tuple((i+1)%w for i in range(w))
    def endpoints(shift):
        columns=brc.columns('cyclic_bit_wires',wire,shift)
        return tuple(sum(1<<columns[i] for i in range(w) if z>>i&1) for z in range(N+1))
    rotations=[endpoints(i) for i in range(w)]
    for z in range(N):
        assert rotations[1][z]==(2*z if 2*z<N else 2*z-N)
    assert rotations[1][N]==N
    moves=[rotations[(1<<(WIDTH-1-i))%w] for i in range(WIDTH)]
    inv=[[col.index(z) for z in range(N+1)] for col in moves]
    all_z=range(N+1)
    compiled={():{z:(UNIT if z==1 else ZERO) for z in all_z}}
    # Forward landing contraction over integers; common denominator 2^depth.
    for i in range(WIDTH):
        for h in product((0,1),repeat=i):
            old=compiled[h]
            for bit in (0,1):
                after={}
                for z in all_z:
                    right=brc.action(old[inv[i][z]],quarter=i==1 and h[0]==1,negative=bool(bit))
                    after[z]=brc.add(old[z],right)
                compiled[h+(bit,)]=after

    def suffix_atom(row,h,cut,bits):
        shift=0
        for i,choice in enumerate(bits,cut):
            if choice:
                shift+=1<<(WIDTH-1-i)
                row=brc.action(row,quarter=i==1 and h[0]==1,negative=bool(h[i]))
        return shift%w,row

    def suffix_kernels(h):
        # K_i[delta] is the actual positive transfer on both sign endpoints
        # of all 61 coordinates. Prepending a selected gate composes it FIRST.
        d=len(h); eye=[{src:1} for src in range(2*D)]
        layers=[None]*(d+1);layers[d]={0:eye}
        for i in reversed(range(d)):
            current={}
            for shift,kernel in layers[i+1].items():
                for selected in (False,True):
                    dest_shift=(shift+int(selected)*(1<<(WIDTH-1-i)))%w
                    if dest_shift not in current:
                        current[dest_shift]=[{} for _ in range(2*D)]
                    bank=current[dest_shift]
                    for src in range(2*D):
                        mid=brc.destination(src,i==1 and h[0]==1,bool(h[i])) if selected else src
                        for dst,mass in kernel[mid].items():
                            bank[src][dst]=brc.plus(bank[src].get(dst,0),mass)
            layers[i]=current
        return layers

    def contract(prefix,layer,z):
        counts=[0]*(2*D)
        for shift,kernel in layer.items():
            source=rotations[(-shift)%w][z]
            for src,mass in enumerate(prefix[source]):
                if mass:
                    for dest,coefficient in kernel[src].items():
                        counts[dest]=brc.plus(counts[dest],brc.times(coefficient,mass))
        return tuple(counts)

    direct={}
    rows=[]; cut_tests=0
    digest=sha256()
    for d in range(WIDTH+1):
        for h in product((0,1),repeat=d):
            key=''.join(map(str,h))
            reference={z:ZERO for z in all_z}
            for word in product((0,1),repeat=d):
                # No inverse lookup or grouped prefix here.
                z=1;atom=UNIT
                for i,b in enumerate(word):
                    if b:
                        z=moves[i][z]
                        atom=brc.action(atom,quarter=i==1 and h[0]==1,negative=bool(h[i]))
                reference[z]=brc.add(reference[z],atom)
            direct[h]=reference
            layers=suffix_kernels(h)
            for cut in range(d+1):
                # Group the suffix words by actual cyclic displacement, but apply
                # each signed feedback word in its declared chronological order.
                packets=defaultdict(list)
                for word in product((0,1),repeat=d-cut):
                    shift=sum((1<<(WIDTH-1-i))*b for i,b in enumerate(word,cut))%w
                    packets[shift].append(word)
                for z in all_z:
                    total=ZERO
                    for shift,terms in packets.items():
                        start=rotations[(-shift)%w][z]
                        for word in terms:
                            displacement,part=suffix_atom(compiled[h[:cut]][start],h,cut,word)
                            assert displacement==shift
                            total=brc.add(total,part)
                    from_kernel=contract(compiled[h[:cut]],layers[cut],z)
                    assert from_kernel==total==reference[z]==compiled[h][z]
                    cut_tests+=1
            sparse=[];h_norm=0
            for z in all_z:
                positive=reference[z]
                signed=[positive[i]-positive[i+1] for i in range(0,2*D,2)]
                n=brc.norm(positive);h_norm=brc.plus(h_norm,n)
                digest.update(json.dumps([key,z,signed],separators=(',',':')).encode()+b'\n')
                if any(positive):
                    sparse.append(dict(z=z,sign_endpoints=[[j,positive[2*j],positive[2*j+1]]
                        for j in range(D) if positive[2*j] or positive[2*j+1]],
                        norm_numerator=n))
            rows.append(dict(history=key,amplitude_denominator=1<<d,norm_denominator=1<<(2*d),
                             norm_numerator=h_norm,work_rows=sparse))
    joint=[];proposed_checks=0
    for i in range(WIDTH):
        for h in product((0,1),repeat=i):
            parent=direct[h]; m=sum(brc.norm(x) for x in parent.values())
            total=Fraction()
            for z in all_z:
                x=parent[z]; y=brc.action(parent[inv[i][z]],quarter=i==1 and h[0]==1,negative=False)
                s=brc.plus(brc.norm(x),brc.norm(y))
                p=Fraction(s,2*m)
                for bit in (0,1):
                    mixed=brc.add(x,brc.action(y,quarter=False,negative=bool(bit)))
                    c=brc.norm(mixed)
                    branch=Fraction(c,2*s) if s else None
                    conditional_joint=Fraction(c,4*m)
                    assert (p*branch if branch is not None else 0)==conditional_joint
                    assert brc.norm(direct[h+(bit,)][z])==c
                    proposed_checks+=1
                    total+=conditional_joint
                    if s:
                        joint.append(dict(h=''.join(map(str,h)),z=z,bit=bit,
                            proposal=str(p),read_given_z=str(branch),joint_given_h=str(conditional_joint)))
            assert total==1
    by_h={r['history']:r for r in rows}
    if N==7:
        assert [by_h[h]['norm_numerator'] for h in ('00','01','10','11')]==[6,2,4,4]
        assert by_h['01']['work_rows'][0]==dict(z=1,sign_endpoints=[[0,1,1]],norm_numerator=0)
        assert by_h['10']['work_rows'][0]==dict(z=1,sign_endpoints=[[0,1,0],[1,1,0]],norm_numerator=2)
    else:
        assert all(by_h[h]['norm_numerator']==4 for h in ('00','01','10','11'))
    return dict(N=N,a=2,t=2,full_dimension=D,wire_maps_checked_on_labels=N+1,
         raw_and_all_cut_rows_checked=cut_tests,walker_joint_triplets_checked=proposed_checks,
         dense_signed_coordinate_sha256=digest.hexdigest(),rows=rows,walker_joint=joint)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,default=Path('.'))
    p.add_argument('--output',type=Path)
    a=p.parse_args();b=Positive(a.repo)
    cases=[test(n,b) for n in (7,15)]
    out={'core_sha256':CORE,'frozen_quarter_compiler_sha256':COMPILER,
         'positive_core_calls_by_type':dict(b.calls),'cases':cases,
         'sparse_rows':'61 coordinates, each [coordinate,positive_count,negative_count]; missing entries are zero'}
    txt=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if a.output:a.output.write_text(txt)
    print(txt,end='')


if __name__=='__main__':main()
