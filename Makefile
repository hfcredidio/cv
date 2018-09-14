default: cv

data.bin: data.toml data.py
	@python data.py data.toml data.bin ${CVKEY}

cv: data.py data.bin template.html
	python render.py

clean:
	rm -rf cv.html
