#include <bits/stdc++.h>
using namespace std;

int main()
{
	int arr[10];
	int j;
	int key;
	cout << "Enter the values in the array !";
	for (int i=0;i<10;i++)
	{
		cin >> arr[i];
	}
	cout << "Enter your key !";
	cin >> key;
	for (int i=0;i<10;i++)
	{
		if (key==arr[i])
		{
           j=i;
           break;
		}
		else
		{
			j=50;
		}
	}
	if (j==50)
	{
		cout << "Your Key is not Found!";
	}
	else
	{
		cout << "Your key" << key <<" is found in place "<<j+1;
	}
	return 0;
}