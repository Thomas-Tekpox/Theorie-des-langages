import random

# def start():
#     print("Voici un générateur de PHP !")

# def inputVar():
#     print("Entrez le noms des variables que vous souhaitez utiliser :")
#     print("Ctrl+C pour passer à l'étape suivante")
#     while True:
#         try:
#             uneVar = input()
#             if uneVar != "":
#                 varNames.append("$"+uneVar.lower())
#         except KeyboardInterrupt:
#             break
#     print("Voici la liste de vos variables")
#     print(varNames)

# def inputName():
#     print("Entrez des chaînes de caractères :")
#     print("Ctrl+C pour passer à l'étape suivante")
#     while True:
#         try:
#             unName = input()
#             if unName != "":
#                 names.append(unName)
#         except KeyboardInterrupt:
#             break
#     print("Voici la liste de chaînes de cractères")
#     print(names)

# def randomRule(rules, left):
#     availableRules = []
#     for rule in rules:
#         if rule.left == left:
#             availableRules.append(rule)
#     return random.choice(availableRules)

# def generate(rules, todo):
#     terminated = []
#     while len(todo) >0:
#         sym = todo.pop(0)
#         if type(sym) == Terminal:
#             terminated.append(sym)
#         else:
#             rule = randomRule(rules, sym)
#             for newSym in reversed(rule.right):
#                 todo.insert(0, newSym)
#     return terminated

# def construct():
#     s = ""
#     for word in text:
#         s += str(word)
#     return s

# def generatePHP():
#     code = ""
#     while code == "":
#         code = construct()
#     print(code)
#     fichier = open("codotron.php", "w")
#     fichier.write("<?php\n"+ code +"\n?>")
#     fichier.close()

varNames = ["$t",
            "$x"]

tools = [
    "if",
    "else",
    "for",
    "while",
]

conditionSigns = [
    "<",
    ">",
    "<=",
    ">=",
    "!=",
]

signs = [
    "+",
    "-",
    "*",
    "/",
]

names = ["camion",
         "chat"]

numbers = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

class Symbol:
    def __init__(self, word):
        self.word = word
    def __str__(self):
        return self.word

class Terminal(Symbol):
    pass
class NonTerminal(Symbol):
    pass

class Rule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def __str__(self):
        s = str(self.left) + " -> "
        for sym in self.right:
            s += str(sym) + " "
        return s

epsilon = Terminal("")
comaPoint = Terminal(";")
comment = Terminal("//")
string = Terminal("'")
equal = Terminal("=")
enter = Terminal("\n")
equalCheck = Terminal("==")
oBracket = Terminal("(")
cBracket = Terminal(")")
oWaveBracket = Terminal("{")
cWaveBracket = Terminal("}")
tab = Terminal("  ")
unIf = Terminal("if")
unElse = Terminal("else")
unFor = Terminal("for")
unWhile = Terminal("while")
space = Terminal(" ")
unIn = Terminal("in")
strlenght = Terminal("strlen")
echo = Terminal("echo")
unEsle = Terminal("else")
unEsleIf = Terminal("elseif")
minus = Terminal("--")
plus = Terminal("++")

PROG = NonTerminal("PROG")
LINE = NonTerminal("LINE")
COMMENT = NonTerminal("COMMENT")
DESC = NonTerminal("DESC")
VAR = NonTerminal("VAR")
NUMBER = NonTerminal("NUMBER")
TEXT = NonTerminal("TEXT")
SIGN = NonTerminal("SIGN")
AFFECTATION = NonTerminal("AFFECTATION")
TOOL = NonTerminal("TOOL")
INSIDELINE = NonTerminal("INSIDELINE")
CONDITIONSIGN = NonTerminal("CONDITIONSIGN")
INSIDEIF = NonTerminal("INSIDEIF")
ELSEIF = NonTerminal("ELSEIF")
STOPCONDITION = NonTerminal("STOPCONDITION")


rules = [
    Rule(PROG, [LINE, enter, PROG]),
    Rule(PROG, [LINE, enter, PROG]),
    Rule(PROG, [LINE, enter, PROG]),
    Rule(PROG, [LINE, enter, PROG]),
    Rule(PROG, [epsilon]),
    Rule(LINE, [comment, DESC]),
    Rule(LINE, [AFFECTATION, comaPoint]),
    Rule(LINE, [echo, space, VAR, comaPoint]),
    Rule(LINE, [unIf, oBracket, VAR, equalCheck, VAR, cBracket, space, oWaveBracket, enter, tab, INSIDEIF, enter]),
    Rule(LINE, [unIf, oBracket, VAR, equalCheck, NUMBER, cBracket, space, oWaveBracket, enter, tab, INSIDEIF, enter]),
    Rule(LINE, [unFor, oBracket, VAR, equal, NUMBER, space, comaPoint, space, strlenght, oBracket, string, TEXT, string, cBracket, CONDITIONSIGN, VAR, space, comaPoint, space, VAR, STOPCONDITION, cBracket, space, oWaveBracket, enter, tab, INSIDELINE, enter, cWaveBracket]),
    Rule(LINE, [unFor, oBracket, VAR, equal, NUMBER, space, comaPoint, space, strlenght, oBracket, string, TEXT, string, cBracket, CONDITIONSIGN, NUMBER, space, comaPoint, space, VAR, STOPCONDITION, cBracket, space, oWaveBracket, enter, tab, INSIDELINE, enter, cWaveBracket]),
    Rule(LINE, [unWhile, oBracket, strlenght, oBracket, string, TEXT, string, cBracket, CONDITIONSIGN, NUMBER, cBracket, space, oWaveBracket, enter, tab, INSIDELINE, enter, cWaveBracket]),
    Rule(AFFECTATION, [VAR, equal, NUMBER]),
    Rule(AFFECTATION, [VAR, equal, VAR]),
    Rule(AFFECTATION, [VAR, equal, string, TEXT, string]),
    Rule(AFFECTATION, [VAR, equal, VAR, SIGN, VAR]),
    Rule(AFFECTATION, [VAR, equal, NUMBER, SIGN, VAR]),
    Rule(AFFECTATION, [VAR, equal, VAR, SIGN, NUMBER]),
    Rule(INSIDELINE, [AFFECTATION, comaPoint]),
    Rule(INSIDELINE, [echo, space, VAR, comaPoint]),
    Rule(INSIDEIF, [AFFECTATION, comaPoint, enter, cWaveBracket]),
    Rule(INSIDEIF, [echo, space, VAR, comaPoint, enter, cWaveBracket]),
    Rule(INSIDEIF, [INSIDELINE, enter, cWaveBracket, enter, ELSEIF, space, oWaveBracket, enter, tab, INSIDELINE, enter, cWaveBracket]),
    Rule(INSIDEIF, [INSIDELINE, enter, cWaveBracket, enter, unEsle, space, oWaveBracket, enter, tab, INSIDELINE, enter, cWaveBracket]),
    Rule(ELSEIF, [unEsleIf, oBracket, VAR, equalCheck, VAR, cBracket]),
    Rule(ELSEIF, [unEsleIf, oBracket, VAR, equalCheck, NUMBER, cBracket]),
    Rule(STOPCONDITION, [minus]),
    Rule(STOPCONDITION, [plus]),
]

for varName in varNames:
    rules.append(Rule(DESC, [Terminal(varName)]))
    rules.append(Rule(VAR, [Terminal(varName)]))
    
for name in names:
    rules.append(Rule(DESC, [Terminal(name)]))
    rules.append(Rule(TEXT, [Terminal(name)]))
    
for number in numbers:
    rules.append(Rule(NUMBER, [Terminal(number)]))
    
for sign in signs:
    rules.append(Rule(SIGN, [Terminal(sign)]))
    
for tool in tools:
    rules.append(Rule(TOOL, [Terminal(tool)]))
    
for conditionSign in conditionSigns:
    rules.append(Rule(CONDITIONSIGN, [Terminal(conditionSign)]))

def randomRule(rules, left):
    availableRules = []
    for rule in rules:
        if rule.left == left:
            availableRules.append(rule)
    return random.choice(availableRules)

def generate(rules, todo):
    terminated = []
    while len(todo) >0:
        sym = todo.pop(0)
        if type(sym) == Terminal:
            terminated.append(sym)
        else:
            rule = randomRule(rules, sym)
            for newSym in reversed(rule.right):
                todo.insert(0, newSym)
    return terminated

# print("Voici un générateur de PHP !")
# print("Entrez le noms des variables que vous souhaitez utiliser :")
# print("Ctrl+C pour passer à l'étape suivante")
# while True:
#     try:
#         uneVar = input()
#         if uneVar != "":
#             varNames.append("$"+uneVar.lower())
#     except KeyboardInterrupt:
#         break
# print("Voici la liste de vos variables")
# print(varNames)
# print("Entrez des chaînes de caractères :")
# print("Ctrl+C pour passer à l'étape suivante")
# while True:
#     try:
#         unName = input()
#         if unName != "":
#             names.append(unName)
#     except KeyboardInterrupt:
#         break
# print("Voici la liste de chaînes de cractères")
# print(names)

text = generate(rules, [PROG])
s = ""

for word in text:
    s += str(word)
print(s)

fichier = open("codotron.php", "w")
fichier.write("<?php\n\n"+ s +"?>")
fichier.close()

# start()
# inputVar()
# inputName()
# generatePHP()