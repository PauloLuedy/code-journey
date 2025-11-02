function reverseWords(s) {
  const chars = s.split(""); 
  let start = 0;

  for (let end = 0; end <= chars.length; end++) {
    if (end === chars.length || chars[end] === " ") {
      reverse(chars, start, end - 1);
      start = end + 1;
    }
  }

  return chars.join("");
}

function reverse(arr, left, right) {
  while (left < right) {
    const temp = arr[left];
    arr[left] = arr[right];
    arr[right] = temp;
    left++;
    right--;
  }
}

// Teste de performance
const text = "Let's take LeetCode contest ".repeat(2000).trim();

console.time("reverseWords performance");
reverseWords(text);
console.timeEnd("reverseWords performance");
