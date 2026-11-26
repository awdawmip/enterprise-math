#include <gmpxx.h>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <numeric>
using namespace std;
using Z=mpz_class;
constexpr int N=12,CAP=2331;
Z B,Q,L[N],T[N],MM[N][N],step[N],bound;
long C[14][13][N],c[N],z[N],b;
long long nodes=0,leaves=0,actual=0,common=0,representatives=0;
vector<int> pp,np,pl,nl;
void dfs(int i,const Z& spent){
 if(i<0){++leaves;cout<<"W";for(int t:pl)cout<<' '<<t;for(int t:nl)cout<<' '<<t;for(long v:z)cout<<' '<<v;cout<<'\n';return;}
 ++nodes;Z h=L[i]*c[i];for(int j=i+1;j<N;++j)h+=MM[i][j]*z[j];
 Z near,nh=-h;mpz_fdiv_q(near.get_mpz_t(),nh.get_mpz_t(),step[i].get_mpz_t());
 Z r=h+step[i]*near;
 for(int k=0;k<2;++k){Z e=spent+T[i]*r*r;if(e<=bound){Z zz=c[i]+B*(near+k);if(!zz.fits_slong_p())abort();z[i]=zz.get_si();dfs(i-1,e);}r+=step[i];}
 z[i]=c[i];
}
struct Roster{vector<int> labels;long mass;vector<long> vec;};
vector<Roster> pos,neg;
void enumerate(const vector<int>& pat,vector<int>& lab,int i,int sum,int q,vector<Roster>& out){
 int m=pat.size();int limit=(CAP-169*q+m)/13;
 if(i==m){long mass=169*q+13*sum-m;if(mass>CAP)abort();vector<long> vec(N);for(int k=0;k<m;++k)for(int j=0;j<N;++j)vec[j]+=C[pat[k]][lab[k]][j];out.push_back({lab,mass,vec});return;}
 int lo=(i&&pat[i]==pat[i-1])?lab[i-1]:1,hi=min(12,limit-sum-(m-i-1));for(int r=lo;r<=hi;++r){lab[i]=r;enumerate(pat,lab,i+1,sum+r,q,out);}
}
int main(int argc,char**argv){ifstream in(argv[1]);in>>B>>Q;b=B.get_si();for(auto& x:L)in>>x;for(auto& x:T)in>>x;for(int i=0;i<N;++i){step[i]=B*L[i];for(int j=i+1;j<N;++j)in>>MM[i][j];}for(int a=1;a<=13;++a)for(int t=1;t<=12;++t)for(long& x:C[a][t])in>>x;if(!in)abort();long long lo=atoll(argv[2]),hi=atoll(argv[3]);bool side=false;for(int k=4;k<argc;++k){if(string(argv[k])=="--"){side=true;continue;}(side?np:pp).push_back(atoi(argv[k]));}pl.resize(pp.size());nl.resize(np.size());enumerate(pp,pl,0,0,accumulate(pp.begin(),pp.end(),0),pos);enumerate(np,nl,0,0,accumulate(np.begin(),np.end(),0),neg);
 if(lo<0||hi<lo||hi>(long long)neg.size())abort();for(long long ix=lo;ix<hi;++ix){const auto& n=neg[ix];nl=n.labels;for(const auto& p:pos){pl=p.labels;++actual;bool shared=false, nonminimal=false;for(size_t i=0;i<pp.size();++i)for(size_t j=0;j<np.size();++j)if(pp[i]==np[j]&&pl[i]==nl[j]){shared=true;if(pl[i]!=1)nonminimal=true;}common+=shared;if(nonminimal)continue;++representatives;bound=Q*((CAP-p.mass)*(CAP-p.mass)+(CAP-n.mass)*(CAP-n.mass));for(int j=0;j<N;++j){c[j]=(n.vec[j]-p.vec[j])%b;if(c[j]<0)c[j]+=b;z[j]=c[j];}dfs(N-1,Z(0));}}
 cout<<"R "<<pos.size()<<' '<<(hi-lo)<<' '<<actual<<' '<<common<<' '<<nodes<<' '<<leaves<<' '<<representatives<<'\n';
}
