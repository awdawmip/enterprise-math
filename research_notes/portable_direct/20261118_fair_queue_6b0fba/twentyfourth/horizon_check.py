#!/usr/bin/env python3
"""Full native 13-endpoint forward run; exact cyclic-polynomial restoration."""
import argparse
import gzip
import hashlib
import json
import math
import platform
import sys
from fractions import Fraction as Q
from pathlib import Path

import numpy as np
import scipy
from scipy.optimize import linear_sum_assignment

HERE = Path(__file__).resolve().parent
PRO = HERE / "horizon_protocol.json"
EXPECTED = "f8e7799b75c1da1e284c3edab7d57dc5846a8c39c7a3dafb5f0434d4c1b927e5"
N = 65536
FLOOR = 1e-8
TIMES = np.arange(N + 1)
SITES = [tuple(int(j == i//2 or (i%2 and j == (i//2+1)%6)) for j in range(6))
         for i in range(12)] + [(0,)*6]
COLUMNS = ([f"tv_axis_{i+1}" for i in range(6)] + ["tv_joint_123","tv_joint_456",
           "tv_full","signed_axis_1","mu_ring","nu_ring"] +
           [f"{side}_{metric}" for side in ["mu","nu"] for metric in
            ["p1","var","k4","gamma","gamma_status","reset_from_ring","stay_on_ring"]])


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def init(name):
    if name in ("even","odd"):
        return [Q(int(i%2 == (name == "odd")),6) for i in range(12)] + [Q(0)]
    j = 12 if name == "o" else int(name[1:])
    return [Q(i == j) for i in range(13)]


def cases():
    assert sha(PRO) == EXPECTED
    cfg = json.loads(PRO.read_text())
    out = []
    for name, af, bf, df, left, right in cfg["a_b_d_and_initial_laws"]:
        a,b,d = map(Q,(af,bf,df))
        out.append((name, (a,b,1-a-b-d,d), init(left),init(right)))
    return out


def push_exact(law, rates):
    a,b,c,d = rates
    out = [Q(0)] * 13
    for i,v in enumerate(law):
        for dest,w in [(12 if i==12 else (i+1)%12,a),
                       (12 if i==12 else (i-1)%12,b),(i,c),(12,d)]:
            out[dest] += v*w
    return out


def conv(x,y):
    return [sum(x[i]*y[(j-i)%12] for i in range(12)) for j in range(12)]


def exact_blocks(allcases):
    data = {}
    for name,rates,left,right in allcases:
        den = math.lcm(*(q.denominator for q in rates))
        a,b,c,d = [int(den*v) for v in rates]
        word = [c,a]+[0]*9+[b]
        row = [1]+[0]*11
        # Each integer is hexadecimal; scale at residual index t equals den**t.
        rows = []
        for t in range(257):
            rows.append([format(v,"x") for v in row])
            if t<256:
                row = [a*row[(j-1)%12]+b*row[(j+1)%12]+c*row[j] for j in range(12)]
        assert row == conv([int(v,16) for v in rows[255]],word)
        data[name] = {"den":den,"block":rows}
    return data


def restore(data,name,n,x):
    if not 0 <= n <= N:
        raise ValueError(f"restore step must be between 0 and {N}")
    item = data[name]
    h,t = divmod(n,256)
    rows = item["block"]
    q = item["den"]
    result = [int(v,16) for v in rows[t]]
    power = [int(v,16) for v in rows[256]]
    while h:
        if h&1:
            result = conv(result,power)
        h //= 2
        if h:
            power = conv(power,power)
    den = q**n
    scale = math.lcm(*(z.denominator for z in x))
    r = conv([int(scale*z) for z in x[:12]],result)
    ring = [Q(z,scale*den) for z in r]
    return ring+[sum(x)-sum(ring)]


def archive(path, raw):
    with path.open("wb") as fp:
        with gzip.GzipFile(filename="", fileobj=fp, mode="wb", mtime=0,compresslevel=5) as gz:
            gz.write(raw)


def direct(allcases):
    rates = np.array([[float(z) for z in v] for _,v,_,_ in allcases])
    a,b,c,d = [v[:,None,None] for v in rates.T]
    path = np.zeros((N+1,len(allcases),3,13))
    for j,(_,_,l,r) in enumerate(allcases):
        path[0,j] = np.array([l,r,[x-y for x,y in zip(l,r)]],dtype=float)
    for n in range(N):
        old = path[n]
        ring = old[:,:,:12]
        out = path[n+1]
        out[:,:,:12] = a*np.roll(ring,1,axis=2)+b*np.roll(ring,-1,axis=2)+c*ring
        out[:,:,12] = old[:,:,12] + d[:,:,0]*np.sum(ring,axis=2)
    return path


def supports(x,rates):
    a,b,c,d = rates
    mask = sum(1<<i for i,p in enumerate(x) if p)
    seen, seq = {}, []
    while mask not in seen:
        seen[mask] = len(seq)
        seq.append(mask)
        m = 0
        for i in range(13):
            if mask >> i & 1:
                for dest,w in [(12 if i==12 else (i+1)%12,a),
                               (12 if i==12 else (i-1)%12,b),(i,c),(12,d)]:
                    if w: m |= 1<<dest
        mask = m
    start = seen[mask]
    period = len(seq)-start
    return np.array([seq[t if t<start else start+(t-start)%period] for t in range(N+1)])


def projections(path,rates,left,right):
    a,b,c,d = map(float,rates)
    delta = path[:,2,:]
    values = []
    for axes in [(i,) for i in range(6)]+[(0,1,2),(3,4,5)]:
        groups = {}
        for i,row in enumerate(SITES):
            groups.setdefault(tuple(row[h] for h in axes),[]).append(i)
        values.append(sum(np.abs(delta[:,group].sum(axis=1)) for group in groups.values())/2)
    axis = [i for i,s in enumerate(SITES) if s[0]]
    success_mask = sum(1<<i for i in axis)
    values += [np.abs(delta).sum(axis=1)/2,delta[:,axis].sum(axis=1)]
    mass = path[:,:,:12].sum(axis=2)
    values += [mass[:,0],mass[:,1]]
    for j,x in enumerate([left,right]):
        p = path[:,j,:][:,axis].sum(axis=1).clip(0,1)
        var = p*(1-p)
        k4 = var*(1-6*var)
        mask = supports(x,rates)
        pure = ((mask & success_mask)==0) | ((mask & (8191^success_mask))==0)
        # 0 exactly undefined; 1 certified away from numerical floor; 2 positive,
        # but too small to certify gamma in the direct arithmetic.
        status = np.where(pure,0,np.where(var>=FLOOR,1,2))
        gamma = np.full(N+1,np.nan)
        good = status==1
        gamma[good] = 1/var[good]-6
        values += [p,var,k4,gamma,status,mass[:,j]*d,mass[:,j]*c]
    return np.column_stack(values)


def active_modes(x):
    # Cyclotomic z^4-z^2+1=0. Exact arithmetic, including uniform parity laws.
    basis = [[1,0,0,0]]
    for k in range(1,12):
        w = basis[-1]
        basis.append([-w[3],w[0],w[1]+w[3],w[2]])
    return [k for k in range(12) if any(sum(x[j]*basis[k*j%12][i] for j in range(12))
                                           for i in range(4))]


def get_spectrum(rates,delta):
    a,b,c,d = map(float,rates)
    omega = np.exp(-2j*np.pi*np.arange(12)/12)
    lam = a*omega+b*omega.conjugate()+c
    matrix = np.array([push_exact([Q(i==j) for i in range(13)],rates)
                       for j in range(13)],dtype=float)
    actual = np.linalg.eigvals(matrix)
    dist = abs(actual[:,None]-np.r_[lam,1][None,:])
    rr,cc = linear_sum_assignment(dist)
    modes = active_modes(delta)
    x = np.fft.fft(np.asarray(delta[:12],dtype=float))
    x[[k for k in range(12) if k not in modes]] = 0
    powers = lam[None,:]**TIMES[:,None]
    ring = np.fft.ifft(powers*x[None,:],axis=1).real
    obs = np.c_[ring,-ring.sum(axis=1)]
    rho = max(abs(lam[k]) for k in modes)
    dominant = [k for k in modes if abs(abs(lam[k])-rho)<1e-12]
    return {"active_ring":modes,"dominant_ring":dominant,"rho":float(rho),
            "e_fold_steps":float(-1/math.log(rho)) if 0<rho<1-1e-14 else None,
            "dense_eig_max_error":float(dist[rr,cc].max())},obs


def fit(tv,tr,te,kind):
    ti = TIMES[(TIMES>=tr[0])&(TIMES<=tr[1])&(tv>=FLOOR)]
    hi = TIMES[(TIMES>=te[0])&(TIMES<=te[1])&(tv>=FLOOR)]
    ans = {"train_n":len(ti),"holdout_n":len(hi)}
    if not len(ti):
        ans["status"]="no training samples"
        return ans
    if kind=="period12":
        if len(set(ti%12))!=12:
            ans["status"]="missing residues"
            return ans
        p = np.array([tv[ti[ti%12==j]].mean() for j in range(12)])
        estimate = lambda z: p[z%12]
    else:
        plateau = 0.5 if kind=="plateau_half+exp" else 0
        if np.any(tv[ti]<=plateau) or len(ti)<2:
            ans["status"]="log residual outside domain or too few samples"
            return ans
        xx = np.log(ti) if kind=="power" else ti.astype(float)
        yy = np.log(tv[ti]-plateau)
        slope = np.sum((xx-xx.mean())*(yy-yy.mean()))/np.sum((xx-xx.mean())**2)
        intercept = yy.mean()-slope*xx.mean()
        ans["slope"] = float(slope)
        estimate = lambda z: plateau+np.exp(intercept+slope*(np.log(z) if kind=="power" else z))
    ans["status"]="scored" if len(hi) else "no eligible holdout"
    for label,z in [("train",ti),("holdout",hi)]:
        ans[label+"_rmse"] = float(np.sqrt(np.mean((estimate(z)-tv[z])**2))) if len(z) else None
    return ans


def inspect(case,path,data):
    name,rates,left,right = case
    delta = [l-r for l,r in zip(left,right)]
    spec,reference = get_spectrum(rates,delta)
    error = float(np.max(abs(reference-path[:,2,:])))
    assert error<1e-9 and spec["dense_eig_max_error"]<1e-12
    audit = []
    for j,x in enumerate([left,right,delta]):
        exact = x
        for n in range(25):
            assert restore(data,name,n,x)==exact
            audit.append(max(abs(path[n,j]-np.array(exact,dtype=float))))
            exact = push_exact(exact,rates)
        y = restore(data,name,513,x)
        assert max(abs(path[513,j]-np.array(y,dtype=float)))<1e-12
    obs = projections(path,rates,left,right)
    tv = obs[:,8]
    windows = [(1,4096),(1,256),(257,4096)]
    fits = {f"{lo}..{hi}":{m:fit(tv,(lo,hi),(4097,N),m) for m in
                                ["period12","exp","plateau_half+exp","power"]} for lo,hi in windows}
    # Record finite sign transitions among points above threshold, preserving time gaps.
    s = obs[:,9]
    sign = {}
    for tag,lo,hi in [("train",1,4096),("holdout",4097,N)]:
        z = s[lo:hi+1]
        sign[tag] = {lab:int(np.count_nonzero(mask)) for lab,mask in
                     [("positive",z>=FLOOR),("negative",z<=-FLOOR),("below",np.abs(z)<FLOOR)]}
        sign[tag]["adjacent_sign_changes"] = int(np.count_nonzero((np.abs(z[:-1])>=FLOOR)&
                                   (np.abs(z[1:])>=FLOOR)&(np.sign(z[:-1])!=np.sign(z[1:]))))
    summary = {"spectrum":spec,"fourier_delta_max_abs_error":error,"short_exact_max_abs_error":float(max(audit)),
               "direct_cancellation_max_abs_error":float(np.max(abs((path[:,0,:]-path[:,1,:])-path[:,2,:]))),
               "mass_conservation_max_abs_error":float(np.max(abs(path[:,:2,:].sum(axis=2)-1))),
               "scored_range":[int(TIMES[tv>=FLOOR][0]),int(TIMES[tv>=FLOOR][-1])],
               "fit":fits,"first_axis_sign":sign,
               "snapshots":{str(n):[float(z) if math.isfinite(z) else None for z in obs[n]]
                            for n in [0,1,2,12,256,4096,4097,32768,N]}}
    if name=="near_shift":
        eta = float(rates[1])
        comparisons = {}
        for n in [12,256,4096,32768,N]:
            mean = n*eta
            prob = math.exp(-mean)
            wrapped = np.zeros(12)
            for k in range(51):
                wrapped[(n-2*k)%12] += prob
                prob *= mean/(k+1)
            tail = prob/(1-mean/52)
            distance = float(sum(abs(path[n,0,:12]-wrapped))/2)
            assert distance <= n*eta**2+tail+1e-10
            comparisons[str(n)] = {"distance_to_wrapped_Poisson":distance,
                                    "bound":n*eta*(-math.expm1(-eta)),"series_tail_bound":tail}
        summary["rare_reverse_Poisson"] = comparisons
    if name in ("drift","bipartite"):
        y = restore(data,name,N,left)
        assert sum(y)==1
        summary["final_exact_block_max_abs_error_mu"] = float(max(abs(path[N,0]-np.array(y,dtype=float))))
        assert summary["final_exact_block_max_abs_error_mu"]<1e-10
    return summary,obs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,default=HERE)
    parser.add_argument("--raw",action="store_true",help="also archive all direct laws and readouts as float64")
    parser.add_argument("--restore",nargs=3,metavar=("CASE","N","mu|nu|delta"))
    args = parser.parse_args()
    allcases = cases()
    out = args.out
    if args.restore:
        name, step, which = args.restore
        by_name = {case[0]: case for case in allcases}
        if name not in by_name:
            parser.error("restore CASE must be one of " + ", ".join(by_name))
        try:
            n = int(step)
        except ValueError:
            parser.error(f"restore N must be an integer between 0 and {N}")
        if not 0 <= n <= N:
            parser.error(f"restore N must be between 0 and {N}")
        if which not in ("mu", "nu", "delta"):
            parser.error("restore law must be mu, nu or delta")
        case = by_name[name]
        x = {"mu":case[2],"nu":case[3],"delta":[u-v for u,v in zip(case[2],case[3])]}[which]
        blocks = json.loads(gzip.decompress((out/"horizon_blocks.json.gz").read_bytes()))
        # Large exact outputs use hexadecimal numerators/denominators, unaffected by decimal digit limits.
        print(json.dumps([[hex(z.numerator),hex(z.denominator)] for z in restore(blocks,name,n,x)]))
        return
    out.mkdir(parents=True,exist_ok=True)
    blocks = exact_blocks(allcases)
    archive(out/"horizon_blocks.json.gz",json.dumps(blocks,separators=(",",":")).encode())
    path = direct(allcases)
    rep = {"protocol_sha256":EXPECTED,"environment":[platform.python_version(),np.__version__,scipy.__version__],
           "n":[0,N],"full_case_times":(N+1)*len(allcases),"columns":COLUMNS,"cases":{},
           "exact_archive":{"name":"horizon_blocks.json.gz","sha256":sha(out/"horizon_blocks.json.gz"),
                           "bytes":(out/"horizon_blocks.json.gz").stat().st_size}}
    digest = hashlib.sha256()
    raw_path = out/"horizon_direct.f64.gz"
    fp = raw_path.open("wb") if args.raw else None
    gz = gzip.GzipFile(filename="",fileobj=fp,mode="wb",mtime=0,compresslevel=5) if fp else None
    for j,case in enumerate(allcases):
        summary,obs = inspect(case,path[:,j],blocks)
        rep["cases"][case[0]] = summary
        payload = np.c_[path[:,j].reshape(N+1,39),obs].astype("<f8").tobytes()
        digest.update(payload)
        if gz: gz.write(payload)
    if gz:
        gz.close()
        fp.close()
    rep["direct_uncompressed_sha256"]=digest.hexdigest()
    rep["direct_rows_layout"]="case,n, (mu,nu,delta with r0..r11,o), followed by columns; little-endian float64"
    (out/"horizon_checked.json").write_text(json.dumps(rep,indent=2,allow_nan=False)+"\n")


if __name__=="__main__":
    main()
