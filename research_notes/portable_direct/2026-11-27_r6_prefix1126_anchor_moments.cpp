#include <gmpxx.h>
#include <vector>
#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;
using Z=mpz_class;
vector<Z> moments(vector<int> av,vector<int> r,int N){
 int A=0;for(size_t i=0;i<r.size();i++) A+=av[i]*r[i];
 vector<vector<int>> st(1);for(int n:r){vector<vector<int>> nx;for(auto a:st)for(int j=0;j<=n;j++){auto b=a;b.push_back(j);nx.push_back(b);}st=nx;}
 auto sm=[](const vector<int>&v){int s=0;for(int x:v)s+=x;return s;}; stable_sort(st.begin(),st.end(),[&](auto&a,auto&b){return sm(a)>sm(b);});
 int sz=st.size();vector<int> ah(sz);vector<vector<pair<int,int>>> up(sz),dn(sz);for(int i=0;i<sz;i++)for(size_t k=0;k<r.size();k++){ah[i]+=av[k]*st[i][k];auto h=st[i];if(h[k]<r[k]){h[k]++;up[i].push_back({r[k]-st[i][k],int(find(st.begin(),st.end(),h)-st.begin())});}h=st[i];if(h[k]){h[k]--;dn[i].push_back({st[i][k],int(find(st.begin(),st.end(),h)-st.begin())});}}
 vector<Z> prev(sz),cur(sz),out;mpz_fac_ui(prev.back().get_mpz_t(),A);for(size_t i=0;i<r.size();i++){Z f;mpz_fac_ui(f.get_mpz_t(),av[i]);for(int j=0;j<r[i];j++)prev.back()/=f;}out.push_back(prev.back());
 for(int j=1;j<=N;j++){long jj=long(j)*(j+A);for(int i=0;i<sz;i++){Z v=0,w=0;for(auto[c,p]:up[i])v+=c*cur[p];for(auto[c,p]:dn[i])w+=c*prev[p];v+=jj*w;assert(mpz_divisible_ui_p(v.get_mpz_t(),j+ah[i]));mpz_divexact_ui(cur[i].get_mpz_t(),v.get_mpz_t(),j+ah[i]);}out.push_back(cur.back());swap(cur,prev);}return out;
}
Z beta(const vector<Z>&m,int k,int q){Z acc=0,c=1,v;for(int j=0;j<=k;j++){v=m[j];if(q){v*=q;assert(mpz_divisible_ui_p(v.get_mpz_t(),j+q+1));mpz_divexact_ui(v.get_mpz_t(),v.get_mpz_t(),j+q+1);}acc*=36;if(j%2)acc-=c*v;else acc+=c*v;if(j<k){c*=k-j;assert(mpz_divisible_ui_p(c.get_mpz_t(),j+1));mpz_divexact_ui(c.get_mpz_t(),c.get_mpz_t(),j+1);}}Z den,H;mpz_ui_pow_ui(den.get_mpz_t(),36,k);den*=q?q:1;mpz_ui_pow_ui(H.get_mpz_t(),10,120);acc*=H;mpz_fdiv_q(v.get_mpz_t(),acc.get_mpz_t(),den.get_mpz_t());return v;}
int main(int argc,char**argv){assert(argc>=2);int k0=atoi(argv[1]),kmax=atoi(argv[argc-1]);auto m0=moments({0},{6},kmax);for(int j=1;j<argc;j++)cout<<beta(m0,atoi(argv[j]),0)<<endl;auto m1=moments({0,1},{4,2},k0);cout<<beta(m1,k0,1)<<endl;auto m2=moments({0,1,2},{4,1,1},k0);cout<<beta(m2,k0,2)<<endl;}
