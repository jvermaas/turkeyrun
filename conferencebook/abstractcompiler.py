import glob

pdfs = sorted(glob.glob("abstracts/*pdf"),key=str.casefold)

talklastnames = {"Govindjee", "Gisriel", "Ponomarenko", "Kashyap", "Metskas", "Rillema", "Sharma", "Malnoe", "Steiner", "Phadkule", "Elrefaiy", "Bindra", "Vinyard", "Lakshmi", "Vermaas", "Jones", "Hou", "Mohamed"}
talkalphabet = ""
posteralphabet = ""
talkincludes = ""
posterincludes = ""
for pdf in pdfs:
	lastname = pdf.split("/")[1].split("_")[0].title()
	print(lastname)
	if lastname in talklastnames:
		talkincludes += "\\includepdf[link=true,linkname=%s,pagecommand={\\thispagestyle{plain}},addtolist={1,talk,heading,abs:%s}]{%s}\n" % (lastname, lastname, pdf)
		talkalphabet += "\\item \\hyperlink{%s.1}{%s} pg. \\pageref{abs:%s}\n" % (lastname, lastname, lastname)
	else:
		posterincludes += "\\includepdf[link=true,linkname=%s,pagecommand={\\thispagestyle{plain}},addtolist={1,nottalk,heading,abs:%s}]{%s}\n" % (lastname, lastname, pdf)
		posteralphabet += "\\item \\hyperlink{%s.1}{%s} pg. \\pageref{abs:%s}\n" % (lastname, lastname, lastname)
fout = open("talkincludes.tex", "w")
fout.write(talkincludes)
fout.close()
fout = open("posterincludes.tex", "w")
fout.write(posterincludes)
fout.close()
fout = open("talkalphabet.tex", "w")
fout.write(talkalphabet)
fout.close()
fout = open("posteralphabet.tex", "w")
fout.write(posteralphabet)
fout.close()