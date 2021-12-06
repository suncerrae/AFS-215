
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


