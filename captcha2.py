
#captcha2 module
from io import BytesIO
import numpy as np
import random,requests
from PIL import Image,ImageFilter,ImageOps
import pytesseract as pyt
def levenshteinDistance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
def remove_noise_by_pixel(img, column, line, pass_factor):
    if img.getpixel((column, line)) < pass_factor:
        return (0)
    return (255)
def remove_noise(img, pass_factor):
    for column in range(img.size[0]):
        for line in range(img.size[1]):
            value = remove_noise_by_pixel(img, column, line, pass_factor)
            img.putpixel((column, line), value)
    return img
	

def solveCaptcha(url='http://result2.gtu.ac.in/Handler.ashx',cookies=None,headers=None,requests_content=None):
	if not requests_content:
		de=requests.get(url,cookies=cookies or {},headers=headers or {})
		i1=Image.open(BytesIO(de.content))
	else:
		de=None        
		i1=Image.open(BytesIO(requests_content))
	#remove red box boundary
	i2=i1.crop((i1.width*.1,i1.height*.1,i1.width*.9,i1.height*.9))
	#grayscale
	i3=ImageOps.invert(i2).copy().convert('L')
	#crop empty gray space
	newI=[]
	for r in np.array(i3):
		if sum(r)>=26*len(r):newI.append(r.tolist())
	newIc=[]
	for c in np.array(newI).astype('uint8').T:
		if sum(c)>=26*len(c):newIc.append(c.tolist())
	Fimg=np.array(newIc).T.astype('uint8')
	iff=ImageOps.invert(Image.fromarray(Fimg))
	#remove single pixel line (strike)
	minis,mini=sum(np.array(iff)[0]),0
	for ir,r in enumerate(np.array(iff)):
		if sum(r)<minis:
			minis=sum(r)
			mini=ir
	fif=[]
	#add extra whitespace (by padh%)
	padh=.25
	for padi in range(int(iff.height*padh)):
		fif.append([255]*iff.width)
	for ir,r in enumerate(np.array(iff)):
		if ir!=mini:fif.append(r.tolist())
		else:
			#add avg pixel instead of strike line
			fiifi=r.tolist()
			for ifiifi,vfiifi in enumerate(fiifi):
				fiifi[ifiifi]=int((int(np.array(iff)[ir-1][ifiifi])+int(np.array(iff)[ir+1][ifiifi]))/2)
			fif.append(fiifi)
	for padi in range(int(iff.height*padh)):
		fif.append([255]*iff.width)
	
	fof=Image.fromarray(np.array(fif).astype('uint8'))

	#change grey pixels to white
	fof=remove_noise(fof.copy(),150)
	
	#scaler func [simple image resize -maintain ratio]
	def resz(im,sc):
		imr=im.resize((sc,int(sc*im.height/im.width)))
		return imr
	ocr=[]
	for s in [fof.size[0],60,90,120]:
		ocrs=''.join(filter((lambda x:x.isalnum()),pyt.image_to_string(resz(fof.copy(),s))))
		#print("scale=",s,"ocr=",ocrs)
		ocr.append(ocrs)
	ed=[]
	for oi,ov in enumerate(ocr):
		for oj,ovj in enumerate(ocr[oi+1:]):
			ed.append([oi,oi+1+oj,levenshteinDistance(ov,ovj)])
	#print("ed",ed)
	nocr=set()
	med=min(ed,key=lambda x:x[-1])
	#print("med",med)
	for oi,oj,edi in ed:
		if edi==med[-1]:
			nocr.add(ocr[oi]) 
			nocr.add(ocr[oj])
	return {'captcha':random.choice(list(nocr)),'conf':int(99.9/len(nocr)),'requests':de,'imgObj':i1}
if __name__=='__main__':
	s=solveCaptcha()
	print(s)
	display(s['imgObj'])
