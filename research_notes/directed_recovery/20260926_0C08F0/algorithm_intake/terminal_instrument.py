"""Exact terminal-instrument compilation of frozen Stage80 BRC Shor.
No trigonometric/QFT replacement, hidden order, new precision, or mode reset.
Input/output semantics use the parent's declared quadratic probability readout.
"""
from __future__ import annotations
import argparse, gzip, hashlib, json, random, sys
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path
from time import perf_counter_ns

ROOT=Path(__file__).resolve().parent
DEFAULT_SOURCE=ROOT.parents[1]/"sep26-local-takeover"/"intake_brc"/"stage87-source"
SOURCE=Path(__import__("os").environ.get("BRC_STAGE87_SOURCE",str(DEFAULT_SOURCE))).resolve()
sys.path.insert(0,str(SOURCE))
sys.set_int_max_str_digits(0)
from stage80.fixed_phase import FixedRotor, QuarterTurn, prepare_fixed, cp_step, h4_step, run_qft, law, reduce_state, fixed_error
from stage78.shor_benchmark import reverse_bits, classical_postprocess, modular_columns
from stage45.brc_loop_recheck import verify_vendor, CALLS

def load_frozen_bank(max_m=10):
    saved=json.loads((SOURCE/"stage80"/"RESULTS.json").read_text(encoding="utf-8"))
    dim=saved["internal_real_mode_count"]
    if saved["target_parameter_bits"]!=32 or saved["unit_vector_bits"]!=64 or dim!=61:
        raise AssertionError("unexpected frozen bank precision/dimension")
    bank={2:QuarterTurn(dim)}
    for name,record in saved["phase_gates"].items():
        if int(name)>max_m:continue
        rotor=FixedRotor(record["integer_unit_vector"],record["bits"],record)
        if json.loads(json.dumps(rotor.word))!=record["word_to_basis"]:
            raise AssertionError("reconstructed basis word differs from frozen word")
        if json.loads(json.dumps(rotor.inverse_phase_word))!=record["fixed_inverse_phase_word"]:
            raise AssertionError("reconstructed word differs from frozen word")
        if rotor.full_columns_checked!=dim:raise AssertionError("missing full-column execution")
        bank[int(name)]=rotor
    intv={int(m):{k:F(v) for k,v in record.items()} for m,record in saved["target_intervals"].items()}
    return bank,intv,dim

@dataclass
class Branch:
    next_bit: int
    history: int
    state: dict
    den: int

def mass(branch):
    return F(sum(v*v for row in branch.state.values() for v in row),branch.den*branch.den)

def canonical_branch(next_bit,history,state,den):
    state,den=reduce_state(state,den)
    return Branch(next_bit,history,state,den)

def start_branch(source,den,t):
    # Same bit reversal as original run_qft; original source kept unmodified.
    return Branch(0,0,{(reverse_bits(x,t),w,anc):row for (x,w,anc),row in source.items()},den)

def advance(branch,bank,dim):
    """One original CP/H4 block, then terminal control measurement.

    Old control bits are classical history; spectator and all residual modes
    are retained. Exact rational common-factor reduction is NOT normalization.
    Both children are returned even if their exact weight is zero.
    """
    b=branch.next_bit
    if not branch.state:
        return (Branch(b+1,branch.history,{},1),
                Branch(b+1,branch.history|(1<<b),{},1))
    state={((x<<b)|branch.history,w,anc):row for (x,w,anc),row in branch.state.items()}
    den=branch.den
    for ctrl in range(b):
        state,den=cp_step(state,den,b,ctrl,bank[b-ctrl+1])
    compact={(x>>b,w,anc):row for (x,w,anc),row in state.items()}
    compact,den=h4_step(compact,den,0,dim)
    parts=[{},{}]
    for (x,w,anc),row in compact.items():
        parts[x&1][x>>1,w,anc]=row
    children=tuple(canonical_branch(b+1,branch.history|(r<<b),parts[r],den) for r in (0,1))
    if mass(children[0])+mass(children[1])!=mass(branch):
        raise AssertionError("instrument is not mass preserving")
    return children

def enumerate_leaves(source,den,t,bank,dim):
    branches=[start_branch(source,den,t)]
    stats=[]
    for b in range(t):
        branches=[child for branch in branches for child in advance(branch,bank,dim)]
        stats.append({"after_bit":b,"branches":len(branches),"positive_branches":sum(bool(p.state) for p in branches),
          "zero_branches":sum(not p.state for p in branches),
          "total_endpoint_count":sum(len(p.state) for p in branches),
          "max_single_branch_endpoints":max(len(p.state) for p in branches),
          "max_single_branch_scalar_slots":max(len(p.state)*dim for p in branches),
          "max_denominator_bits":max(p.den.bit_length() for p in branches),
          "total_mass":sum((mass(p) for p in branches),F(0)),
          "spectator_one_mass":sum((F(sum(v*v for (x,w,anc),row in p.state.items() if anc==1 for v in row),p.den*p.den) for p in branches),F(0)),
          "all_extra_mode_mass":sum((F(sum(v*v for row in p.state.values() for v in row[2:]),p.den*p.den) for p in branches),F(0))})
        if stats[-1]["total_mass"]!=1:raise AssertionError("lost probability")
    return branches,stats

def uniform_below(n,rng,stats=None):
    """Exact uniform integer in [0,n), with an external unbiased getrandbits.
    Rejection ensures no modulo bias. Almost sure finite, not worst-case capped.
    """
    if not isinstance(n,int) or n<1:raise ValueError("positive bound required")
    if n==1:return 0
    width=(n-1).bit_length()
    while True:
        u=rng.getrandbits(width)
        if not isinstance(u,int) or not 0<=u<(1<<width):raise ValueError("invalid external random bits")
        if stats is not None:
            stats["draws"]+=1;stats["bits"]+=width
        if u<n:return u
        if stats is not None:stats["rejections"]+=1

def bernoulli_zero(p,rng,stats=None):
    if not 0<=p<=1:raise ValueError("invalid exact probability")
    if p==0:return 1
    if p==1:return 0
    return 0 if uniform_below(p.denominator,rng,stats)<p.numerator else 1

def sample_single(source,den,t,bank,dim,rng):
    branch=start_branch(source,den,t)
    trace=[];random_stats={"draws":0,"bits":0,"rejections":0}
    max_endpoints=len(branch.state)
    for b in range(t):
        children=advance(branch,bank,dim)
        weights=[mass(child) for child in children];parent=mass(branch)
        if parent<=0:raise AssertionError("cannot condition on zero branch")
        p=weights[0]/parent
        r=bernoulli_zero(p,rng,random_stats)
        branch=children[r]
        if mass(branch)<=0:raise AssertionError("sampled zero probability outcome")
        max_endpoints=max(max_endpoints,len(branch.state))
        trace.append({"bit":b,"zero_probability":p,"selected":r,"unconditional_prefix_mass":mass(branch),"retained_endpoints":len(branch.state)})
    return {"k":branch.history,"trace":trace,"random_source_contract":"external unbiased independent getrandbits",
      "random_stats":random_stats,"max_selected_branch_endpoints":max_endpoints,
      "state":branch.state,"den":branch.den}

class StreamingProgram:
    """One active control bit; exact retained-mode BRC terminal instrument.

    Boundary state uses (x=0, work, spectator) labels. History is the tuple of
    measured low-to-high inverse-QFT bits. Preparation/modexp are streamed;
    neither a full control superposition nor an order is an input.
    """
    def __init__(self,N,a,t,bank,dim):
        if not isinstance(N,int) or N<3:raise ValueError("N>=3")
        if not isinstance(a,int) or not 1<=a<N:raise ValueError("1<=a<N")
        if not isinstance(t,int) or t<2 or t%2:raise ValueError("even t>=2 required by frozen preparation")
        if any(m not in bank for m in range(2,t+1)):raise ValueError("frozen phase bank does not cover t")
        self.N,self.a,self.t,self.bank,self.dim=N,a,t,bank,dim
        b=a%N;powers=[]
        for _ in range(t):
            powers.append(b);b=b*b%N
        self.modular_powers=tuple(reversed(powers))
        self.tables=tuple(modular_columns(N,b) for b in self.modular_powers)
        self.metrics={"branch_calls":0,"empty_branch_calls":0,"phase_calls":0,
          "H4_calls":0,"modular_column_applications":0,"peak_endpoints":0,
          "peak_scalar_slots":0,"peak_nonzero_scalars":0,"peak_denominator_bits":0,
          "boundary_spectator_nonzero_seen":False}
        self.depth_metrics={}

    def _observe(self,state,den,depth,operation):
        m={"endpoints":len(state),"scalar_slots":len(state)*self.dim,
           "nonzero_scalars":sum(bool(v) for row in state.values() for v in row),
           "denominator_bits":den.bit_length()}
        for k in m:self.metrics["peak_"+k]=max(self.metrics["peak_"+k],m[k])
        key=(depth,operation)
        if key not in self.depth_metrics:self.depth_metrics[key]={"calls":0,**{k:0 for k in m}}
        target=self.depth_metrics[key];target["calls"]+=1
        for k in m:target[k]=max(target[k],m[k])

    def initial(self):
        return {(0,1,0):(1,*([0]*(self.dim-1)))},1

    def branches(self,state,den,history):
        history=tuple(history);i=len(history)
        if i>=self.t or any(r not in (0,1) for r in history):raise ValueError("invalid measurement history")
        if any(x!=0 for x,w,h in state):raise ValueError("control bit must be empty at round boundary")
        self.metrics["branch_calls"]+=1
        if not state:
            self.metrics["empty_branch_calls"]+=1
            return [({},1),({},1)]
        before=F(sum(v*v for row in state.values() for v in row),den*den)
        self._observe(state,den,i,"initial_boundary")
        state,den=h4_step(state,den,0,self.dim)
        self.metrics["H4_calls"]+=1;self._observe(state,den,i,"prepare_H4")
        table=self.tables[i]
        state={(x,table[w] if x else w,anc):row for (x,w,anc),row in state.items()}
        self.metrics["modular_column_applications"]+=1;self._observe(state,den,i,"controlled_modular_power")
        hbits=sum(r<<j for j,r in enumerate(history))
        for ctrl in range(i):
            expanded={((x<<i)|hbits,w,anc):row for (x,w,anc),row in state.items()}
            expanded,den=cp_step(expanded,den,i,ctrl,self.bank[i-ctrl+1])
            state={(x>>i,w,anc):row for (x,w,anc),row in expanded.items()}
            self.metrics["phase_calls"]+=1;self._observe(state,den,i,"CP_"+str(i-ctrl+1))
        state,den=h4_step(state,den,0,self.dim)
        self.metrics["H4_calls"]+=1;self._observe(state,den,i,"read_H4")
        parts=[{},{}]
        for (x,w,anc),row in state.items():parts[x][0,w,anc]=row
        children=[reduce_state(part,den) for part in parts]
        after=sum((F(sum(v*v for row in p.values() for v in row),d*d) for p,d in children),F(0))
        if before!=after:raise AssertionError("streaming mass lost")
        if any(anc for p,d in children for x,w,anc in p):
            self.metrics["boundary_spectator_nonzero_seen"]=True
            raise AssertionError("shared spectator failed to return, never reset")
        for part,d in children:self._observe(part,d,i,"child_boundary")
        return children

    def report_metrics(self):
        return {**self.metrics,"depth_maxima":[{"depth":d,"operation":op,**m}
          for (d,op),m in sorted(self.depth_metrics.items())]}

def streaming_leaves(program):
    state,den=program.initial();branches=[((),state,den)]
    for i in range(program.t):
        branches=[(history+(r,),p,d) for history,state,den in branches
                  for r,(p,d) in enumerate(program.branches(state,den,history))]
    return branches

def encode(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,Path):return str(x)
    if isinstance(x,dict):return {str(k):encode(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [encode(v) for v in x]
    return x

def digest_rows(rows):
    h=hashlib.sha256()
    for row in rows:h.update((json.dumps(encode(row),separators=(",",":"))+"\n").encode())
    return h.hexdigest()

def verify_case(N,a,t,bank,intv,dim):
    started=perf_counter_ns()
    source,den,_=prepare_fixed(N,a,t,dim)
    full,fd,ft=run_qft(source,den,t,bank,dim,trace=True)
    nums,pden=law(full,fd,t)
    leaves,stats=enumerate_leaves(source,den,t,bank,dim)
    reconstructed={}
    law_by_leaf={}
    comparisons=0
    for leaf in leaves:
        law_by_leaf[leaf.history]=mass(leaf)
        if leaf.next_bit!=t:raise AssertionError("incomplete history")
        for (remaining,w,anc),row in leaf.state.items():
            if remaining!=0:raise AssertionError("unmeasured control remains")
            key=(leaf.history,w,anc)
            reconstructed[key]=(row,leaf.den)
    allkeys=set(full)|set(reconstructed)
    for key in allkeys:
        original=full.get(key,(0,)*dim)
        row,ld=reconstructed.get(key,((0,)*dim,1))
        comparisons+=dim
        if any(x*ld!=y*fd for x,y in zip(original,row)):
            raise AssertionError(("full joint amplitude mismatch",N,a,t,key))
    if any(law_by_leaf[k]!=F(nums[k],pden) for k in range(1<<t)):
        raise AssertionError("control law mismatch")
    full_joint_rows=((list(key)+[j,F(v*v,fd*fd)]) for key,row in sorted(full.items()) for j,v in enumerate(row) if v)
    branch_joint_rows=((list(key)+[j,F(v*v,ld*ld)]) for key,(row,ld) in sorted(reconstructed.items()) for j,v in enumerate(row) if v)
    full_hash=digest_rows(full_joint_rows);branch_hash=digest_rows(branch_joint_rows)
    if full_hash!=branch_hash:raise AssertionError("full joint probability hashes differ")
    # Stronger candidate: never prepares all Q control paths.
    streaming=StreamingProgram(N,a,t,bank,dim)
    stream_leaves=streaming_leaves(streaming)
    stream_reconstructed={}
    stream_law={}
    for history,state,sd in stream_leaves:
        k=sum(r<<i for i,r in enumerate(history))
        stream_law[k]=F(sum(v*v for row in state.values() for v in row),sd*sd)
        for (x,w,anc),row in state.items():
            if x!=0:raise AssertionError("stream control bit not removed")
            stream_reconstructed[k,w,anc]=(row,sd)
    stream_comparisons=0
    for key in set(full)|set(stream_reconstructed):
        original=full.get(key,(0,)*dim);row,sd=stream_reconstructed.get(key,((0,)*dim,1))
        stream_comparisons+=dim
        if any(x*sd!=y*fd for x,y in zip(original,row)):
            raise AssertionError(("streamed full joint amplitude mismatch",N,a,t,key))
    stream_hash=digest_rows((list(key)+[j,F(v*v,sd*sd)]) for key,(row,sd) in sorted(stream_reconstructed.items()) for j,v in enumerate(row) if v)
    if stream_hash!=full_hash:raise AssertionError("streamed full joint probability hash mismatch")
    if any(stream_law[k]!=law_by_leaf[k] for k in range(1<<t)):raise AssertionError("streamed control law mismatch")
    posts={k:classical_postprocess(N,a,t,k) for k in range(1<<t)}
    success=sum((law_by_leaf[k] for k,p in posts.items() if p["factors"]),F(0))
    original_success=F(sum(nums[k] for k,p in posts.items() if p["factors"]),pden)
    if success!=original_success:raise AssertionError("postprocessing law mismatch")
    status_law={}
    factor_law={}
    for k,p in posts.items():
        status_law[p["status"]]=status_law.get(p["status"],F(0))+law_by_leaf[k]
        fs=tuple(p["factors"]);factor_law[str(fs)]=factor_law.get(str(fs),F(0))+law_by_leaf[k]
    rng=random.Random(20260926+N*101+a*3+t)
    sample=sample_single(source,den,t,bank,dim,rng)
    selected=next(p for p in leaves if p.history==sample["k"])
    if sample["state"]!=selected.state or sample["den"]!=selected.den:raise AssertionError("sample replay differs")
    del sample["state"];del sample["den"]
    sample["postprocessing"]=posts[sample["k"]]
    # An explicitly injected illegal spectator deletion is detected at bit0.
    c0,c1=advance(start_branch(source,den,t),bank,dim)
    kept_zero=sum((F(sum(v*v for (x,w,h),row in p.state.items() if h==0 for v in row),p.den*p.den) for p in (c0,c1)),F(0))
    if kept_zero!=F(1,2):raise AssertionError("spectator deletion negative control failed")
    return {"N":N,"a":a,"t":t,"dim":dim,"Q":1<<t,
      "all_leaf_slots":len(leaves),"zero_leaf_slots":sum(not p.state for p in leaves),
      "full_joint_amplitude_coordinate_comparisons":comparisons,
      "all_joint_amplitudes_exact_equal":True,"all_joint_probabilities_exact_equal":True,
      "all_control_bins_exact_equal":True,"postprocessing_status_and_factor_law_exact_equal":True,
      "streaming_all_joint_amplitudes_exact_equal":True,
      "streaming_all_control_bins_exact_equal":True,
      "streaming_joint_amplitude_coordinate_comparisons":stream_comparisons,
      "streaming_full_joint_probability_sha256":stream_hash,
      "streaming_all_leaf_slots":len(stream_leaves),
      "streaming_zero_leaf_slots":sum(not s for h,s,d in stream_leaves),
      "streaming_modular_powers_from_input":streaming.modular_powers,
      "streaming_metrics":streaming.report_metrics(),
      "full_joint_probability_sha256":full_hash,"branch_joint_probability_sha256":branch_hash,
      "control_law":[law_by_leaf[k] for k in range(1<<t)],"status_law":status_law,"factor_law":factor_law,
      "success_probability":success,"all_modes_retained":True,"shared_spectator_retained":True,
      "spectator_deletion_detected_mass":kept_zero,"ideal_reference_error_inherited":fixed_error(t,intv,64),
      "resource_stats":stats,"original_full_max_macro_endpoints":max([len(source)]+[r["endpoints"] for r in ft]),
      "original_full_final_endpoints":len(full),"selected_path_sample":sample,
      "no_polynomial_runtime_or_independent_review_claim":True,"elapsed_ns":perf_counter_ns()-started}

class Tape:
    def __init__(self,values):self.values=list(values);self.calls=[]
    def getrandbits(self,k):
        if not self.values:raise AssertionError("tape exhausted")
        v=self.values.pop(0);self.calls.append((k,v));return v

def sampler_unit_checks():
    no_bits=Tape([])
    assert bernoulli_zero(F(0),no_bits)==1 and bernoulli_zero(F(1),no_bits)==0
    stats={"draws":0,"bits":0,"rejections":0};tape=Tape([3,0])
    assert bernoulli_zero(F(1,3),tape,stats)==0 and stats=={"draws":2,"bits":4,"rejections":1}
    assert bernoulli_zero(F(1,3),Tape([1]))==1
    # Exhaustive accepted integer positions realize p/q for several denominators.
    for q in (2,3,5,7,8,13):
        for p in range(q+1):
            zeros=sum(bernoulli_zero(F(p,q),Tape([v]))==0 for v in range(F(p,q).denominator))
            assert zeros==F(p,q).numerator
    return {"zero_and_one_consume_no_bits":True,"non_power_of_two_denominator":3,"rejection_tape":tape.calls,"rejection_stats":stats,"finite_accepted_slot_counts_checked":True}

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--out",default=str(ROOT/"terminal_output"));args=parser.parse_args()
    out=Path(args.out);out.mkdir(parents=True,exist_ok=True)
    begin=perf_counter_ns();core=verify_vendor();print("verified BRC vendor",flush=True)
    bank,intv,dim=load_frozen_bank()
    print("compiled frozen bank",dim,"BRC calls",len(CALLS),flush=True)
    results=[]
    for spec in [(15,2,4),(21,2,6),(15,14,4)]:
        print("case",spec,flush=True);row=verify_case(*spec,bank,intv,dim);results.append(row)
        (out/f"CASE_{spec[0]}_{spec[1]}_{spec[2]}.json").write_text(json.dumps(encode(row),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print("passed",spec,"amplitude checks",row["full_joint_amplitude_coordinate_comparisons"],flush=True)
    tests=sampler_unit_checks()
    payload={"schema":"BRC_SHOR_TERMINAL_INSTRUMENT_V1","status":"AUTHOR_EXECUTED_UNREVIEWED_NOT_ADMITTED",
      "activity":"RA-40F334CAC4876C16B82B0215","researcher":"EM-DIRECT-0C08F0",
      "frozen_input_head":"0852cad130c1d877174d235687cf60c19f318c58",
      "new_execution_source":"c412dcb62f4b27189afd8e5748ff5f8dbb3c17dd",
      "route":"ACTUAL_TYPED_BRC_ONLY","frozen_bank":{"max_m":10,"target_bits":32,"vector_bits":64,"dimension":dim},
      "core":core,"actual_brc_calls":len(CALLS),"call_receipts":CALLS,"sampler_checks":tests,"cases":results,
      "probability_semantics":"BORROWED_REFERENCE_SQUARED_NORM","elapsed_ns":perf_counter_ns()-begin,
      "scope":"Terminal computational control output and unchanged CF/gcd. No later coherent use of measured control labels.",
      "not_claimed":["polynomial classical simulation","spatial hardware closure","native Born law","independent review"]}
    raw=json.dumps(encode(payload),ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
    (out/"RESULTS.json.gz").write_bytes(gzip.compress(raw,mtime=0))
    brief={k:v for k,v in payload.items() if k not in ("call_receipts","cases")}
    brief["case_summaries"]=[{k:r[k] for k in ("N","a","t","dim","all_leaf_slots","zero_leaf_slots","full_joint_amplitude_coordinate_comparisons","full_joint_probability_sha256","all_joint_amplitudes_exact_equal","all_joint_probabilities_exact_equal","all_control_bins_exact_equal","postprocessing_status_and_factor_law_exact_equal","original_full_max_macro_endpoints","original_full_final_endpoints","elapsed_ns")} for r in results]
    brief["full_payload_sha256"]=hashlib.sha256(raw).hexdigest()
    brief["streaming"]=True
    for summary,row in zip(brief["case_summaries"],results):
        for key in ("streaming_all_joint_amplitudes_exact_equal","streaming_all_control_bins_exact_equal","streaming_joint_amplitude_coordinate_comparisons","streaming_full_joint_probability_sha256","streaming_all_leaf_slots","streaming_zero_leaf_slots"):
            summary[key]=row[key]
        summary["streaming_peak_endpoints"]=row["streaming_metrics"]["peak_endpoints"]
        summary["streaming_peak_scalar_slots"]=row["streaming_metrics"]["peak_scalar_slots"]
    (out/"SUMMARY.json").write_text(json.dumps(encode(brief),ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print("COMPLETE","BRC calls",len(CALLS),"seconds",(perf_counter_ns()-begin)//1000000000,flush=True)
if __name__=="__main__":main()
