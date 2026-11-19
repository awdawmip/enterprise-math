"""Exact commutator ranks, native six-axis probes, and a complete GL3(F2) control."""
import argparse
import importlib.util
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path


def unit(n,i,j):
    return tuple(int(k==i and l==j) for k in range(n) for l in range(n))


def identity(n):
    return tuple(int(i==j) for i in range(n) for j in range(n))


def add(x,y,k=1,q=None):
    result=[a+k*b for a,b in zip(x,y)]
    return tuple(result if q is None else [v%q for v in result])


def mul(a,b,n,p):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%p
                 for i in range(n) for j in range(n))


def comm(x,a,n,p):
    return add(mul(x,a,n,p),mul(a,x,n,p),-1,p)


def rank(rows,p):
    pivots={}
    for vec in rows:
        v=list(vec)
        for i in range(len(v)):
            k=v[i]%p
            if not k:
                continue
            if i not in pivots:
                inv=pow(k,-1,p)
                pivots[i]=[a*inv%p for a in v]
                break
            v=[(a-k*b)%p for a,b in zip(v,pivots[i])]
    return len(pivots)


def kernel_dimension(actions,n,p):
    units=[unit(n,i,j) for i in range(n) for j in range(n)]
    directions=[tuple(y for a in actions for y in comm(x,a,n,p)) for x in units]
    return n*n-rank(directions,p)


def rows(flat,n):
    return tuple(tuple(flat[i*n:(i+1)*n]) for i in range(n))


def cycle_generators(n):
    return [add(identity(n),unit(n,i,(i+1)%n)) for i in range(n)]


def all_gl3():
    n=3
    ident=identity(n)
    reps=[(0,)+r for r in itertools.product(range(2),repeat=8)]
    kernels={}
    orbit_ranks=Counter()
    for A in itertools.product(range(2),repeat=9):
        if rank(rows(A,n),2)<n:
            continue
        shifts={comm(x,A,n,2) for x in reps}
        ker=frozenset(i for i,x in enumerate(reps) if not any(comm(x,A,n,2)))
        assert len(shifts)*len(ker)==len(reps)
        orbit_ranks[len(shifts)]+=1
        kernels[A]=ker
    assert len(kernels)==168
    small=[k for A,k in kernels.items() if len(k)==16]
    assert small and all(len(a&b)>=2 for a,b in itertools.combinations(small,2))
    cycle=cycle_generators(n)
    assert set.intersection(*(set(kernels[a]) for a in cycle))=={0}
    # Enumerate actual mod-4 normalized projective representatives and the
    # actual conjugations (I+2X)A(I-2X), rather than only commutator coordinates.
    def normalized(a):
        pivot=next(value for value in a if value%2)
        return tuple(v*pow(pivot,-1,4)%4 for v in a)
    def move(x,a):
        return normalized(mul(mul(add(ident,x,2),a,n,4),add(ident,x,-2),n,4))
    support=set()
    for a in cycle:
        orbit={move(x,a) for x in reps}
        assert len(orbit)==16 and not orbit&support
        support.update(orbit)
    ordered=sorted(support)
    induced={tuple(move(x,a) for a in ordered) for x in reps}
    assert len(induced)==256 and all(set(permutation)==support for permutation in induced)
    return {"group":"PGL congruence kernel at modulus 4, three axes, p=2",
            "reduced_invertible_actions":len(kernels),
            "orbit_sizes_by_number_of_actions":dict(sorted(orbit_ranks.items())),
            "all_pairs_of_minimal_actions":len(small)*(len(small)-1)//2,
            "smallest_common_kernel_order_of_a_pair":min(len(a&b) for a,b in itertools.combinations(small,2)),
            "constructed_distinct_fine_classes":len(support),"different_induced_permutations":len(induced)}


def two_digit_control():
    # Genuine normalized matrices in GL3(Z/8) equal to I mod 2. The kth
    # diagonal (outside i,j) of both products fixes any projective multiplier.
    n=3
    q=8
    ident=identity(n)
    counts=[0]*n
    joint=0
    tested=0
    for tail in itertools.product(range(4),repeat=8):
        x=(0,)+tail
        f=add(ident,x,2,q)
        fixed=[]
        for i in range(n):
            j=(i+1)%n
            k=(i+2)%n
            assert f[n*k+k]%2
            good=all(((f[n*r+i] if c==j else 0)-
                      (f[n*j+c] if r==i else 0))%q==0 for r in range(n) for c in range(n))
            counts[i]+=good
            fixed.append(good)
        joint+=all(fixed)
        tested+=1
    g=add(ident,unit(n,0,1),2,q)
    h=add(ident,unit(n,1,2),2,q)
    assert mul(g,h,n,q)!=mul(h,g,n,q)
    assert tested==65536 and counts==[256]*3 and joint==1
    return {"p":2,"axes":3,"m":1,"digits":2,"normalized_high_frames_enumerated":tested,
            "three_single_anchor_stabilizers":counts,"joint_stabilizer":joint,
            "union_of_three_orbit_sizes":sum(tested//z for z in counts),
            "noncommuting_frames":True}


def field_cases():
    ans=[]
    for p in (2,3,5,7,11):
        n=6
        a=cycle_generators(n)
        cases={"scalar":[identity(n)],"nilpotent_rank_one":[a[0]],
               "split_rank_one":[add(identity(n),unit(n,0,0))],
               "split_four_plus_two":[tuple((int(i==j)*(1+int(i in (4,5)))) for i in range(n) for j in range(n))],
               "two_nilpotent_blocks":[add(a[0],unit(n,2,3))],
               "cycle":a,"first_five":a[:5]}
        dims={name:kernel_dimension(actions,n,p) for name,actions in cases.items()}
        assert [dims[key] for key in ("scalar","nilpotent_rank_one","split_rank_one",
                                      "split_four_plus_two","two_nilpotent_blocks","cycle")]==[36,26,26,20,20,1]
        assert dims["first_five"]>1
        projective_examples={}
        for name in ("nilpotent_rank_one", "two_nilpotent_blocks"):
            mat=cases[name][0]
            vectors=[comm(unit(n,i,j),mat,n,p) for i in range(n) for j in range(n)]
            projective_examples[name]=rank(vectors+[mat],p)-1
        assert projective_examples["nilpotent_rank_one"]==10
        if p in (2,3):
            mat=tuple((int(i==j)+int(i//p==j//p and j==i+1))%p
                      for i in range(n) for j in range(n))
            witness=tuple((-i%p if i//p==j//p and i in (j,j+1) else 0)
                          for i in range(n) for j in range(n))
            assert comm(witness,mat,n,p)==mat
            vecs=[comm(unit(n,i,j),mat,n,p) for i in range(n) for j in range(n)]
            ordinary=rank(vecs,p)
            projective_examples["wild_Jordan"]={"ordinary":ordinary,
                "projective":rank(vecs+[mat],p)-1,"commutator_equals_A":True}
            assert projective_examples["wild_Jordan"]["projective"]==ordinary-1
        if p==2:
            # The two split test matrices above are singular in F2, so do not
            # report them as examples of admissible unit actions.
            del dims["split_rank_one"],dims["split_four_plus_two"]
        # On the full list of six rank-one row/combinations with v_i=e_i,
        # compare matrix calculations to the connected-components test.
        tests=0
        for mask in range(64):
            actions=[]
            parent=list(range(n))
            def find(x):
                while parent[x]!=x:
                    x=parent[x]
                return x
            for i in range(n):
                if mask>>i & 1:
                    a_i=add(identity(n),unit(n,i,(i+1)%n))
                    parent[find(i)]=find((i+1)%n)
                else:
                    if p==2:
                        j=(i+2)%n
                        a_i=add(identity(n),unit(n,i,j))
                        parent[find(i)]=find(j)
                    else:
                        a_i=add(identity(n),unit(n,i,i))
                actions.append(a_i)
            assert kernel_dimension(actions,n,p)==len({find(i) for i in range(n)})
            tests+=1
        ans.append({"p":p,"common_centralizer_dimensions":dims,
                    "projective_orbits":projective_examples,"six_orbit_graph_cases":tests,"minimum_fine_classes":6*p**10,
                    "distinct_one_digit_frames":p**35})
    return ans


def native(repo, earlier):
    spec=importlib.util.spec_from_file_location("hbw_sixteenth_stabilizer",earlier)
    old=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(old)
    old.setup(repo.resolve())
    n=6
    identity6=old.eye(n)
    zero=(0,)*n
    matrices=cycle_generators(n)
    def packet(d):
        return old.ControlPacket.from_edges(1,0,1,[(0,0,Fraction(1),old.Affine(old.matrix(rows(d,n)),zero),1)])
    # Test one native-packet singleton per orbit at two protected depths,
    # together with a good translated singleton and a wrong fine-class digit.
    reports=[]
    for p in (2,3,5):
        for m in (1,2):
            a_reports=[]
            for i,a in enumerate(matrices):
                x=unit(n,(i+1)%n,(i+2)%n)
                delta=comm(x,a,n,p)
                assert any(delta)
                b=add(a,delta,p**m)
                c=add(a,unit(n,(i+3)%n,(i+4)%n),p**m)
                left=packet(a)
                right=packet(b)
                frame=old.matrix(rows(add(identity(n),x,p**m),n))
                prob=old.wl.WeightedLiftProblem.from_control_packets(left,right,p)
                assert prob.guard==0 and prob.row_certificate(identity6,m)
                assert prob.row_certificate(frame,m+1)
                native_germs=old.wm.packet_germ_classes(left,p,m+1)
                assert len(native_germs)==1
                pair=old.direct(left,right,identity6,p,m=m,witness=frame)
                assert pair["status"]=="COMPLETE" and pair["kernel_dim"]==25
                assert pair["count"]==p**25 and pair["image_order"]==1
                miss=old.direct(left,packet(c),identity6,p,m=m)
                assert miss["status"]=="NO_LIFTS"
                a_reports.append({"i":i,"fine_germs":1,"guard":prob.guard,"one_edge_lifts":pair["count"],
                                  "single_point_permutation_order":pair["image_order"],
                                  "off_orbit_packet_result":miss["status"]})
            def six_packet(actions):
                return old.ControlPacket.from_edges(1,0,1,[(0,0,Fraction(1,6),
                    old.Affine(old.matrix(rows(a,n)),zero),1) for a in actions])
            common_x=add(unit(n,0,2),unit(n,3,5))
            frame=old.matrix(rows(add(identity(n),common_x,p**m),n))
            target=[add(a,comm(common_x,a,n,p),p**m) for a in matrices]
            left=six_packet(matrices)
            right=six_packet(target)
            out=old.direct(left,right,identity6,p,m=m,witness=frame)
            assert out["status"]=="COMPLETE" and out["count"]==1 and out["kernel_dim"]==0
            reports.append({"p":p,"m":m,"native_singleton_transports":a_reports,
                            "six_sparse_anchors_shared_transporter_count":out["count"]})
    return {"frozen_bridge":"sixteenth/stabilizer_check.py setup and direct, WM packet_germ_classes, WL row_certificate",
            "original_WL_sha256":"9cb757ea3df90ff11b5f943410b1f1e90181d53bb5a95e995b76dd8068cbbcf1",
            "original_WM_sha256":"5077223829003df6e4ea890e3190a15d7583c115463a4046e0a2b74e30f78ef3",
            "primes":[2,3,5],"representatives":"I+E_{i,i+1 mod 6}","cases":reports,
            "full_six_axis_support_expanded":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--earlier",type=Path,default=Path(__file__).resolve().parents[1]/"sixteenth"/"stabilizer_check.py")
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result={"dimension_six":field_cases(),"complete_small_model":all_gl3(),
            "native_six_axis":native(args.repo,args.earlier),"two_digit_control":two_digit_control()}
    output=json.dumps(result,indent=2)+"\n"
    if args.output:
        args.output.write_text(output)
    else:
        print(output,end="")


if __name__=="__main__":
    main()
