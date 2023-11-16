// # EvenPairsOnCycle

// # You are given N numbers on a circle, described by an array A. Find the maximum number of neighbouring pairs whose sums are even.
// # One element can belong to only one pair.

// # Write a function:

// # def solution(A)

// # that, given an array A consisting of N integers, returns the maximum number of neighbouring pairs whose sums are even.

// # Examples:

// # 1. Given A = [4, 2, 5, 8, 7, 3, 7], the function should return 2. We can create two pairs with even sums: (A[0], A[1]) and (A[4], A[5]). Another way to choose two pairs is: (A[0], A[1]) and (A[5], A[6]).

// # Picture illustrates the first example.

// # 2. Given A = [14, 21, 16, 35, 22], the function should return 1. There is only one qualifying pair:
// # (A[0], A[4]).

// # Picture illustrates the second example.

// # 3. Given A = [5, 5, 5, 5, 5, 5], the function should return 3. We can create three pairs: (A[0], A[5]), (A[1], A[2]) and (A[3], A[4]).

// # Picture illustrates the third example.

// # Write an efficient algorithm for the following assumptions:

// # N is an integer within the range [1..100,000];
// # each element of array A is an integer within the range [0..1,000,000,000].

// # def solution(A):
// #     even_count = 0
// #     # odd_count = 0


// #     if len(A) % 2 ==0:
// #         pairs = [A[i:i+2] for i in range(0, len(A), 2)]
// #         print(pairs)
    
// #     for pair in pairs:
// #         if sum(pair) % 2 == 0:
// #             even_count +=1
// #             print(even_count)


//     # for num in A:
//     #     if num % 2 == 0:
//     #         even_count += 1
//     #     else:
//     #         odd_count += 1

//     # max_pairs = min(even_count, odd_count)
    
//     # if len(A) % 2 == 1 or max_pairs== len(A):
//     #     max_pairs -= 1

//     # return max_pairs

// # print(solution([4, 2, 5, 8, 7, 3, 7]))  # Output: 2
// # print(solution([14, 21, 16, 35, 22]))    # Output: 1
// # print(solution([5, 5, 5, 5, 5, 5]))      # Output: 3

// def solution(A):
//     n = len(A)
//     i = 1
//     while i< n:
//         value 


// solution([5, 5, 5, 5, 5, 5])


// function solution(A) {
//     const n = A.length;

//     // Count the occurrences of even and odd numbers
//     let evenCount = 0;

//     for (let i = 0; i < n; i += 2) {
//         if ((A[i] + A[i + 1]) % 2 === 0) {
//             evenCount++;
//         }
//     }
   
//     return evenCount;
// }

function solution(A) {
    const n = A.length;

    // Count the occurrences of even and odd numbers
    let evenCount = 0;

    for (let i = 0; i < n; i += 2) {
        if ((A[i] + A[i + 1]) % 2 === 0) {
            evenCount++;
        }
    }
    if ((A[0]+A[1])%2!=0 && (A[0]+A[n-1])%2=== 0) {
        evenCount++
    }
    return evenCount;
}

console.log(solution([4, 2, 5, 8, 7, 3, 7]))  // Output: 2
console.log(solution([14, 21, 16, 35, 22]))    // Output: 1
console.log(solution([5, 5, 5, 5, 5, 5]))      // Output: 3
