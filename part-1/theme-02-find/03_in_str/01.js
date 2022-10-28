let { readFileSync } = require("fs");

const get_pos_niave = (txt, word) => {
    for (let pos=0; pos<txt.length; pos++) {
        let b = true;
        for (let i=0; i<word.length; i++) {
            if (word[i] !== txt[pos+i]) {
                b = false;
                break;
            }
        }
        if (b === true) { return pos; } 
    }
    return -1;
}

const get_pos_equel = (txt, word) => {
    let lw = word.length;
    for (let pos=0; pos<txt.length; pos++) {
        if (word === txt.slice(pos, pos+lw)) {
            return pos;
        }
    }
    return -1;
}

const get_pos_bm = (txt, word) => {
    let dct = get_dict(word); // { 'к': 3, 'р': 1, 'а': 2 }
    return find_pos_bm(txt, word, dct);
}

console.clear();

let txt = readFileSync("./draft.txt", "utf8");
let word = "кора";

console.time("find");
console.log(get_pos_niave(txt, word));
console.timeEnd("find");

console.time("find");
console.log(get_pos_equel(txt, word));
console.timeEnd("find");

// Алгоритм Бойера-Мура
console.time("find");
console.log(get_pos_niave(txt, word));
console.timeEnd("find");

console.time("find");
console.log(txt.indexOf(word));
console.timeEnd("find");
