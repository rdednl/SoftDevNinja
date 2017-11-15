P=$(wildcard pictures/*.jpg)
T=$(P:pictures/%.jpg=thumbs/%.jpg)
all: $(T)
thumbs/%.jpg: pictures/%.jpg
	convert -thumbnail 100 $^ $@