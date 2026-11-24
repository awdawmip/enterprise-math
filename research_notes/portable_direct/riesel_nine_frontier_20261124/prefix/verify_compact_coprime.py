#!/usr/bin/env python3
"""Direct total-cover lower bound for the existing 160-digit one-W root.

Uses the already verified 20160-period zero phases. It enumerates only private
indices in that same period, then computes full integer terms and all 406 gcds.
It does not rerun the 4800 phase classification or any native BRC harness.
"""

from itertools import combinations
from math import gcd, lcm
from pathlib import Path
import hashlib
import json

ROOT = 2770714492093438838433084226801660296418766175867271008480060095168867099351242904608463381362983433276866993594996807812925055515290327478920627884582606119453


def main():
    here=Path(__file__).resolve().parent
    source=here/"nine_prefix_certificate.json"
    source_bytes=source.read_bytes()
    old=json.loads(source_bytes)["compact_exact_cost9_root"]
    assert int(old["root"])==ROOT
    a=ROOT
    a2=a*a
    coverage=old["coverage"]
    L=coverage["scalar_executed_full_residue_period"]
    orders={int(q):d for q,d in coverage["base2_orders"].items()}
    phases={int(q):b for q,b in coverage["zero_phases"].items()}
    qs=sorted(orders)
    assert len(qs)==29 and L==20160==lcm(*orders.values())
    for q in qs:
        d=orders[q]
        assert pow(2,d,q)==1
        assert all(pow(2,e,q)!=1 for e in range(1,d))
        assert (a2*pow(2,phases[q],q)-1)%q==0
    private={q:[] for q in qs}
    for n in range(1,L+1):
        hits=[q for q in qs if n%orders[q]==phases[q]]
        if len(hits)==1:
            private[hits[0]].append(n)
    assert all(private[q] for q in qs)

    def greedy(reserve73):
        chosen=[]
        rejections=[]
        for q in qs:
            for n in private[q]:
                value=(a2<<n)-1
                if reserve73 and q!=92737 and value%73==0:
                    rejections.append({"q":q,"n":n,"reason":"73 reserved for a forced future private term"})
                    continue
                conflicts=[(p,m,gcd(value,w)) for p,m,w in chosen if gcd(value,w)!=1]
                if conflicts:
                    rejections.append({"q":q,"n":n,"reason":"nontrivial gcd with an already selected term",
                                       "conflicts":[[p,m,str(g)] for p,m,g in conflicts]})
                    continue
                chosen.append((q,n,value))
                break
            else:
                return chosen,rejections,q
        return chosen,rejections,None

    naive,naive_rejections,failed=greedy(False)
    assert failed==92737 and len(naive)==26
    # All q=92737 private terms necessarily carry the unselected fixed prime 73.
    # This proves that reserving 73 is a necessary compatibility condition,
    # rather than an enlarged search through later periods.
    assert len(private[92737])==32
    assert all((a2*pow(2,n,73)-1)%73==0 for n in private[92737])
    chosen,rejections,failed=greedy(True)
    assert failed is None and len(chosen)==29
    assert [q for q,_,_ in chosen]==qs
    gcd_records=[]
    for (q,n,value),(p,m,other) in combinations(chosen,2):
        g=gcd(value,other)
        assert g==1,(q,p,n,m,g)
        gcd_records.append([q,p,g])
    assert len(gcd_records)==406
    terms=[]
    for q,n,value in chosen:
        assert 1<=n<=L
        assert value==(a*a<<n)-1
        assert value>q and value%q==0
        assert [p for p in qs if value%p==0]==[q]
        terms.append({"assigned_prime":q,"exponent":n,
                      "full_integer_hex":hex(value),"bit_length":value.bit_length(),
                      "assigned_prime_quotient_hex":hex(value//q),"remainder":0})
    result={"schema":"riesel-160-digit-one-W-root-direct-29-coprime-witnesses-v1",
            "status":"PASS_DIRECT_EXACT_INTEGER_GCD_CERTIFICATE",
            "root":str(a),"source_certificate":"nine_prefix_certificate.json",
            "source_sha256":hashlib.sha256(source_bytes).hexdigest(),
            "private_index_enumeration_period":L,
            "private_indices_by_selected_prime":private,
            "total_private_indices":sum(map(len,private.values())),
            "naive_greedy_result":{"selected_count":len(naive),"failed_prime":92737,
                                   "chosen_exponents":[[q,n] for q,n,_ in naive],
                                   "reason":"The earlier q43 witness n128 shares forced prime73 with every q92737 private term"},
            "necessary_reserved_prime":{"prime":73,"assigned_to":92737,
                                        "forced_private_index_count":32,
                                        "all_forced_private_indices_verified":True},
            "successful_method":"Increasing assigned prime; first private index in the same period avoiding reserved73 and every previous full-integer gcd",
            "greedy_rejections":rejections,"selected_terms":terms,
            "pairwise_gcds":gcd_records,"pairwise_gcd_count":len(gcd_records),
            "all_pairwise_gcds_equal_one":True,
            "supplementary_minimum":9,"unrestricted_total_minimum":29,
            "upper_bound_basis":"The original proper 29-prime full-sequence cover",
            "lower_bound_basis":"A prime cannot divide two of the 29 pairwise-coprime positive terms, so every full covering dictionary needs at least29 distinct primes",
            "selected_dictionary_irredundancy_alone_used_for_total_minimum":False,
            "native_BRC_execution_claimed":False,
            "independent_project_review_claimed":False}
    target=here/"compact_coprime_certificate.json"
    target.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({"status":"PASS","certificate":str(target),
                      "private_indices":result["total_private_indices"],
                      "selected_terms":len(chosen),"gcd_pairs":len(gcd_records),
                      "maximum_selected_exponent":max(n for _,n,_ in chosen),
                      "delta":9,"tau":29}))


if __name__=="__main__":
    main()
