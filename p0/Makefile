
SRC=hw
EXE=$(SRC)


do: console

all: console postscript troff clean

console: awk bc c c++ factor forth haskell java javascript lisp lua perl python ruby rust scheme sh \
	 clean

python: $(SRC).py
	@echo "Hello world en $@..."
	python3 $<
clean:
	@echo "Limpiando..."
	rm -f $(EXE) HelloWorld.class
