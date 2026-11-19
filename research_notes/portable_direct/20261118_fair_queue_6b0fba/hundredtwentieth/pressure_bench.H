// In-process comparison at the native scalar pEqn.solve() site, before the stock solve.
#include "GAMGAgglomeration.H"
#include <chrono>
#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <limits>
#include <stdexcept>
#include <vector>

namespace pressureStudy {
using Vec = std::vector<double>;
using Timer = std::chrono::steady_clock;
inline void require(bool b, const char* msg) { if (!b) throw std::runtime_error(msg); }
inline long long ns(Timer::time_point t) {
    return std::chrono::duration_cast<std::chrono::nanoseconds>(Timer::now()-t).count();
}
struct Tridiagonal {
    Vec diag,edge;
    Tridiagonal(const Foam::fvScalarMatrix& eq) : diag(eq.diag().size()),edge(diag.size()-1,0) {
        auto all=eq.D();
        for (size_t i=0;i<diag.size();++i) diag[i]=-all()[i];
        const auto& addr=eq.lduAddr();
        require(eq.symmetric() && eq.upper().size()==Foam::label(edge.size()),"not a symmetric path");
        forAll(eq.upper(),i) {
            int u=addr.lowerAddr()[i],v=addr.upperAddr()[i];
            require(v==u+1 && edge[u]==0,"unexpected native face addressing");
            edge[u]=-eq.upper()[i];
        }
    }
};
inline Vec rhs(const Foam::fvScalarMatrix& eq) {
    Vec ret(eq.source().size());
    forAll(eq.source(),i) ret[i]=-eq.source()[i];
    forAll(eq.boundaryCoeffs(),patch) {
        require(!eq.psi().boundaryField()[patch].coupled(),"coupled patch unsupported");
        const auto& owners=eq.lduAddr().patchAddr(patch);
        forAll(owners,j) ret[owners[j]]-=eq.boundaryCoeffs()[patch][j];
    }
    return ret;
}
struct Pivot { int i,l,r; double pivot,al,ar; };
struct Factor {
    std::vector<Pivot> ops;
    int ports;
    explicit Factor(const Tridiagonal& a,int block) {
        const int n=a.diag.size();
        Vec diag=a.diag, edge=a.edge;
        std::vector<int> left(n),right(n),order;
        for(int i=0;i<n;++i) {left[i]=i-1;right[i]=i+1<n?i+1:-1;}
        for (int i=0;i<n;++i) if((i+1)%block && i!=n-1) order.push_back(i);
        ports=n-order.size();
        for (int i=0;i<n;++i) if(!((i+1)%block) || i==n-1) order.push_back(i);
        require(int(order.size())==n,"incomplete elimination order");
        ops.reserve(n);
        for (int i:order) {
            int l=left[i],r=right[i];
            double d=diag[i],al=l<0?0:edge[l],ar=r<0?0:edge[i];
            require(d>0,"singular pivot");
            ops.push_back({i,l,r,d,al/d,ar/d});
            if(l>=0) {diag[l]-=al*al/d;right[l]=r;}
            if(r>=0) {diag[r]-=ar*ar/d;left[r]=l;}
            if(l>=0 && r>=0) edge[l]=-al*ar/d;
        }
    }
    void solve(Vec& x) const {
        for(const Pivot& p:ops) {
            if(p.l>=0) x[p.l]-=p.al*x[p.i];
            if(p.r>=0) x[p.r]-=p.ar*x[p.i];
        }
        for(auto j=ops.rbegin();j!=ops.rend();++j) {
            double v=x[j->i]/j->pivot;
            if(j->l>=0) v-=j->al*x[j->l];
            if(j->r>=0) v-=j->ar*x[j->r];
            x[j->i]=v;
        }
    }
};
struct Thomas {
    Vec diag,l;
    explicit Thomas(const Tridiagonal& a):diag(a.diag),l(a.edge) {
        for(size_t i=0;i<l.size();++i) {
            require(diag[i]>0,"nonpositive Thomas pivot");
            l[i]/=diag[i]; diag[i+1]-=l[i]*a.edge[i];
        }
        require(diag.back()>0,"singular Thomas system");
    }
    void solve(Vec& x) const {
        for(size_t i=0;i<l.size();++i) x[i+1]-=l[i]*x[i];
        x.back()/=diag.back();
        for(int i=int(l.size())-1;i>=0;--i) x[i]=x[i]/diag[i]-l[i]*x[i+1];
    }
};
struct Harmonic {
    Vec part,left,right;
    Harmonic(const Tridiagonal& a,const Vec& fixed,double gl,double gr):
        part(fixed),left(part.size(),0),right(part.size(),0) {
        Thomas f(a);left.front()=gl;right.back()=gr;f.solve(part);f.solve(left);f.solve(right);
    }
    Vec solve(double l,double r) const {
        Vec x(part.size());
        for(size_t i=0;i<x.size();++i) x[i]=part[i]+l*left[i]+r*right[i];
        return x;
    }
};
inline void bench(Foam::fvScalarMatrix& eq,Foam::volScalarField& p) {
    using namespace Foam;
    const fvMesh& mesh=p.mesh();
    int n=mesh.nCells(), b=std::stoi(std::getenv("EM_PRESSURE_BLOCK"));
    const int left=mesh.boundaryMesh().findPatchID("left"), right=mesh.boundaryMesh().findPatchID("right");
    std::ofstream out(std::getenv("EM_PRESSURE_RECEIPT"));
    out<<std::setprecision(17);
    require(left>=0 && right>=0 && !p.needReference(),"Dirichlet benchmark required");
    const double gl=-eq.internalCoeffs()[left][0],gr=-eq.internalCoeffs()[right][0];
    auto bc=[&](double l,double r){
        p.boundaryFieldRef()[left]==l; p.boundaryFieldRef()[right]==r;
        eq.boundaryCoeffs()[left][0]=-gl*l; eq.boundaryCoeffs()[right][0]=-gr*r;
    };
    auto reset=[&](){p.primitiveFieldRef()=scalar(0);};
    auto copyback=[&](const Vec& x){
        auto& v=p.primitiveFieldRef(); for(int i=0;i<n;++i)v[i]=x[i]; p.correctBoundaryConditions();
    };
    Tridiagonal audit(eq);
    for(int i=0;i<n;++i) require(std::abs(audit.diag[i]-n*(i==0||i==n-1?3:2))<1e-7,"native diagonal");
    for(double g:audit.edge) require(std::abs(g+n)<1e-7,"native offdiagonal");
    require(std::abs(gl-2*n)<1e-7 && std::abs(gr-2*n)<1e-7,"boundary conductance");
    bc(0,0);Vec fixed=rhs(eq); double sourceMax=0;
    for(double v:fixed) sourceMax=std::max(sourceMax,std::abs(v));
    Vec particular(n,0);
    double leftCorrection=0,rightCorrection=0;
    for(int j=0;j<n;++j) {
        double xj=(j+0.5)/n;
        leftCorrection-=(1-xj)*fixed[j]; rightCorrection+=xj*fixed[j];
        for(int i=0;i<n;++i) {
            double xi=(i+0.5)/n;
            particular[i]+=std::min(xi,xj)*(1-std::max(xi,xj))*fixed[j];
        }
    }
    out<<"SOURCE";for(double v:fixed)out<<" "<<v;out<<"\n";
    out<<"GEOMETRY "<<n<<" "<<b<<" "<<gl<<" "<<gr<<" "<<sourceMax<<" "<<sizeof(Pivot)<<"\n";
    for(int trial=0;trial<5;++trial) {
        for(int j=0;j<4;++j) {
            int method=(j+trial)%4;
            bc(0,0); reset();
            std::unique_ptr<Tridiagonal> a;
            std::unique_ptr<Thomas> th;std::unique_ptr<Factor> sc;std::unique_ptr<Harmonic> har;
            autoPtr<fvMatrix<scalar>::fvSolver> gamg;
            auto start=Timer::now();
            if(method==0){
                require(!mesh.foundObject<GAMGAgglomeration>(GAMGAgglomeration::typeName),"GAMG unexpectedly warm");
                gamg=eq.solver();
            } else {
                a.reset(new Tridiagonal(eq));
                if(method==1)sc.reset(new Factor(*a,b));
                if(method==2)th.reset(new Thomas(*a));
                if(method==3)har.reset(new Harmonic(*a,rhs(eq),gl,gr));
                a.reset();
            }
            long long setup=ns(start);
            if(method==0 && trial==0){
                const auto& ag=mesh.lookupObject<GAMGAgglomeration>(GAMGAgglomeration::typeName);
                out<<"LEVELS";
                for(int i=0;i<ag.size();++i)out<<" "<<ag.nCells(i)<<":"<<ag.nFaces(i);
                out<<"\n";
            }
            long long time=0;int maxiter=0,miniter=999999,totaliter=0;
            double residual=0,err=0,fluxerr=0,solverNorm=0;
            for(int r=0;r<24;++r) {
                double l=(r%3==0?1:(r%3==1?0:3)), u=(r%3==0?0:(r%3==1?1:-1));
                start=Timer::now();bc(l,u);reset();
                if(method==0) {
                    auto info=gamg->solve();
                    maxiter=std::max(maxiter,int(info.nIterations()));
                    miniter=std::min(miniter,int(info.nIterations()));
                    totaliter+=info.nIterations();solverNorm=std::max(solverNorm,double(info.finalResidual()));
                } else if(method==3) {
                    copyback(har->solve(l,u));
                } else {
                    auto x=rhs(eq);
                    if(method==1)sc->solve(x);else th->solve(x);
                    copyback(x);
                }
                const auto& w=p.primitiveField();
                double fl=gl*(l-w[0]),fr=gr*(w[n-1]-u);
                time+=ns(start);
                // Untimed independent recomputation, using original (uncondensed) entries.
                const Vec f=rhs(eq);
                for(int i=0;i<n;++i){
                    double expected=l+(u-l)*(i+.5)/n+particular[i];
                    err=std::max(err,std::abs(w[i]-expected));
                    double v=audit.diag[i]*w[i]-f[i];
                    if(i) v+=audit.edge[i-1]*w[i-1];
                    if(i+1<n) v+=audit.edge[i]*w[i+1];
                    residual=std::max(residual,std::abs(v));
                }
                fluxerr=std::max(fluxerr,std::max(std::abs(fl-(l-u)-leftCorrection),std::abs(fr-(l-u)-rightCorrection)));
            }
            out<<"RUN "<<trial<<" "<<method<<" "<<setup<<" "<<time<<" "<<residual<<" "<<err
               <<" "<<fluxerr<<" "<<(method==0?miniter:0)<<" "<<maxiter<<" "<<totaliter<<" "<<solverNorm<<"\n";
        }
    }
    bc(1,0);reset();
}
} // namespace pressureStudy
