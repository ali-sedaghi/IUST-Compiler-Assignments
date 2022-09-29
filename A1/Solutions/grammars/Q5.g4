// scheme:[//[user:password@]host[:port]][/]path[?query][#fragment]
grammar Q5;

compilationUnit: string '://' login? hostname (':' port)? ('/' path?)? query? frag? WS?;
hostname: '/'? string ('.' string)*;
login: username (':' password)? '@';
username: string;
password: string;
port: DIGITS;
path: string ('/' string)* '/'?;
frag: '#' (string | DIGITS);
query: '?' search;
search: searchparameter ('&' searchparameter)*;
searchparameter: string ('=' (string | DIGITS | HEX))?;
string: STRING | DIGITS;

// Lexical Rules
DIGITS: [0-9] +;
HEX: ('%' [a-fA-F0-9] [a-fA-F0-9]) +;
STRING: ([a-zA-Z~0-9] | HEX) ([a-zA-Z0-9.+-] | HEX)*;
WS: [\r\n] +;
