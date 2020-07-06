import java.util.*;

public class Inversions {

    private static long getNumberOfInversions(int[] a, int[] b, int left, int right) {
        long numberOfInversions = 0;
        if (right <= left + 1) {
            b[left]=a[left];
            return numberOfInversions;
        }
if(right==left+2){if(a[left]>a[left+1]){b[left]=a[right-1];b[right-1]=a[left];return 1;}
b[left]=a[left];b[right-1]=a[right-1];return 0;}
        int ave = (left + right) / 2;
       
        //write your code here
numberOfInversions += getNumberOfInversions(a, b, left, ave);
        numberOfInversions += getNumberOfInversions(a, b, ave, right);
int j=left,k=ave,i=left;
while(j<ave&&k<right)
{if(b[j]<=b[k])
{a[i]=b[j];j++;}
else{a[i]=b[k];k++;
numberOfInversions+=(ave-j);}i++;}
if(j<ave){for(;i<right;i++){a[i]=b[j];j++;}k=right;}
for(i=left;i<k;i++)
b[i]=a[i];
 

        return numberOfInversions;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = scanner.nextInt();
        }
        int[] b = new int[n];
        System.out.println(getNumberOfInversions(a, b, 0, a.length));
    }
}


