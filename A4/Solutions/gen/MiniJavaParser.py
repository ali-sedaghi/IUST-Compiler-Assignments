# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3*")
        buf.write("\u0156\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\7\2\30\n\2\f\2\16")
        buf.write("\2\33\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3")
        buf.write("\4\5\4\66\n\4\3\4\3\4\7\4:\n\4\f\4\16\4=\13\4\3\4\7\4")
        buf.write("@\n\4\f\4\16\4C\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\7\6U\n\6\f\6\16\6X\13\6")
        buf.write("\5\6Z\n\6\3\6\3\6\3\6\7\6_\n\6\f\6\16\6b\13\6\3\6\3\6")
        buf.write("\3\6\7\6g\n\6\f\6\16\6j\13\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\5\7w\n\7\3\b\3\b\3\b\3\b\3\b\7\b~\n")
        buf.write("\b\f\b\16\b\u0081\13\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\b\u00c1\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\5\t\u00ec\n\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7\t")
        buf.write("\u0144\n\t\f\t\16\t\u0147\13\t\5\t\u0149\n\t\3\t\3\t\3")
        buf.write("\t\7\t\u014e\n\t\f\t\16\t\u0151\13\t\3\n\3\n\3\n\3\n\2")
        buf.write("\3\20\13\2\4\6\b\n\f\16\20\22\2\2\2\u016f\2\24\3\2\2\2")
        buf.write("\4\36\3\2\2\2\6\61\3\2\2\2\bF\3\2\2\2\nJ\3\2\2\2\fv\3")
        buf.write("\2\2\2\16\u00c0\3\2\2\2\20\u00eb\3\2\2\2\22\u0152\3\2")
        buf.write("\2\2\24\25\b\2\1\2\25\31\5\4\3\2\26\30\5\6\4\2\27\26\3")
        buf.write("\2\2\2\30\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\34")
        buf.write("\3\2\2\2\33\31\3\2\2\2\34\35\7\2\2\3\35\3\3\2\2\2\36\37")
        buf.write("\7\3\2\2\37 \5\22\n\2 !\7\6\2\2!\"\7\17\2\2\"#\7\20\2")
        buf.write("\2#$\7\21\2\2$%\7\22\2\2%&\7\4\2\2&\'\7\23\2\2\'(\7\b")
        buf.write("\2\2()\7\t\2\2)*\5\22\n\2*+\7\5\2\2+,\7\6\2\2,-\5\16\b")
        buf.write("\2-.\7\7\2\2./\7\7\2\2/\60\b\3\1\2\60\5\3\2\2\2\61\62")
        buf.write("\7\3\2\2\62\65\5\22\n\2\63\64\7\24\2\2\64\66\5\22\n\2")
        buf.write("\65\63\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\67;\7\6\2\2")
        buf.write("8:\5\b\5\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<A\3")
        buf.write("\2\2\2=;\3\2\2\2>@\5\n\6\2?>\3\2\2\2@C\3\2\2\2A?\3\2\2")
        buf.write("\2AB\3\2\2\2BD\3\2\2\2CA\3\2\2\2DE\7\7\2\2E\7\3\2\2\2")
        buf.write("FG\5\f\7\2GH\5\22\n\2HI\7\n\2\2I\t\3\2\2\2JK\7\17\2\2")
        buf.write("KL\5\f\7\2LM\5\22\n\2MY\7\4\2\2NO\5\f\7\2OV\5\22\n\2P")
        buf.write("Q\7\13\2\2QR\5\f\7\2RS\5\22\n\2SU\3\2\2\2TP\3\2\2\2UX")
        buf.write("\3\2\2\2VT\3\2\2\2VW\3\2\2\2WZ\3\2\2\2XV\3\2\2\2YN\3\2")
        buf.write("\2\2YZ\3\2\2\2Z[\3\2\2\2[\\\7\5\2\2\\`\7\6\2\2]_\5\b\5")
        buf.write("\2^]\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2ah\3\2\2\2b")
        buf.write("`\3\2\2\2cd\5\16\b\2de\b\6\1\2eg\3\2\2\2fc\3\2\2\2gj\3")
        buf.write("\2\2\2hf\3\2\2\2hi\3\2\2\2ik\3\2\2\2jh\3\2\2\2kl\7\25")
        buf.write("\2\2lm\5\20\t\2mn\7\n\2\2no\7\7\2\2o\13\3\2\2\2pq\7\26")
        buf.write("\2\2qr\7\b\2\2rw\7\t\2\2sw\7\27\2\2tw\7\26\2\2uw\5\22")
        buf.write("\n\2vp\3\2\2\2vs\3\2\2\2vt\3\2\2\2vu\3\2\2\2w\r\3\2\2")
        buf.write("\2xy\7\6\2\2y\177\b\b\1\2z{\5\16\b\2{|\b\b\1\2|~\3\2\2")
        buf.write("\2}z\3\2\2\2~\u0081\3\2\2\2\177}\3\2\2\2\177\u0080\3\2")
        buf.write("\2\2\u0080\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u00c1")
        buf.write("\7\7\2\2\u0083\u0084\7\30\2\2\u0084\u0085\7\4\2\2\u0085")
        buf.write("\u0086\5\20\t\2\u0086\u0087\7\5\2\2\u0087\u0088\5\16\b")
        buf.write("\2\u0088\u0089\7\31\2\2\u0089\u008a\5\16\b\2\u008a\u008b")
        buf.write("\b\b\1\2\u008b\u008c\b\b\1\2\u008c\u008d\b\b\1\2\u008d")
        buf.write("\u008e\b\b\1\2\u008e\u008f\b\b\1\2\u008f\u0090\b\b\1\2")
        buf.write("\u0090\u0091\b\b\1\2\u0091\u0092\b\b\1\2\u0092\u0093\b")
        buf.write("\b\1\2\u0093\u0094\b\b\1\2\u0094\u0095\b\b\1\2\u0095\u0096")
        buf.write("\b\b\1\2\u0096\u0097\b\b\1\2\u0097\u00c1\3\2\2\2\u0098")
        buf.write("\u0099\7\32\2\2\u0099\u009a\7\4\2\2\u009a\u009b\5\20\t")
        buf.write("\2\u009b\u009c\7\5\2\2\u009c\u009d\5\16\b\2\u009d\u009e")
        buf.write("\b\b\1\2\u009e\u009f\b\b\1\2\u009f\u00a0\b\b\1\2\u00a0")
        buf.write("\u00a1\b\b\1\2\u00a1\u00a2\b\b\1\2\u00a2\u00a3\b\b\1\2")
        buf.write("\u00a3\u00a4\b\b\1\2\u00a4\u00c1\3\2\2\2\u00a5\u00a6\7")
        buf.write("\33\2\2\u00a6\u00a7\7\4\2\2\u00a7\u00a8\5\20\t\2\u00a8")
        buf.write("\u00a9\7\5\2\2\u00a9\u00aa\7\n\2\2\u00aa\u00c1\3\2\2\2")
        buf.write("\u00ab\u00ac\5\22\n\2\u00ac\u00ad\7\34\2\2\u00ad\u00ae")
        buf.write("\5\20\t\2\u00ae\u00af\7\n\2\2\u00af\u00b0\b\b\1\2\u00b0")
        buf.write("\u00b1\b\b\1\2\u00b1\u00b2\b\b\1\2\u00b2\u00c1\3\2\2\2")
        buf.write("\u00b3\u00b4\5\22\n\2\u00b4\u00b5\7\b\2\2\u00b5\u00b6")
        buf.write("\5\20\t\2\u00b6\u00b7\7\t\2\2\u00b7\u00b8\7\34\2\2\u00b8")
        buf.write("\u00b9\5\20\t\2\u00b9\u00ba\7\n\2\2\u00ba\u00bb\b\b\1")
        buf.write("\2\u00bb\u00bc\b\b\1\2\u00bc\u00bd\b\b\1\2\u00bd\u00be")
        buf.write("\b\b\1\2\u00be\u00bf\b\b\1\2\u00bf\u00c1\3\2\2\2\u00c0")
        buf.write("x\3\2\2\2\u00c0\u0083\3\2\2\2\u00c0\u0098\3\2\2\2\u00c0")
        buf.write("\u00a5\3\2\2\2\u00c0\u00ab\3\2\2\2\u00c0\u00b3\3\2\2\2")
        buf.write("\u00c1\17\3\2\2\2\u00c2\u00c3\b\t\1\2\u00c3\u00c4\7\4")
        buf.write("\2\2\u00c4\u00c5\5\20\t\2\u00c5\u00c6\7\5\2\2\u00c6\u00c7")
        buf.write("\b\t\1\2\u00c7\u00c8\b\t\1\2\u00c8\u00c9\b\t\1\2\u00c9")
        buf.write("\u00ca\b\t\1\2\u00ca\u00ec\3\2\2\2\u00cb\u00cc\7*\2\2")
        buf.write("\u00cc\u00ec\b\t\1\2\u00cd\u00ce\7\r\2\2\u00ce\u00ec\b")
        buf.write("\t\1\2\u00cf\u00d0\7\16\2\2\u00d0\u00ec\b\t\1\2\u00d1")
        buf.write("\u00d2\5\22\n\2\u00d2\u00d3\b\t\1\2\u00d3\u00ec\3\2\2")
        buf.write("\2\u00d4\u00d5\7%\2\2\u00d5\u00ec\b\t\1\2\u00d6\u00d7")
        buf.write("\7$\2\2\u00d7\u00d8\7\26\2\2\u00d8\u00d9\7\b\2\2\u00d9")
        buf.write("\u00da\5\20\t\2\u00da\u00db\7\t\2\2\u00db\u00dc\b\t\1")
        buf.write("\2\u00dc\u00ec\3\2\2\2\u00dd\u00de\7$\2\2\u00de\u00df")
        buf.write("\5\22\n\2\u00df\u00e0\7\4\2\2\u00e0\u00e1\7\5\2\2\u00e1")
        buf.write("\u00e2\b\t\1\2\u00e2\u00ec\3\2\2\2\u00e3\u00e4\7#\2\2")
        buf.write("\u00e4\u00e5\5\20\t\3\u00e5\u00e6\b\t\1\2\u00e6\u00e7")
        buf.write("\b\t\1\2\u00e7\u00e8\b\t\1\2\u00e8\u00e9\b\t\1\2\u00e9")
        buf.write("\u00ea\b\t\1\2\u00ea\u00ec\3\2\2\2\u00eb\u00c2\3\2\2\2")
        buf.write("\u00eb\u00cb\3\2\2\2\u00eb\u00cd\3\2\2\2\u00eb\u00cf\3")
        buf.write("\2\2\2\u00eb\u00d1\3\2\2\2\u00eb\u00d4\3\2\2\2\u00eb\u00d6")
        buf.write("\3\2\2\2\u00eb\u00dd\3\2\2\2\u00eb\u00e3\3\2\2\2\u00ec")
        buf.write("\u014f\3\2\2\2\u00ed\u00ee\f\22\2\2\u00ee\u00ef\7 \2\2")
        buf.write("\u00ef\u00f0\5\20\t\23\u00f0\u00f1\b\t\1\2\u00f1\u00f2")
        buf.write("\b\t\1\2\u00f2\u00f3\b\t\1\2\u00f3\u00f4\b\t\1\2\u00f4")
        buf.write("\u00f5\b\t\1\2\u00f5\u00f6\b\t\1\2\u00f6\u00f7\b\t\1\2")
        buf.write("\u00f7\u014e\3\2\2\2\u00f8\u00f9\f\21\2\2\u00f9\u00fa")
        buf.write("\7!\2\2\u00fa\u00fb\5\20\t\22\u00fb\u00fc\b\t\1\2\u00fc")
        buf.write("\u00fd\b\t\1\2\u00fd\u00fe\b\t\1\2\u00fe\u00ff\b\t\1\2")
        buf.write("\u00ff\u0100\b\t\1\2\u0100\u0101\b\t\1\2\u0101\u0102\b")
        buf.write("\t\1\2\u0102\u014e\3\2\2\2\u0103\u0104\f\20\2\2\u0104")
        buf.write("\u0105\7\37\2\2\u0105\u0106\5\20\t\21\u0106\u0107\b\t")
        buf.write("\1\2\u0107\u0108\b\t\1\2\u0108\u0109\b\t\1\2\u0109\u010a")
        buf.write("\b\t\1\2\u010a\u010b\b\t\1\2\u010b\u010c\b\t\1\2\u010c")
        buf.write("\u010d\b\t\1\2\u010d\u014e\3\2\2\2\u010e\u010f\f\17\2")
        buf.write("\2\u010f\u0110\7\35\2\2\u0110\u0111\5\20\t\20\u0111\u0112")
        buf.write("\b\t\1\2\u0112\u0113\b\t\1\2\u0113\u0114\b\t\1\2\u0114")
        buf.write("\u0115\b\t\1\2\u0115\u0116\b\t\1\2\u0116\u0117\b\t\1\2")
        buf.write("\u0117\u0118\b\t\1\2\u0118\u014e\3\2\2\2\u0119\u011a\f")
        buf.write("\16\2\2\u011a\u011b\7\36\2\2\u011b\u011c\5\20\t\17\u011c")
        buf.write("\u011d\b\t\1\2\u011d\u011e\b\t\1\2\u011e\u011f\b\t\1\2")
        buf.write("\u011f\u0120\b\t\1\2\u0120\u0121\b\t\1\2\u0121\u0122\b")
        buf.write("\t\1\2\u0122\u0123\b\t\1\2\u0123\u014e\3\2\2\2\u0124\u0125")
        buf.write("\f\r\2\2\u0125\u0126\7\b\2\2\u0126\u0127\5\20\t\2\u0127")
        buf.write("\u0128\7\t\2\2\u0128\u0129\b\t\1\2\u0129\u012a\b\t\1\2")
        buf.write("\u012a\u012b\b\t\1\2\u012b\u012c\b\t\1\2\u012c\u012d\b")
        buf.write("\t\1\2\u012d\u012e\b\t\1\2\u012e\u012f\b\t\1\2\u012f\u0130")
        buf.write("\b\t\1\2\u0130\u0131\b\t\1\2\u0131\u0132\b\t\1\2\u0132")
        buf.write("\u0133\b\t\1\2\u0133\u014e\3\2\2\2\u0134\u0135\f\f\2\2")
        buf.write("\u0135\u0136\7\f\2\2\u0136\u0137\7\"\2\2\u0137\u0138\b")
        buf.write("\t\1\2\u0138\u0139\b\t\1\2\u0139\u013a\b\t\1\2\u013a\u013b")
        buf.write("\b\t\1\2\u013b\u014e\b\t\1\2\u013c\u013d\f\13\2\2\u013d")
        buf.write("\u013e\7\f\2\2\u013e\u013f\5\22\n\2\u013f\u0148\7\4\2")
        buf.write("\2\u0140\u0145\5\20\t\2\u0141\u0142\7\13\2\2\u0142\u0144")
        buf.write("\5\20\t\2\u0143\u0141\3\2\2\2\u0144\u0147\3\2\2\2\u0145")
        buf.write("\u0143\3\2\2\2\u0145\u0146\3\2\2\2\u0146\u0149\3\2\2\2")
        buf.write("\u0147\u0145\3\2\2\2\u0148\u0140\3\2\2\2\u0148\u0149\3")
        buf.write("\2\2\2\u0149\u014a\3\2\2\2\u014a\u014b\7\5\2\2\u014b\u014c")
        buf.write("\b\t\1\2\u014c\u014e\3\2\2\2\u014d\u00ed\3\2\2\2\u014d")
        buf.write("\u00f8\3\2\2\2\u014d\u0103\3\2\2\2\u014d\u010e\3\2\2\2")
        buf.write("\u014d\u0119\3\2\2\2\u014d\u0124\3\2\2\2\u014d\u0134\3")
        buf.write("\2\2\2\u014d\u013c\3\2\2\2\u014e\u0151\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u014f\u0150\3\2\2\2\u0150\21\3\2\2\2\u0151\u014f")
        buf.write("\3\2\2\2\u0152\u0153\7)\2\2\u0153\u0154\b\n\1\2\u0154")
        buf.write("\23\3\2\2\2\22\31\65;AVY`hv\177\u00c0\u00eb\u0145\u0148")
        buf.write("\u014d\u014f")
        return buf.getvalue()


class MiniJavaParser ( Parser ):

    grammarFileName = "MiniJavaParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','", "'.'", "'true'", "'false'", 
                     "'public'", "'static'", "'void'", "'main'", "'String'", 
                     "'extends'", "'return'", "'int'", "'boolean'", "'if'", 
                     "'else'", "'while'", "'System.out.println'", "'='", 
                     "'+'", "'-'", "'*'", "'<'", "'&&'", "'length'", "'!'", 
                     "'new'", "'this'" ]

    symbolicNames = [ "<INVALID>", "CLASS", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "LBRACK", "RBRACK", "SEMI", "COMMA", "DOT", 
                      "TRUE", "FALSE", "PUBLIC", "STATIC", "VOID", "MAIN", 
                      "STRING", "EXTENDS", "RETURN", "INT", "BOOLEAN", "IF", 
                      "ELSE", "WHILE", "SOUT", "ASSIGN", "ADD", "SUB", "MUL", 
                      "LT", "ANDAND", "LEN", "NOT", "NEW", "THIS", "WS", 
                      "COMMENT", "LINE_COMMENT", "IDENTIFIER", "INTEGER_LITERAL" ]

    RULE_program = 0
    RULE_mainClass = 1
    RULE_classDeclaration = 2
    RULE_varDeclaration = 3
    RULE_methodDeclaration = 4
    RULE_type_ = 5
    RULE_statement = 6
    RULE_expression = 7
    RULE_identifier = 8

    ruleNames =  [ "program", "mainClass", "classDeclaration", "varDeclaration", 
                   "methodDeclaration", "type_", "statement", "expression", 
                   "identifier" ]

    EOF = Token.EOF
    CLASS=1
    LPAREN=2
    RPAREN=3
    LBRACE=4
    RBRACE=5
    LBRACK=6
    RBRACK=7
    SEMI=8
    COMMA=9
    DOT=10
    TRUE=11
    FALSE=12
    PUBLIC=13
    STATIC=14
    VOID=15
    MAIN=16
    STRING=17
    EXTENDS=18
    RETURN=19
    INT=20
    BOOLEAN=21
    IF=22
    ELSE=23
    WHILE=24
    SOUT=25
    ASSIGN=26
    ADD=27
    SUB=28
    MUL=29
    LT=30
    ANDAND=31
    LEN=32
    NOT=33
    NEW=34
    THIS=35
    WS=36
    COMMENT=37
    LINE_COMMENT=38
    IDENTIFIER=39
    INTEGER_LITERAL=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    temp_counter = 0
    goto_counter = 0
    def create_goto(self):
        self.goto_counter += 1
        return 'L' + str(self.goto_counter)
    def create_temp(self):
        self.temp_counter += 1
        return 'T' + str(self.temp_counter)
    def remove_temp(self):
        self.temp_counter -= 1
    def get_temp(self):
        return 'T' + str(self.temp_counter)



    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mainClass(self):
            return self.getTypedRuleContext(MiniJavaParser.MainClassContext,0)


        def EOF(self):
            return self.getToken(MiniJavaParser.EOF, 0)

        def classDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ClassDeclarationContext,i)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniJavaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            print('\nTAC generated for statements:')
            self.state = 19
            self.mainClass()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaParser.CLASS:
                self.state = 20
                self.classDeclaration()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(MiniJavaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainClassContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None # StatementContext

        def CLASS(self):
            return self.getToken(MiniJavaParser.CLASS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,i)


        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaParser.LBRACE)
            else:
                return self.getToken(MiniJavaParser.LBRACE, i)

        def PUBLIC(self):
            return self.getToken(MiniJavaParser.PUBLIC, 0)

        def STATIC(self):
            return self.getToken(MiniJavaParser.STATIC, 0)

        def VOID(self):
            return self.getToken(MiniJavaParser.VOID, 0)

        def MAIN(self):
            return self.getToken(MiniJavaParser.MAIN, 0)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)

        def STRING(self):
            return self.getToken(MiniJavaParser.STRING, 0)

        def LBRACK(self):
            return self.getToken(MiniJavaParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniJavaParser.RBRACK, 0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaParser.RBRACE)
            else:
                return self.getToken(MiniJavaParser.RBRACE, i)

        def statement(self):
            return self.getTypedRuleContext(MiniJavaParser.StatementContext,0)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_mainClass

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainClass" ):
                listener.enterMainClass(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainClass" ):
                listener.exitMainClass(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainClass" ):
                return visitor.visitMainClass(self)
            else:
                return visitor.visitChildren(self)




    def mainClass(self):

        localctx = MiniJavaParser.MainClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mainClass)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(MiniJavaParser.CLASS)
            self.state = 29
            self.identifier()
            self.state = 30
            self.match(MiniJavaParser.LBRACE)
            self.state = 31
            self.match(MiniJavaParser.PUBLIC)
            self.state = 32
            self.match(MiniJavaParser.STATIC)
            self.state = 33
            self.match(MiniJavaParser.VOID)
            self.state = 34
            self.match(MiniJavaParser.MAIN)
            self.state = 35
            self.match(MiniJavaParser.LPAREN)
            self.state = 36
            self.match(MiniJavaParser.STRING)
            self.state = 37
            self.match(MiniJavaParser.LBRACK)
            self.state = 38
            self.match(MiniJavaParser.RBRACK)
            self.state = 39
            self.identifier()
            self.state = 40
            self.match(MiniJavaParser.RPAREN)
            self.state = 41
            self.match(MiniJavaParser.LBRACE)
            self.state = 42
            localctx.s = self.statement()
            self.state = 43
            self.match(MiniJavaParser.RBRACE)
            self.state = 44
            self.match(MiniJavaParser.RBRACE)
            print(localctx.s.value_attr)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(MiniJavaParser.CLASS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,i)


        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)

        def EXTENDS(self):
            return self.getToken(MiniJavaParser.EXTENDS, 0)

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.VarDeclarationContext,i)


        def methodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.MethodDeclarationContext,i)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_classDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDeclaration" ):
                listener.enterClassDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDeclaration" ):
                listener.exitClassDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDeclaration" ):
                return visitor.visitClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def classDeclaration(self):

        localctx = MiniJavaParser.ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MiniJavaParser.CLASS)
            self.state = 48
            self.identifier()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniJavaParser.EXTENDS:
                self.state = 49
                self.match(MiniJavaParser.EXTENDS)
                self.state = 50
                self.identifier()


            self.state = 53
            self.match(MiniJavaParser.LBRACE)
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaParser.INT) | (1 << MiniJavaParser.BOOLEAN) | (1 << MiniJavaParser.IDENTIFIER))) != 0):
                self.state = 54
                self.varDeclaration()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniJavaParser.PUBLIC:
                self.state = 60
                self.methodDeclaration()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(MiniJavaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None # Type_Context
            self.i = None # IdentifierContext

        def SEMI(self):
            return self.getToken(MiniJavaParser.SEMI, 0)

        def type_(self):
            return self.getTypedRuleContext(MiniJavaParser.Type_Context,0)


        def identifier(self):
            return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_varDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDeclaration" ):
                listener.enterVarDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDeclaration" ):
                listener.exitVarDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclaration" ):
                return visitor.visitVarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def varDeclaration(self):

        localctx = MiniJavaParser.VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            localctx.t = self.type_()
            self.state = 69
            localctx.i = self.identifier()
            self.state = 70
            self.match(MiniJavaParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None # StatementContext

        def PUBLIC(self):
            return self.getToken(MiniJavaParser.PUBLIC, 0)

        def type_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.Type_Context)
            else:
                return self.getTypedRuleContext(MiniJavaParser.Type_Context,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,i)


        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)

        def RETURN(self):
            return self.getToken(MiniJavaParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(MiniJavaParser.SEMI, 0)

        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)

        def varDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.VarDeclarationContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.VarDeclarationContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.StatementContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaParser.COMMA)
            else:
                return self.getToken(MiniJavaParser.COMMA, i)

        def getRuleIndex(self):
            return MiniJavaParser.RULE_methodDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMethodDeclaration" ):
                listener.enterMethodDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMethodDeclaration" ):
                listener.exitMethodDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDeclaration" ):
                return visitor.visitMethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def methodDeclaration(self):

        localctx = MiniJavaParser.MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_methodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(MiniJavaParser.PUBLIC)
            self.state = 73
            self.type_()
            self.state = 74
            self.identifier()
            self.state = 75
            self.match(MiniJavaParser.LPAREN)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaParser.INT) | (1 << MiniJavaParser.BOOLEAN) | (1 << MiniJavaParser.IDENTIFIER))) != 0):
                self.state = 76
                self.type_()
                self.state = 77
                self.identifier()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniJavaParser.COMMA:
                    self.state = 78
                    self.match(MiniJavaParser.COMMA)
                    self.state = 79
                    self.type_()
                    self.state = 80
                    self.identifier()
                    self.state = 86
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 89
            self.match(MiniJavaParser.RPAREN)
            self.state = 90
            self.match(MiniJavaParser.LBRACE)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 91
                    self.varDeclaration() 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaParser.LBRACE) | (1 << MiniJavaParser.IF) | (1 << MiniJavaParser.WHILE) | (1 << MiniJavaParser.SOUT) | (1 << MiniJavaParser.IDENTIFIER))) != 0):
                self.state = 97
                localctx.s = self.statement()
                print(localctx.s.value_attr)
                self.state = 104
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 105
            self.match(MiniJavaParser.RETURN)
            self.state = 106
            self.expression(0)
            self.state = 107
            self.match(MiniJavaParser.SEMI)
            self.state = 108
            self.match(MiniJavaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.i = None # IdentifierContext

        def INT(self):
            return self.getToken(MiniJavaParser.INT, 0)

        def LBRACK(self):
            return self.getToken(MiniJavaParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniJavaParser.RBRACK, 0)

        def BOOLEAN(self):
            return self.getToken(MiniJavaParser.BOOLEAN, 0)

        def identifier(self):
            return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,0)


        def getRuleIndex(self):
            return MiniJavaParser.RULE_type_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_" ):
                listener.enterType_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_" ):
                listener.exitType_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_" ):
                return visitor.visitType_(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = MiniJavaParser.Type_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type_)
        try:
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 110
                self.match(MiniJavaParser.INT)
                self.state = 111
                self.match(MiniJavaParser.LBRACK)
                self.state = 112
                self.match(MiniJavaParser.RBRACK)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(MiniJavaParser.BOOLEAN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.match(MiniJavaParser.INT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 115
                localctx.i = self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.old_value_attr = str()
            self.s = None # StatementContext
            self.e = None # ExpressionContext
            self.s1 = None # StatementContext
            self.s2 = None # StatementContext
            self.i = None # IdentifierContext
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext

        def LBRACE(self):
            return self.getToken(MiniJavaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniJavaParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.StatementContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.StatementContext,i)


        def IF(self):
            return self.getToken(MiniJavaParser.IF, 0)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)

        def ELSE(self):
            return self.getToken(MiniJavaParser.ELSE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def WHILE(self):
            return self.getToken(MiniJavaParser.WHILE, 0)

        def SOUT(self):
            return self.getToken(MiniJavaParser.SOUT, 0)

        def SEMI(self):
            return self.getToken(MiniJavaParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(MiniJavaParser.ASSIGN, 0)

        def identifier(self):
            return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,0)


        def LBRACK(self):
            return self.getToken(MiniJavaParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(MiniJavaParser.RBRACK, 0)

        def getRuleIndex(self):
            return MiniJavaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniJavaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 118
                self.match(MiniJavaParser.LBRACE)
                localctx.value_attr=''
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaParser.LBRACE) | (1 << MiniJavaParser.IF) | (1 << MiniJavaParser.WHILE) | (1 << MiniJavaParser.SOUT) | (1 << MiniJavaParser.IDENTIFIER))) != 0):
                    self.state = 120
                    localctx.s = self.statement()
                    localctx.value_attr=localctx.value_attr+localctx.s.value_attr+'\n'
                    self.state = 127
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 128
                self.match(MiniJavaParser.RBRACE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(MiniJavaParser.IF)
                self.state = 130
                self.match(MiniJavaParser.LPAREN)
                self.state = 131
                localctx.e = self.expression(0)
                self.state = 132
                self.match(MiniJavaParser.RPAREN)
                self.state = 133
                localctx.s1 = self.statement()
                self.state = 134
                self.match(MiniJavaParser.ELSE)
                self.state = 135
                localctx.s2 = self.statement()
                goto1 = self.create_goto()
                goto2 = self.create_goto()
                for item in localctx.e.temp_list:
                    localctx.value_attr = localctx.value_attr + item + '\n'
                    #print(item)
                #print('\t\t'+'if (',localctx.e.value_attr,') goto ',goto1)
                localctx.value_attr=localctx.value_attr+'\t\t'+'if ('+localctx.e.value_attr+') goto '+goto1+'\n'
                #print(localctx.s2.value_attr,end='')
                localctx.value_attr = localctx.value_attr + localctx.s2.value_attr
                #print('\t\t'+'goto ',goto2)
                localctx.value_attr= localctx.value_attr+'\t\t'+'goto '+goto2+'\n'
                #print(goto1,':',localctx.s1.value_attr,end='')
                localctx.value_attr = localctx.value_attr+goto1+':'+localctx.s1.value_attr
                #print(goto2,':\t\t',end='')
                localctx.value_attr= localctx.value_attr + goto2+':\t\t'
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 150
                self.match(MiniJavaParser.WHILE)
                self.state = 151
                self.match(MiniJavaParser.LPAREN)
                self.state = 152
                localctx.e = self.expression(0)
                self.state = 153
                self.match(MiniJavaParser.RPAREN)
                self.state = 154
                localctx.s = self.statement()
                goto1 = self.create_goto()
                goto2 = self.create_goto()
                localctx.value_attr= '\t\t'+'goto '+goto1+'\n'
                localctx.value_attr = localctx.value_attr+goto2+':'+localctx.s.value_attr
                localctx.value_attr= localctx.value_attr + goto1+':'
                for item in localctx.e.temp_list:
                    localctx.value_attr = localctx.value_attr + item + '\n'
                    #print(item)
                localctx.value_attr=localctx.value_attr+'\t\t'+'if ('+localctx.e.value_attr+') goto '+goto2+'\n'
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 163
                self.match(MiniJavaParser.SOUT)
                self.state = 164
                self.match(MiniJavaParser.LPAREN)
                self.state = 165
                self.expression(0)
                self.state = 166
                self.match(MiniJavaParser.RPAREN)
                self.state = 167
                self.match(MiniJavaParser.SEMI)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 169
                localctx.i = self.identifier()
                self.state = 170
                self.match(MiniJavaParser.ASSIGN)
                self.state = 171
                localctx.e = self.expression(0)
                self.state = 172
                self.match(MiniJavaParser.SEMI)
                localctx.value_attr = ''
                for item in localctx.e.temp_list:
                    localctx.value_attr=localctx.value_attr+item+'\n'
                localctx.value_attr=localctx.value_attr+'\t\t'+localctx.i.value_attr +' = '+ localctx.e.value_attr
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 177
                localctx.i = self.identifier()
                self.state = 178
                self.match(MiniJavaParser.LBRACK)
                self.state = 179
                localctx.e1 = self.expression(0)
                self.state = 180
                self.match(MiniJavaParser.RBRACK)
                self.state = 181
                self.match(MiniJavaParser.ASSIGN)
                self.state = 182
                localctx.e2 = self.expression(0)
                self.state = 183
                self.match(MiniJavaParser.SEMI)
                localctx.value_attr = ''
                for item in localctx.e1.temp_list:
                    localctx.value_attr=localctx.value_attr+item+'\n'
                for item in localctx.e2.temp_list:
                    localctx.value_attr=localctx.value_attr+item+'\n'
                temp = self.create_temp()
                localctx.value_attr=localctx.value_attr+'\t\t'+temp+ '='+'sizeOf('+ localctx.i.value_attr+')\n'+'\t\t'+temp+ '='+temp+'*'+localctx.e1.value_attr+'\n'+'\t\t'+temp+ '= &'+localctx.i.value_attr+'+'+temp+'\n'+'\t\t'+'*'+ temp +' = '+ localctx.e2.value_attr
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self.old_value_attr = str()
            self.temp_list = []


        def getRuleIndex(self):
            return MiniJavaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)
            self.value_attr = ctx.value_attr
            self.type_attr = ctx.type_attr
            self.old_value_attr = ctx.old_value_attr
            self.temp_list = ctx.temp_list


    class Expression6Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FALSE(self):
            return self.getToken(MiniJavaParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression6" ):
                listener.enterExpression6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression6" ):
                listener.exitExpression6(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)


    class Expression7Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.i = None # IdentifierContext
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression7" ):
                listener.enterExpression7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression7" ):
                listener.exitExpression7(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)


    class Expression4Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self._INTEGER_LITERAL = None # Token
            self.copyFrom(ctx)

        def INTEGER_LITERAL(self):
            return self.getToken(MiniJavaParser.INTEGER_LITERAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression4" ):
                listener.enterExpression4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression4" ):
                listener.exitExpression4(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)


    class Expression5Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(MiniJavaParser.TRUE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression5" ):
                listener.enterExpression5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression5" ):
                listener.exitExpression5(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)


    class Expression2Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e = None # ExpressionContext
            self.copyFrom(ctx)

        def DOT(self):
            return self.getToken(MiniJavaParser.DOT, 0)
        def LEN(self):
            return self.getToken(MiniJavaParser.LEN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression2" ):
                listener.enterExpression2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression2" ):
                listener.exitExpression2(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)


    class Expression3Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)

        def DOT(self):
            return self.getToken(MiniJavaParser.DOT, 0)
        def identifier(self):
            return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,0)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniJavaParser.COMMA)
            else:
                return self.getToken(MiniJavaParser.COMMA, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression3" ):
                listener.enterExpression3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression3" ):
                listener.exitExpression3(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)


    class Expression1Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.copyFrom(ctx)

        def LBRACK(self):
            return self.getToken(MiniJavaParser.LBRACK, 0)
        def RBRACK(self):
            return self.getToken(MiniJavaParser.RBRACK, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression1" ):
                listener.enterExpression1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression1" ):
                listener.exitExpression1(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)


    class Expression8Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def THIS(self):
            return self.getToken(MiniJavaParser.THIS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression8" ):
                listener.enterExpression8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression8" ):
                listener.exitExpression8(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)


    class Expression10Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(MiniJavaParser.NEW, 0)
        def identifier(self):
            return self.getTypedRuleContext(MiniJavaParser.IdentifierContext,0)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression10" ):
                listener.enterExpression10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression10" ):
                listener.exitExpression10(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)


    class Expression9Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEW(self):
            return self.getToken(MiniJavaParser.NEW, 0)
        def INT(self):
            return self.getToken(MiniJavaParser.INT, 0)
        def LBRACK(self):
            return self.getToken(MiniJavaParser.LBRACK, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,0)

        def RBRACK(self):
            return self.getToken(MiniJavaParser.RBRACK, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression9" ):
                listener.enterExpression9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression9" ):
                listener.exitExpression9(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)


    class Expression12Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e = None # ExpressionContext
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(MiniJavaParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(MiniJavaParser.RPAREN, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression12" ):
                listener.enterExpression12(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression12" ):
                listener.exitExpression12(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression12" ):
                return visitor.visitExpression12(self)
            else:
                return visitor.visitChildren(self)


    class Expression01Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.copyFrom(ctx)

        def MUL(self):
            return self.getToken(MiniJavaParser.MUL, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression01" ):
                listener.enterExpression01(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression01" ):
                listener.exitExpression01(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression01" ):
                return visitor.visitExpression01(self)
            else:
                return visitor.visitChildren(self)


    class Expression11Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e = None # ExpressionContext
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MiniJavaParser.NOT, 0)
        def expression(self):
            return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression11" ):
                listener.enterExpression11(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression11" ):
                listener.exitExpression11(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)


    class Expression00Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.copyFrom(ctx)

        def ANDAND(self):
            return self.getToken(MiniJavaParser.ANDAND, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression00" ):
                listener.enterExpression00(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression00" ):
                listener.exitExpression00(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression00" ):
                return visitor.visitExpression00(self)
            else:
                return visitor.visitChildren(self)


    class Expression03Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.copyFrom(ctx)

        def ADD(self):
            return self.getToken(MiniJavaParser.ADD, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression03" ):
                listener.enterExpression03(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression03" ):
                listener.exitExpression03(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression03" ):
                return visitor.visitExpression03(self)
            else:
                return visitor.visitChildren(self)


    class Expression02Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.copyFrom(ctx)

        def LT(self):
            return self.getToken(MiniJavaParser.LT, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression02" ):
                listener.enterExpression02(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression02" ):
                listener.exitExpression02(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression02" ):
                return visitor.visitExpression02(self)
            else:
                return visitor.visitChildren(self)


    class Expression04Context(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MiniJavaParser.ExpressionContext
            super().__init__(parser)
            self.e1 = None # ExpressionContext
            self.e2 = None # ExpressionContext
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(MiniJavaParser.SUB, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniJavaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MiniJavaParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression04" ):
                listener.enterExpression04(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression04" ):
                listener.exitExpression04(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression04" ):
                return visitor.visitExpression04(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniJavaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = MiniJavaParser.Expression12Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 193
                self.match(MiniJavaParser.LPAREN)
                self.state = 194
                localctx.e = self.expression(0)
                self.state = 195
                self.match(MiniJavaParser.RPAREN)
                localctx.type_attr = localctx.e.type_attr
                localctx.value_attr = localctx.e.value_attr
                localctx.old_value_attr = localctx.e.old_value_attr
                localctx.temp_list = localctx.e.temp_list
                pass

            elif la_ == 2:
                localctx = MiniJavaParser.Expression4Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 201
                localctx._INTEGER_LITERAL = self.match(MiniJavaParser.INTEGER_LITERAL)

                localctx.type_attr = 'INT'
                localctx.value_attr = (None if localctx._INTEGER_LITERAL is None else localctx._INTEGER_LITERAL.text)
                localctx.old_value_attr = None

                pass

            elif la_ == 3:
                localctx = MiniJavaParser.Expression5Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 203
                self.match(MiniJavaParser.TRUE)

                localctx.type_attr = 'BOOL'
                localctx.value_attr = 'true'
                localctx.old_value_attr = None

                pass

            elif la_ == 4:
                localctx = MiniJavaParser.Expression6Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 205
                self.match(MiniJavaParser.FALSE)

                localctx.type_attr = 'BOOL'
                localctx.value_attr = 'false'
                localctx.old_value_attr = None

                pass

            elif la_ == 5:
                localctx = MiniJavaParser.Expression7Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 207
                localctx.i = self.identifier()

                if localctx.i.type_attr != 'UNKOWN':
                    print('Semantic error in "'+localctx.i.value_attr+'" Identifier: "'+localctx.i.value_attr+'" is not Declared!')
                else:
                    localctx.type_attr = localctx.i.type_attr
                    localctx.value_attr = localctx.i.value_attr
                    localctx.old_value_attr = None

                pass

            elif la_ == 6:
                localctx = MiniJavaParser.Expression8Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 210
                self.match(MiniJavaParser.THIS)
                # object reference is not TAC convertable! or is it? don't know don't care!
                pass

            elif la_ == 7:
                localctx = MiniJavaParser.Expression9Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 212
                self.match(MiniJavaParser.NEW)
                self.state = 213
                self.match(MiniJavaParser.INT)
                self.state = 214
                self.match(MiniJavaParser.LBRACK)
                self.state = 215
                self.expression(0)
                self.state = 216
                self.match(MiniJavaParser.RBRACK)
                # initialization is not TAC convertable! or is it? don't know don't care!
                pass

            elif la_ == 8:
                localctx = MiniJavaParser.Expression10Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 219
                self.match(MiniJavaParser.NEW)
                self.state = 220
                self.identifier()
                self.state = 221
                self.match(MiniJavaParser.LPAREN)
                self.state = 222
                self.match(MiniJavaParser.RPAREN)
                # initialization is not TAC convertable! or is it? don't know don't care!
                pass

            elif la_ == 9:
                localctx = MiniJavaParser.Expression11Context(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 225
                self.match(MiniJavaParser.NOT)
                self.state = 226
                localctx.e = self.expression(1)
                localctx.temp_list = localctx.e.temp_list
                localctx.type_attr = 'BOOL'
                if localctx.e.old_value_attr is not None:
                        temp = self.create_temp()
                        localctx.temp_list.append('\t\t'+temp+'='+localctx.e.old_value_attr)
                        #print('\t\t',temp, '=', localctx.e.old_value_attr)
                        localctx.e1.value_attr = temp
                localctx.value_attr = '!'+localctx.e.value_attr
                localctx.old_value_attr = '!'+localctx.e.value_attr
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 333
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 331
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        localctx = MiniJavaParser.Expression02Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 235
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 236
                        self.match(MiniJavaParser.LT)
                        self.state = 237
                        localctx.e2 = self.expression(17)
                        localctx.temp_list = localctx.e1.temp_list
                        localctx.type_attr = 'BOOL'
                        if localctx.e1.old_value_attr is not None:
                                      temp = self.create_temp()
                                      localctx.temp_list.append('\t\t'+temp+'='+localctx.e1.old_value_attr)
                                      #print('\t\t',temp, '=', localctx.e1.old_value_attr)
                                      localctx.e1.value_attr = temp
                        localctx.temp_list =localctx.temp_list + localctx.e2.temp_list
                        if localctx.e2.old_value_attr is not None:
                                      temp = self.create_temp()
                                      localctx.temp_list.append('\t\t'+temp+'='+localctx.e2.old_value_attr)
                                      #print('\t\t',temp, '=', localctx.e2.old_value_attr)
                                      localctx.e2.value_attr = temp
                        localctx.value_attr = localctx.e1.value_attr + " < " + localctx.e2.value_attr
                        localctx.old_value_attr = localctx.e1.value_attr + " < " + localctx.e2.value_attr
                        pass

                    elif la_ == 2:
                        localctx = MiniJavaParser.Expression00Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 246
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 247
                        self.match(MiniJavaParser.ANDAND)
                        self.state = 248
                        localctx.e2 = self.expression(16)
                        localctx.type_attr = 'BOOL'
                        localctx.temp_list = localctx.e1.temp_list
                        if localctx.e1.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e1.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e1.old_value_attr)
                                          localctx.e1.value_attr = temp
                        localctx.temp_list =localctx.temp_list + localctx.e2.temp_list
                        if localctx.e2.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e2.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e2.old_value_attr)
                                          localctx.e2.value_attr = temp
                        localctx.value_attr = localctx.e1.value_attr + " && " + localctx.e2.value_attr
                        localctx.old_value_attr = localctx.e1.value_attr + " && " + localctx.e2.value_attr
                        pass

                    elif la_ == 3:
                        localctx = MiniJavaParser.Expression01Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 257
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 258
                        self.match(MiniJavaParser.MUL)
                        self.state = 259
                        localctx.e2 = self.expression(15)
                        localctx.temp_list = localctx.e1.temp_list
                        localctx.type_attr = 'INT'
                        if localctx.e1.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e1.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e1.old_value_attr)
                                          localctx.e1.value_attr = temp
                        localctx.temp_list =localctx.temp_list + localctx.e2.temp_list
                        if localctx.e2.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e2.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e2.old_value_attr)
                                          localctx.e2.value_attr = temp
                        localctx.value_attr = localctx.e1.value_attr + " * " + localctx.e2.value_attr
                        localctx.old_value_attr = localctx.e1.value_attr + " * " + localctx.e2.value_attr
                        pass

                    elif la_ == 4:
                        localctx = MiniJavaParser.Expression03Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 268
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 269
                        self.match(MiniJavaParser.ADD)
                        self.state = 270
                        localctx.e2 = self.expression(14)
                        localctx.temp_list = localctx.e1.temp_list
                        localctx.type_attr = 'INT'
                        if localctx.e1.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e1.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e1.old_value_attr)
                                          localctx.e1.value_attr = temp
                        localctx.temp_list =localctx.temp_list + localctx.e2.temp_list
                        if localctx.e2.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e2.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e2.old_value_attr)
                                          localctx.e2.value_attr = temp
                        localctx.value_attr = localctx.e1.value_attr + " + " + localctx.e2.value_attr
                        localctx.old_value_attr = localctx.e1.value_attr + " + " + localctx.e2.value_attr
                        pass

                    elif la_ == 5:
                        localctx = MiniJavaParser.Expression04Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 279
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 280
                        self.match(MiniJavaParser.SUB)
                        self.state = 281
                        localctx.e2 = self.expression(13)
                        localctx.temp_list = localctx.e1.temp_list
                        localctx.type_attr = 'INT'
                        if localctx.e1.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e1.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e1.old_value_attr)
                                          localctx.e1.value_attr = temp
                        localctx.temp_list =localctx.temp_list + localctx.e2.temp_list
                        if localctx.e2.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e2.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e2.old_value_attr)
                                          localctx.e2.value_attr = temp
                        localctx.value_attr = localctx.e1.value_attr + " - " + localctx.e2.value_attr
                        localctx.old_value_attr = localctx.e1.value_attr + " - " + localctx.e2.value_attr
                        pass

                    elif la_ == 6:
                        localctx = MiniJavaParser.Expression1Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e1 = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 290
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 291
                        self.match(MiniJavaParser.LBRACK)
                        self.state = 292
                        localctx.e2 = self.expression(0)
                        self.state = 293
                        self.match(MiniJavaParser.RBRACK)
                        localctx.temp_list = localctx.e1.temp_list
                        localctx.temp_list =localctx.temp_list + localctx.e2.temp_list
                        localctx.type_attr = 'INT'
                        if localctx.e1.old_value_attr is not None:
                                          print('\t\t','Semantic error in '+localctx.e1.value_attr+' : only Arrays are itratable!')
                        if localctx.e2.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e2.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e2.old_value_attr)
                                          localctx.e2.value_attr = temp
                        temp = self.create_temp()
                        localctx.temp_list.append('\t\t'+temp+ '='+'sizeOf('+ localctx.e1.value_attr+')')
                        localctx.temp_list.append('\t\t'+temp+ '='+temp+'*'+localctx.e2.value_attr)
                        localctx.temp_list.append('\t\t'+temp+ '= &'+localctx.e1.value_attr+'+'+temp)
                        localctx.value_attr = '*'+temp
                        localctx.old_value_attr = '*'+temp
                        pass

                    elif la_ == 7:
                        localctx = MiniJavaParser.Expression2Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        localctx.e = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 306
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 307
                        self.match(MiniJavaParser.DOT)
                        self.state = 308
                        self.match(MiniJavaParser.LEN)
                        localctx.temp_list = localctx.e.temp_list
                        localctx.type_attr = 'INT'
                        if localctx.e.old_value_attr is not None:
                                          temp = self.create_temp()
                                          localctx.temp_list.append('\t\t'+temp+'='+localctx.e.old_value_attr)
                                          #print('\t\t',temp, '=', localctx.e.old_value_attr)
                                          localctx.e.value_attr = temp
                        localctx.value_attr = localctx.e.value_attr + ".length "
                        localctx.old_value_attr = localctx.e.value_attr + ".length "
                        pass

                    elif la_ == 8:
                        localctx = MiniJavaParser.Expression3Context(self, MiniJavaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 314
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 315
                        self.match(MiniJavaParser.DOT)
                        self.state = 316
                        self.identifier()
                        self.state = 317
                        self.match(MiniJavaParser.LPAREN)
                        self.state = 326
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniJavaParser.LPAREN) | (1 << MiniJavaParser.TRUE) | (1 << MiniJavaParser.FALSE) | (1 << MiniJavaParser.NOT) | (1 << MiniJavaParser.NEW) | (1 << MiniJavaParser.THIS) | (1 << MiniJavaParser.IDENTIFIER) | (1 << MiniJavaParser.INTEGER_LITERAL))) != 0):
                            self.state = 318
                            self.expression(0)
                            self.state = 323
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            while _la==MiniJavaParser.COMMA:
                                self.state = 319
                                self.match(MiniJavaParser.COMMA)
                                self.state = 320
                                self.expression(0)
                                self.state = 325
                                self._errHandler.sync(self)
                                _la = self._input.LA(1)



                        self.state = 328
                        self.match(MiniJavaParser.RPAREN)
                        # Function call is not TAC convertable! or is it? don't know don't care!
                        pass

             
                self.state = 335
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value_attr = str()
            self.type_attr = str()
            self._IDENTIFIER = None # Token

        def IDENTIFIER(self):
            return self.getToken(MiniJavaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MiniJavaParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = MiniJavaParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            localctx._IDENTIFIER = self.match(MiniJavaParser.IDENTIFIER)

            localctx.value_attr = (None if localctx._IDENTIFIER is None else localctx._IDENTIFIER.text)
            localctx.type_attr = 'UNKOWN'

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 9)
         




