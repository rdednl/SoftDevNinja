import gdb

class pstruct(gdb.Command):
	def __init__(self):
		gdb.Command.__init__(self, "pstruct", gdb.COMMAND_NONE)
	
	def invoke(self, arguments, from_tty):
		def formatstring(char, mem):
			if char == 'i':
				res =  gdb.execute("x/dw" + hex(mem), False, True)
				print ">", res.split()[1]
				mem = mem + 4
			elif char == 'l':
				res = gdb.execute("x/dg" + hex(mem), False, True)
				print ">", res.split()[1]
				mem = mem + 4
			elif char == 'f':
				res = gdb.execute("x/fw" + hex(mem), False, True)
				print ">", res.split()[1]
				mem = mem + 4
			elif char == 's':
				res = gdb.execute("x/sb" + hex(mem), False, True)
				print ">", res.split()[1]
				mem = mem + 4
			elif char == 'p':
				res =  gdb.execute("x/ag" + hex(mem), False, True)
				print ">", res.split()[1]
				mem = mem + 48
			elif char == '.':
				mem = mem + 4
			return mem

		argv = gdb.string_to_argv(arguments)
		mem = int(argv[0], 16)
		print "-------------"
		res2 = 0
		while True:
			for char in argv[1]:
				if char != 'n':
					mem = formatstring(char, mem)
				else:
					res2 = gdb.execute("x/ag" + hex(mem), False, True)
					res2 = int(res2.split()[1], 16)
					mem = mem + 8
			print "-------------"
			if (res2 == 0):
				return
			else:
				mem = res2
pstruct()
