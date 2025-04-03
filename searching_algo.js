// JavaScript: Linear Search, Binary Search
function linearSearch(arr, target) {
    for(let i = 0; i < arr.length; i++) 
        if (arr[i] == target) 
            return i; // No curly braces (style issue)
    return -1;
}

function binarySearch(arr, target) {
    let left=0, right=arr.length-1;  // No spaces around '=' (style issue)
    while(left <= right) {
        let mid = Math.floor((left + right) / 2);
        if(arr[mid] == target) return mid;
        else if(arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

console.log(linearSearch([1,2,3,4], 3));
console.log(binarySearch([1,2,3,4], 3));
