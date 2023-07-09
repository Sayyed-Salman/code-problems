
class ContainsDuplicate{
    constructor(list){
        this.arr = list;
    }

    add(val){
        this.arr.push(val);
    }

    contains(val){
        return this.arr.includes(val);
    }

    checkDuplicate(){
        let hashset = new Set();
        this.arr.forEach(element => {
            if(hashset.has(element)){
                return true;
            }
            hashset.add(element);
        })
        return false;
    }

    containsDuplicateForOf(){
        let hashset = new Set()
        let List = this.arr

        for(const element of List){
            if(hashset.has(element)){
                return true;
            }
            hashset.add(element);
        }
        return false;
    }
}

let containsDuplicate = new ContainsDuplicate([1,2,3,4,5,6,7,8,9,10,1]);

console.log("contains");
console.log(containsDuplicate.contains(1));

console.log("checkDuplicate");
console.log(containsDuplicate.checkDuplicate());

console.log("containsDuplicateForOf");
console.log(containsDuplicate.containsDuplicateForOf());

