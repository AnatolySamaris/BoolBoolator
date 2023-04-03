"""
dealwithbool v2.0
copyright AnatolySamaris
"""

# Basic (bit) operations
NEGBAS = '!'
ANDBAS = '&'
ORBAS = '|'
EQUALBAS = '~'

# Advanced (logical) operations
NEGADV = '¬'
ANDADV = '∧'
ORADV = '∨'
EQUALADV = '~'
XORADV = '⊕'
NOR = '↓'
NAND = '|'
IMPLIC = '→'


class BoolExp:
    """
    The class is used to calculate common things with boolean functions and
    boolean expressions (with zeros and ones, without variables).
    """
    __ACTIONS_BASIC = {'!': (4, lambda a: int(not a)), '&': (3, lambda a, b: int(a and b)),
                       '|': (2, lambda a, b: int(a or b)), '~': (1, lambda a, b: int(a == b))}

    __ACTIONS_ADVANCED = {'¬': (5, lambda a: int(not a)),
                          '∧': (4, lambda a, b: int(a and b)), '|': (4, lambda a, b: int(not (a and b))),
                          '∨': (3, lambda a, b: int(a or b)), '↓': (3, lambda a, b: int(not (a or b))),
                          '→': (2, lambda a, b: 0 if (a == 1 and b == 0) else 1),
                          '~': (1, lambda a, b: int(a == b)), '⊕': (1, lambda a, b: int(a != b))}

    def __init__(self, expression: str, mode='basic'):
        """
        :param expression(str): a boolean function or expression. It must consist of
            boolean functions and some variables (or zeros and ones).
        :param mode(str, optional): 'basic', 'advanced'. Defines a set of boolean functions that
            is used for all calculations.
        """
        assert len(expression) > 0, "Missed an expression."
        assert mode in ['basic', 'advanced'], "Only 'basic' or 'advanced' is allowed!"

        self.expression = expression
        self.mode = mode
        self.variables = sorted([i for i in set(expression) if i.isalpha()])  # In alphabet order

    @staticmethod
    def __merge_minterms(one: list, two: list) -> list:
        """
        The function is used in "get_pnf" method when minimizing pdnf of pcnf.
        Merges two terms that are different on only one element, that is replaced with -1 if it is possible
        ('-' in Quine-McCluskey algorithm: https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm).

        :param one(list): first term to merge.
        :param two(list): second term to merge.
        :return: list, a merged term.
        """
        assert len(one) == len(two)

        index_to_replace = -1
        for i in range(len(one)):
            if one[i] != two[i]:
                if index_to_replace == -1:
                    index_to_replace = i
                else:
                    return []
        one[index_to_replace] = '-1'
        return one

    @staticmethod
    def __is_equal(term: list, pattern: list) -> bool:
        """
        The function is used in "get_pnf" method when minimizing pdnf or pcnf. Checks if one of terms
        can be a pattern for second term.

        :param term(list): a term for which we're checking for patterns.
        :param pattern(list): a term which can be a pattern for first term.
        :return: bool, is the second term a pattern for the first or not.
        """
        assert len(term) == len(pattern)

        for i in range(len(term)):
            if term[i] != pattern[i] and ('-1' not in [term[i], pattern[i]]):
                return False
        return True

    def evaluate(self, exp='') -> int:
        """
        Calculates a value of concrete expression that has ones and zeros instead of all variables.
        If exp parameter is empty, the function will evaluate for self.expression. The function is
        also used in "calculate" method.

        :param exp: str,
        :return: int, a value of a boolean expression (1 or 0).
        """
        exp = self.expression if exp == '' else exp
        actions = self.__ACTIONS_BASIC if self.mode == 'basic' else self.__ACTIONS_ADVANCED

        # Parsing the expression
        parsed_exp = []
        for i in exp:
            if i in '01':
                parsed_exp.append(int(i))
            if i in actions or i in '()':
                parsed_exp.append(i)

        # Conversion the expression to postfix (polish) notation
        polish_exp = []
        stack = []
        for token in parsed_exp:
            if token in actions:
                while stack and stack[-1] != '(' and actions[token][0] <= actions[stack[-1]][0]:
                    polish_exp.append(stack.pop())
                stack.append(token)
            elif token == ')':
                while stack:
                    x = stack.pop()
                    if x == '(':
                        break
                    polish_exp.append(x)
            elif token == '(':
                stack.append(token)
            else:
                polish_exp.append(token)
        while stack:
            polish_exp.append(stack.pop())

        # Calculating the value of expression
        for token in polish_exp:
            if token in actions and token not in ['¬', '!']:
                y, x = stack.pop(), stack.pop()
                stack.append(actions[token][1](x, y))
            elif token in ['¬', '!']:
                x = stack.pop()
                stack.append(actions[token][1](x))
            else:
                stack.append(token)
        return stack[0]

    def calculate(self) -> list:
        """
        Calculates values of a boolean function for all possible sets of variables.
        It works only with the function that is passed when the BoolExp object is created.

        :return: list, a list of sets of variables + corresponding function values in the end
        of every set, i.e. it seems like a dataset with values in the last column and
        arguments in others.
        """
        size = len(self.variables)
        if size == 0:
            return [self.evaluate(self.expression)]
        else:
            answer = []
            for i in range(2 ** size):
                bin_i = bin(i)[2:]
                var_set = list('0' * (size - len(bin_i)) + bin_i)

                exp = self.expression
                for var in range(size):
                    exp = exp.replace(self.variables[var], var_set[var])
                answer.append(var_set + [self.evaluate(exp)])
            return answer

    def get_pnf(self, res_exp=None, pnf_mode='pdnf', minimized=False, pretty=False):
        """
        Calculates pdnf (principal disjunctive normal form) or pcnf (principal conjunctive normal form)
        depending on passed argument 'pnf_mode'. If argument 'res_exp' is empty, the method will
        calculate for the function that is passed when the BoolExp object is created. The method
        is available only for functions with at least one variable.

        :param pnf_mode: str. 'pdnf', 'pcnf'. Defines what kind of principal normal function
        will be calculated by the method.
        :param res_exp: list. A list of sets of values + corresponding function values, i.e. the
        result of 'calculate' method. If it's empty, the method will prepare the required list.
        :param minimized: bool. If True, calculates minimized principal normal form. Here
        Quine-McCluskey algorithm is used.
        :param pretty: bool. If True, returns a string representing the pnf as usual in logic,
        otherwise returns just a list of terms.
        :return: str or list representing chosen principal normal form.
        """
        assert len(self.variables) > 0 or len([i for i in set(res_exp) if i.isalpha()]) > 0, "Only for advanced mode."
        assert pnf_mode in ['pdnf', 'pcnf'], 'Only "pdnf" or "pcnf" is available!'

        res_exp = res_exp if (not None) else self.calculate()

        no = '!' if self.mode == 'basic' else '¬'
        res = 1 if pnf_mode == 'pdnf' else 0
        if pnf_mode == 'pdnf':
            inside = '&' if self.mode == 'basic' else '∧'
            outside = '|' if self.mode == 'basic' else '∨'
        else:
            inside = '|' if self.mode == 'basic' else '∨'
            outside = '&' if self.mode == 'basic' else '∧'

        pnf = []
        if minimized:
            for res_set in res_exp:
                if res_set[-1] == res:
                    pnf.append(res_set[:-1])
        else:
            for res_set in res_exp:
                if res_set[-1] == res:
                    pnf_chunk = []
                    for var in range(len(self.variables)):
                        pnf_chunk.append(self.variables[var] if int(res_set[var]) == res
                                         else (no + str(self.variables[var])))
                    pnf.append(pnf_chunk if not pretty else f' {inside} '.join(pnf_chunk))

        if minimized:
            min_terms = [[] for _ in range(len(self.variables))]
            for i in range(len(pnf)):
                min_terms[pnf[i].count(str(res))-1].append(pnf[i])

            terms_to_check = [term[:-1] for term in res_exp if term[-1] == res]

            # Minimizing
            final_terms = []
            if len(min_terms) == 1:
                final_terms = [min_terms]
            else:
                while min_terms:
                    temp_terms = []
                    if len(min_terms) <= 1:
                        final_terms.extend(min_terms)
                        break
                    for i in range(len(min_terms) - 1):
                        terms_i = []
                        used_terms = [[0] * len(min_terms[i]), [0] * len(min_terms[i + 1])]
                        for term1 in range(len(min_terms[i])):
                            for term2 in range(len(min_terms[i + 1])):
                                merged = self.__merge_minterms(min_terms[i][term1], min_terms[i + 1][term2])
                                if merged:
                                    terms_i.append(merged)
                                    used_terms[0][term1] = 1
                                    used_terms[1][term2] = 1
                        temp_terms.append(terms_i)
                        for term1 in range(len(min_terms[i])):
                            if int(used_terms[0][term1]) == 0 and min_terms[i][term1] not in final_terms:
                                final_terms.append(min_terms[i][term1])
                        for term2 in range(len(min_terms[i + 1])):
                            if int(used_terms[1][term2]) == 0 and min_terms[i+1][term2] not in final_terms:
                                final_terms.append(min_terms[i + 1][term2])
                    min_terms = temp_terms

            # Filtering
            final_terms = [i for i in final_terms if i != []]
            if len(final_terms) == 1:
                final_min_terms = final_terms
            else:
                final_min_terms = [term for group in final_terms for term in group]
            patterns = {}
            for check in range(len(terms_to_check)):
                for term in final_min_terms:
                    if self.__is_equal(terms_to_check[check], term):
                        patterns[check] = patterns.get(check, []) + [term]
            min_terms_ans = [value[1][0] for value in patterns.items() if len(value[1]) == 1]
            pnf.clear()    # Clearing to avoid code copying

            # Constructing
            for term in min_terms_ans:
                pnf_chunk = []
                for var in range(len(self.variables)):
                    if int(term[var]) == res:
                        pnf_chunk.append(self.variables[var])
                    elif int(term[var]) == (not res):
                        pnf_chunk.append(no + self.variables[var])
                pnf.append(pnf_chunk if not pretty else f' {inside} '.join(pnf_chunk))

        if not pretty:
            return pnf
        else:
            return '(' + f') {outside} ('.join(pnf) + ')'

    def get_zhegalkin(self, res_exp=None, pretty=False):
        """
        Calculates the zhegalkin polynomial for the boolean function using Pascal's triangle algorithm.
        If argument 'res_exp' is empty, the method will calculate for the function that is passed
        when the BoolExp object is created. The method is available only for functions with at least one variable.

        :param res_exp: list. A list of sets of values + corresponding function values, i.e. the
        result of 'calculate' method. If it's empty, the method will prepare the required list.
        :param pretty: bool. If True, returns a string representing the polynomial as usual in logic,
        otherwise returns just a list of terms.
        :return: str or list representing zhegalkin polynomial.
        """
        assert len(self.variables) > 0 or len([i for i in set(res_exp) if i.isalpha()]) > 0, "Only for advanced mode."
        res_exp = res_exp if (not None) else self.calculate()

        func_values = [i[-1] for i in res_exp]
        coefs = [func_values[0]]
        for _ in range(len(res_exp) - 1):
            temp = []
            for i in range(len(func_values) - 1):
                temp.append(int(func_values[i]) != int(func_values[i + 1]))
            func_values = temp
            coefs.append(int(temp[0]))

        set_var = [i[:-1] for i in res_exp]  # Sets of variable values
        result = ['1' * coefs[0]]
        for vars_ in range(1, len(set_var)):
            if coefs[vars_] == 1:
                result.append(''.join([self.variables[i] for i in range(len(set_var[vars_]))
                                       if int(set_var[vars_][i])]))
        result = result[1:] if result[0] == '' else result
        result.sort(key=lambda x: (len(x), x))

        if not pretty:
            return result
        else:
            return ' ⊕ '.join(result)

    def get_classes(self, res_exp=None) -> list:
        """
        Examines the boolean function for belonging to Post classes.
        The method is available only for functions with at least one variable.

        :param res_exp: list. A list of sets of values + corresponding function values, i.e. the
        result of 'calculate' method. If it's empty, the method will prepare the required list.
        :return: list, a list containing class designations of classes which
        the function belongs to. If the function belongs to no one Post class,
        returns an empty list.
        """
        assert len(self.variables) > 0 or len([i for i in set(res_exp) if i.isalpha()]) > 0, "Only for advanced mode."
        res_exp = res_exp if (not None) else self.calculate()
        result = []

        # class T0
        if res_exp[0][-1] == 0:  # if 0, 0, ..., 0 -> 0
            result.append('T0')

        # class T1
        if res_exp[-1][-1] == 1:  # if 1, 1, ..., 1 -> 1
            result.append('T1')

        # class S
        func_values = [term[-1] for term in res_exp]
        if func_values == [int(not i) for i in func_values[::-1]]:
            result.append('S')

        # class L
        for term in self.get_zhegalkin(res_exp):
            if len(term) > 1:
                break
        else:
            result.append('L')

        # class M
        for i in range(len(res_exp)):
            if res_exp[i][-1] == 1:
                for j in range(i + 1, len(res_exp)):
                    # If sets are different on only one variable
                    if abs(sum(map(lambda x: int(x[0]) - int(x[1]), zip(res_exp[i][:-1], res_exp[j][:-1])))) == 1:
                        if res_exp[j][-1] == 0:
                            break
                else:  # Don't blame me please
                    continue
                break
        else:
            result.append('M')
        return result
