// Exact result-specific certificate for min_{|det A|=19} Delta_6(A)=77.
//
// No floating point is used. The program enumerates the finite symmetric
// integral Gram window forced by Delta_6<77, classifies every determinant-361
// candidate below the bound as H19 (+) H19 with Delta_6=72, proves that the
// same-phase discriminant form has no order-19 isotropic glue, and checks an
// explicit determinant-19 equality transport with Delta_6=77.
//
// This is RESULT_ONLY research evidence, not a reusable top-level tool family
// and not a Foundation mutation.

#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>

using ll = long long;
using Matrix6 = std::array<std::array<ll, 6>, 6>;

static const std::array<std::pair<int,int>,15> EDGES = []{
    std::array<std::pair<int,int>,15> e{};
    int k=0;
    for(int i=0;i<6;i++) for(int j=i+1;j<6;j++) e[k++]={i,j};
    return e;
}();

struct Conf {
    std::array<int8_t,15> v{};
    int mass=0;
};

ll det_bareiss(Matrix6 a){
    ll sign=1, prev=1;
    for(int k=0;k<5;k++){
        if(a[k][k]==0){
            int sw=-1;
            for(int r=k+1;r<6;r++) if(a[r][k]!=0){ sw=r; break; }
            if(sw<0) return 0;
            std::swap(a[k],a[sw]);
            sign=-sign;
        }
        ll pivot=a[k][k];
        for(int i=k+1;i<6;i++) for(int j=k+1;j<6;j++){
            __int128 num=(__int128)a[i][j]*pivot-(__int128)a[i][k]*a[k][j];
            if(k>0) num/=prev;
            a[i][j]=(ll)num;
        }
        prev=pivot;
        for(int i=k+1;i<6;i++) a[i][k]=0;
    }
    return sign*a[5][5];
}

int diagonal_defect(const std::array<int,6>&d){
    int s=0;
    for(int i=0;i<6;i++) for(int j=i+1;j<6;j++){
        int x=d[i]-d[j]; s+=x*x;
    }
    return s;
}

Matrix6 make_gram(const std::array<int,6>&d,const Conf&c){
    Matrix6 g{};
    for(int i=0;i<6;i++) g[i][i]=d[i];
    for(int k=0;k<15;k++) if(c.v[k]){
        auto [i,j]=EDGES[k];
        g[i][j]=g[j][i]=c.v[k];
    }
    return g;
}

void gen_conf(int idx,int mass,std::array<int8_t,15>&v,
              std::array<std::vector<Conf>,7>&out){
    if(mass>6) return;
    if(idx==15){ out[mass].push_back({v,mass}); return; }
    v[idx]=0; gen_conf(idx+1,mass,v,out);
    v[idx]=-1; gen_conf(idx+1,mass+1,v,out);
    v[idx]= 1; gen_conf(idx+1,mass+1,v,out);
    v[idx]=-2; gen_conf(idx+1,mass+4,v,out);
    v[idx]= 2; gen_conf(idx+1,mass+4,v,out);
    v[idx]=0;
}

void gen_diag(int pos,int last,int minimum,std::array<int,6>&d,
              std::vector<std::pair<std::array<int,6>,int>>&out){
    if(pos==6){
        int D=diagonal_defect(d);
        if(D<77) out.push_back({d,D});
        return;
    }
    for(int x=last;x<=minimum+4;x++){
        d[pos]=x;
        gen_diag(pos+1,x,minimum,d,out);
    }
}

bool canonical_false_type(const std::array<int,6>&d,const Conf&c){
    // Sorted diagonal must be 2,2,3,3,4,4 and exactly four unit edges.
    if(d != std::array<int,6>{2,2,3,3,4,4}) return false;
    if(c.mass!=4) return false;
    int degree[6]={0,0,0,0,0,0};
    std::vector<int> adj[6];
    for(int k=0;k<15;k++) if(c.v[k]){
        if(std::abs((int)c.v[k])!=1) return false;
        auto [i,j]=EDGES[k];
        degree[i]++; degree[j]++;
        adj[i].push_back(j); adj[j].push_back(i);
    }
    // Must be exactly two 3-vertex path components. In each component the
    // degree-2 center has diagonal 4 and endpoints have diagonals 2 and 3.
    bool seen[6]={false,false,false,false,false,false};
    int comps=0;
    for(int s=0;s<6;s++) if(!seen[s]){
        std::vector<int> stack{s}, nodes;
        seen[s]=true;
        while(!stack.empty()){
            int u=stack.back(); stack.pop_back(); nodes.push_back(u);
            for(int w:adj[u]) if(!seen[w]){seen[w]=true;stack.push_back(w);}    
        }
        if(nodes.size()!=3) return false;
        comps++;
        int center=-1; std::vector<int> ends;
        for(int u:nodes){ if(degree[u]==2) center=u; else if(degree[u]==1) ends.push_back(u); else return false; }
        if(center<0 || d[center]!=4 || ends.size()!=2) return false;
        int a=d[ends[0]], b=d[ends[1]];
        if(!((a==2&&b==3)||(a==3&&b==2))) return false;
    }
    return comps==2;
}

int legendre_has_nonzero_self_glue_mod19(){
    // H19 has discriminant coefficient 11, a square mod19. Two identical
    // copies require x^2+y^2=0 mod19. Return number of nonzero solutions.
    int count=0;
    for(int x=0;x<19;x++) for(int y=0;y<19;y++){
        if(x==0 && y==0) continue;
        if((x*x+y*y)%19==0) count++;
    }
    return count;
}

Matrix6 gram_of(const Matrix6&A){
    Matrix6 g{};
    for(int i=0;i<6;i++) for(int j=0;j<6;j++){
        ll s=0; for(int k=0;k<6;k++) s+=A[k][i]*A[k][j];
        g[i][j]=s;
    }
    return g;
}

ll delta6(const Matrix6&g){
    ll tr=0,tr2=0;
    for(int i=0;i<6;i++) tr+=g[i][i];
    for(int i=0;i<6;i++) for(int j=0;j<6;j++) tr2+=g[i][j]*g[j][i];
    return 6*tr2-tr*tr;
}

int main(){
    std::array<std::vector<Conf>,7> confs;
    std::array<int8_t,15> v{};
    gen_conf(0,0,v,confs);

    // If all diagonals are at least 5, write G=5I+E+R. Delta<77 gives
    // M<=6. The same trace/square argument makes 5I+E positive definite;
    // determinant is then coordinatewise increasing in R. Exact E scan:
    ll floor5=std::numeric_limits<ll>::max();
    std::array<int,6>d5{5,5,5,5,5,5};
    for(int m=0;m<=6;m++) for(const auto&c:confs[m])
        floor5=std::min(floor5,det_bareiss(make_gram(d5,c)));
    if(floor5!=10800) return 10;

    // Range>=5 already gives diagonal defect >=77, so only minima 1..4 remain.
    std::vector<std::pair<std::array<int,6>,int>> diags;
    std::array<int,6>d{};
    for(int minimum=1;minimum<=4;minimum++){
        d[0]=minimum;
        gen_diag(1,minimum,minimum,d,diags);
    }

    long long checked=0,hits=0;
    int best_delta=100000;
    long long best_count=0;
    for(const auto&item:diags){
        const auto&dg=item.first;
        int D=item.second;
        int maxM=std::min(6,(76-D)/12);
        for(int m=0;m<=maxM;m++){
            int delta=D+12*m;
            if(delta>=77) continue;
            for(const auto&c:confs[m]){
                checked++;
                if(det_bareiss(make_gram(dg,c))==361){
                    hits++;
                    if(delta<best_delta){best_delta=delta;best_count=0;}
                    if(delta==best_delta){
                        best_count++;
                        if(!canonical_false_type(dg,c)) return 20;
                    }
                }
            }
        }
    }

    if(checked!=5926168LL) return 30;
    if(hits!=64 || best_delta!=72 || best_count!=64) return 31;
    if(legendre_has_nonzero_self_glue_mod19()!=0) return 40;

    // Exact equality transport with Delta=77.
    Matrix6 A{{
        {{ 1,-1,-1, 0, 0, 1}},
        {{ 1, 0, 0, 0, 1,-1}},
        {{ 1, 1, 0, 0,-1, 0}},
        {{ 0,-1, 1,-1, 0, 0}},
        {{ 0, 0,-1,-1,-1,-1}},
        {{ 0, 0, 0,-1, 0, 1}}
    }};
    if(std::llabs(det_bareiss(A))!=19) return 50;
    Matrix6 G=gram_of(A);
    if(det_bareiss(G)!=361 || delta6(G)!=77) return 51;

    std::cout << "EXACT_CERTIFICATE_PASSED\n"
              << "min_det_5I_plus_E=" << floor5 << "\n"
              << "low_window_checked=" << checked << "\n"
              << "det361_abstract_candidates_below77=" << hits << "\n"
              << "all_abstract_candidates_delta=" << best_delta << "\n"
              << "all_abstract_candidates_type=H19_plus_H19\n"
              << "same_phase_glue=OBSTRUCTED_MOD_19\n"
              << "explicit_det19_delta=77\n"
              << "conclusion=min_{|det A|=19} Delta_6(A)=77\n";
    return 0;
}
