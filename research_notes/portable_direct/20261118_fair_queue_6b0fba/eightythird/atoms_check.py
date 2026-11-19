"""Exact zero-winding partner counts for the primitive Gaussian atom table."""
import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import combinations
import importlib.util
import json
from math import gcd, isqrt
from pathlib import Path


def multiply(z, w):
    x,y = z
    u,v = w
    return x*u-y*v, x*v+y*u


def fold(z):
    a,b = sorted(map(abs,z))
    assert 0<a<b
    return b,a


def octant(z):
    x,y=z
    if x>0 and y>=0:
        d,u,v=0,x,y
    elif x<=0 and y>0:
        d,u,v=2,y,-x
    elif x<0 and y<=0:
        d,u,v=4,-x,-y
    else:
        d,u,v=6,-y,x
    return d+int(v>=u)


def advance(z,w,octants):
    new=multiply(z,w)
    g=gcd(*new)
    new=(new[0]//g,new[1]//g)
    move=(octant(new)-octants)%8
    assert move in (0,1,7)
    return new,octants+(move if move!=7 else -1)


def lifted_pair(a,b,c,d):
    z=(1,0)
    octants=0
    for (x,y),coefficient in ((a,c),(b,d)):
        w=(x,y if coefficient>0 else -y)
        for _ in range(abs(coefficient)):
            z,octants=advance(z,w,octants)
    assert 0 in z or abs(z[0])==abs(z[1])
    return octants


def coordinate_totals(H):
    phi=list(range(H+1))
    for p in range(2,H+1):
        if phi[p]==p:
            for n in range(p,H+1,p):
                phi[n]-=phi[n]//p
    all_atoms=sum(phi[2:])
    complements=sum(phi[3::2])//2
    return all_atoms,complements


def possible_roots(bound):
    for b in range(2,isqrt(bound)+1):
        for a in range(1,min(b-1,isqrt(bound-b*b))+1):
            if (a+b)%2 and gcd(a,b)==1:
                yield b,a


def primitive_roots(bound):
    # Remove every proper Gaussian power modulo units and conjugation, without factoring each root.
    excluded=set()
    for z in possible_roots(isqrt(bound)):
        base=z[0]**2+z[1]**2
        n=base**2
        w=multiply(z,z)
        while n<=bound:
            excluded.add(fold(w))
            n*=base
            w=multiply(w,z)
    for z in possible_roots(bound):
        if z not in excluded:
            yield z


def divisors(n):
    return [d for d in range(2,n+1) if n%d==0]


def add_classified(row,m,j,divs):
    odd=m//(m&-m)
    row['all']+=2*(m-1)
    row['C8']+=odd-1 if j%2==0 else 2*m-odd-1
    row['principal']+=2*sum(gcd(d,j)==1 for d in divs)


def signed_partners(levels,m,j,divs,cert):
    """Emit both signed coefficients of the positive quarter-turn relation."""
    high,high_sign=levels[m][j]
    for A in divs:
        if gcd(A,j)!=1:
            continue
        for det in (-1,1):
            q=(det*pow(j,-1,A))%A
            h=m//A*q
            low_index=(q*j-det)//A
            low,low_sign=levels[h][low_index]
            c,d=det*A*low_sign,-det*q*high_sign
            pair=high+low+(d,c) if high<low else low+high+(c,d)
            assert pair not in cert
            cert.add(pair)


def signed_digest(rows):
    text=''.join(','.join(map(str,r))+'\n' for r in sorted(rows))
    return sha256(text.encode('ascii')).hexdigest()


def fast(H):
    total,complements=coordinate_totals(H)
    top=Counter()
    layers=defaultdict(Counter)
    B=H*H+(H-1)**2
    bound=isqrt(B)
    root_count=0
    cert=set() if H==1000 else None
    for z in primitive_roots(bound):
        root_count+=1
        w=z
        b,a=z
        norm=b*b+a*a
        power_norm=norm
        m=1
        octants=0
        levels={1:{0:(z,1),1:((b+a,b-a),-1)}} if cert is not None else None
        size=2 # both first-level atoms fit whenever a higher atom fits
        while power_norm*norm<=B:
            w,new_octants=advance(w,z,octants)
            assert 0<=new_octants-octants<=1
            octants=new_octants
            m+=1
            power_norm*=norm
            b,a=fold(w)
            if b>H:
                break
            divs=divisors(m)
            row=layers[m]
            j_even=octants+(octants%2)
            j_odd=octants+(1-octants%2)
            if cert is not None:
                levels[m]={j_even:((b,a),1 if j_even==octants else -1),
                           j_odd:((b+a,b-a),1 if j_odd==octants else -1)}
                signed_partners(levels,m,j_even,divs,cert)
            row['P']+=1
            size+=1
            add_classified(row,m,j_even,divs)
            if b+a<=H:
                if cert is not None:
                    signed_partners(levels,m,j_odd,divs,cert)
                size+=1
                row['C']+=1
                add_classified(row,m,j_odd,divs)
        if size>=3:
            top[size]+=1
    upper_odd=sum(r['P'] for r in layers.values())
    upper_even=sum(r['C'] for r in layers.values())
    groups=total-complements-upper_odd
    at_least_two=complements-upper_even
    large=sum(top.values())
    top[1]=groups-at_least_two
    top[2]=at_least_two-large
    assert sum(k*v for k,v in top.items())==total
    pairs={k:sum(r[k] for r in layers.values()) for k in ('all','C8','principal')}
    assert pairs['all']+complements==sum(k*(k-1)//2*v for k,v in top.items())
    if cert is not None:
        assert len(cert)==pairs['principal']
    return dict(H=H,signed_unequal_sha256=signed_digest(cert) if cert is not None else None,
                root_norm_bound=bound,projectively_primitive_roots_examined=root_count,
                atoms=total,groups=groups,same_level_complements=complements,
                group_size={str(i):v for i,v in sorted(top.items()) if v},
                unequal=pairs,all_pairs={k:v+complements for k,v in pairs.items()},
                layers={str(i): dict(layers[i]) for i in sorted(layers)})


def from_frozen_dictionary(H, filename):
    expected_sha='398899655f04b5a50758bbb7eb2207cd19fe900b79d1ec7f84afecad8f6b54e1'
    if sha256(filename.read_bytes()).hexdigest()!=expected_sha:
        raise ValueError('unexpected wave-8 Gaussian-generator bytes')
    spec=importlib.util.spec_from_file_location('wave8_atoms',filename)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    groups=defaultdict(list)
    def emit(b,a,eps,pos,path,sign):
        del pos
        m=0
        for p,e in path:
            m=gcd(m,e)
        direction=tuple((p,e//m) for p,e in path)
        groups[direction].append((b,a,eps,sign*m))
    module.generate(H,emit)
    counts=Counter()
    signed=Counter()
    sheets=Counter()
    witness={}
    records=set()
    for atoms in groups.values():
        for left,right in combinations(sorted(atoms),2):
            b,a,eps,m=left
            y,x,eta,n=right
            g=gcd(m,n)
            c,d=n//g,-m//g
            t=(c*eps+d*eta)%8
            counts['all']+=1
            if t%2==0:
                continue
            counts['C8']+=1
            if abs(m)==abs(n):
                assert b*y-a*x==b*x+a*y and gcd(a,b)==gcd(x,y)==1
                signed['++']+=1
                counts['principal']+=1
                sheets['1']+=1
                continue
            w=lifted_pair((b,a),(y,x),c,d)
            assert w%8==t
            sheets[str(abs(w))]+=1
            if abs(w)==1:
                counts['principal']+=1
                c*=w
                d*=w
                records.add((b,a,y,x,c,d))
                signword=('+' if c>0 else '-')+('+' if d>0 else '-')
                signed[signword]+=1
            else:
                key=str(abs(w))
                candidate=[b,a,y,x,c,d,w]
                if key not in witness or candidate<witness[key]:
                    witness[key]=candidate
    return dict(atoms=sum(map(len,groups.values())),groups=len(groups),pairs=dict(counts),
                signs_in_increasing_b_then_a_order=dict(sorted(signed.items())),
                primitive_absolute_quarterturns=dict(sorted(sheets.items())),
                nonprincipal_examples=witness,signed_unequal_sha256=signed_digest(records))


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--heights',type=int,nargs='+',default=[100,1000,10000,100000])
    parser.add_argument('--source',type=Path,default=Path(__file__).resolve().parent.parent/'eighth/atoms_check.py')
    parser.add_argument('--without-dictionary',action='store_true')
    parser.add_argument('--out',type=Path)
    args=parser.parse_args()
    if min(args.heights)<2:
        parser.error('heights must be at least two')
    rows=[fast(H) for H in args.heights]
    data={'quadratic_height_samples':rows}
    if not args.without_dictionary:
        direct=from_frozen_dictionary(1000,args.source)
        compare=next((r for r in rows if r['H']==1000),None) or fast(1000)
        assert (direct['atoms'],direct['groups'])==(304191,202662)
        assert direct['pairs']['all']==102186 and direct['pairs']['C8']==101706
        assert direct['pairs']==compare['all_pairs']
        assert direct['signed_unequal_sha256']==compare['signed_unequal_sha256']
        data['wave8_dictionary_H1000']=direct
    text=json.dumps(data,indent=2,sort_keys=True)+'\n'
    if args.out:
        args.out.write_text(text)
    else:
        print(text,end='')


if __name__=='__main__':
    main()
