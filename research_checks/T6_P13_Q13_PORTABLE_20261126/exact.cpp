#include <gmpxx.h>
#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdlib>
using namespace std;
using Z=mpz_class;
constexpr int N=12, CAP=2331;
Z B,Q,L[N],T[N],MM[N][N],step[N];
long C[14][13][N],c[N],z[N];
long b;
long long nodes=0,leaves=0,actual=0,cf=0;
vector<int> pat,labels;
int s;
Z bound;
void dfs(int i,const Z& spent){
 if(i<0){++leaves; cout<<"W "<<s;for(int r:labels)cout<<' '<<r;for(long v:z)cout<<' '<<v;cout<<'\n';return;}
 ++nodes; Z h=L[i]*c[i];for(int j=i+1;j<N;++j)h+=MM[i][j]*z[j];
 Z near,nh=-h; mpz_fdiv_q(near.get_mpz_t(),nh.get_mpz_t(),step[i].get_mpz_t());
 Z r=h+step[i]*near; long n=near.get_si(); if(!near.fits_slong_p())abort();
 for(int k=0;k<2;++k){Z e=spent+T[i]*r*r;if(e<=bound){z[i]=c[i]+b*(n+k);dfs(i-1,e);}r+=step[i];}
 z[i]=c[i];
}
void enumerate(int i,int sum,int limit){
 int m=pat.size();if(i==m){
  long cn=169*12+13*sum-m; if(cn>CAP)abort();
  long neg[N]={};bool common[13]={};for(int k=0;k<m;++k){for(int j=0;j<N;++j)neg[j]+=C[pat[k]][labels[k]][j];if(pat[k]==1)common[labels[k]]=true;}
  for(s=1;s<=12;++s){++actual;cf+=common[s];long cp=169+13*s-1;bound=Q*((CAP-cp)*(CAP-cp)+(CAP-cn)*(CAP-cn));for(int j=0;j<N;++j){c[j]=(neg[j]-C[1][s][j])%b;if(c[j]<0)c[j]+=b;z[j]=c[j];}dfs(11,Z(0));}return;
 }
 int lo=(i&&pat[i]==pat[i-1])?labels[i-1]:1;int hi=min(12,limit-sum-(m-i-1));for(int r=lo;r<=hi;++r){labels[i]=r;enumerate(i+1,sum+r,limit);}
}
int main(int argc,char**argv){ifstream in(argv[1]);in>>B>>Q;b=B.get_si();for(auto &x:L)in>>x;for(auto &x:T)in>>x;for(int i=0;i<N;++i){step[i]=B*L[i];for(int j=i+1;j<N;++j)in>>MM[i][j];}for(int a=1;a<=13;++a)for(int t=1;t<=12;++t)for(long &x:C[a][t])in>>x;if(!in)abort();for(int k=2;k<argc;++k)pat.push_back(atoi(argv[k]));labels.resize(pat.size());enumerate(0,0,(CAP-169*12+pat.size())/13);cout<<"R "<<actual<<' '<<cf<<' '<<nodes<<' '<<leaves<<'\n';}
