ifeq ($(OS),Windows_NT)
	uname_S := Windows
	WinBuild = 1
	BFLAGS= -DWinBuild
else 
	uname_S := $(shell uname -s)
	BFLAGS= 	
endif

# PREFIX is environment variable, but if it is not set, then set default value
ifeq ($(PREFIX),)
    PREFIX := ~/bin
endif

setup: requirements.txt
	pip3 install -r requirements.txt

clean:
	rm -rf __pycache__

install:
	install -m 755 changeBrightness.py $(PREFIX)/
	install -m 755 changeColor.py $(PREFIX)/
	install -m 755 coolerColor.py $(PREFIX)/
	install -m 755 info_keyLight.py $(PREFIX)/
	install -m 755 setColor.py $(PREFIX)/
	install -m 755 toggle_keyLight.py $(PREFIX)/
	install -m 755 turnOff_keyLight.py $(PREFIX)/
	install -m 755 turnOn_keyLight.py $(PREFIX)/
	install -m 755 warmerColor.py $(PREFIX)/

remove:
	rm $(PREFIX)/changeBrightness.py
	rm $(PREFIX)/changeColor.py
	rm $(PREFIX)/coolerColor.py
	rm $(PREFIX)/info_keyLight.py
	rm $(PREFIX)/setColor.py
	rm $(PREFIX)/toggle_keyLight.py 
	rm $(PREFIX)/turnOff_keyLight.py
	rm $(PREFIX)/turnOn_keyLight.py
	rm $(PREFIX)/warmerColor.py
