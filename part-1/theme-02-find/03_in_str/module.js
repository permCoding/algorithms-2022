const get_pos_niave = (txt, word) => {
    let lw = word.length;
    for (let pos=0; pos<txt.length-lw; pos++) {
        let b = true;
        for (let i=0; i<lw; i++) {
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

let get_dict_set = (txt, word) => {
    let st = new Set(txt);
    let dct = {};
    let lw = word.length;
    for (let smb of st) { dct[smb] = lw; }
    for (let i=0; i<lw-1; i++) {
        dct[word[i]] = lw-1 - i; // qwerty  для e => i=2 lw=6 sm=3
    }
    return dct;
}

let get_dict_for = (txt, word) => {
    let dct = {};
    let lw = word.length;
    for (let smb of txt) { dct[smb] = lw; }
    for (let i=0; i<lw-1; i++) {
        dct[word[i]] = lw-1 - i; // qwerty  для e => i=2 lw=6 sm=3
    }
    return dct;
}

let find_pos_bm_set = (txt, word, dct) => {
    let lw = word.length;
    let pos=0;
    while (pos < txt.length-lw) {
        let b = true;
        for (let i=0; i<lw; i++) {
            if (word[i] !== txt[pos+i]) {
                b = false;
                pos += dct[txt[pos+lw-1]];
                break;
            }
        }
        if (b === true) { return pos; } 
    }
    return -1;
}

const get_pos_bm_set = (txt, word) => {
    let dct = get_dict_set(txt, word); // { 'к': 3, 'р': 1, 'а': 2, '#': 4, '&': 4 }
    // let dct = get_dict_for(txt, word);
    return find_pos_bm_set(txt, word, dct);
}

let get_dict = (word) => {
    let dct = {};
    let lw = word.length;
    for (let i=0; i<lw-1; i++) {
        dct[word[i]] = lw-1 - i; // qwerty  для e => i=2 lw=6 sm=3
    }
    return dct;
}

let find_pos_bm = (txt, word, dct) => {
    let lw = word.length, pos=0;
    while (pos < txt.length-lw) {
        if (word === txt.slice(pos,pos+lw)) { return pos; }
        let last = txt[pos+lw-1];
        pos += (last in dct)? dct[last]: lw;        
    }
    return -1;
}

const get_pos_bm = (txt, word) => {
    let dct = get_dict(word); // { 'к': 3, 'р': 1, 'а': 2 }
    return find_pos_bm(txt, word, dct);
}

module.exports = {
    gpn: get_pos_niave,
    gpe: get_pos_equel,
    gps: get_pos_bm_set,
    gpb: get_pos_bm,
}
