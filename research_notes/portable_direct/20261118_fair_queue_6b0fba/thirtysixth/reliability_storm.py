"""Storm 2.0.0 exact sparse-DTMC baseline. See --help for the optional cost log.

Python 3.12 was used. Install with python -m pip install --only-binary=:all: stormpy==2.0.0
No repository checkout or source archives are required.
"""
import argparse
from collections import defaultdict
from contextlib import contextmanager
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from math import comb
from pathlib import Path
import os
import platform
import resource
import sys
import tempfile
from time import perf_counter

t_start = perf_counter()
import stormpy as storm
import stormpy.info as storm_info

TIMING = defaultdict(float)
TIMING["import_storm"] = perf_counter() - t_start


def ratio(x):
    return str(x)


def formula(probability, update):
    return f"{ratio(probability)} : {update}"


def next_environments(current, latent):
    if not latent:
        return ((0,F(1)),)
    if current==2:
        return ((0,F(1,2)),(1,F(1,2)))
    return ((current,F(3,4)),(1-current,F(1,4)))


def write_mask_model(n, shock, latent, iid_failure=F(1,10)):
    """Each transition is one actual tick, including the first. Nodes are labeled subsets."""
    full=(1<<n)-1
    commands=["dtmc","module mission",f" m:[0..{full}] init {full};",
              (" e:[0..2] init 2;" if latent else " e:[0..1] init 0;")," seen:bool init false;"]
    for e in ((0,1,2) if latent else (0,)):
        masks=[full] if e==2 else range(full+1)
        for m in masks:
            branches=[]
            for after,w in next_environments(e,latent):
                p=((F(1,4),F(3,4))[after] if latent else iid_failure)
                if shock:
                    branches.append(formula(w*shock,f"(m'=0)&(e'={after})&(seen'=true)"))
                sub=m
                while True:
                    stay=sub.bit_count()
                    loss=m.bit_count()-stay
                    mass=w*(1-shock)*(1-p)**stay*p**loss
                    branches.append(formula(mass,f"(m'={sub})&(e'={after})"))
                    if sub==0:break
                    sub=(sub-1)&m
            commands.append(f" [] e={e} & m={m} -> " + " + ".join(branches)+";")
    commands+=["endmodule",'label "shock" = seen;']
    commands.append('label "component0_bad" = '+ " | ".join(f"(m={m})" for m in range(0,full+1,2)) + ";")
    for k in range(1,n+1):
        # No k-out-of-n binomial collapse in Storm's state graph.
        safe=" | ".join(f"(m={m})" for m in range(full+1) if m.bit_count()>=k)
        commands.append(f'label "ok{k}" = {safe};')
    return "\n".join(commands)+"\n"


def write_hmm(independent=False):
    out=["dtmc","module observation"," e:[0..2] init 2;"," n:[0..2] init 0;",
         " a:[0..1] init 0;"," b:[0..1] init 0;"," firstenv:[0..1] init 0;"]
    for tick in (0,1):
        for e in ((2,) if tick==0 else (0,1)):
            branches=[]
            for after,w in next_environments(e,True):
                p=F(1,2) if independent else (F(1,4),F(3,4))[after]
                for f in (0,1):
                    memory=f"(a'={f})&(firstenv'={after})" if tick==0 else f"(b'={f})"
                    branches.append(formula(w*(p if f else 1-p),f"(n'={tick+1})&(e'={after})&{memory}"))
            out.append(f" [] n={tick} & e={e} -> "+" + ".join(branches)+";")
    out+=[" [] n=2 -> true;","endmodule"]
    for name,expr in [("F1","a=1"),("F2","b=1"),("both","(a=1)&(b=1)")]:
        out.append(f'label "{name}" = (n=2)&({expr});')
    for i,j in product(range(2),repeat=2):
        out.append(f'label "E{i}{j}" = (n=2)&(a=1)&(b=1)&(firstenv={i})&(e={j});')
    return "\n".join(out)+"\n"


def tail(n,k,survival):
    return sum(comb(n,r)*survival**r*(1-survival)**(n-r) for r in range(k,n+1))


def reference_grid(n,s,latent):
    """Distinct derivation by hidden words. Given a word and no shock the lives are iid."""
    ref={k:[F(1)] for k in range(2,n+1)}
    for t in range(1,9):
        weights=defaultdict(F)
        if latent:
            for word in product((0,1),repeat=t):
                changes=sum(a!=b for a,b in zip(word,word[1:]))
                weight=F(1,2)*F(1,4)**changes*F(3,4)**(t-1-changes)
                survival=F(3,4)**word.count(0)*F(1,4)**word.count(1)
                weights[survival]+=weight
        else:
            weights[F(9,10)**t]=F(1)
        assert sum(weights.values())==1
        for k in ref:
            ref[k].append((1-s)**t*sum(p*tail(n,k,h) for h,p in weights.items()))
    return ref


def build(text,model_file):
    t=perf_counter()
    model_file.write_text(text)
    TIMING["write_model"]+=perf_counter()-t
    t=perf_counter()
    parsed=storm.parse_prism_program(str(model_file))
    TIMING["parse_model"]+=perf_counter()-t
    t=perf_counter()
    model=storm.build_model[storm.Rational](parsed)
    TIMING["build_exact_sparse_graph"]+=perf_counter()-t
    return parsed,model


def query(parsed,model,formula_text):
    t=perf_counter()
    prop=storm.parse_property(formula_text,parsed)
    TIMING["parse_properties"]+=perf_counter()-t
    t=perf_counter()
    res=storm.model_checking(model,prop,only_initial_states=True)
    TIMING["storm_exact_check"]+=perf_counter()-t
    t=perf_counter()
    x=F(str(res.get_value(model.initial_states[0])))
    TIMING["recover_exact_values"]+=perf_counter()-t
    return x


def info(text,model):
    return {"prism_utf8_bytes":len(text.encode()),"prism_sha256":hashlib.sha256(text.encode()).hexdigest(),
            "reachable_states":model.nr_states,"transition_entries":model.nr_transitions}


def factorized_hmm_mask(n):
    """A synchronous component model. One choose and one commit equal one physical tick."""
    lines=["dtmc","module sources"," phase:[0..1] init 0;"," e:[0..2] init 2;",
           " hit:bool init false;"," seen:bool init false;"]
    for e in (0,1,2):
        branches=[]
        for after,weight in next_environments(e,True):
            for hit,p in ((False,F(4,5)),(True,F(1,5))):
                update=f"(phase'=1)&(e'={after})&(hit'={str(hit).lower()})"
                branches.append(formula(weight*p,update))
        lines.append(f" [choose] phase=0 & e={e} -> "+" + ".join(branches)+";")
    lines+=[" [commit] phase=1 -> (phase'=0)&(seen'=(seen|hit));","endmodule"]
    for j in range(n):
        lines += [f"module life{j}",f" a{j}:[0..1] init 1;",
                  f" [commit] hit | a{j}=0 -> (a{j}'=0);"]
        for e,p in ((0,F(1,4)),(1,F(3,4))):
            lines += [f" [commit] !hit & a{j}=1 & e={e} -> {p}:(a{j}'=0) + {1-p}:(a{j}'=1);"]
        lines+=["endmodule"]
    lines+=['label "failed" = '+'+'.join(f'a{j}' for j in range(n))+'<4;']
    return "\n".join(lines)+"\n"


@contextmanager
def native_logs_to_stderr():
    # Sylvan may emit host thread-count messages from native C++ code on stdout.
    sys.stdout.flush()
    saved=os.dup(1)
    try:
        os.dup2(2,1)
        yield
    finally:
        os.dup2(saved,1)
        os.close(saved)


def dd_example(path,properties,expected):
    with native_logs_to_stderr():
        start=perf_counter()
        prism=storm.parse_prism_program(str(path))
        props=[storm.parse_property(s,prism) for s in properties]
        TIMING["dd_parse_model_and_properties"]+=perf_counter()-start
        start=perf_counter()
        model=storm.build_model[storm.Rational](prism,props,engine=storm.Engine.DD)
        TIMING["dd_build_symbolic_graph"]+=perf_counter()-start
        start=perf_counter()
        results=[]
        for prop in props:
            vals=storm.model_checking(model,prop,engine=storm.Engine.DD)
            vals.filter(storm.create_filter_initial_states(model))
            results.append(F(str(vals.get_min())))
        assert results==expected
        TIMING["dd_exact_check_and_validate"]+=perf_counter()-start
        return {**info(path.read_text(),model),"queries":properties,"exact_values":list(map(str,results))}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cost",type=Path,help="optional machine-dependent timing and process RSS log")
    ap.add_argument("--models",type=Path,help="optional directory for all generated PRISM source models")
    args=ap.parse_args()
    if storm.__version__!="2.0.0":
        raise SystemExit("This run targets the exact APIs in stormpy==2.0.0")
    scenario={}
    numerator_bits=denominator_bits=0
    with tempfile.TemporaryDirectory() as tempdir:
        destination=args.models or Path(tempdir)
        destination.mkdir(parents=True,exist_ok=True)
        for n,s,latent in product((3,5,7),(F(0),F(1,5)),(False,True)):
            tag=f'n{n}_shock{int(bool(s))}_latent{int(latent)}'
            t=perf_counter()
            text=write_mask_model(n,s,latent)
            TIMING["generate_prism"]+=perf_counter()-t
            program,model=build(text,destination/(tag+".pm"))
            t=perf_counter()
            reference=reference_grid(n,s,latent)
            TIMING["reference_hidden_word_check_generation"]+=perf_counter()-t
            shocks=[query(program,model,f'P=? [ F<={t} "shock" ]') for t in range(1,9)]
            assert shocks==[1-(1-s)**t for t in range(1,9)]
            if n==3 and s==F(1,5) and not latent:
                member_failure=query(program,model,'P=? [ F<=1 "component0_bad" ]')
                assert member_failure==F(7,25)
            by_k={}
            for k in range(2,n+1):
                triples=[]
                for t in range(1,9):
                    failed=query(program,model,f'P=? [ F<={t} !"ok{k}" ]')
                    source=query(program,model,f'P=? [ "ok{k}" U<={t} "shock" ]')
                    start=perf_counter()
                    safe=1-failed
                    independent=failed-source
                    assert safe==reference[k][t]
                    assert source==s*sum(reference[k][:t])
                    assert independent>=0 and safe+source+independent==1
                    for v in (safe,source,independent):
                        numerator_bits=max(numerator_bits,v.numerator.bit_length())
                        denominator_bits=max(denominator_bits,v.denominator.bit_length())
                    triples.append([ratio(safe),ratio(source),ratio(independent)])
                    TIMING["validate_and_assemble_rows"]+=perf_counter()-start
                by_k[k]=triples
            scenario[tag]={**info(text,model),"ever_shock_t1_to_8":list(map(ratio,shocks)),
                           "by_threshold":by_k}
        t=perf_counter()
        text=write_hmm()
        TIMING["generate_prism"]+=perf_counter()-t
        program,model=build(text,destination/"source_b_hmm.pm")
        hmm={label:query(program,model,f'P=? [ F<=2 "{label}" ]')
             for label in ("F1","F2","both","E00","E01","E10","E11")}
        assert [hmm[k] for k in ("F1","F2","both")]==[F(1,2),F(1,2),F(9,32)]
        assert [hmm[k] for k in ("E00","E01","E10","E11")]==[F(3,128)]*3+[F(27,128)]
        hmm["F2_given_F1"]=hmm["both"]/hmm["F1"]
        assert hmm["F2_given_F1"]==F(9,16)
        hmm_meta=info(text,model)
        text_wrong_a=write_mask_model(3,F(0),False,iid_failure=F(7,25))
        wrong_a_prog,wrong_a_model=build(text_wrong_a,destination/"incorrect_iid_A.pm")
        wrong_a=1-query(wrong_a_prog,wrong_a_model,'P=? [ F<=1 !"ok2" ]')
        text_wrong_b=write_hmm(independent=True)
        wrong_b_prog,wrong_b_model=build(text_wrong_b,destination/"incorrect_iid_B.pm")
        wrong_b=query(wrong_b_prog,wrong_b_model,'P=? [ F<=2 "both" ]')
        assert wrong_a==F(12636,15625) and wrong_b==F(1,4)
        assert wrong_a-F(486,625)==F(486,15625)
        t=perf_counter()
        compact=factorized_hmm_mask(7)
        compact_file=destination/"factorized_n7_hmm_shock.pm"
        compact_file.write_text(compact)
        TIMING["write_factorized_model"]+=perf_counter()-t
        q_bad=F(scenario["n7_shock1_latent1"]["by_threshold"][4][-1][0])
        symbolic={
            "frozen_A":dd_example(destination/"n3_shock1_latent0.pm",
                ['P=? [ F<=1 !"ok2" ]'],[F(139,625)]),
            "frozen_B":dd_example(destination/"source_b_hmm.pm",
                ['P=? [ F<=2 "both" ]'],[F(9,32)]),
            "n7_shock_and_HMM_T8_k4_two_microsteps_per_tick":dd_example(compact_file,
                ['P=? [ F<=16 "failed" ]'],[1-q_bad])}
    table=scenario["n3_shock1_latent0"]["by_threshold"][2]
    assert table[0]==["486/625","1/5","14/625"]
    output={"stormpy":storm.__version__,"storm":storm_info.storm_long_version(),
            "model_A_reliability_T1":table[0][0],"model_B_two_observations":{k:str(v) for k,v in hmm.items()},
            "hmm_graph":hmm_meta,"grid_rows":384,"sparse_properties_checked":12*8+2*384+7+3,
            "symbolic_properties_checked":3,"symbolic_exact_sylvan_checks":symbolic,
            "actual_model_A_single_component_failure":str(member_failure),
            "incorrect_independence_controls":{"A_reliability":str(wrong_a),"B_joint":str(wrong_b),
                "A_graph":info(text_wrong_a,wrong_a_model),"B_graph":info(text_wrong_b,wrong_b_model)},
            "field_order":["alive_count_at_least_k","first_threshold_crossing_caused_by_shock",
                           "first_threshold_crossing_without_shock"],
            "environment_labels":{"0":"H","1":"L","2":"initial_mix"},
            "max_numerator_bits":numerator_bits,"max_denominator_bits":denominator_bits,
            "scenarios":scenario}
    t=perf_counter()
    print(json.dumps(output,sort_keys=True,indent=2))
    TIMING["serialize_results_to_stdout"]+=perf_counter()-t
    if args.cost:
        cost={"python":platform.python_version(),"os":platform.platform(),"machine":platform.machine(),
              "stormpy":storm.__version__,"storm":storm_info.storm_long_version(),"seconds":dict(TIMING),
              "sum_seconds_since_import_start":perf_counter()-t_start,"process_RSS_high_water_KiB_Linux":
                  resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              "scope":"one serial run; Python process includes native Storm, exact cross-check and writing JSON; no installer time or wheel-storage charge"}
        args.cost.write_text(json.dumps(cost,indent=2,sort_keys=True)+"\n")


if __name__=="__main__":
    main()
