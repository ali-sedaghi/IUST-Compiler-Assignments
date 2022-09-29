grammar helloID;

compilationUnit:
    'hello' ' ' IDENTIFIER EOF
;

IDENTIFIER:
    Letter LetterOrDigit*
;

fragment Letter:
	[a-zA-Z_]
;

fragment LetterOrDigit:
	Letter
    | [0-9]
;