//const { expect } = require('@jest/globals');
//const fizzbuzz = require('./fizzbuzzkata');

import { assert, expect } from 'chai'
import fizzbuzz from '../fizzbuzzkata.js'

describe('Test', () => {
    it('Get “1” when I pass in 1', () => {
        assert.equal(fizzbuzz(1), '1')
    })
    it('Get “2” when I pass in 2', () => {
        assert.equal(fizzbuzz(2), '2')
    })
})

//test('1 = 1 and 2 = 2', () => {
    //expect("1").toEqual("1");
    //expect("2").toEqual("2");
//});
