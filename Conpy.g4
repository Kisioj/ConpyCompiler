grammar Conpy;

FUNC: 'func';
IF: 'if';
ELSE: 'else';
INT: [0-9]+;
NAME: [a-zA-Z_][a-zA-Z_0-9]*;
WHITESPACE: [ \t]+ -> skip;
NEWLINE: ('\r' '\n'? | '\n') -> skip;

main: (funcDef | funcCall)* EOF;
funcDef: FUNC funcNameDef '(' paramDef? ')' block;
block: '{' (ifStmt | funcCall)* '}';
ifStmt: IF '(' expr ')' block (ELSE block)?;
funcCall: funcNameRef '(' expr? ')' ';';
expr: expr '*' expr | expr '+' expr | value;
value: paramRef | INT;
paramDef: NAME;
paramRef: NAME;
funcNameDef: NAME;
funcNameRef: NAME;