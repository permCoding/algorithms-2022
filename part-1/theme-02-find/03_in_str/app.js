let { readFileSync } = require("fs");
let { gpn, gpe, gps, gpb } = require("./module");

console.clear();

let txt = readFileSync("./txt/book.txt", "utf8");
let word = "Уникальными талантами не отмечен - верно?";

console.time("find");
console.log(gpn(txt, word));
console.timeEnd("find");

console.time("find");
console.log(gpe(txt, word));
console.timeEnd("find");

console.time("find");
console.log(gps(txt, word)); // Алгоритм Бойера-Мура
console.timeEnd("find");

console.time("find");
console.log(gpb(txt, word)); // Алгоритм Бойера-Мура
console.timeEnd("find");

console.time("find");
console.log(txt.indexOf(word));
console.timeEnd("find");
