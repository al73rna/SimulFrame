import dominate
#import pdfkit
from dominate.tags import *

class Reports_and_Results():
	def __init__(self):
		self.counter = 0
		self.doc = dominate.document(title='Results & Reports')
		self.initialize_doc()

	def initialize_doc(self):
		with self.doc.head:
			link(rel='stylesheet', href='chartist.min.css')
			link(rel='stylesheet', href='jquery.dataTables.min.css')
			script(type='text/javascript', src='jquery-2.1.4.min.js')
			script(type='text/javascript', src='jquery.dataTables.min.js')
			f1 = open('chart.js', 'w')
			f2 = open('table.js', 'w')
			f1.close()
			f2.close()

	def finalize_doc(self):
		with self.doc:
			script(type='text/javascript', src='chartist.min.js')
			script(type='text/javascript', src='chart.js')
			script(type='text/javascript', src='table.js')

	def add_text(self, text):
		with self.doc:
			p(text)

	def add_table(self, titles, dataset):
		self.counter += 1
		f = open('table.js', 'a')
		ptrn = "var %s = %s;"
		f.write(ptrn%("dataSet"+str(self.counter), dataset))
		new_titles = list()
		for title in titles:
			new_titles.append({'title' : title})
		title_pattern = "$('document').ready(function(){$('#%s').DataTable({data: %s,columns:%s});});"
		f.write(title_pattern %("table"+str(self.counter), "dataSet"+str(self.counter), str(new_titles)))
		f.close()

		with self.doc:
			dominate.tags.table(cls='display', id='%s'%('table'+str(self.counter)))

	def add_chart(self, chart_type, labels, values):
		self.counter += 1
		if chart_type == "pie":
			pattern = self.pie_chart(labels, values)
		elif chart_type == "line":
			pattern = self.line_chart(labels, values)
		elif chart_type == "area":
			pattern = self.area_chart(labels, values)
		elif chart_type == "bar":
			pattern = self.bar_chart(labels, values)
		else:
			pattern = ""

		js_file = open('chart.js', 'a')
		js_file.write(pattern %(chart_type+str(self.counter), chart_type+str(self.counter), str(labels), str(values)))
		js_file.close()

		with self.doc:
			div(cls='ct-chart ct-perfect-fourth', id='%s'%(chart_type+str(self.counter)), style="width:600px; height:400px;")

	def pie_chart(self, labels, values):
		pattern = "var %s = new Chartist.Pie('#%s', { labels: %s, series: %s }, { width: 540, height: 360, labelInterpolationFnc: function(value) {return value[0]} }, [['screen and (min-width: 640px)', {chartPadding: 30,labelOffset: 100,labelDirection: 'explode',labelInterpolationFnc: function(value) {return value;}}],['screen and (min-width: 1024px)', {labelOffset: 80, chartPadding: 20}]]);"
		return pattern

	def line_chart(self, labels, values):
		pattern = "var %s = new Chartist.Line('#%s', { labels: %s, series: [%s] }, { width: 540, height: 360 });"
		return pattern

	def area_chart(self, labels, values):
		pattern = "var %s = new Chartist.Line('#%s', { labels: %s, series: [%s] }, { width: 540, height: 360, low: 0, showArea: true });"
		return pattern

	def bar_chart(self, labels, values):
		pattern = "var %s = new Chartist.Bar('#%s', { labels: %s, series: [%s] }, { width: 540, height: 360 });"
		return pattern

	def generate_reports_and_results(self):
		self.finalize_doc()
		with open('index.html', 'w') as f:
			f.write(self.doc.render())
		#pdfkit.from_file('index.html', 'Reports.pdf')


