var uniqueInOrder=function(iterable){
    return [...iterable].filter((a, i) => a !== iterable[i-1])
}

//test cases
/*
const chai = require("chai");
const assert = chai.assert;
chai.config.truncateThreshold=0;  

describe("lets test it", function(){
  it("should work with empty array", function(){
    assert.deepEqual(uniqueInOrder(''),[]);
  });
  it("should work with one element", function(){
    assert.deepEqual(uniqueInOrder('A'),['A']);
  });
  it("should reduce duplicates", function(){
    assert.deepEqual(uniqueInOrder('AA'),['A']);
    assert.deepEqual(uniqueInOrder('AAAABBBCCDAABBB'),['A', 'B', 'C', 'D', 'A', 'B']);
    assert.deepEqual(uniqueInOrder('AADD'),['A','D']);
    assert.deepEqual(uniqueInOrder('AAD'),['A','D']);
    assert.deepEqual(uniqueInOrder('ADD'),['A','D']);
  });
  it("and treat lowercase as different from uppercase", function(){
    assert.deepEqual(uniqueInOrder('ABBCcAD'),['A', 'B', 'C', 'c', 'A', 'D']);
  });
  it("and work with int arrays", function(){
    assert.deepEqual(uniqueInOrder([1,2,3,3]),[1,2,3]);
  });
  it("and work with char arrays", function(){
    assert.deepEqual(uniqueInOrder(['a','b','b']),['a','b']);
  });
});
*/