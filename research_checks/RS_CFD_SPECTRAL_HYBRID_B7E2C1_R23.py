from fractions import Fraction as F
import ctypes.util, importlib.util, json, os, shutil


def robust_denominator(T_hat, D_hat, H_hat, eT, eD, eH, A):
    """Sharp lower bound for 1 + (H-A*D)/T under the stated box errors.

    Preconditions: T in [T_hat-eT,T_hat+eT], D <= D_hat+eD,
    H >= max(0,H_hat-eH), 0<=A<=1, and D_plus<=T_minus.
    """
    Tm, Tp = T_hat-eT, T_hat+eT
    Dp = D_hat+eD
    Hm = max(F(0), H_hat-eH)
    assert Tm > 0 and F(0) <= A <= F(1) and F(0) <= Dp <= Tm
    N = Hm - A*Dp
    T_extreme = Tp if N >= 0 else Tm
    return F(1) + N/T_extreme


def host_probe():
    modules = ["spectralDNS", "shenfun", "mpi4py", "mpi4py_fft", "pyfftw"]
    commands = ["mpicc", "mpicxx"]
    headers = ["mpi.h", "fftw3.h"]
    p = {
        "modules": {m: bool(importlib.util.find_spec(m)) for m in modules},
        "commands": {c: shutil.which(c) for c in commands},
        "libraries": {l: ctypes.util.find_library(l) for l in ["mpi", "fftw3"]},
        "headers": {h: any(os.path.exists(x) for x in [f"/usr/include/{h}", f"/usr/local/include/{h}"]) for h in headers},
    }
    p["native_ready"] = (all(p["modules"].values()) and all(p["commands"].values())
                         and p["libraries"]["mpi"] is not None
                         and p["libraries"]["fftw3"] is not None
                         and all(p["headers"].values()))
    return p

# Exact finite-grid verification of the endpoint extremum.
checked = 0
for Th in [F(1), F(3,2), F(2)]:
    for eT in [F(0), F(1,20), F(1,10)]:
        if Th <= eT:
            continue
        Tm, Tp = Th-eT, Th+eT
        for Dh in [F(1,5), F(2,5), F(3,5)]:
            for eD in [F(0), F(1,20)]:
                Dp = Dh+eD
                if Dp > Tm:
                    continue
                for Hh in [F(0), F(1,20), F(1,5)]:
                    for eH in [F(0), F(1,50)]:
                        Hm=max(F(0),Hh-eH)
                        for A in [F(0),F(1,5),F(1,2),F(1)]:
                            g=robust_denominator(Th,Dh,Hh,eT,eD,eH,A)
                            # Box-corner enumeration. D=max and H=min are always adverse;
                            # T endpoint is chosen by the sign of Hm-A*Dp.
                            vals=[F(1)+(Hm-A*Dp)/T for T in [Tm,Tp]]
                            assert g == min(vals)
                            checked += 1

# Frozen R19 illustration, now with a deterministic measurement-error envelope.
# Normalize observed dense baseline T_hat=1. R19 illustration has
# A=alpha_bar*w_bar=(7/10)*(2/11)=7/55, D_hat/T_hat=4/5,
# H_hat/T_hat=1/50 and target q=11/10.
A=F(7,55); fhat=F(4,5); hhat=F(1,50); q=F(11,10)
c=F(1)-F(1,1)/q
margin=c+hhat-A*fhat
assert margin == F(1,110)
# In the active branch H_- - A D_+ < 0, the exact target-rejection margin is
# margin - (c+1+A)*delta. Hence delta_crit is rational and exact.
delta_crit = margin/(c+F(1)+A)
assert delta_crit == F(1,134)
assert delta_crit < hhat and delta_crit < (F(1)-fhat)/2

for delta, should_reject in [(F(1,200),True),(F(1,134),False),(F(1,100),False)]:
    g=robust_denominator(F(1),fhat,hhat,delta,delta,delta,A)
    assert (g > F(1,1)/q) == should_reject
assert robust_denominator(F(1),fhat,hhat,F(1,134),F(1,134),F(1,134),A) == F(10,11)

probe=host_probe()
certificate={
    "schema":"ENTERPRISE_MATH_CFD_ROBUST_ATTRIBUTION_CERTIFICATE_V1",
    "claim":"CLM-CFD-B7E2C1-20260922-R23",
    "theorem":{
        "R19_rewrite":"S <= 1/[1 + (H - A*D)/T], with A=alpha_bar*w_bar",
        "measurement_box":"T in [T_hat-eT,T_hat+eT], D<=D_hat+eD, H>=max(0,H_hat-eH), D_plus<=T_minus",
        "sharp_denominator":"g_rob=1+N/T_plus if N>=0 else 1+N/T_minus, N=H_minus-A*D_plus",
        "target_rejection":"q-speedup is impossible whenever g_rob > 1/q"
    },
    "R19_illustration_only":{
        "A":"7/55","f_hat":"4/5","h_hat":"1/50","q":"11/10",
        "zero_error_margin":"1/110",
        "exact_delta_crit":"1/134",
        "delta_crit_percent":float(F(100,134)),
        "interpretation":"If each aggregate T,D,H has deterministic absolute error < delta*T_hat under this symmetric envelope, delta<1/134 preserves the 1.10x impossibility certificate; equality is non-rejecting."
    },
    "host_probe":probe,
    "verification":{"exact_endpoint_cases":checked,"status":"PASS"},
    "boundary":"No native spectralDNS execution and no measured speedup claim."
}
print(json.dumps(certificate, indent=2, sort_keys=True))
