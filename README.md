# Cornell Roster #
This is a small project used to explore and learn mongodb and pymongo.

## Getting Started ##
First, we'll scrape the web for the cornell roster. Make sure you're inside the
`scraping` directory.

    make db

This will create a csv of the roster and then use `mongoimport` to create a
roster collection inside the cornell database. Now, we're all set to query the
roster. Head over to the `repl` directory.

    python repl.py

From here, you can enter words and phrases.

## Dependencies ##
- mongodb
- pymongo
- beautifulsoup4
