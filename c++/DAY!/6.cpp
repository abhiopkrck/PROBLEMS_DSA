#include <iostream>
using namespace std;

int main(){
    string name[]={"ABHIAHWK","abhijjeet","Shraddha","ankita","samiksha"};
    int arr[]={12,13,14,15,16};
    int n=sizeof(name)/sizeof(name[0]);
    int n2=sizeof(arr)/sizeof(arr[0]);
    string reverse_string[n];
    int reverse_int[n];

    for(int i=0;i<n;i++){
        // string temp=arr[i];
        // arr[i]=arr[n-1-i];
        // arr[n-1-i]=temp;
        reverse_string[i]=name[n-1-i];
        reverse_int[i]=arr[n-1-i];
    }
    for(int i=0;i<n;i++){
        cout<<reverse_int[i]<<" ";
    }
    for(int i=0;i<n;i++){
        cout<<reverse_string[i]<<" ";
    }
    return 0;
}