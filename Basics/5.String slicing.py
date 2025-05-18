'''
from numpy import True_, var


alpha = "abcdefghijklmnopqrstuvwxyz"
var vowels = "aeiou"
function isPangram(sentence) {
    var letterObj = {}
    for (var i=0; i<26; i++) {
        letterObj[alpha.charAt(i)] = 0
    }
    sentence = sentence.toLowerCase()
    for (var j=0; j<sentence.length; j++) {
        if (vowels.indexOf(sentence.charAt(j))==-1 && letterObj[sentence.charAt(j)]++ == 0) {
            return false
        }
    }
    return true
}
console.log(isPangram(" The quick brown fox jumps over the lazy dog")) //True_
'''

alpha = "abcdefghijklmnopqrstuvwxyz"
print(alpha)
print(alpha[8])
print(alpha[8:14])
print(alpha[8:14:1])
print(alpha[8:14:2])
print(alpha[8:14:40])
print(alpha[:])
print(alpha[:14])
print(alpha[:14:1])
print(alpha[:14:2])
print(alpha[:14:40])
print(alpha[8])
print(alpha[8:])
print(alpha[8::1])
print(alpha[8::2])
print(alpha[8::40])
print(len(alpha))
print(len(alpha+alpha))
print(type(alpha))
print(type(alpha+alpha))
print(alpha[::])
print(alpha[::2])
print(alpha[:2:])
print(alpha[2::])