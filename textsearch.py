import os
import re
import sys


findData = []
filefullpath = ""
fileList = []
screenName = ""

def search(dirname):

	try:
		filenames = os.listdir(dirname)
		for filename in filenames:
			full_filename = os.path.join(dirname, filename)
			if os.path.isdir(full_filename):
				search(full_filename)
			else:
				ext = os.path.splitext(full_filename)[-1]
				if ext == '.cs':
					fileList.append(full_filename)
	except PermissionError:
		pass
	return fileList

def findtext(filepathList, target):
	findData.clear()
	for filepath in filepathList:
		try:
			f = open(filepath, "r", encoding="utf-8")
			document_text = f.read()
			match_pattern = re.search(target, document_text)
			if match_pattern != None:
				findData.append(filepath)
			f.close()
		except BaseException:
			print("error : ", filepath, match_pattern)
	writecsv(findData, target)


#file path 에서 \ 기준으로 마지막 문자 파싱. 마지막 문자에서 . 기준으로 처음 문자 파싱 => 화면명 및 컨트롤 명 추출됨
def parsing(filepath):
	parsed = filepath.split("\\")
	screenName = parsed[-1].split(".")[0]
	return screenName

#csv 파일로 쓰기
def writecsv(foundList, target):
	if os.path.exists("result.csv"):
		f = open("result.csv", "a")
	else:
		f = open("result.csv", "w")
	for content in foundList:
		screenName = parsing(content)
		print(screenName)
		f.write(screenName + "," + target + "\n")
	f.close()

# 검색할 파일 리스트 찾기
csFileList = search(sys.argv[1])
#csFileList 에서 문자열 찾기
# findtext(csFileList,"(외국인등록번호)")
# findtext(csFileList,"(외국인 등록번호)")
# findtext(csFileList,"(외국인등록 번호)")
# findtext(csFileList,"(주민번호)")
# findtext(csFileList,"(주민 번호)")
# findtext(csFileList,"(주민등록번호)")
# findtext(csFileList,"(주민등록 번호)")
# findtext(csFileList,"(주민 등록번호)")
# findtext(csFileList,"(주민 등록 번호)")
# findtext(csFileList,"(여권번호)")
# findtext(csFileList,"(여권 번호)")
# findtext(csFileList,"(운전면허 번호)")
# findtext(csFileList,"(운전 면허번호)")
# findtext(csFileList,"(운전면허번호)")
# findtext(csFileList,"(운전 면허 번호)")
# findtext(csFileList,"SimplePrint")
findtext(csFileList,"PrintDialog")
# findtext(csFileList,"PrintPreview")
findtext(csFileList,"ExportToXlsx")
findtext(csFileList,"ExportToXls")

#testparsing(csFileList)
