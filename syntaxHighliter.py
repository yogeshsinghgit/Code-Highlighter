from tkinter import *
from tkinter.ttk import Combobox,Checkbutton
from tkinter import ttk,messagebox
from tkinter.scrolledtext import ScrolledText
from pygments import highlight # pip install pygments
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import re
import pyperclip as pc 

class HighlightCode():
	"""
	Created by yogesh singh and please follow my instagram page @dynamiccoding for more projects 
	Plese install pygments and pyperclip .
	.
	make sure to follow me on github as well .

	and give feedback and suggestions also .........
	"""
	def __init__(self,root):
		self.root = root

		self.check_line_on = BooleanVar()   

		self.code_text = ScrolledText(self.root,bd=4,relief=GROOVE)
		self.code_text.place(x=0,y=0,height=300,width=300)


		self.output_code = ScrolledText(self.root,bd=4,relief=GROOVE)
		self.output_code.place(x=300,y=0,height=300,width=300) 

		self.control_frame = Frame(self.root,bd=2,relief=GROOVE)
		self.control_frame.place(x=25,y=310,height=130,width=550)

		# ................ controls in control frames ...................

		self.languages = ['python','C','C++','java','php','C#']

		self.borders = ['dotted','dashed','solid','double','groove','ridge','inset','none','hidden']

		#self.border_width = ['2px','4px','6px','8px','10px','medium','thick']

		self.border_clrs = ['red','black','gray','white','green','yellow','pink','cyan','sky blue']

		self.styles = ['default', 'emacs', 'friendly', 'colorful', 'autumn', 'murphy', 
		 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 
		'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 
		'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap',
		 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 'inkpot']

		self.style_combo = Combobox(self.control_frame,width=20,values=self.styles,justify=CENTER)
		self.style_combo.set('Select Style')
		self.style_combo.place(x=10,y=5)

		self.border_combo = Combobox(self.control_frame,width=20,values=self.borders,justify=CENTER)
		self.border_combo.set('Select Border')
		self.border_combo.place(x=10,y=45)

		
		self.border_color_combo = Combobox(self.control_frame,width=20,values=self.border_clrs,justify=CENTER)
		self.border_color_combo.set('Border Color')
		self.border_color_combo.place(x=10,y=85)

		self.language_combo = Combobox(self.control_frame,width=15,values=self.languages,justify=CENTER)
		self.language_combo.set('python')
		self.language_combo.place(x=180,y=40)

		self.Line_no_check = Checkbutton(self.control_frame,text='Enable Line No.',onvalue=True,offvalue=False,
			variable=self.check_line_on)
		self.Line_no_check.place(x=180,y=9)

		


		highlight_btn = ttk.Button(self.control_frame,text='Highlight',command=self.highlight_code)
		highlight_btn.place(x=300,y=10)

		copy_edit_code = ttk.Button(self.control_frame,text='Copy Code',command=self.copy_code)
		copy_edit_code.place(x=300,y=50)

		clear_input_text = ttk.Button(self.control_frame,text='Clear Input Box',
			width=20,command=lambda:self.code_text.delete(0.0,END))
		clear_input_text.place(x=400,y=10)

		clear_output_text = ttk.Button(self.control_frame,text='Clear Output Box',
			width=20,command=lambda:self.output_code.delete(0.0,END))
		clear_output_text.place(x=400,y=50)


# ............... Functions  .....................

	def highlight_code(self):
		self.output_code.delete(0.0,END)
		lexer = self.language_combo.get()
		linenos = self.check_line_on.get()
		defstyles = 'overflow:auto;width:auto;'
		divstyles = self.get_default_style()
		style = self.style_combo.get()
		if style == 'Select Style':
			style ='default'

		code = self.code_text.get(0.0,END)

		formatter = HtmlFormatter(style=style,
                              linenos=False,
                              noclasses=True,
                              cssclass='',
                              cssstyles=defstyles + divstyles,
                              prestyles='margin: 0')
		html = highlight(code, get_lexer_by_name(lexer, stripall=True), formatter)
		if linenos:
			html = self.insert_line_numbers(html)
		html = "<!-- Syntax Highlighter by Dynamic Coding Code Highlighter -->" + html
		self.output_code.insert(0.0,html)

	def get_default_style(self):
		if self.border_color_combo.get() != 'Border Color'  or self.border_combo.get() != 'Select Border':
			if self.border_color_combo.get() == 'Border Color':
				self.border_color_combo.set('solid')
			if self.border_combo.get() == 'Select Border':
				self.border_combo.set('gray')

			return 'border:'+str(self.border_combo.get())+' '+str(self.border_color_combo.get())+';border-width:.1em .1em .1em .8em;padding:.2em .6em;'
		else:
			return 'border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;'

	def insert_line_numbers(self,html):
	    match = re.search('(<pre[^>]*>)(.*)(</pre>)', html, re.DOTALL)
	    if not match: return html

	    pre_open = match.group(1)
	    pre = match.group(2)
	    pre_close = match.group(3)

	    html = html.replace(pre_close, '</pre></td></tr></table>')
	    numbers = range(1, pre.count('\n') + 1)
	    format = '%' + str(len(str(numbers[-1]))) + 'i'
	    lines = '\n'.join(format % i for i in numbers)
	    html = html.replace(pre_open, '<table><tr><td>' + pre_open + lines + '</pre></td><td>' + pre_open)
	    return html

	def copy_code(self):
		pc.copy(self.output_code.get(0.0,END))
		messagebox.showinfo("Highlighter says"," Code is copied to Clipboard")


if __name__ == '__main__':
	root = Tk()
	HighlightCode(root)
	root.title("Code Highlighter")
	root.geometry('600x450+250+200')
	root.configure(bg='white')
	root.resizable(0,0)
	print(" Created by yogesh singh and please follow my instagram page @dynamiccoding for more projects ")
	root.mainloop()
	


