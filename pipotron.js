noms = [
    "Loan",
    "Jeremy",
    "Rayen",
    "Sylvain",
    "Dany",
    "Luc",
    "Robin",
    "Tom",
    "Mathis",
    "Baptiste",
    "Thomas",
    "Tom",
    "Romain",
    "Thibault",
    "Hugo",
    "Timothée",
    "Solo",
    "Mathis",
    "Noa",
    "Mathis",
    "Joyce",
    "Steven",
    "une chaise",
    "le chat",
    "une sesto elemento FE",
    "un tourne-vis",
    "une pizza",
    "une glace",
    "un test-PCR",
    "un journal",
    "un koala",
    "une trotinette",
    "un aspirateur",
    "une limace"
]

verbes = [
    "a",
    "est",
    "tape",
    "mange",
    "conduit",
    "embrasse",
    "déteste",
    "lèche",
    "découpe",
    "insulte",
    "torture",
    "démonte",
    "fabrique",
    "explose",
    "soulève",
    "complimente",
    "protège",
    "enjambe",
    "aime",
    "cuisine",
    "glisse sur",
    "danse sur",
    "répare",
    "décore",
]

verbess = [
    "sont",
    "ont",
    "tape",
    "mange",
    "conduisent",
    "embrasse",
    "déteste",
    "lèche",
    "découpe",
    "insulte",
    "torture",
    "démonte",
    "fabrique",
    "explose",
    "soulève",
    "complimente",
    "protège",
    "enjambe",
    "aime",
    "cuisine",
    "glisse sur",
    "danse sur",
    "répare",
    "décore",
]

ets = [
    "et",
    ]

liaisonsNom = [
    "sur",
    "avec",
    "parce que",
]

liaisonsVerbe = [
    "qui",
]

adjectifs = [
    "l'illuminé",
    "fatigué",
    "énervé",
    "essouflé",
    ",le petit génie",
    "le beau gosse",
    ",le roi de la glisse",
]

adjectifss = [
    "les illuminés",
    "fatigué",
    "énervé",
    "essouflé",
    ",les petit génie",
    "les beaux gosses",
    ",les roi de la glisse",
]


class Symbol {
    constructor(self, word) {
        this.word = word
    }
}
    
class Terminal extends Symbol {
    pass
}

class NonTerminal extends Symbol {
    pass
}

class Rule {
    constructor(self, left, right) {
        this.left = left
        this.right = right
    }
    // toString override added to prototype of Foo class
    Rule.prototype.toString = function() {
        s = this.left.toString() + " -> "
        for(sym in this.right) {
            s += sym.toString() + " "
        }
        return s
    }
}

epsilon = Terminal("")
point = Terminal(".")

TEXTE = NonTerminal("TEXTE")
PHRASE = NonTerminal("PHRASE")
SUJET = NonTerminal("SUJET")
VERBE = NonTerminal("VERBE")
COMPLEMENT = NonTerminal("COMPLEMENT")
LIAISONNOM = NonTerminal("LIAISONNOM")
LIAISONVERBE = NonTerminal("LIAISONVERBE")
ADJECTIF = NonTerminal("ADJECTIF")
NOM = NonTerminal("NOM")
ET = NonTerminal("ET")
ADJECTIFS = NonTerminal("ADJECTIFS")
VERBES = NonTerminal("VERBES")

rules = [
    Rule(TEXTE, [PHRASE, point, TEXTE]),
    Rule(TEXTE, [PHRASE, point, TEXTE]),
    Rule(TEXTE, [PHRASE, point, TEXTE]),
    Rule(TEXTE, [epsilon]),
    Rule(PHRASE, [SUJET, VERBE, COMPLEMENT, point]),
    Rule(PHRASE, [SUJET, ET, NOM, VERBES, COMPLEMENT, point]),
    Rule(PHRASE, [SUJET, ADJECTIF, VERBE, COMPLEMENT, point]),
    Rule(PHRASE, [SUJET, ET, NOM, ADJECTIFS, VERBES, COMPLEMENT, point]),
    Rule(COMPLEMENT, [NOM, LIAISONNOM, NOM]),
    Rule(COMPLEMENT, [NOM, ET, NOM, LIAISONNOM, NOM]),
    Rule(COMPLEMENT, [NOM, LIAISONNOM, NOM, ET, NOM]),
    Rule(COMPLEMENT, [NOM, ET, NOM, LIAISONNOM, NOM, ET, NOM]),
    Rule(COMPLEMENT, [NOM, LIAISONVERBE, VERBE, NOM]),
    Rule(COMPLEMENT, [NOM, LIAISONVERBE, VERBE, NOM, LIAISONNOM, COMPLEMENT]),
]

for(nom in noms) {
    rules.append(Rule(SUJET, [Terminal(nom)]))
    rules.append(Rule(NOM, [Terminal(nom)]))
}

for(liaison in liaisonsNom) {
    rules.append(Rule(LIAISONNOM, [Terminal(liaison)]))
}
    
for(liaison in liaisonsVerbe) {
    rules.append(Rule(LIAISONVERBE, [Terminal(liaison)]))
}
    
for(adjectif in adjectifs) {
    rules.append(Rule(ADJECTIF, [Terminal(adjectif)]))
}
    
for(adjectif in adjectifss) {
    rules.append(Rule(ADJECTIFS, [Terminal(adjectif)]))
}

for(verbe in verbes) {
    rules.append(Rule(VERBE, [Terminal(verbe)]))
}

for(verbe in verbess) {
    rules.append(Rule(VERBES, [Terminal(verbe)]))
}

for(et in ets) {
    rules.append(Rule(ET, [Terminal(et)]))
}

function randomRule(rules, left) {
    availableRules = []
    for(rule in rules) {
        if(rule.left == left) {
            availableRules.append(rule)
        }
    }
    return random.choice(availableRules)
}

function generate(rules, todo) {
    terminated = []
    while(todo.lenght() > 0) {
        sym = todo.pop(0)
        if(type(sym) == Terminal) {
            terminated.append(sym)
        }
        else {
            rule = randomRule(rules, sym)
            for(newSym in reversed(rule.right)) {
                todo.insert(0, newSym)
            }
        }
    }
    return terminated
}


text = generate(rules, [TEXTE])
s = ""

for(word in text) {
    s += str(word) + " "
}

print(s)