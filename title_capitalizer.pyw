from titlecase import titlecase
import pyperclip

string = pyperclip.paste()

title = titlecase(string)
pyperclip.copy(title)
