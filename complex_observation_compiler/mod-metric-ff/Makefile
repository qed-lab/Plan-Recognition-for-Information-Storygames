#!/bin/sh
#
# Makefile for FF v 1.0
#


####### FLAGS

TYPE	=
ADDONS	=

CC      = gcc

CFLAGS	= -O6 -Wall -g -ansi $(TYPE) $(ADDONS)
# -g -pg

LIBS    = -lm


####### Files

PDDL_PARSER_SRC	= scan-fct_pddl.tab.c \
	scan-ops_pddl.tab.c \
	scan-probname.tab.c \
	lex.fct_pddl.c \
	lex.ops_pddl.c

PDDL_PARSER_OBJ = scan-fct_pddl.tab.o \
	scan-ops_pddl.tab.o


SOURCES 	= main.c \
	memory.c \
	output.c \
	parse.c \
	expressions.c \
	inst_pre.c \
	inst_easy.c \
	inst_hard.c \
	inst_final.c \
	relax.c \
	search.c \
	utility.c

LIB_SOURCES = libff.c \
	memory.c \
	output.c \
	parse.c \
	expressions.c \
	inst_pre.c \
	inst_easy.c \
	inst_hard.c \
	inst_final.c \
	relax.c \
	search.c \
	utility.c


OBJECTS 	= $(SOURCES:.c=.o)
LIB_OBJECTS	= $(LIB_SOURCES:.c=.o)

####### Implicit rules

.SUFFIXES:

.SUFFIXES: .c .o

.c.o:; $(CC) -c $(CFLAGS) $<

####### Build rules

libff: $(LIB_OBJECTS) $(PDDL_PARSER_OBJ)
	ar cru libff.a $(LIB_OBJECTS) $(PDDL_PARSER_OBJ)

ff: $(OBJECTS) $(PDDL_PARSER_OBJ)
	$(CC) -static -o ff $(OBJECTS) $(PDDL_PARSER_OBJ) $(CFLAGS) $(LIBS)

# pddl syntax
scan-fct_pddl.tab.c: scan-fct_pddl.y lex.fct_pddl.c
	bison -pfct_pddl -bscan-fct_pddl scan-fct_pddl.y

scan-ops_pddl.tab.c: scan-ops_pddl.y lex.ops_pddl.c
	bison -pops_pddl -bscan-ops_pddl scan-ops_pddl.y

lex.fct_pddl.c: lex-fct_pddl.l
	flex -Pfct_pddl lex-fct_pddl.l

lex.ops_pddl.c: lex-ops_pddl.l
	flex -Pops_pddl lex-ops_pddl.l

test_lib: test_main.cxx
	g++ -static -o test_lib test_main.cxx -lff -L./

# misc
clean:
	rm -f *.o *.bak *~ *% core *_pure_p9_c0_400.o.warnings test_lib \
        \#*\# $(RES_PARSER_SRC) $(PDDL_PARSER_SRC)

veryclean: clean
	rm -f ff H* J* K* L* O* graph.* *.symbex gmon.out \
	$(PDDL_PARSER_SRC) \
	lex.fct_pddl.c lex.ops_pddl.c lex.probname.c \
	*.output

depend:
	makedepend -- $(SOURCES)  $(LIB_SOURCES) $(PDDL_PARSER_SRC) test_main.cxx

lint:
	lclint -booltype Bool $(SOURCES) 2> output.lint

# DO NOT DELETE

main.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
main.o: /usr/include/strings.h /usr/include/features.h
main.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
main.o: /usr/include/ctype.h memory.h /usr/include/string.h output.h parse.h
main.o: expressions.h inst_pre.h inst_easy.h inst_hard.h inst_final.h relax.h
main.o: search.h
memory.o: /usr/include/string.h /usr/include/strings.h
memory.o: /usr/include/features.h /usr/include/features-time64.h
memory.o: /usr/include/stdc-predef.h ff.h /usr/include/stdlib.h
memory.o: /usr/include/stdio.h /usr/include/ctype.h memory.h inst_pre.h
output.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
output.o: /usr/include/strings.h /usr/include/features.h
output.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
output.o: /usr/include/ctype.h utility.h output.h
parse.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
parse.o: /usr/include/strings.h /usr/include/features.h
parse.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
parse.o: /usr/include/ctype.h memory.h /usr/include/string.h output.h parse.h
expressions.o: /usr/include/string.h /usr/include/strings.h
expressions.o: /usr/include/features.h /usr/include/features-time64.h
expressions.o: /usr/include/stdc-predef.h ff.h /usr/include/stdlib.h
expressions.o: /usr/include/stdio.h /usr/include/ctype.h output.h memory.h
expressions.o: expressions.h
inst_pre.o: /usr/include/string.h /usr/include/strings.h
inst_pre.o: /usr/include/features.h /usr/include/features-time64.h
inst_pre.o: /usr/include/stdc-predef.h ff.h /usr/include/stdlib.h
inst_pre.o: /usr/include/stdio.h /usr/include/ctype.h output.h memory.h
inst_pre.o: expressions.h inst_pre.h
inst_easy.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
inst_easy.o: /usr/include/strings.h /usr/include/features.h
inst_easy.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
inst_easy.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
inst_easy.o: expressions.h inst_pre.h inst_easy.h
inst_hard.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
inst_hard.o: /usr/include/strings.h /usr/include/features.h
inst_hard.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
inst_hard.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
inst_hard.o: expressions.h inst_pre.h inst_hard.h
inst_final.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
inst_final.o: /usr/include/strings.h /usr/include/features.h
inst_final.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
inst_final.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
inst_final.o: expressions.h inst_pre.h inst_final.h
relax.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
relax.o: /usr/include/strings.h /usr/include/features.h
relax.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
relax.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
relax.o: expressions.h relax.h search.h
search.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
search.o: /usr/include/strings.h /usr/include/features.h
search.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
search.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
search.o: expressions.h relax.h search.h
utility.o: /usr/include/string.h /usr/include/strings.h
utility.o: /usr/include/features.h /usr/include/features-time64.h
utility.o: /usr/include/stdc-predef.h utility.h ff.h /usr/include/stdlib.h
utility.o: /usr/include/stdio.h /usr/include/ctype.h output.h
libff.o: libff.h ff.h /usr/include/stdlib.h /usr/include/stdio.h
libff.o: /usr/include/strings.h /usr/include/features.h
libff.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
libff.o: /usr/include/ctype.h memory.h /usr/include/string.h output.h parse.h
libff.o: expressions.h inst_pre.h inst_easy.h inst_hard.h inst_final.h
memory.o: /usr/include/string.h /usr/include/strings.h
memory.o: /usr/include/features.h /usr/include/features-time64.h
memory.o: /usr/include/stdc-predef.h ff.h /usr/include/stdlib.h
memory.o: /usr/include/stdio.h /usr/include/ctype.h memory.h inst_pre.h
output.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
output.o: /usr/include/strings.h /usr/include/features.h
output.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
output.o: /usr/include/ctype.h utility.h output.h
parse.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
parse.o: /usr/include/strings.h /usr/include/features.h
parse.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
parse.o: /usr/include/ctype.h memory.h /usr/include/string.h output.h parse.h
expressions.o: /usr/include/string.h /usr/include/strings.h
expressions.o: /usr/include/features.h /usr/include/features-time64.h
expressions.o: /usr/include/stdc-predef.h ff.h /usr/include/stdlib.h
expressions.o: /usr/include/stdio.h /usr/include/ctype.h output.h memory.h
expressions.o: expressions.h
inst_pre.o: /usr/include/string.h /usr/include/strings.h
inst_pre.o: /usr/include/features.h /usr/include/features-time64.h
inst_pre.o: /usr/include/stdc-predef.h ff.h /usr/include/stdlib.h
inst_pre.o: /usr/include/stdio.h /usr/include/ctype.h output.h memory.h
inst_pre.o: expressions.h inst_pre.h
inst_easy.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
inst_easy.o: /usr/include/strings.h /usr/include/features.h
inst_easy.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
inst_easy.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
inst_easy.o: expressions.h inst_pre.h inst_easy.h
inst_hard.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
inst_hard.o: /usr/include/strings.h /usr/include/features.h
inst_hard.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
inst_hard.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
inst_hard.o: expressions.h inst_pre.h inst_hard.h
inst_final.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
inst_final.o: /usr/include/strings.h /usr/include/features.h
inst_final.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
inst_final.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
inst_final.o: expressions.h inst_pre.h inst_final.h
relax.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
relax.o: /usr/include/strings.h /usr/include/features.h
relax.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
relax.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
relax.o: expressions.h relax.h search.h
search.o: ff.h /usr/include/stdlib.h /usr/include/stdio.h
search.o: /usr/include/strings.h /usr/include/features.h
search.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
search.o: /usr/include/ctype.h output.h memory.h /usr/include/string.h
search.o: expressions.h relax.h search.h
utility.o: /usr/include/string.h /usr/include/strings.h
utility.o: /usr/include/features.h /usr/include/features-time64.h
utility.o: /usr/include/stdc-predef.h utility.h ff.h /usr/include/stdlib.h
utility.o: /usr/include/stdio.h /usr/include/ctype.h output.h
test_main.o: libff.h ff.h /usr/include/stdlib.h /usr/include/stdio.h
test_main.o: /usr/include/strings.h /usr/include/features.h
test_main.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
test_main.o: /usr/include/ctype.h output.h
