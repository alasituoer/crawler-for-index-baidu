#coding:utf-8
from PIL import Image

working_space = 'captures/'

im = Image.open(working_space + '1号店.png')
print im.format, im.size, im.mode
#im.show()

index_profile = im.crop((36, 476, 2231, 754))
#index_profile.show()

start_date = index_profile.crop((235, 25, 375, 55))
end_date = index_profile.crop((400, 25, 535, 55))
#start_date.show()
#end_date.show()

search_index_all = index_profile.crop((536, 185, 715, 250))
search_index_mobile = index_profile.crop((715, 185, 900, 250))
#search_index_all.show()
#search_index_mobile.show()

keyword = index_profile.crop((45, 175, 325, 255))
#keyword.show()

