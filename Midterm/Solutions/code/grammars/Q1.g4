grammar Q1;

compilationUnit: 'F1:'Number1 | 'F2:'Number2;

Number1: Max11','Max12','Max13;
Number2: Max21','Max22','Max23;

Max11: '0'?'0'?[0-9] | '0'?[1-9][0-9] | [1-6][0-9][0-9] | '7'[0-7][0-9] | '7''8'[0-8];
Max12: '0'?'0'?[0-9] | '0'?[1-9][0-9] | [1-3][0-9][0-9] | '4'[0-1][0-9] | '4''2'[0-2];
Max13: '0'?'0'?[0-9] | '0'?[1-9][0-9] | [1-2][0-9][0-9] | '3'[0-1][0-9] | '3''2'[0-5];


Max21: '0'?'0'?[0-9] | '0'?[1-9][0-9] | '1'[0-1][0-9] | '1''2'[0-3];
Max22: '0'?'0'?[0-9] | '0'?[1-9][0-9] | [1-3][0-9][0-9] | '4'[0-5][0-9] | '4''6'[0-1];
Max23: '0'?'0'?[0-9] | '0'?[1-9][0-9] | '1'[0-9][0-9] | '200';
