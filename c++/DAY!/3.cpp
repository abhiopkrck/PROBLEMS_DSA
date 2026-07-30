#include <iostream>
using namespace std;

int main(){
    int nums[]={189,22,33,44,55,66,77,88,89};
    int n=sizeof(nums) /sizeof(nums[0]);
    int lowest=nums[0];
    for(int i=0;i<n;i++){
        if(nums[i]<lowest){
            lowest=nums[i];
        }
    }
    cout<<"lowest:"<<lowest;
    return 0;
}