default: cv

data.toml:
	python data.py decrypt data.bin > data.toml

data.bin: data.toml data.py
	python data.py encrypt data.toml > data.bin

cv: data.py data.bin template.html
	python render.py

clean:
	rm -rf cv.html
