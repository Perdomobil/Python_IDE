import tempfile
import subprocess
import Tkinter


class Python_IDE:
	def __init__(self, obj):
		self.save_file_path = Tkinter.Text(obj, font = "Arial 12", wrap = Tkinter.WORD)
                self.save_file_path.place(relx = 0.05, rely = 0.12, relwidth = 0.2, relheight = 0.075)
                self.save_file_path.insert(Tkinter.END, "pri.py")

		self.compile_button = Tkinter.Button(obj, text = "Compile", font = "Arial 12")
		self.compile_button.bind("<Button-1>", self.compile_Button_Handler)
		self.compile_button.place(relx = 0.75, rely = 0.12, relwidth = 0.2, relheight = 0.075)

		self.code_text = Tkinter.Text(obj, font = "Arial 12", wrap = Tkinter.WORD)
		self.code_text.place(relx = 0.05, rely = 0.2, relwidth = 0.9, relheight = 0.54)
		"""scrollbar = Tkinter.Scrollbar(self.code_text)
		scrollbar.pack(side = "right")
		scrollbar["command"] = self.code_text.yview
		self.code_text["yscrollcommand"] = scrollbar.set"""

		self.output_text = Tkinter.Text(obj, font = "Arial 12", wrap = Tkinter.WORD)
		self.output_text.place(relx = 0.05, rely = 0.75, relwidth = 0.9, relheight = 0.2)

	def _code_to_file(self, path):
		code_text = self.code_text.get(1.0, Tkinter.END)
		with open(path, 'w') as f:
			f.write(code_text)

	def _compile_code(self):
		python_path = "python2.7"
		with tempfile.NamedTemporaryFile("w") as tf:
			self._code_to_file(tf.name)
                        cmd  = "{} {}".format(python_path, tf.name)
                        popen = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
			return popen.communicate(), popen.returncode


	def compile_Button_Handler(self, event):
		self.output_text.delete(1.0, Tkinter.END)
		(stdoutdata, stderrdata), return_err_code = self._compile_code()
		if return_err_code:
			self.output_text.insert(Tkinter.END, stderrdata)
		else:
			self.output_text.insert(Tkinter.END, stdoutdata)
                        self._code_to_file(self.save_file_path.get(1.0, Tkinter.END).replace("\n",""))

def main():
	root = Tkinter.Tk()
	root.title("Python IDE")
	root.geometry("600x400")
	python_IDE = Python_IDE(root)
	root.mainloop()

main()

