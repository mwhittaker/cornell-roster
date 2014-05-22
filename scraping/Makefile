roster.csv: scrape.py
	python scrape.py | uniq > $@

db: roster.csv
	mongoimport --db cornell        \
				--collection roster \
			   	--type csv          \
				--headerline        \
				--file roster.csv   \
				--drop

clean:
	test ! -f roster.csv || rm -i roster.csv
