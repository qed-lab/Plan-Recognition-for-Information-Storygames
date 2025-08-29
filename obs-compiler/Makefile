CC = g++
BISON = bison
FLEX = flex

NFF_TARGET = pr2plan

#CXXFLAGS = -g -Wall -Imod-metric-ff -DDEBUG -DPDDL_TYPE_CHECKING
CXXFLAGS = -O3 -Wall -Imod-metric-ff -DNDEBUG
LDFLAGS = -Lmod-metric-ff/
#EFENCE = -lefence
STATIC = -static
LIBS = -lff $(EFENCE)

NFF_SOURCES = PDDL.cxx \
	pddl_fluent_set.cxx \
	pddl_string_table.cxx \
	bitarray.cxx \
	global_options.cxx \
	options.cxx \
	pr_obs_reader.cxx \
	pr_strips_mapping.cxx \
	strips_writer.cxx \
	act_obs.cxx \
	main.cxx

NFF_OBJECTS = $(NFF_SOURCES:.cxx=.o) 

# Implicit rules
#
.SUFFIXES:

.SUFFIXES: .cxx .C .o

.cxx.o:; $(CC) -o $@ -c $(CXXFLAGS) $<
.C.o:; $(CC) -o $@ -c $(CXXFLAGS) $<

# build rules

all : $(NFF_TARGET) 

$(NFF_TARGET) : $(PARSER_OBJ) $(NFF_OBJECTS)
	$(CC) -o $(NFF_TARGET) $(STATIC) $(PARSER_OBJ) $(NFF_OBJECTS) $(LDFLAGS) $(LIBS)

# dependencies
depend:
	# Updating dependencies
	@makedepend -- $(CXXFLAGS) -- $(NFF_SOURCES) $(MAIN_NFF_SOURCES)

# Cleaning
clean:
	rm -rf $(NFF_OBJECTS) $(NFF_TARGET) $(PARSER_SRC)  $(PARSER_HDR) *.o *.hh
# DO NOT DELETE

PDDL.o: PDDL.hxx pddl_basic_types.hxx pddl_string_table.hxx
PDDL.o: pddl_fluent_set.hxx bitarray.hxx nff_logic.hxx /usr/include/stdint.h
PDDL.o: utils.hxx /usr/include/unistd.h /usr/include/features.h
PDDL.o: /usr/include/features-time64.h /usr/include/stdc-predef.h options.hxx
PDDL.o: mod-metric-ff/libff.h mod-metric-ff/ff.h /usr/include/stdlib.h
PDDL.o: /usr/include/alloca.h /usr/include/stdio.h /usr/include/strings.h
PDDL.o: /usr/include/ctype.h
pddl_fluent_set.o: pddl_fluent_set.hxx bitarray.hxx
pddl_string_table.o: pddl_string_table.hxx pddl_basic_types.hxx
bitarray.o: bitarray.hxx
global_options.o: global_options.hxx
options.o: options.hxx /usr/include/getopt.h /usr/include/features.h
options.o: /usr/include/features-time64.h /usr/include/stdc-predef.h
pr_obs_reader.o: pr_obs_reader.hxx act_obs.hxx string_ops.hxx PDDL.hxx
pr_obs_reader.o: pddl_basic_types.hxx pddl_string_table.hxx
pr_obs_reader.o: pddl_fluent_set.hxx bitarray.hxx nff_logic.hxx
pr_obs_reader.o: /usr/include/stdint.h
pr_strips_mapping.o: pr_strips_mapping.hxx strips_writer.hxx act_obs.hxx
pr_strips_mapping.o: PDDL.hxx pddl_basic_types.hxx pddl_string_table.hxx
pr_strips_mapping.o: pddl_fluent_set.hxx bitarray.hxx nff_logic.hxx
pr_strips_mapping.o: /usr/include/stdint.h options.hxx
strips_writer.o: strips_writer.hxx PDDL.hxx pddl_basic_types.hxx
strips_writer.o: pddl_string_table.hxx pddl_fluent_set.hxx bitarray.hxx
strips_writer.o: nff_logic.hxx /usr/include/stdint.h string_ops.hxx
act_obs.o: act_obs.hxx pddl_string_table.hxx pddl_basic_types.hxx PDDL.hxx
act_obs.o: pddl_fluent_set.hxx bitarray.hxx nff_logic.hxx
act_obs.o: /usr/include/stdint.h
main.o: /usr/include/signal.h /usr/include/features.h
main.o: /usr/include/features-time64.h /usr/include/stdc-predef.h utils.hxx
main.o: /usr/include/unistd.h PDDL.hxx pddl_basic_types.hxx
main.o: pddl_string_table.hxx pddl_fluent_set.hxx bitarray.hxx nff_logic.hxx
main.o: /usr/include/stdint.h options.hxx pr_obs_reader.hxx act_obs.hxx
main.o: pr_strips_mapping.hxx strips_writer.hxx string_ops.hxx
