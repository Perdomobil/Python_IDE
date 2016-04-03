import tempfile, subprocess, Tkinter


class Python_IDE:
	def __init__(self, obj):
		self.compile_button = Tkinter.Button(obj, text = "Compile")
		self.compile_button.bind("<Button-1>", self.Compile_Button_Handler)
		self.compile_button.place(relx = 0.7, rely = 0.05, relwidth = 0.2, relheight = 0.1)

		self.source_code = Tkinter.Text(obj, font = "Arial 14", wrap = Tkinter.WORD)
		self.source_code.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.49)

		self.result_message = Tkinter.Text(obj, font = "Arial 14", wrap = Tkinter.WORD)
		self.result_message.place(relx = 0.05, rely = 0.7, relwidth = 0.9, relheight = 0.2)


	def _source_to_file(self, path):
		source_text = self.source_code.get(1.0, Tkinter.END)
		with open(path, 'w') as f:
			f.write(source_text)


	def Compile_Button_Handler(self, event):
		python_path = "python2.7"
		save_file_path = "pri.py"

		self._source_to_file(save_file_path)

		cmd  = "%s %s" % (python_path, save_file_path)
		popen = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
		stdoutdata, stderrdata = popen.communicate()
		out_message = stderrdata if popen.returncode else stdoutdata
		self.result_message.insert(Tkinter.END, out_message)


def main():
	root = Tkinter.Tk()
	root.title("Python IDE")
	root.geometry("600x400")
	python_IDE = Python_IDE(root)
	root.mainloop()

main()

