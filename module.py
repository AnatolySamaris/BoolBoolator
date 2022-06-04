class Decider:

	ACTIONS = {'¬':(5, lambda a: not a) , '∨':(3, lambda a,b: a or b) , '∧':(4, lambda a,b: a and b), 
		'→':(2, lambda a,b: 0 if (a == 1 and b == 0) else 1), '~':(1, lambda a, b: a == b), '⊕':(1, lambda a,b: a != b), 
		'|':(4, lambda a,b: not(a and b)), '↓':(3, lambda a,b: not(a or b))}


	def __init__(self, expression):
		self.expression = expression
		self.lines = []
		self.answers = []
		self.pdnf = []
		self.pcnf = []
		self.classes = ''
		self.ans_pdnf = ''
		self.ans_pcnf = ''
		self.zhegalkin = ''
		self.ans = ''
		self.carnot = []
		self.ans_carnot = ''
		self.min_pdnf = ''
		self.min_pcnf = ''
		self.schaef_basis = ''
		self.pier_basis = ''
		

	def get_size(self):
		size = ''
		for i in self.expression:
			if i in 'xyzt' and i not in size:
				size += i
		return len(size)


	def prepare_ans(self):
		size = len(self.lines[0])
		if size == 2:
			self.ans += f'x | f(x)\n'
		elif size == 3:
			self.ans += f'x | y | f(x,y)\n'
		elif size == 4:
			self.ans += f'x | y | z | f(x,y,z)\n'
		elif size == 5:
			self.ans += f'x | y | z | t | f(x,y,z,t)\n'
		for line in self.lines:
			if size == 2:
				self.ans += f'{line[0]} | {int(line[1])}\n'
			elif size == 3:
				self.ans += f'{line[0]} | {line[1]} |     {int(line[2])}\n'
			elif size == 4:
				self.ans += f'{line[0]} | {line[1]} | {line[2]} |     {int(line[3])}\n'
			elif size == 5:
				self.ans += f'{line[0]} | {line[1]} | {line[2]} | {line[3]} |     {int(line[4])}\n'


	def get_classes(self):
		if self.lines[0] == [0] * len(self.lines[0]):
			self.classes += 'T0 '

		if self.lines[-1] == [1] * len(self.lines[0]):
			self.classes += 'T1 '

		if self.answers == [self.ACTIONS['¬'][1](int(i)) for i in self.answers[::-1]]:
			self.classes += 'S '

		lin = True
		for i in ['xy', 'xz', 'xt', 'yz', 'yt', 'zt', 'xyz', 'xyt', 'xzt', 'yzt', 'xyzt']:
			if i in self.zhegalkin:
				lin = False
				break
		res = 'L ' if lin else ''
		self.classes += res

		size = len(self.lines)-1
		if size == 3:
			if self.answers[0] <= self.answers[2] and self.answers[1] <= self.answers[3]:
				self.classes += 'M '

		elif size == 4:
			for i in range(4):
				if self.answers[i] > self.answers[i+4]:
					break
			else:
				one = []; one.extend(self.answers[:2]); one.extend(self.answers[4:6])
				two = []; two.extend(self.answers[2:4]); two.extend(self.answers[6:])
				for j in range(2):
					if one[j] > one[j+2] or two[j] > two[j+2]:
						break
				else:
					self.classes += 'M '

		elif size == 5:
			for i in range(8):
				if self.answers[i] > self.answers[i+8]:
					break
			else:
				one = []; one.extend(self.answers[:4]); one.extend(self.answers[8:12])
				two = []; two.extend(self.answers[4:8]); two.extend(self.answers[12:])
				for j in range(4):
					if one[j] > one[j+4] or two[j] > two[j+4]:
						break
				else:
					one_1 = []; one_1.extend(one[:2]); one_1.extend(one[4:6])
					one_2 = []; one_2.extend(one[2:4]); one_2.extend(one[6:])
					two_1 = []; two_1.extend(two[:2]); two_1.extend(two[4:6])
					two_2 = []; two_2.extend(two[2:4]); two_2.extend(two[6:])
					for k in range(2):
						if one_1[k] > one1[k+2] or one_2[k] > one_2[k+2] or two_1[k] > two_1[k+2] or two_2[k] > two_2[k+2]:
							break
					else:
						self.classes += 'M '
		if len(self.classes) == 0:
			self.classes = 'Не принадлежит ни одному классу'


	def make_carnot(self):
		size = len(self.lines[0])
		if size == 3:
			self.ans_carnot = 'x\\y | 0 | 1 \n'
			for x in [0, 1]:
				ans_line = []
				for y in [0, 1]:
					for l in self.lines:
						if l[:-1] == [x, y]:
							ans_line.append(str(l[-1]))
				self.carnot.append(ans_line)
				self.ans_carnot += ' ' + str(x) + '   | ' + ' | '.join(ans_line) + '\n'

		elif size == 4:
			yz = ['00', '01', '11', '10']
			self.ans_carnot = 'x\\yz | ' + '  | '.join(yz) + '\n'
			for x in [0, 1]:
				ans_line = []
				for i in yz:
					line = [x, int(i[0]), int(i[1])]
					for l in self.lines:
						if l[:-1] == line:
							ans_line.append(str(l[-1]))
				self.carnot.append(ans_line)
				self.ans_carnot += '  ' + str(x) + '    | ' + '   |   '.join(ans_line) + '\n'

		elif size == 5:
			var = ['00', '01', '11', '10']
			self.ans_carnot = 'xy\\zt | ' + '  | '.join(var) + '\n'
			for i in var:
				ans_line = []
				for j in var:
					line = [int(i[0]), int(i[1]), int(j[0]), int(j[1])]
					for l in self.lines:
						if l[:-1] == line:
							ans_line.append(str(l[-1]))
				self.carnot.append(ans_line)
				self.ans_carnot += '   ' + i[0] + i[1] + '   | ' + '   |   '.join(ans_line) + '\n'


	def minimization(self):
		def get_split(pnf):
			ans = []
			t = ''
			in_b = False
			for i in pnf:
				if i == '(':
					in_b = True
				if in_b:
					if i == ')':
						t += ')'
						ans.append(t)
						t = ''
						in_b = False
					else:
						t += i
			return ans

		def get_vars(form):
			ans = ''
			for i in form:
				if i in 'xyzt':
					ans += i
			return ans

		def to_binary(pnf):
		    res = []
		    for i in range(len(pnf)):
		        if pnf[i] in 'xyzt' and pnf[i-1] != '¬':
		            res.append(1)
		        elif pnf[i] in 'xyzt' and pnf[i-1] == '¬':
		            res.append(-1)
		    return res

		def binary_eat(one, two):
		    res = []
		    for i in range(len(one)):
		        res.append(one[i] + two[i])
		    return res 

		def check_vars(one, two):
			one_vars = ''
			two_vars = ''
			for i in 'xyzt':
				if i in one:
					one_vars += i
				if i in two:
					two_vars += i
			
			return 1 if one_vars == two_vars else 0


		def eating_them(start_pnf, sep, antisep):
		    actual_pnf = start_pnf
		    while True:
		        if len(actual_pnf) == 0:
		            break
		        used = [0] * len(actual_pnf)
		        temp_res = []
		        found = False
		        for p in range(len(actual_pnf)):
		            if used[p] == 1:
		                continue
		            one = actual_pnf[p]
		            if p == len(actual_pnf) - 1:
		            	temp_res.append(one)
		            binary_one = to_binary(one)

		            for i in range(p+1, len(actual_pnf)):
		                two = actual_pnf[i]
		                binary_two = to_binary(two)
		                if len(binary_two) != len(binary_one):
		                	continue
		                if not check_vars(one, two):
		                	continue
		                eaten_list = [binary_one[b] + binary_two[b] for b in range(len(binary_one))]
		                if eaten_list.count(0) > 1:
		                    used[p] = 1
		                    continue
		                        
		                t_res = []
		                actual_vars = get_vars(one)
		                for k in range(len(eaten_list)):
		                    if eaten_list[k] == 2:
		                        t_res.append(actual_vars[k])
		                    elif eaten_list[k] == -2:
		                        t_res.append('¬' + actual_vars[k])
		                    elif eaten_list == 0:
		                        continue
		                temp_res.append('(' + sep.join(t_res) + ')')
		                found = True
		                used[p] = 1
		                used[i] = 1
		                break

		            else:
		            	temp_res.append(one)
		            	used[p] = 1

		        if not found:
		        	ans = []
		        	for clean in temp_res:
		        		if clean not in ans:
		        			ans.append(clean)
		        	return antisep.join(ans)
		        else:
		        	actual_pnf = temp_res

		split_pdnf = get_split(self.ans_pdnf)
		split_pcnf = get_split(self.ans_pcnf)

		self.min_pdnf = eating_them(split_pdnf, ' ∧ ', ' ∨ ')
		self.min_pcnf = eating_them(split_pcnf, ' ∨ ', ' ∧ ')


	def pdnf_pcnf(self):
		for i in self.pdnf:
			self.ans_pdnf += '('
			if len(i) == 1:
				if i[0] == 0:
					self.ans_pdnf += '¬x'
				else:
					self.ans_pdnf += 'x'

			elif len(i) == 2:
				if i[0] == 0:
					self.ans_pdnf += '¬x ∧ '
				else:
					self.ans_pdnf += 'x ∧ '
				if i[1] == 0:
					self.ans_pdnf += '¬y'
				else:
					self.ans_pdnf += 'y'

			elif len(i) == 3:
				if i[0] == 0:
					self.ans_pdnf += '¬x ∧ '
				else:
					self.ans_pdnf += 'x ∧ '
				if i[1] == 0:
					self.ans_pdnf += '¬y ∧ '
				else:
					self.ans_pdnf += 'y ∧ '
				if i[2] == 0:
					self.ans_pdnf += '¬z'
				else:
					self.ans_pdnf += 'z'

			elif len(i) == 4:
				if i[0] == 0:
					self.ans_pdnf += '¬x ∧ '
				else:
					self.ans_pdnf += 'x ∧ '
				if i[1] == 0:
					self.ans_pdnf += '¬y ∧ '
				else:
					self.ans_pdnf += 'y ∧ '
				if i[2] == 0:
					self.ans_pdnf += '¬z ∧ '
				else:
					self.ans_pdnf += 'z ∧ '
				if i[3] == 0:
					self.ans_pdnf += '¬t'
				else:
					self.ans_pdnf += 't'
			self.ans_pdnf += ') ∨ '
		self.ans_pdnf = self.ans_pdnf[:-2]


		for i in self.pcnf:
			self.ans_pcnf += '('
			if len(i) == 1:
				if i[0] == 1:
					self.ans_pcnf += '¬x'
				else:
					self.ans_pcnf += 'x'

			elif len(i) == 2:
				if i[0] == 1:
					self.ans_pcnf += '¬x ∨ '
				else:
					self.ans_pcnf += 'x ∨ '
				if i[1] == 1:
					self.ans_pcnf += '¬y'
				else:
					self.ans_pcnf += 'y'

			elif len(i) == 3:
				if i[0] == 1:
					self.ans_pcnf += '¬x ∨ '
				else:
					self.ans_pcnf += 'x ∨ '
				if i[1] == 1:
					self.ans_pcnf += '¬y ∨ '
				else:
					self.ans_pcnf += 'y ∨ '
				if i[2] == 1:
					self.ans_pcnf += '¬z'
				else:
					self.ans_pcnf += 'z'

			elif len(i) == 4:
				if i[0] == 1:
					self.ans_pcnf += '¬x ∨ '
				else:
					self.ans_pcnf += 'x ∨ '
				if i[1] == 1:
					self.ans_pcnf += '¬y ∨ '
				else:
					self.ans_pcnf += 'y ∨ '
				if i[2] == 1:
					self.ans_pcnf += '¬z ∨ '
				else:
					self.ans_pcnf += 'z ∨ '
				if i[3] == 1:
					self.ans_pcnf += '¬t'
				else:
					self.ans_pcnf += 't'
			self.ans_pcnf += ') ∧ '
		self.ans_pcnf = self.ans_pcnf[:-2]


	def Zhegalkin(self):
		post_answers = [self.answers[0]]
		pre_answers = self.answers
		for _ in range(len(self.answers)-1):
			temp_ans = []
			for i in range(len(pre_answers)-1):
				temp_ans.append(self.ACTIONS['⊕'][1](int(pre_answers[i]), int(pre_answers[i+1])))
			pre_answers = temp_ans
			post_answers.append(int(temp_ans[0]))
		
		sets = [i[:-1] for i in self.lines]
		conjuctions = [] 
		size = len(sets[0])

		for i in sets:
				if size == 1:
					conj = ''
					if i[0] == 1:
						conj += 'x'
					if conj == '':
						conj = '1'
					conjuctions.append(conj)

				elif size == 2:
					conj = ''
					if i[0] == 1:
						conj += 'x'
					if i[1] == 1:
						conj += 'y'
					if conj == '':
						conj = '1'
					conjuctions.append(conj)

				elif size == 3:
					conj = ''
					if i[0] == 1:
						conj += 'x'
					if i[1] == 1:
						conj += 'y'
					if i[2] == 1:
						conj += 'z'
					if conj == '':
						conj = '1'
					conjuctions.append(conj)

				elif size == 4:
					conj = ''
					if i[0] == 1:
						conj += 'x'
					if i[1] == 1:
						conj += 'y'
					if i[2] == 1:
						conj += 'z'
					if i[3] == 1:
						conj += 't'
					if conj == '':
						conj = '1'
					conjuctions.append(conj)

		ans = []
		for i in range(len(conjuctions)):
			if post_answers[i] == 1:
				ans.append(conjuctions[i])
		self.zhegalkin = ' ⊕ '.join(sorted(ans))


	def evaluate(self, exp, mode):
		def parse(subexp):
			for i in subexp:
				if i in '01':
					yield int(i)
				if i in self.ACTIONS or i in '()':
					yield i 

		def shunting_yard(parsed_subexp):
			stack = []
			for token in parsed_subexp:
				if token in self.ACTIONS:
					while stack and stack[-1] != '(' and self.ACTIONS[token][0] <= self.ACTIONS[stack[-1]][0]:
						yield stack.pop()
					stack.append(token)
				elif token == ')':
					while stack:
						x = stack.pop()
						if x == '(':
							break
						yield x 
				elif token == '(':
					stack.append(token)
				else:
					yield token
			while stack:
				yield stack.pop()

		def make_schaef(polish_exp):
			stack = []
			for tiken in polish_exp:
				if token == '∧':
					y, x = stack.pop(), stack.pop()
					stack.append(f'({str(x)}|{str(y)})|({str(x)}|{str(y)})')
				elif token == '∨':
					y, x = stack.pop(), stack.pop()
					stack.append(f'({str(x)}|{str(x)})|({str(y)}|{str(y)})')
				elif token == '¬':
					x = stack.pop()
					stack.append(f'{str(x)}|{str(x)}')
			return stack[0]

		def calc(polish_exp):
			stack = []
			for token in polish_exp:
				if token in self.ACTIONS and token != '¬':
					y, x = stack.pop(), stack.pop()
					stack.append(self.ACTIONS[token][1](x, y))
				elif token == '¬':
					x = stack.pop()
					stack.append(self.ACTIONS[token][1](x))
				else:
					stack.append(token)
			return stack[0]

		if mode == 'calc':
			return int(calc(shunting_yard(parse(exp))))
		elif mode == 'schaef':
			self.shaef_basis = make_schaef(shunting_yard(parse(self.ans_pdnf)))
		elif mode == 'pier':
			pass



	def make_table(self, size):

		if size == 1:
			for x in [0, 1]:
				expr = self.expression
				expression = ''
				for i in expr:
					if i == 'x':
						expression += str(x)
					else:
						expression += i
				f = self.evaluate(expression, 'calc')
				if f == 1:
					self.pdnf.append([x])
				else:
					self.pcnf.append([x])
				self.lines.append([x, f])
				self.answers.append(f)

		elif size == 2:
			for x in [0,1]:
				for y in [0,1]:
					expr = self.expression
					expression = ''
					for i in expr:
						if i == 'x':
							expression += str(x)
						elif i == 'y':
							expression += str(y)
						else:
							expression += i
					f = self.evaluate(expression, 'calc')
					if f == 1:
						self.pdnf.append([x, y])
					else:
						self.pcnf.append([x, y])
					self.lines.append([x, y, f])
					self.answers.append(f)

		if size == 3:
			for x in [0,1]:
				for y in [0,1]:
					for z in [0,1]:
						expr = self.expression
						expression = ''
						for i in expr:
							if i == 'x':
								expression += str(x)
							elif i == 'y':
								expression += str(y)
							elif i == 'z':
								expression += str(z)
							else:
								expression += i
						f = self.evaluate(expression, 'calc')
						if f == 1:
							self.pdnf.append([x, y, z])
						else:
							self.pcnf.append([x, y, z])
						self.lines.append([x, y, z, f])
						self.answers.append(f)

		if size == 4:
			for x in [0,1]:
				for y in [0,1]:
					for z in [0,1]:
						for t in [0,1]:
							expr = self.expression
							expression = ''
							for i in expr:
								if i == 'x':
									expression += str(x)
								elif i == 'y':
									expression += str(y)
								elif i == 'z':
									expression += str(z)
								elif i == 't':
									expression += str(t)
								else:
									expression += i
							f = self.evaluate(expression, 'calc')
							if f == 1:
								self.pdnf.append([x, y, z, t])
							else:
								self.pcnf.append([x, y, z, t])
							self.lines.append([x, y, z, t, f])
							self.answers.append(f)