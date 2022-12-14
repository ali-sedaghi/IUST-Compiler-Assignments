from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u012f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\6%")
        buf.write("\u00f8\n%\r%\16%\u00f9\3%\3%\3&\3&\3&\3&\7&\u0102\n&\f")
        buf.write("&\16&\u0105\13&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\7\'\u0110")
        buf.write("\n\'\f\'\16\'\u0113\13\'\3\'\3\'\3(\3(\7(\u0119\n(\f(")
        buf.write("\16(\u011c\13(\3)\3)\3)\7)\u0121\n)\f)\16)\u0124\13)\5")
        buf.write(")\u0126\n)\3*\3*\3+\3+\3,\3,\5,\u012e\n,\3\u0103\2-\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S\2U\2W\2\3\2\7\5\2\13\f\16\17\"\"\4\2\f\f\17\17\3\2\63")
        buf.write(";\3\2\62;\5\2C\\aac|\2\u0132\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\3Y\3\2\2\2\5_\3\2\2\2\7a\3\2\2\2\tc")
        buf.write("\3\2\2\2\13e\3\2\2\2\rg\3\2\2\2\17i\3\2\2\2\21k\3\2\2")
        buf.write("\2\23m\3\2\2\2\25o\3\2\2\2\27q\3\2\2\2\31v\3\2\2\2\33")
        buf.write("|\3\2\2\2\35\u0083\3\2\2\2\37\u008a\3\2\2\2!\u008f\3\2")
        buf.write("\2\2#\u0094\3\2\2\2%\u009b\3\2\2\2\'\u00a3\3\2\2\2)\u00aa")
        buf.write("\3\2\2\2+\u00ae\3\2\2\2-\u00b6\3\2\2\2/\u00b9\3\2\2\2")
        buf.write("\61\u00be\3\2\2\2\63\u00c4\3\2\2\2\65\u00d7\3\2\2\2\67")
        buf.write("\u00d9\3\2\2\29\u00db\3\2\2\2;\u00dd\3\2\2\2=\u00df\3")
        buf.write("\2\2\2?\u00e1\3\2\2\2A\u00e4\3\2\2\2C\u00eb\3\2\2\2E\u00ed")
        buf.write("\3\2\2\2G\u00f1\3\2\2\2I\u00f7\3\2\2\2K\u00fd\3\2\2\2")
        buf.write("M\u010b\3\2\2\2O\u0116\3\2\2\2Q\u0125\3\2\2\2S\u0127\3")
        buf.write("\2\2\2U\u0129\3\2\2\2W\u012d\3\2\2\2YZ\7e\2\2Z[\7n\2\2")
        buf.write("[\\\7c\2\2\\]\7u\2\2]^\7u\2\2^\4\3\2\2\2_`\7*\2\2`\6\3")
        buf.write("\2\2\2ab\7+\2\2b\b\3\2\2\2cd\7}\2\2d\n\3\2\2\2ef\7\177")
        buf.write("\2\2f\f\3\2\2\2gh\7]\2\2h\16\3\2\2\2ij\7_\2\2j\20\3\2")
        buf.write("\2\2kl\7=\2\2l\22\3\2\2\2mn\7.\2\2n\24\3\2\2\2op\7\60")
        buf.write("\2\2p\26\3\2\2\2qr\7v\2\2rs\7t\2\2st\7w\2\2tu\7g\2\2u")
        buf.write("\30\3\2\2\2vw\7h\2\2wx\7c\2\2xy\7n\2\2yz\7u\2\2z{\7g\2")
        buf.write("\2{\32\3\2\2\2|}\7r\2\2}~\7w\2\2~\177\7d\2\2\177\u0080")
        buf.write("\7n\2\2\u0080\u0081\7k\2\2\u0081\u0082\7e\2\2\u0082\34")
        buf.write("\3\2\2\2\u0083\u0084\7u\2\2\u0084\u0085\7v\2\2\u0085\u0086")
        buf.write("\7c\2\2\u0086\u0087\7v\2\2\u0087\u0088\7k\2\2\u0088\u0089")
        buf.write("\7e\2\2\u0089\36\3\2\2\2\u008a\u008b\7x\2\2\u008b\u008c")
        buf.write("\7q\2\2\u008c\u008d\7k\2\2\u008d\u008e\7f\2\2\u008e \3")
        buf.write("\2\2\2\u008f\u0090\7o\2\2\u0090\u0091\7c\2\2\u0091\u0092")
        buf.write("\7k\2\2\u0092\u0093\7p\2\2\u0093\"\3\2\2\2\u0094\u0095")
        buf.write("\7U\2\2\u0095\u0096\7v\2\2\u0096\u0097\7t\2\2\u0097\u0098")
        buf.write("\7k\2\2\u0098\u0099\7p\2\2\u0099\u009a\7i\2\2\u009a$\3")
        buf.write("\2\2\2\u009b\u009c\7g\2\2\u009c\u009d\7z\2\2\u009d\u009e")
        buf.write("\7v\2\2\u009e\u009f\7g\2\2\u009f\u00a0\7p\2\2\u00a0\u00a1")
        buf.write("\7f\2\2\u00a1\u00a2\7u\2\2\u00a2&\3\2\2\2\u00a3\u00a4")
        buf.write("\7t\2\2\u00a4\u00a5\7g\2\2\u00a5\u00a6\7v\2\2\u00a6\u00a7")
        buf.write("\7w\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7p\2\2\u00a9(\3")
        buf.write("\2\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad*\3\2\2\2\u00ae\u00af\7d\2\2\u00af\u00b0")
        buf.write("\7q\2\2\u00b0\u00b1\7q\2\2\u00b1\u00b2\7n\2\2\u00b2\u00b3")
        buf.write("\7g\2\2\u00b3\u00b4\7c\2\2\u00b4\u00b5\7p\2\2\u00b5,\3")
        buf.write("\2\2\2\u00b6\u00b7\7k\2\2\u00b7\u00b8\7h\2\2\u00b8.\3")
        buf.write("\2\2\2\u00b9\u00ba\7g\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\60\3\2\2\2\u00be\u00bf")
        buf.write("\7y\2\2\u00bf\u00c0\7j\2\2\u00c0\u00c1\7k\2\2\u00c1\u00c2")
        buf.write("\7n\2\2\u00c2\u00c3\7g\2\2\u00c3\62\3\2\2\2\u00c4\u00c5")
        buf.write("\7U\2\2\u00c5\u00c6\7{\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8")
        buf.write("\7v\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7o\2\2\u00ca\u00cb")
        buf.write("\7\60\2\2\u00cb\u00cc\7q\2\2\u00cc\u00cd\7w\2\2\u00cd")
        buf.write("\u00ce\7v\2\2\u00ce\u00cf\7\60\2\2\u00cf\u00d0\7r\2\2")
        buf.write("\u00d0\u00d1\7t\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7p")
        buf.write("\2\2\u00d3\u00d4\7v\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7p\2\2\u00d6\64\3\2\2\2\u00d7\u00d8\7?\2\2\u00d8\66\3")
        buf.write("\2\2\2\u00d9\u00da\7-\2\2\u00da8\3\2\2\2\u00db\u00dc\7")
        buf.write("/\2\2\u00dc:\3\2\2\2\u00dd\u00de\7,\2\2\u00de<\3\2\2\2")
        buf.write("\u00df\u00e0\7>\2\2\u00e0>\3\2\2\2\u00e1\u00e2\7(\2\2")
        buf.write("\u00e2\u00e3\7(\2\2\u00e3@\3\2\2\2\u00e4\u00e5\7n\2\2")
        buf.write("\u00e5\u00e6\7g\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7i")
        buf.write("\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea\7j\2\2\u00eaB\3\2")
        buf.write("\2\2\u00eb\u00ec\7#\2\2\u00ecD\3\2\2\2\u00ed\u00ee\7p")
        buf.write("\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7y\2\2\u00f0F\3\2")
        buf.write("\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3\7j\2\2\u00f3\u00f4")
        buf.write("\7k\2\2\u00f4\u00f5\7u\2\2\u00f5H\3\2\2\2\u00f6\u00f8")
        buf.write("\t\2\2\2\u00f7\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9")
        buf.write("\u00f7\3\2\2\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\3\2\2\2")
        buf.write("\u00fb\u00fc\b%\2\2\u00fcJ\3\2\2\2\u00fd\u00fe\7\61\2")
        buf.write("\2\u00fe\u00ff\7,\2\2\u00ff\u0103\3\2\2\2\u0100\u0102")
        buf.write("\13\2\2\2\u0101\u0100\3\2\2\2\u0102\u0105\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0103\u0101\3\2\2\2\u0104\u0106\3\2\2\2")
        buf.write("\u0105\u0103\3\2\2\2\u0106\u0107\7,\2\2\u0107\u0108\7")
        buf.write("\61\2\2\u0108\u0109\3\2\2\2\u0109\u010a\b&\2\2\u010aL")
        buf.write("\3\2\2\2\u010b\u010c\7\61\2\2\u010c\u010d\7\61\2\2\u010d")
        buf.write("\u0111\3\2\2\2\u010e\u0110\n\3\2\2\u010f\u010e\3\2\2\2")
        buf.write("\u0110\u0113\3\2\2\2\u0111\u010f\3\2\2\2\u0111\u0112\3")
        buf.write("\2\2\2\u0112\u0114\3\2\2\2\u0113\u0111\3\2\2\2\u0114\u0115")
        buf.write("\b\'\2\2\u0115N\3\2\2\2\u0116\u011a\5U+\2\u0117\u0119")
        buf.write("\5W,\2\u0118\u0117\3\2\2\2\u0119\u011c\3\2\2\2\u011a\u0118")
        buf.write("\3\2\2\2\u011a\u011b\3\2\2\2\u011bP\3\2\2\2\u011c\u011a")
        buf.write("\3\2\2\2\u011d\u0126\7\62\2\2\u011e\u0122\t\4\2\2\u011f")
        buf.write("\u0121\5S*\2\u0120\u011f\3\2\2\2\u0121\u0124\3\2\2\2\u0122")
        buf.write("\u0120\3\2\2\2\u0122\u0123\3\2\2\2\u0123\u0126\3\2\2\2")
        buf.write("\u0124\u0122\3\2\2\2\u0125\u011d\3\2\2\2\u0125\u011e\3")
        buf.write("\2\2\2\u0126R\3\2\2\2\u0127\u0128\t\5\2\2\u0128T\3\2\2")
        buf.write("\2\u0129\u012a\t\6\2\2\u012aV\3\2\2\2\u012b\u012e\5U+")
        buf.write("\2\u012c\u012e\5S*\2\u012d\u012b\3\2\2\2\u012d\u012c\3")
        buf.write("\2\2\2\u012eX\3\2\2\2\n\2\u00f9\u0103\u0111\u011a\u0122")
        buf.write("\u0125\u012d\3\2\3\2")
        return buf.getvalue()


class MiniJavaLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CLASS = 1
    LPAREN = 2
    RPAREN = 3
    LBRACE = 4
    RBRACE = 5
    LBRACK = 6
    RBRACK = 7
    SEMI = 8
    COMMA = 9
    DOT = 10
    TRUE = 11
    FALSE = 12
    PUBLIC = 13
    STATIC = 14
    VOID = 15
    MAIN = 16
    STRING = 17
    EXTENDS = 18
    RETURN = 19
    INT = 20
    BOOLEAN = 21
    IF = 22
    ELSE = 23
    WHILE = 24
    SOUT = 25
    ASSIGN = 26
    ADD = 27
    SUB = 28
    MUL = 29
    LT = 30
    ANDAND = 31
    LEN = 32
    NOT = 33
    NEW = 34
    THIS = 35
    WS = 36
    COMMENT = 37
    LINE_COMMENT = 38
    IDENTIFIER = 39
    INTEGER_LITERAL = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'class'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "'.'", "'true'", "'false'", "'public'", "'static'", "'void'", 
            "'main'", "'String'", "'extends'", "'return'", "'int'", "'boolean'", 
            "'if'", "'else'", "'while'", "'System.out.println'", "'='", 
            "'+'", "'-'", "'*'", "'<'", "'&&'", "'length'", "'!'", "'new'", 
            "'this'" ]

    symbolicNames = [ "<INVALID>",
            "CLASS", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", "RBRACK", 
            "SEMI", "COMMA", "DOT", "TRUE", "FALSE", "PUBLIC", "STATIC", 
            "VOID", "MAIN", "STRING", "EXTENDS", "RETURN", "INT", "BOOLEAN", 
            "IF", "ELSE", "WHILE", "SOUT", "ASSIGN", "ADD", "SUB", "MUL", 
            "LT", "ANDAND", "LEN", "NOT", "NEW", "THIS", "WS", "COMMENT", 
            "LINE_COMMENT", "IDENTIFIER", "INTEGER_LITERAL" ]

    ruleNames = [ "CLASS", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                  "RBRACK", "SEMI", "COMMA", "DOT", "TRUE", "FALSE", "PUBLIC", 
                  "STATIC", "VOID", "MAIN", "STRING", "EXTENDS", "RETURN", 
                  "INT", "BOOLEAN", "IF", "ELSE", "WHILE", "SOUT", "ASSIGN", 
                  "ADD", "SUB", "MUL", "LT", "ANDAND", "LEN", "NOT", "NEW", 
                  "THIS", "WS", "COMMENT", "LINE_COMMENT", "IDENTIFIER", 
                  "INTEGER_LITERAL", "Digit", "Letter", "LetterOrDigit" ]

    grammarFileName = "MiniJavaLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


