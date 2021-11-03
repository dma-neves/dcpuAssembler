PROGRAM = average

ROM_DIR = /home/david/Desktop/David/Programming/HDL/projects/dcpu/src/Memory/ROM.vhd
LOCAL_ROM = files/ROM256.vhd

all: $(ROM_DIR)

%.strbinary: %.s src/assembler.py
	python3 src/assembler.py $< s

$(LOCAL_ROM): files/$(PROGRAM).strbinary src/romGenerator.py
	python3 src/romGenerator.py $<

$(ROM_DIR): $(LOCAL_ROM)
	cp -f files/ROM.vhd $(ROM_DIR)