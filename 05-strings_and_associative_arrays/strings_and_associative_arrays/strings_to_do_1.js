// REMOVE BLANKS

function removeBlanks(sentence) {
    let sentence_new = [];
    for (idx = 0; idx < sentence.length; idx++) {
        if (sentence[idx] != " ") {
            sentence_new.push(sentence[idx]);
        }
    }
    sentence_new = sentence_new.join("");
    return sentence_new;
}

// console.log(removeBlanks(" Pl ayTha tF u nkyM usi c "));
// console.log(removeBlanks("I can not BELIEVE it's not BUTTER"));

// =====

// GET DIGITS

function getDigits(phrase) {
    let phrase_new = [];
    for (idx = 0; idx < phrase.length; idx++) {
        if (isNaN(phrase[idx]) !== true) {
            phrase_new.push(phrase[idx]);
        }
    }
    phrase_new = phrase_new.join("");
    return phrase_new;
}

// console.log(getDigits("abc8c0d1ngd0j0!8"));
// console.log(getDigits("0s1a3y5w7h9a2t4?6!8?0"));

// =====

// ACRONYMS

function acronym(sentence) {
    let sentence_new = [];
    let sentence_split = sentence.split(" ");
    for (idx = 0; idx < sentence_split.length; idx++) {
        for (index = 0; index < 1; index++) {
            if (sentence_split[idx][index] != " ") {
                sentence_new.push(sentence_split[idx][index]);
            }
        }
    }
    sentence_new = sentence_new.join("");
    return sentence_new.toUpperCase();
}

// console.log(acronym(" there's no free lunch - gotta pay yer way. "));
// console.log(acronym("Live from New York, it's Saturday Night!"));

// =====

// COUNT NON-SPACES

function countNonSpaces(sentence) {
    let counter = 0;
    for (idx = 0; idx < sentence.length; idx++) {
        if (sentence[idx] != " ") {
            counter++;
        }
    }
    return counter;
}

// console.log(countNonSpaces("Honey pie, you are driving me crazy"));
// console.log(countNonSpaces("Hello world !"));

// =====

// REMOVE SHORTER STRINGS

function removeShorterStrings(sentence, cutoff) {
    let sentence_new = [];
    for (idx = 0; idx < sentence.length; idx++) {
        if (sentence[idx].length >= cutoff) {
            sentence_new.push(sentence[idx]);
        }
    }
    return sentence_new;
}

// console.log(removeShorterStrings(['Good morning', 'sunshine', 'the', 'Earth', 'says', 'hello'], 4));
// console.log(removeShorterStrings(['There', 'is', 'a', 'bug', 'in', 'the', 'system'], 3));