"""
generate_mailto.py
create a mailto with a subject and body
"""
import webbrowser

def gen_mailto(subject, body, recipient='capital.agile.services@gmail.com'):
	"""
	generate mailto
	"""
	webbrowser.open(f"mailto:{recipient}?subject={subject}&body={body}")
