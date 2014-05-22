roster.csv: scrape.py
	python scrape.py | uniq > $@

clean:
	test ! -f roster.csv || rm -i roster.csv
