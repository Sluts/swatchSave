import urllib.request as ur
import urllib.parse as up
import re

def findem(url, chop, save):
	try:
		resp=ur.urlopen(url)
		data=resp.read().decode('utf-8', errors="ignore")
		imgs=re.findall(r'<img(.*?)>',data)
		downs(imgs,chop, save)
	except Exception as e:
		print(str(e))

def downs(imgs, chop, save):
	for i in imgs:
		src=re.findall(r'src="(.*?)"',i)
		for s in src:
			if "swatch" in s:
				if "png" in s:
					print(chop+s)
					try:
						ur.urlretrieve(str(chop)+str(s), str(save)+s[8:])
					except Exception as e:
						pass
                        
def main():
	url=input("URL: ")
	save=input("Save to: ")
	chop=re.findall(r'(.*?[c][o][m])[/]', url)
	findem(url, chop[0], save)
	return 0
	
main()
