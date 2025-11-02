function reverseWords(s) {
    const result = s.split(' ').map(str => str.split('').reverse().join('')).join(' ');
    return result;
};

// Teste de performance
const text = "Let's take LeetCode contest ".repeat(2000);

console.time("reverseWords performance");
reverseWords(text);
console.timeEnd("reverseWords performance");