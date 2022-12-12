# term-porject
Tesseract and letters and hbcvt were used

!pip install pytesseract

!pip install jamo

!pip install hbcvt

pytesseract : 
https://github.com/UB-Mannheim/tesseract

jamo : 
https://github.com/JDongian/python-jamo

hbcvt:
https://github.com/hyonzin/hangul-braille-converter

pytesseract need to download and set the path
For more information on the settings, please refer to the blog that I referred to
https://joyhong.tistory.com/79

Image :

![gall2](https://user-images.githubusercontent.com/108784781/207126506-939635a9-bbc4-44ad-a2e4-1777b03c0aff.png)

Extract the letters from the image:

타인을 아는 사람은 지혜롭지만

자신을 아는 사람은 현명하다

Separate consonants and vowels:

ㅌㅏㅇㅣㄴㅇㅡㄹ ㅇㅏㄴㅡㄴ ㅅㅏㄹㅏㅁㅇㅡㄴ ㅈㅣㅎㅖㄹㅗㅂㅈㅣㅁㅏㄴ

ㅈㅏㅅㅣㄴㅇㅡㄹ ㅇㅏㄴㅡㄴ ㅅㅏㄹㅏㅁㅇㅡㄴ ㅎㅕㄴㅁㅕㅇㅎㅏㄷㅏ.

Out of the total 6 spaces of braille, order from top right to bottom, then from top left to bottom, 

and put 1 if there are dots in the list and 0 if there are no dots :

['타', [['ㅌ', [[1, 1, 0, 0, 1, 0]]], ['ㅏ', [[1, 1, 0, 0, 0, 1]]]]]

['인', [['ㅇ', [[1, 1, 0, 1, 1, 0]]], ['ㅣ', [[1, 0, 1, 0, 1, 0]]], ['ㄴ', [[0, 1, 0, 0, 1, 0]]]]] 

['을', [['ㅇ', [[1, 1, 0, 1, 1, 0]]], ['ㅡ', [[0, 1, 0, 1, 0, 1]]]

...

Draw a dot based on the list:

![result](https://user-images.githubusercontent.com/108784781/207130841-de5fa96b-09ae-4318-ada5-dd82780cd101.png)

