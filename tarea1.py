# -*- coding: latin-1 -*-
""" Tarea 1 INF335 - Tecnologías de Bíusqueda en la Web
Universidad Técnica Federico Santa Maria"""

__author__ = "Mati, Nico"
__version__ = "0.1"

#import MySQLdb

from helpers import document_wrapper
from helpers import insert_into_mysql

years = ["01", "02", "03", "04", "05", "06",
"07", "08", "09", "10", "11", "12"]

# Fill the Document table using the cx files
# that contains the document description (year,
# title and autors)

# idx folder relative path
idx_path = "nipstxt/idx/"
columns = ["ID", "title", "year", "authors"]

for year in years:
    rows = []
    with open(idx_path + "c" + year + ".txt", "r") as fo:
        for doc in document_wrapper(fo.read().split('\n')):
            insert_into_mysql(
                'Document',
                columns,
                [(int(doc[2]), doc[0], 2000 + int(year), doc[1])])

            # print "Title: ", doc[0]
            # print "Authors: ", doc[1]
            # print "Year: 20" + year
            # print "ID: " + doc[2]
