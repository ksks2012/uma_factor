import pyscreenshot as ImageGrab


# 擷取全螢幕畫面
image = ImageGrab.grab(bbox=(1300, 100, 1920, 800))

# 儲存檔案
image.save("fullscreen.png")