//문제: 19941
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const [a, k] = input[0].split(" ").map(Number);
  let answer = 0;
  const arr = input[1].split("");
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "H") {
      const arr2 =
        i >= k ? arr.slice(i - k, i + k + 1) : arr.slice(0, i + k + 1);
      if (arr2.includes("P")) {
        answer++;
        i >= k
          ? (arr[i + arr2.indexOf("P") - k] = ".")
          : (arr[arr2.indexOf("P") + i] = ".");
      }
    }
  }
  console.log(answer);
}
