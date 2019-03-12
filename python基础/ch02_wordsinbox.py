#以正确的宽度在居中的“盒子”内打印一个句子

#注意，整数除法运算符（//）只用在python2.2及后续版本

sentence=input("Sentence:")

screen_width=80
text_width=len(sentence)
box_width=text_width+6
#左外边距
left_margin=(screen_width-box_width)//2
#左内边距
left_padding=(box_width-2-text_width)//2

print()
print(' '*left_margin+'+'+'-'*    (box_width-2)                     +'+')
print(' '*left_margin+'|'+' '*    (box_width-2)                     +'|')
print(' '*left_margin+'|'+' '*left_padding+sentence+' '*left_padding+'|')
print(' '*left_margin+'|'+' '*    (box_width-2)                     +'|')
print(' '*left_margin+'+'+'-'*(    box_width-2)                     +'+')
print()
