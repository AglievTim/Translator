import os
import docx
import boto3

def readtxt(file):
	doc = docx.Document(file)
	fullText = ''
	for paragraph in doc.paragraphs:
		fullText += paragraph.text
		fullText += '\n\n'
	return fullText; 

def translateText(text):

	translate = boto3.client(service_name = 'translate', region_name = 'eu-west-1',
		use_ssl = True)

	result = translate.translate_text(Text = text, SourceLanguageCode = 'ru',
		TargetLanguageCode = 'en')

	return result.get('TranslatedText')

def createDocx(text):
	doc = docx.Document()
	doc.add_paragraph(text)
	doc.save('file.docx')


createDocx(translateText(readtxt('Input/file.docx')))

