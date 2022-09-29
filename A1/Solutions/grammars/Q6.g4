grammar Q6;

compilationUnit:
    (source
    | catalog
    | standard
    | encrypted
    | trusted
    | multipleActiveResultSets
    | persistSecurityInfo
    | server
    ) * EOF;

source:
    'Data Source=' ID ';'
    ;

catalog:
    'Initial Catalog=' ID ';'
    ;

standard:
    'User id=' ID ';'
    'Password=' STRING ';'
    ;

encrypted:
    'Encrypt=' common ';'
    ;

trusted:
    ('Integrated Security=' | 'Trusted_Connection=') ('sspi' | common) ';'
    ;

multipleActiveResultSets:
    'MultipleActiveResultSets=' bool ';'
    ;

persistSecurityInfo:
    'Persist Security Info=' common ';'
    ;

server:
    'server=(local);'
    ;

bool: ('false' | 'False' | 'True' | 'true');
yn: 'yes' | 'no';
common: bool | yn;

// Lexical Rules
DIGITS: [0-9] +;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: ([a-zA-Z~0-9]) ([a-zA-Z0-9.+-])*;
