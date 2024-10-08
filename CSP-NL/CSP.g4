grammar CSP;

cspFile: (processDefinition | channelDefinition | assertion)+ ;

processDefinition: ID '('? parameters? ')'? '=' expression ;

channelDefinition
    : 'channel' ID (',' ID)* (':' '{' INT ('..' INT)? '}')?
    ;
    
assertion: 'assert' ID assertionType;

assertionType
    : ':[' 'has trace' ']' ':' '<' trace '>' 
    | ':[' assertionModel ']' 
    | ':[' assertionModel ']' ':' '<' trace '>'
    ;

assertionModel: 'deadlock free' | 'divergence free' | 'deterministic';

trace: event (',' event)*;

parameters: ID (',' ID)* ;

expression
    : BOOL '&' expression  // Guarded expression
    | expression '[]' expression  // External choice
    | expression '[' '{' eventList '}' '||' '{' eventList '}' ']' expression // Alphabetised Parallel
    | expression '[|' '{' eventList '}' '|]' expression  // Generalised Parallel
    | expression '|||' expression  // Interleave
    | expression ';' expression  // Sequential Composition
    | nondeterministicRestrictedInputExpression  // Non-deterministic Restricted Input
    | restrictedInputExpression  // Restricted Input
    | inputPatternExpression  // Input Pattern
    | outputExpression  // Output Expression
    | nondeterministicInputExpression  // Non-deterministic Input
    | prefixExpression
    | baseExpression
    ;

prefixExpression: event '->' expression ;

inputPatternExpression: ID '?' ID '->' expression ;  // Input Pattern

restrictedInputExpression: ID '?' ID ':' '{' INT (',' INT)* '}' '->' expression ;  // Restricted Input

nondeterministicRestrictedInputExpression: ID '$' ID ':' '{' INT (',' INT)* '}' '->' expression ;  // Non-deterministic Restricted Input

outputExpression: ID '!' INT '->' expression ;  // Output Expression

nondeterministicInputExpression: ID '$' ID '->' expression ;  // Non-deterministic Input

baseExpression
    : STOP_RULE
    | SKIP_RULE
    | ID
    | '(' expression ')'
    ;

eventList: event (',' event)* ;  // Event set

event: ID ('.' INT)* ;  // Event allows channel name followed by specific values

STOP_RULE: 'STOP' ;

SKIP_RULE: 'SKIP' ;

BOOL: 'true' | 'false' ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;  // Identifier rule

INT: [0-9]+ ;  // Number rule

WS: [ \t\r\n]+ -> skip ;
