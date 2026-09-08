// Exact result-specific certificate for min_{|det A|=41} Delta_6(A)=56.
//
// It verifies the p=13 centered-shape shift prediction at k=1, scans the full
// symmetric integral Gram window forced by Delta_6<56, and checks the explicit
// determinant-41 integer lift. No floating point is used.

#include <array>
#include <cstdint>
#include <iostream>
#include <limits>
#include <utility>
#include <vector>
using ll=long long;
using Mat=std::array<std::array<ll,6>,6>;

static const std::array<std::pair<int,int>,15> EDGES=[]{
    std::array<std::pair<int,int>,15> e{}; int k=0;
    for(int i=0;i<6;i++) for(int j=i+1;j<6;j++) e[k++]={i,j};
    return e;
}();

struct Conf{std::array<int8_t,15>v{};int m=0;};
std::array<std::vector<Conf>,5> confs;

ll detb(Mat a){
    ll sign=1,prev=1;
    for(int k=0;k<5;k++){
        if(a[k][k]==0){int sw=-1;for(int r=k+1;r<6;r++)if(a[r][k]){sw=r;break;}if(sw<0)return 0;std::swap(a[k],a[sw]);sign=-sign;}
        ll piv=a[k][k];
        for(int i=k+1;i<6;i++)for(int j=k+1;j<6;j++){
            __int128 n=(__int128)a[i][j]*piv-(__int128)a[i][k]*a[k][j];
            if(k)n/=prev; a[i][j]=(ll)n;
        }
        prev=piv; for(int i=k+1;i<6;i++)a[i][k]=0;
    }
    return sign*a[5][5];
}

void genconf(int i,int m,std::array<int8_t,15>&v){
    if(m>4)return;
    if(i==15){confs[m].push_back({v,m});return;}
    v[i]=0;genconf(i+1,m,v);
    v[i]=-1;genconf(i+1,m+1,v);v[i]=1;genconf(i+1,m+1,v);
    v[i]=-2;genconf(i+1,m+4,v);v[i]=2;genconf(i+1,m+4,v);
    v[i]=0;
}
int Dd(const std::array<int,6>&d){int s=0;for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){int x=d[i]-d[j];s+=x*x;}return s;}
Mat mk(const std::array<int,6>&d,const Conf&c){Mat g{};for(int i=0;i<6;i++)g[i][i]=d[i];for(int k=0;k<15;k++)if(c.v[k]){auto [i,j]=EDGES[k];g[i][j]=g[j][i]=c.v[k];}return g;}
std::vector<std::pair<std::array<int,6>,int>> diags;
void gd(int pos,int last,int mn,std::array<int,6>&d){if(pos==6){int D=Dd(d);if(D<56)diags.push_back({d,D});return;}for(int x=last;x<=mn+4;x++){d[pos]=x;gd(pos+1,x,mn,d);}}
Mat gram(const Mat&A){Mat g{};for(int i=0;i<6;i++)for(int j=0;j<6;j++){ll s=0;for(int k=0;k<6;k++)s+=A[k][i]*A[k][j];g[i][j]=s;}return g;}
ll delta(const Mat&g){ll t=0,s=0;for(int i=0;i<6;i++)t+=g[i][i];for(int i=0;i<6;i++)for(int j=0;j<6;j++)s+=g[i][j]*g[j][i];return 6*s-t*t;}

int main(){
    std::array<int8_t,15>v{};genconf(0,0,v);

    // Delta<56 => M<=4. If every diagonal >=4, determinant is minimized at
    // 4I+E over this E-family. Exact scan gives 2960 > 41^2.
    std::array<int,6>d4{4,4,4,4,4,4}; ll floor4=std::numeric_limits<ll>::max();
    for(int m=0;m<=4;m++)for(const auto&c:confs[m])floor4=std::min(floor4,detb(mk(d4,c)));
    if(floor4!=2960) return 10;

    // Range>=5 already gives D>=77>56. Thus minima 1,2,3 suffice.
    std::array<int,6>d{};for(int mn=1;mn<=3;mn++){d[0]=mn;gd(1,mn,mn,d);}
    long long checked=0,hits=0;
    for(const auto&it:diags){auto dg=it.first;int D=it.second;int mm=std::min(4,(55-D)/12);for(int m=0;m<=mm;m++){int del=D+12*m;if(del>=56)continue;for(const auto&c:confs[m]){checked++;if(detb(mk(dg,c))==1681)hits++;}}}
    if(checked!=323337LL || hits!=0) return 20;

    // Exact p=13 centered-shape shift lift at k=1.
    Mat A{{
        {{ 1,-1, 1,-1, 0, 0}},
        {{ 1, 0,-1, 0, 1,-1}},
        {{ 1, 0, 0, 1,-1, 1}},
        {{ 0,-1,-1, 0,-1, 0}},
        {{ 0,-1, 0, 0, 1, 1}},
        {{ 0,-1, 1, 1, 0,-1}}
    }};
    if(std::llabs(detb(A))!=41) return 30;
    Mat G=gram(A);
    if(detb(G)!=1681 || delta(G)!=56) return 31;

    // Check exact target Gram (H13+I) (+) (H13+I).
    Mat target{};
    ll H[3][3]={{3,-1,0},{-1,4,-1},{0,-1,4}};
    for(int b=0;b<2;b++)for(int i=0;i<3;i++)for(int j=0;j<3;j++)target[3*b+i][3*b+j]=H[i][j];
    if(G!=target) return 32;

    std::cout<<"EXACT_CERTIFICATE_PASSED\n"
             <<"min_det_4I_plus_E="<<floor4<<"\n"
             <<"low_window_checked="<<checked<<"\n"
             <<"det1681_candidates_below56="<<hits<<"\n"
             <<"explicit_det41_delta=56\n"
             <<"shape_relation=G41=(H13+I)_plus_(H13+I)\n"
             <<"conclusion=min_{|det A|=41} Delta_6(A)=56\n";
    return 0;
}
