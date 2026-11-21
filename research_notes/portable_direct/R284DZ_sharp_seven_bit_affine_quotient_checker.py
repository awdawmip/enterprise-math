#!/usr/bin/env python3
"""R284DZ sharp seven-bit affine quotient for the frozen 65536-state Port model.

Exact 64-cell arithmetic proof, full-universe determinant cross-check, and
2574-triple integer infeasibility certificate for any <=6-bit affine shift.
Requires adjacent published R284DX_six_bit_full_quotient_checker.py.
"""
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path
from R284DX_six_bit_full_quotient_checker import P,FROZEN_SHA,CORE,Q_TABLE,det

COEFFS=(13788,-4799,-4854,14)
SHIFT=7
MINSIX=(3,26,37,43,61,63)
ANCHORS=(3,26,61,63)
INV926=((24,-2,70,-92),(34,-80,22,24),(-132,11,78,43),(-260,2028,-4308,3466))

def core_features(lower):
    u1,a,x,y,u2,w,b,z,u3,g,h,r=lower
    t,s=6-a,13-b
    return (t*s-x*w,s*u1+x*u2,t*u2+w*u1,1)

def key(lower):
    return sum((lower[pos]-1)<<bit for bit,pos in enumerate(CORE))

def cores():
    result=[]
    for k in range(64):
        lower=[1]*12
        for bit,pos in enumerate(CORE):
            lower[pos]=1+((k>>bit)&1)
        result.append(core_features(lower))
    return result

def ceil_div(n,d):return -((-n)//d)

def min_six_bit_certificate(F):
    # The four anchor rows give exact coefficient interval bounds. Verify
    # the integer inverse numerator before any bound is used.
    M=[F[k] for k in ANCHORS]
    assert all(sum(INV926[i][r]*M[r][j] for r in range(4))==926*(i==j)
               for i in range(4) for j in range(4))
    ranges=[]
    for row in INV926:
        base=sum(row[i]*64*Q_TABLE[ANCHORS[i]] for i in range(4))
        nlo=base+sum(63*min(0,v) for v in row)
        nhi=base+sum(63*max(0,v) for v in row)
        ranges.append((ceil_div(nlo,926),nhi//926))
    assert ranges==[(6888,6900),(-2404,-2394),(-2435,-2418),(-292,391)]
    # For each A,B,C in their necessary ranges, intersect all six
    # integer intervals for G. The empty intersection is an exact no-go.
    checked=0; min_gap=None; min_gap_abc=None; survivors=0
    for A in range(ranges[0][0],ranges[0][1]+1):
        for B in range(ranges[1][0],ranges[1][1]+1):
            for C in range(ranges[2][0],ranges[2][1]+1):
                lo=max(64*Q_TABLE[k]-(A*F[k][0]+B*F[k][1]+C*F[k][2]) for k in MINSIX)
                hi=min(64*Q_TABLE[k]+63-(A*F[k][0]+B*F[k][1]+C*F[k][2]) for k in MINSIX)
                gap=lo-hi
                checked+=1
                if gap<=0:survivors+=1
                if min_gap is None or gap<min_gap:
                    min_gap,min_gap_abc=gap,(A,B,C,lo,hi)
    assert checked==13*11*18==2574
    assert survivors==0 and min_gap>0
    return dict(anchor_keys=list(ANCHORS),no_go_keys=list(MINSIX),inverse_numerator_denom=926,
                inverse_numerator_rows=[list(r) for r in INV926],
                necessary_integer_bounds=[list(r) for r in ranges],
                triples_examined=checked,feasible_integer_triples=survivors,
                minimum_interval_disjointness=min_gap,
                closest_triple_with_G_bounds=list(min_gap_abc),
                power_two_denominators_ruled_out=[1,2,4,8,16,32,64],
                argument='A solution with denominator 2^s<=64 scales to a denominator-64 solution; six witness rows exclude denominator 64.')

def main():
    F=cores()
    all_margins=[]
    for k,f in enumerate(F):
        numerator=sum(a*b for a,b in zip(COEFFS,f))
        q=Q_TABLE[k]
        assert q*128<=numerator<q*128+128
        all_margins.append((numerator-q*128,(q+1)*128-numerator))
    nogo=min_six_bit_certificate(F)
    digest=hashlib.sha256(); count=Counter(); n=0
    for upper in itertools.product((1,2),repeat=4):
        top=sum((v-1)<<i for i,v in enumerate(upper))
        for lower in itertools.product((1,2),repeat=12):
            idx=key(lower)
            qcore=sum(a*b for a,b in zip(COEFFS,core_features(lower)))//128
            assert qcore==Q_TABLE[idx]
            T=det(lower,top)
            exception=int(idx==63 and T<2879*P)
            q=qcore-exception
            z=T-q*P
            assert q==T//P and z==T%P and 0<=z<P
            digest.update(z.to_bytes(8,'big'))
            count[(idx,q)]+=1;n+=1
    assert n==65536 and digest.hexdigest()==FROZEN_SHA
    assert all(count[k,Q_TABLE[k]]==1024 for k in range(63))
    assert count[63,2878]==446 and count[63,2879]==578
    return {
      'schema':'R284DZ_SHARP_SEVEN_BIT_AFFINE_QUOTIENT_V1',
      'scope':'Frozen R284CO auxiliary Port; original 65536 source states; no native-X6 transfer',
      'scientific_status':'AUTHOR_PROVED / EXACT_FINITE_CERTIFIED / NOT_REVIEWED',
      'frozen_source':'awdawmip/enterprise-math@acba2d8667903434aaa2a10720f43637fcc2421b:research_notes/portable_direct/R284CO_spectral_witness_checker.py',
      'frozen_git_blob_sha1':'b46e0f682b58e47c27094b4bea6fa4e55119a3ee',
      'frozen_codeword_sha256':FROZEN_SHA,
      'dependency':'R284DX exact 64-core quotient table, already full-population checked',
      'supersedes_in_cost':'R284DY 9-bit affine existence; old artifact preserved',
      'P':P,'states_checked':n,'core_cells':len(F),
      'coefficients':{'u':COEFFS[0],'p1':COEFFS[1],'p2':COEFFS[2],'constant':COEFFS[3]},
      'shift_bits':SHIFT,'divisor':1<<SHIFT,
      'core_quotient_margins_min':[min(v[0] for v in all_margins),min(v[1] for v in all_margins)],
      'exceptional_core_key':63,'exceptional_threshold':2879*P,
      'exceptional_quotient_2878_count':446,'exceptional_quotient_2879_count':578,
      'no_smaller_power_two_shift_certificate':nogo,
      'minimal_shift_claim_scope':'integer affine coefficients in exactly (u,p1,p2,1) with denominator a nonnegative power of two; the 64-core quotient without state-specific correction',
      'all_state_quotient_and_residue_equal_pinned_exact_division':True,
      'ordered_residue_sha256':digest.hexdigest(),
      'all_exact_checks_passed':True,'independent_review':'NOT_REVIEWED'
    }

if __name__=='__main__':
    out=main()
    path=Path(__file__).with_name('R284DZ_sharp_seven_bit_affine_quotient_certificate.json')
    path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('states_checked','coefficients','shift_bits','core_quotient_margins_min','exceptional_quotient_2878_count','no_smaller_power_two_shift_certificate','all_exact_checks_passed')},indent=2,ensure_ascii=False))
