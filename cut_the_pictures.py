#coding:utf-8
from PIL import Image

working_space = 'captures/source_files/'

im = Image.open(working_space + '1号店.png')
print im.format, im.size, im.mode
#im.show()

index_profile = im.crop((36, 476, 2231, 754))
index_profile.save('captures/cropped_files/' + 'index_profile.png', 'png')
#index_profile.show()

start_date = index_profile.crop((235, 25, 375, 55))
end_date = index_profile.crop((400, 25, 535, 55))
start_date.save('captures/cropped_files/' + 'start_date.png', 'png')
end_date.save('captures/cropped_files/' + 'end_date.png', 'png')
#index_profile.show()
#start_date.show()
#end_date.show()

search_index_all = index_profile.crop((536, 185, 715, 250))
search_index_mobile = index_profile.crop((715, 185, 900, 250))
search_index_all.save('captures/cropped_files/' + 'search_index_all.png', 'png')
search_index_mobile.save('captures/cropped_files/' + 'search_index_mobile.png', 'png')
#search_index_all.show()
#search_index_mobile.show()

keyword = index_profile.crop((45, 175, 325, 255))
keyword.save('captures/cropped_files/' + 'keyword.png', 'png')
#keyword.show()




