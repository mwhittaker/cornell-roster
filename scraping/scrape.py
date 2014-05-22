import urllib2
from bs4 import BeautifulSoup

BASEURL = 'http://registrar.sas.cornell.edu/courses/roster/FA14/'

SUBJECTS = ["AAS", "AEM", "AEP", "AGSCI", "AIRS", "AIS", "ALS", "AMST", "ANSC",
"ANTHR", "ARCH", "ARKEO", "ART", "ARTH", "ASIAN", "ASRC", "ASTRO", "BCS",
"BEE", "BENGL", "BIOAP", "BIOEE", "BIOG", "BIOMG", "BIOMI", "BIOMS", "BIONB",
"BIOPL", "BME", "BSOC", "BTRY", "BURM", "CAPS", "CEE", "CHEM", "CHEME", "CHIN",
"CHLIT", "CLASS", "COGST", "COLLS", "COML", "COMM", "CRP", "CS", "CSS", "DEA",
"DSOC", "DUTCH", "EAS", "ECE", "ECON", "EDUC", "ENGL", "ENGRC", "ENGRD",
"ENGRG", "ENGRI", "ENTOM", "FDSC", "FGSS", "FREN", "FSAD", "GERST", "GOVT",
"GRAD", "GREEK", "HADM", "HD", "HE", "HINDI", "HIST", "HORT", "IARD", "ILRHR",
"ILRIC", "ILRID", "ILRLE", "ILRLR", "ILROB", "ILRST", "IM", "INDO", "INFO",
"ITAL", "JAPAN", "JPLIT", "JWST", "KHMER", "KOREA", "LA", "LATA", "LATIN",
"LAW", "LGBT", "LING", "LSP", "MAE", "MATH", "MEDVL", "MILS", "MSE", "MUSIC",
"NAVS", "NBA", "NCC", "NEPAL", "NES", "NRE", "NS", "NSE", "NTRES", "ORIE",
"PAM", "PE", "PHIL", "PHYS", "PLBR", "PLPA", "PLSCI", "PMA", "POLSH", "PORT",
"PSYCH", "RELST", "ROMAN", "ROMS", "RUSSA", "RUSSL", "SANSK", "SEA", "SHUM",
"SINHA", "SNES", "SOC", "SPAN", "STS", "STSCI", "SYSEN", "TAG", "TAMIL",
"THAI", "TIBET", "TOX", "URDU", "VETCS", "VETMI", "VETMM", "VIEN", "VIET",
"VISST", "VTBMS", "VTMED", "VTPMD", "WRIT"]

def scrape_subject(subject):
    page = urllib2.urlopen(BASEURL + subject + "/").read()
    soup = BeautifulSoup(page)
    courses = soup.find_all("div", {"class": "course"})

    for course in courses:
        course_name = course.find("div", {"class": "l1"}).get_text()
        parts = course_name.split()
        print "{}, {}, {}".format(parts[0], parts[1], " ".join(parts[3:]))

def main():
    for subject in SUBJECTS:
        scrape_subject(subject)

if __name__ == "__main__":
    main()

