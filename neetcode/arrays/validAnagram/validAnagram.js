class ValidAnagram{
    constructor(s, t){
        this.s = s;
        this.t = t;
    }

    isAnagram(){
        if(this.s.length !== this.t.length) return false;

        let sMap = new Map();
        let tMap = new Map();

        for(const char in this.s){
            sMap.set(this.s[char], (sMap.get(this.s[char]) || 0) + 1);
            tMap.set(this.t[char], (tMap.get(this.t[char]) || 0) + 1);
        }

        for(const char of sMap.keys()){
            if(sMap.get(char) !== tMap.get(char)) return false;
        }

        console.log(sMap)
        console.log(tMap)
        return true;
    }
}

let validAnagram = new ValidAnagram("anagram", "nagaram");

console.log(validAnagram.isAnagram());