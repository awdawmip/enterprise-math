#include <gmpxx.h>
#include <array>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstdint>
using namespace std;
constexpr int N=12, B=4826809,CAP=2331;
using Vec=array<long,N>;
mpz_class L[N], T[N], Q, M[N][N], step[N];
Vec C[12][13], z,c,acc;
vector<int> p,r; int pr; long radius;
mpz_class bound;
uint64_t raw=0,over=0,common=0,nodes=0,leaves=0;
void descend(int i,const mpz_class &spent){
 if(i<0){++leaves;cout<<"W "<<pr;for(int a:r)cout<<' '<<a;for(long a:z)cout<<' '<<a;cout<<'\n';return;}
 ++nodes; mpz_class h=L[i]*c[i];for(int j=i+1;j<N;j++)if(z[j]>=0)mpz_addmul_ui(h.get_mpz_t(),M[i][j].get_mpz_t(),z[j]);else mpz_submul_ui(h.get_mpz_t(),M[i][j].get_mpz_t(),-z[j]);
 mpz_class near;
 mpz_class minus=-h;mpz_fdiv_q(near.get_mpz_t(),minus.get_mpz_t(),step[i].get_mpz_t());
 long ni=near.get_si();
 for(long n=ni;n<=ni+1;n++){mpz_class x=h+step[i]*n;mpz_class e=spent+T[i]*x*x;if(e<=bound){z[i]=c[i]+B*n;descend(i-1,e);}}
 z[i]=c[i];
}
void roster(int i,int sum){
 if(i==(int)p.size()){
  long cn=1690+13*sum-p.size();
  for(pr=1;pr<=12;pr++){++raw;bool co=false;for(int j=0;j<(int)p.size()&&p[j]==1;j++)co|=r[j]==pr;common+=co;if(cn>CAP){++over;continue;}
   long cp=168+13*pr;radius=(CAP-cp)*(CAP-cp)+(CAP-cn)*(CAP-cn);bound=Q*radius;
   for(int j=0;j<N;j++){long x=(acc[j]-C[1][pr][j])%B;c[j]=x<0?x+B:x;z[j]=c[j];}descend(N-1,mpz_class(0));
  }return;
 }
 int lo=i>0&&p[i]==p[i-1]?r[i-1]:1;
 for(int a=lo;a<=12;a++){r[i]=a;for(int j=0;j<N;j++)acc[j]+=C[p[i]][a][j];roster(i+1,sum+a);for(int j=0;j<N;j++)acc[j]-=C[p[i]][a][j];}
}
int main(int argc,char**argv){ifstream f(argv[1]);f>>Q;for(int i=0;i<N;i++){f>>L[i]>>T[i];step[i]=B*L[i];for(int j=i+1;j<N;j++)f>>M[i][j];}for(int q=1;q<12;q++)for(int a=1;a<=12;a++)for(int j=0;j<N;j++)f>>C[q][a][j];if(!f)return 2;for(int i=2;i<argc;i++)p.push_back(stoi(argv[i]));r.resize(p.size());roster(0,0);cout<<"R "<<raw<<' '<<over<<' '<<common<<' '<<nodes<<' '<<leaves<<'\n';}
