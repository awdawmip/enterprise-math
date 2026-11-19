#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;
constexpr int L=262145, H=524287, C=131072, K=21, K2=23, J=18, MAXT=46;
constexpr int MAXD=MAXT*H;
int main(){
 // An independent method: construct all divisor matches d=t*b, b in Q.
 vector<int> head(MAXD+1,-1), next; vector<int> b_index;
 next.reserve(MAXT*C);b_index.reserve(MAXT*C);
 for(int bi=0;bi<C;bi++){
    int b=L+2*bi;
    for(int t=1;t<=MAXT;t++){
      int d=t*b;
      int id=(int)next.size();
      next.push_back(head[d]);b_index.push_back(bi);head[d]=id;
    }
 }
 array<u64,C/64> row21{},row23{};
 vector<u64> intersection;
 u64 unique21=0,unique23=0,ninter=0,raw21=0,raw23=0;
 int first_exception=0;
 for(int ai=0;ai<C;ai++){
   int a=L+2*ai;
   row21.fill(0);row23.fill(0);
   for(int ii=0;ii<=J;ii++)for(int jj=0;jj<=J;jj++){
      int z=(1<<ii),x=(1<<jj);
      int d21=((K*a)^x)-z;
      int d23=((K2*a)^x)-z;
      if(d21>0&&d21<=MAXD)for(int pos=head[d21];pos>=0;pos=next[pos]){
        int bi=b_index[pos];row21[bi>>6]|=(1ULL<<(bi&63));raw21++;
      }
      if(d23>0&&d23<=MAXD)for(int pos=head[d23];pos>=0;pos=next[pos]){
        int bi=b_index[pos];row23[bi>>6]|=(1ULL<<(bi&63));raw23++;
      }
   }
   for(int w=0;w<C/64;w++){
      unique21+=__builtin_popcountll(row21[w]);
      unique23+=__builtin_popcountll(row23[w]);
      u64 overlap=row21[w]&row23[w];
      ninter+=__builtin_popcountll(overlap);
      while(overlap){
        int bit=__builtin_ctzll(overlap),bi=w*64+bit;
        intersection.push_back((u64)ai*C+bi);
        overlap&=overlap-1;
      }
   }
 }
 ofstream out("PREFIX948_W21_W23_DIRECT_IDS.bin",ios::binary);
 for(u64 id:intersection)out.write(reinterpret_cast<char*>(&id),8);
 out.close();
 cout<<"{\"schema\":\"PREFIX948_R6_DIRECT_DIVISOR_ROWS_V1\",\"raw21\":"<<raw21<<",\"raw23\":"<<raw23<<",\"unique21\":"<<unique21<<",\"unique23\":"<<unique23<<",\"overlap\":"<<ninter<<",\"independent_computation\":true}"<<endl;
}
