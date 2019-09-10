grammar Conpy;

FUNC:           'func';
IF:             'if';
ELSE:           'else';
INT:            [0-9]+;
NAME:           [a-zA-Z_][a-zA-Z_0-9]*;
WHITESPACE:     [ \t]+ -> skip;
NEWLINE:        ('\r' '\n'? | '\n') -> skip;

main: (funcDef | funcCall)* EOF;
funcDef: FUNC NAME '(' params? ')' block;
params: NAME (',' NAME)*;
block: '{' (ifStmt | funcCall)* '}';
ifStmt: IF '(' expr ')' ifBlock=block (ELSE elseBlock=block)?;
funcCall: NAME '(' arguments? ')' ';';
arguments: expr (',' expr)*;
expr:
    expr (oper='*') expr #binaryExpr
    | expr (oper='+') expr #binaryExpr
    | value #valueExpr
    ;
value: paramRef | intLiteral;
paramRef: NAME;
intLiteral: INT;