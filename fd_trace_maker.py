# Created by Mica Gardone on 6/23/2025 | 23/6/2025.

from pddl import parse_domain, parse_problem
from pddl.logic.base import Not, And
from pddl.logic.functions import Increase, EqualTo

class State:
    def __init__(self, fluents, debug=False, added=[], removed=[], prior="", curr="init"):
        self.__fluents = fluents
        
        self.__debug = debug
        if debug:
            self.__removed = removed
            self.__added = added
            self.__prior = prior
            self.__curr = curr
        ##
    ##
    
    def apply_action(self, action):
        fluents = self.__fluents.copy()
        added = []
        removed = []
        
        # Should never be added to the state, only remove
        for eff in action.get_effects():
            if eff.is_not():
                inv_eff = ~eff
                findx = fluents.index(inv_eff) if inv_eff in fluents else -1
                
                if findx > -1:
                    if self.__debug:
                        removed.append(fluents.pop(findx))
                    else:
                        del fluents[findx]
                    ##
                ##
            ##
        ##
        
        # Should add if the fluent doesn't already exist!
        for eff in action.get_effects():
            if eff.is_not() == False and eff not in fluents:
                fluents.append(eff)
                if self.__debug:
                    added.append(eff)
                ##
            ##
        ##
        
        if self.__debug:
            return State(fluents, True, added, removed, self.__curr, action.get_name())
        else:
            return State(fluents)
        ##
    ##
    
    def print_as_expected(self):
        str_eff = [str(e) for e in self.__fluents]
        return ", ".join(str_eff)
    ##
    
    def __str__(self):
        if self.__debug:
            res = f"({self.__prior}) ---> ({self.__curr})\n"
            
            for f in self.__fluents:
                if f in self.__added:
                    res += f"\t++ {f} ++\n"
                else:
                    res += f"\t{f}\n"
                ##
            ##
            
            for r in self.__removed:
                res += f"\t-- {r} --\n"
            ##
            
            return res + "#=#=# END STATE #=#=#"
        ##
        
        str_eff = [str(e) for e in self.__fluents]
        return "STATE:\n\t" + "\n\t".join(str_eff) + "\nEND STATE"
    ##
##

class Effect:
    def __init__(self, name, terms, invert):
        self.__not = invert
        self.__name = name
        self.__terms = terms
    ##
    
    def is_not(self):
        return self.__not
    ##
    
    def get_terms(self):
        return self.__terms
    ##
    
    def __invert__(self):
        return Effect(self.__name, self.__terms, not self.__not)
    ##
    
    def __eq__(self, other):
        if self.__not != other.__not or self.__name != other.__name:
            return False
        ##
        
        for t in self.__terms:
            if t not in other.__terms:
                return False
            ##
        ##
        
        return True
    ##
    
    def __str__(self):
        return ("not " if self.__not else "") + "(" + self.__name + (" " + " ".join(self.__terms) if len(self.__terms) > 0 else "") + ")"
    ##
##

class GroundedAction:
    def __init__(self, name, effects):
        self.__name = name
        self.__effects = effects
    ##
    
    def get_name(self):
        return self.__name
    ##
    
    def get_effects(self):
        return self.__effects
    ##
    
    def __str__(self):
        str_eff = [str(e) for e in self.__effects]
        return self.__name + "\n\t".join(str_eff)
    ##
##

def parse_domain_file(domain):
    return parse_domain(domain)
##

def parse_problem_file(problem):
    return parse_problem(problem)
##

def get_solution_plan(sln_file, actions):
    print(">>> getting solution...")
    steps = []
    
    with open(sln_file, "r") as file:
        for line in file:
            if ";" in line:
                break
            ##
            contents = line.strip().replace("(", "").replace(")", "").strip().split(" ")
            prototype = next((a for a in actions if a.name.lower() == contents[0]), None)
            
            if prototype == None:
                raise Exception(f">>>> ERROR in {sln_file}: Unknown action name, `{contents[0]}`!")
            ##
            
            steps.append(_ground_step(contents, prototype))
        ##
    ##
    
    return steps
##

def _ground_step(step, prototype):
    print(">>> grounding...")
    mappings = []
    effs = []
    
    for i in range(1, len(step)):
        mappings.append((step[i], prototype.parameters[i - 1]))
    ##
    
    if type(prototype.effect) is And:
        for operand in prototype.effect.operands:
            if type(operand) is Increase:
                continue
            ##
            
            actualOperand = operand
            isNot = False
            if type(operand) is Not:
                isNot = True
                actualOperand = operand.argument
            ##
            
            grounded = []
            for t in actualOperand.terms:
                gt = next((m[0] for m in mappings if m[1] == t), None)
                if gt is None:
                    raise Exception(f">>>> Unknown term {t}")
                ##
                grounded.append(gt)
            ##
            eff = Effect(actualOperand.name, grounded, isNot)
            effs.append(eff)
        ##
    elif type(prototype.effect) is Increase:
        pass
    else:
        actualOperand = prototype.effect
        isNot = False
        if type(prototype.effect) is Not:
            isNot = True
            actualOperand = actualOperand.argument
        ##
        
        grounded = []
        for t in actualOperand.terms:
            gt = next((m[0] for m in mappings if m[1] == t), None)
            if gt is None:
                raise Exception(f">>>> Unknown term {t}")
            ##
            grounded.append(gt)
        ##
        eff = Effect(actualOperand.name, grounded, isNot)
        effs.append(eff)
    ##
    
    return GroundedAction(" ".join(step), effs)
##

def _simulate(init, solution) -> list:
    print(">>> simulating...")
    observed_states = []
    curr_state = init
    
    for s in solution:
        #print("applying ", s.get_name())
        curr_state = curr_state.apply_action(s)
        observed_states.append(curr_state)
    ##
    
    print(">>> simulation done!")
    return observed_states
##

def _generate_start_from_problem(problem, debug_enabled=False):
    print(">>> creating initial state...")
    fluents = []
    init = set(problem.init)
    
    #print(init)
    
    for p in init:
        if type(p) is EqualTo:
            continue
        ##
        
        local_terms = [str(t) for t in p.terms]
        
        #print(local_terms)
        fluent = Effect(p.name, local_terms, False)
        # print(fluent)
        fluents.append(fluent)
    ##
    
    return State(fluents, debug=debug_enabled)
##

def generate_trace_from_solution(domain_file, problem_file, sln_file, output_file):
    print(f">> Generating trace from the domain {domain_file}...")
    
    d = parse_domain_file(domain_file)
    p = parse_problem_file(problem_file)
    sln = get_solution_plan(sln_file, list(d.actions))
    init_state = _generate_start_from_problem(p)
    results = _simulate(init_state, sln)
    
    with open(output_file, "w") as file:
        for sindx in range(len(results)):
            file.write(results[sindx].print_as_expected())
            if sindx + 1 < len(results):
                file.write("\n")
            ##
        ##
    ##
    #print("finished writing!")
##

TEST_STYLE = 1
if __name__ == "__main__":
    if TEST_STYLE == 0:
        d = parse_domain_file("Benchmark_Problems/block-words/domain.pddl")
        p = parse_problem_file("Benchmark_Problems/block-words/block-words-aaai_p01_hyp-0_10_0/_fd-hypotheses/hyp_0_problem.pddl") 
        
        #print(list(d.actions)[1])
        sln = get_solution_plan("Benchmark_Problems/block-words/block-words-aaai_p01_hyp-0_10_0/_fd-hypotheses/hyp_0.solution", list(d.actions))
        
        #for s in sln:
        #    print(s)
        ##
        
        init_state = _generate_start_from_problem(p, True)
        # print(init_state)
        results = _simulate(init_state, sln)
        for s in results:
            # print(s)
            print(s.print_as_expected())
        ##
    elif TEST_STYLE == 1:
        generate_trace_from_solution("Benchmark_Problems/kitchen/domain.pddl",
                                        "Benchmark_Problems/kitchen/kitchen_generic_hyp-0_10_1/_fd-hypotheses/hyp_2_problem.pddl",
                                        "Benchmark_Problems/kitchen/kitchen_generic_hyp-0_10_1/_fd-hypotheses/hyp_2.solution",
                                        "Benchmark_Problems/kitchen/kitchen_generic_hyp-0_10_1/_fd-hypotheses/hyp_2.trace")
    ##
##
