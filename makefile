install:
	rm -rf /usr/local/bin/imagemover
	rm -rf /usr/local/bin/imagemover.py
	cp imagemover.py /usr/local/bin
	ln -s /usr/local/bin/imagemover.py /usr/local/bin/imagemover

uninstall:
	rm /usr/local/bin/imagemover
	rm /usr/local/bin/imagemover.py


