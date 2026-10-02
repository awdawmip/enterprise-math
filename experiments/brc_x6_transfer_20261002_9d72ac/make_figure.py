#!/usr/bin/env python3
"""Plot recorded full-law and projected residuals; no fitted curve is substituted for data."""
import csv
import gzip
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent


def run():
    names = ["signed_unit_channel_12_p1_d0", "signed_unit_channel_12_p0p1_d0",
             "signed_unit_channel_12_p0p1_d0p001", "signed_unit_channel_12_p0p1_d0p01"]
    rows = {name: [] for name in names}
    with gzip.open(HERE / "transfer_series.csv.gz", "rt") as handle:
        for row in csv.DictReader(handle):
            if row["case"] in rows:
                rows[row["case"]].append({k:float(row[k]) for k in
                    ("n","tv_spatial","tv_axis_1","tv_axis_4","tv_axes123")})
    plt.rcParams.update({"font.size":10,"axes.spines.top":False,"axes.spines.right":False,
                         "svg.hashsalt":"brc-x6-transfer-20261002"})
    fig, axes = plt.subplots(2,2,figsize=(12,7.8), constrained_layout=True)
    def curve(ax, data, key, label, **kwargs):
        ax.plot([r["n"] for r in data],[r[key] for r in data],label=label,**kwargs)
    a=axes[0,0]; data=rows[names[0]][:25]
    curve(a,data,"tv_spatial","Full X6 law",color="#222222",linestyle="--")
    curve(a,data,"tv_axis_1","Axis 1 observation",drawstyle="steps-post",color="#126fa8")
    a.set(title="A. Hidden at steps 2-10, visible again at 11",ylabel="TV distance",xlabel="Native unit-step index",ylim=(-.05,1.12))
    a.legend(loc="center right",frameon=False)
    a=axes[0,1];data=rows[names[1]][:401]
    for key,label in [("tv_spatial","Full X6 law"),("tv_axis_1","Axis 1"),("tv_axis_4","Axis 4"),("tv_axes123","Axes 1,2,3 jointly")]:
        curve(a,data,key,label)
    a.axhline(.25,color="gray",ls=":",lw=1)
    a.set(title="B. Mixing redistributes visibility (p = 0.1)",ylabel="TV distance",xlabel="Routing tick",ylim=(-.05,1.12))
    a.legend(frameon=False,fontsize=9)
    a=axes[1,0]
    for name,label in [(names[1],"No reset"),(names[2],"Reset probability 0.001"),(names[3],"Reset probability 0.01")]:
        curve(a,rows[name],"tv_spatial",label)
    a.set(yscale="log",title="C. Explicit reset contracts the full spatial law",ylabel="Full X6 TV (log scale)",xlabel="Routing tick")
    a.legend(frameon=False,fontsize=9)
    a=axes[1,1]; n=list(range(9))
    a.plot(n,[(x+1)**2 for x in n],"o-",label="Initial Cov(1,4) = +1")
    a.plot(n,[(x-1)**2 for x in n],"s-",label="Initial Cov(1,4) = -1")
    a.plot(n,[1+x*x for x in n],"--",label="Initially decorrelated")
    a.set(title="D. Same initial marginals, different future variance",ylabel="Variance on axis 1",xlabel="Native unit-step index")
    a.legend(frameon=False,fontsize=9)
    fig.suptitle("Fixed native X6: declared channel controls, not a universal propagation law",fontsize=14)
    fig.savefig(HERE / "x6_transfer.png",dpi=160,metadata={"Software":"BRC X6 transfer experiment"})
    fig.savefig(HERE / "x6_transfer.svg",metadata={"Date":None})
    plt.close(fig)


if __name__ == "__main__":
    run()
