"""Test configs."""
import json 
import pytest
from webapp.panels import Panel, PanelOne, PanelTwo, PanelThree

HTML = """
<!DOCTYPE html>
<html lang="en" class="full-height">
    <head>
        <title>Title</title>
    </head>
    <body>
        <header>
        </header>
        <main>
            <p>Lorem ipsum dolor sit amet justo. Aliquam ante sit amet ultricies urna orci eget egestas sodales,
            augue nec sem nec nulla. Duis ornare euismod. Vestibulum ullamcorper pellentesque. 
            Proin scelerisque sem. Pellentesque at arcu. Pellentesque habitant morbi tristique sodales. 
            Vivamus iaculis, dui sit amet dui. Etiam varius, scelerisque a, faucibus orci ac nunc fringilla enim. 
            Aliquam fringilla, massa. Vivamus ut massa. Curabitur nunc. Suspendisse auctor, sapien sapien, ornare id, 
            tortor. Cum sociis natoque penatibus et nunc ac lectus. In quis nisl. Curabitur arcu quis ipsum. 
            Lorem ipsum primis in vestibulum ac, accumsan vestibulum. Nullam justo. Nulla cursus ut, eleifend
            pede urna sem pede eget augue. Morbi et lacus ultrices posuere, lacus eu odio. Mauris metus. 
            Nulla gravida gravida justo, eget magna. Aliquam nec magna sapien, tempus arcu. Cum sociis natoque penatibus et leo.
            Suspendisse vel ipsum eget nisl. Nulla ligula lorem urna fringilla ante in risus. Sed tempus nulla. 
            Ut wisi vulputate sed, urna. Donec ullamcorper, risus at porttitor magna. Suspendisse ut pede. 
            Curabitur interdum. Donec porttitor varius sit amet lacus. Vivamus lacus sit amet augue at elit eu ante. 
            Quisque.</p>
        </main>
    </body>
</html>
"""

data = """{
 "start": 0,
 "num_found": 487,
 "numFound": 487,
 "docs": [
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL10681058M",
    "OL10236416M",
    "OL21217116M",
    "OL22510662M",
    "OL9559516M",
    "OL7603320M",
    "OL6165495M",
    "OL13807949M",
    "OL13761262M",
    "OL17906645M",
    "OL4883007M",
    "OL5975400M",
    "OL22406853M",
    "OL17990125M",
    "OL16539692M",
    "OL23795326M",
    "OL22815379M",
    "OL5574175M",
    "OL5535578M",
    "OL4382055M",
    "OL21318055M",
    "OL20943851M",
    "OL16791443M",
    "OL21392110M",
    "OL22470927M",
    "OL5237526M",
    "OL10682337M",
    "OL23821472M",
    "OL20200626M",
    "OL22984886M",
    "OL17885449M",
    "OL22858420M",
    "OL20943862M",
    "OL20943868M",
    "OL17912024M",
    "OL1974942M",
    "OL22836449M",
    "OL1532643M",
    "OL21217131M",
    "OL25175074M",
    "OL26450492M",
    "OL22831274M",
    "OL21217165M",
    "OL22193052M",
    "OL10236393M",
    "OL22572775M",
    "OL21058613M",
    "OL19620537M",
    "OL3966044M",
    "OL8269996M",
    "OL9444589M",
    "OL7468970M",
    "OL26418460M",
    "OL7946403M",
    "OL22820202M",
    "OL9216449M",
    "OL7261734M",
    "OL3659520M",
    "OL9216964M",
    "OL7262249M",
    "OL22819486M",
    "OL3670214M",
    "OL3380031M",
    "OL22816363M",
    "OL3321902M",
    "OL3404981M",
    "OL24278639M",
    "OL24261347M"
   ],
   "cover_i": 8069767,
   "isbn": [
    "8020409262",
    "9780618346240",
    "0618042210",
    "0618517650",
    "9780061917806",
    "9780618640157",
    "0261102389",
    "9780048230911",
    "0586218696",
    "9780395193952",
    "9780618042203",
    "0618260587",
    "039564738X",
    "0618260269",
    "0618640150",
    "0261102419",
    "061826051X",
    "1402505205",
    "0807286087",
    "9780261102347",
    "0048231495",
    "9780061917813",
    "9780618042258",
    "0618260285",
    "0007123817",
    "9780618042265",
    "0739408259",
    "9780345247865",
    "0395647398",
    "0618260595",
    "9780395647394",
    "0395647401",
    "9780586218693",
    "9780618260256",
    "9780618260553",
    "0898452236",
    "9780618042241",
    "0007172001",
    "9780807286081",
    "0061952877",
    "006191780X",
    "9781402505201",
    "9780395647387",
    "0007144083",
    "9780395974681",
    "0261102435",
    "9780618260249",
    "9780007149247",
    "0395595118",
    "9780048232007",
    "9780007144082",
    "9780618042234",
    "9780395595114",
    "3895840432",
    "0618042261",
    "9780261103566",
    "9780007635610",
    "9780618260270",
    "9780618645619",
    "0007149247",
    "9783895840432",
    "0048232009",
    "0618645616",
    "0618260250",
    "9780618260263",
    "0261103563",
    "9780898452235",
    "9780618042227",
    "004823091X",
    "9780618260584",
    "0618042253",
    "0395193958",
    "0007322593",
    "9788445070321",
    "9780261102958",
    "0061917818",
    "0618260242",
    "9780618346257",
    "0618260552",
    "9780007123810",
    "9780618042210",
    "9780618037667",
    "0618042245",
    "9780261102415",
    "0618346252",
    "0345020200",
    "9780618260515",
    "0261102346",
    "8445070320",
    "0618260277",
    "9780618517657",
    "0395974682",
    "0618042237",
    "0007635613",
    "9780048230874",
    "9780618260591",
    "0048230871",
    "9780618260287",
    "9780007322596",
    "9780007172009",
    "0618346244",
    "9780261102385",
    "9780739408254",
    "9780048231499",
    "0345247868",
    "9788422616337",
    "9780395647400",
    "8422616335",
    "0618042202",
    "0618042229",
    "9780261102439",
    "0618037667",
    "9780345020208",
    "0261102958",
    "9780061952876",
    "9780618129027",
    "9788020409263",
    "0618129022"
   ],
   "has_fulltext": true,
   "text": [
    "OL10681058M",
    "OL10236416M",
    "OL21217116M",
    "OL22510662M",
    "OL9559516M",
    "OL7603320M",
    "OL6165495M",
    "OL13807949M",
    "OL13761262M",
    "OL17906645M",
    "OL4883007M",
    "OL5975400M",
    "OL22406853M",
    "OL17990125M",
    "OL16539692M",
    "OL23795326M",
    "OL22815379M",
    "OL5574175M",
    "OL5535578M",
    "OL4382055M",
    "OL21318055M",
    "OL20943851M",
    "OL16791443M",
    "OL21392110M",
    "OL22470927M",
    "OL5237526M",
    "OL10682337M",
    "OL23821472M",
    "OL20200626M",
    "OL22984886M",
    "OL17885449M",
    "OL22858420M",
    "OL20943862M",
    "OL20943868M",
    "OL17912024M",
    "OL1974942M",
    "OL22836449M",
    "OL1532643M",
    "OL21217131M",
    "OL25175074M",
    "OL26450492M",
    "OL22831274M",
    "OL21217165M",
    "OL22193052M",
    "OL10236393M",
    "OL22572775M",
    "OL21058613M",
    "OL19620537M",
    "OL3966044M",
    "OL8269996M",
    "OL9444589M",
    "OL7468970M",
    "OL26418460M",
    "OL7946403M",
    "OL22820202M",
    "OL9216449M",
    "OL7261734M",
    "OL3659520M",
    "OL9216964M",
    "OL7262249M",
    "OL22819486M",
    "OL3670214M",
    "OL3380031M",
    "OL22816363M",
    "OL3321902M",
    "OL3404981M",
    "OL24278639M",
    "OL24261347M",
    "8020409262",
    "9780618346240",
    "0618042210",
    "0618517650",
    "9780061917806",
    "9780618640157",
    "0261102389",
    "9780048230911",
    "0586218696",
    "9780395193952",
    "9780618042203",
    "0618260587",
    "039564738X",
    "0618260269",
    "0618640150",
    "0261102419",
    "061826051X",
    "1402505205",
    "0807286087",
    "9780261102347",
    "0048231495",
    "9780061917813",
    "9780618042258",
    "0618260285",
    "0007123817",
    "9780618042265",
    "0739408259",
    "9780345247865",
    "0395647398",
    "0618260595",
    "9780395647394",
    "0395647401",
    "9780586218693",
    "9780618260256",
    "9780618260553",
    "0898452236",
    "9780618042241",
    "0007172001",
    "9780807286081",
    "0061952877",
    "006191780X",
    "9781402505201",
    "9780395647387",
    "0007144083",
    "9780395974681",
    "0261102435",
    "9780618260249",
    "9780007149247",
    "0395595118",
    "9780048232007",
    "9780007144082",
    "9780618042234",
    "9780395595114",
    "3895840432",
    "0618042261",
    "9780261103566",
    "9780007635610",
    "9780618260270",
    "9780618645619",
    "0007149247",
    "9783895840432",
    "0048232009",
    "0618645616",
    "0618260250",
    "9780618260263",
    "0261103563",
    "9780898452235",
    "9780618042227",
    "004823091X",
    "9780618260584",
    "0618042253",
    "0395193958",
    "0007322593",
    "9788445070321",
    "9780261102958",
    "0061917818",
    "0618260242",
    "9780618346257",
    "0618260552",
    "9780007123810",
    "9780618042210",
    "9780618037667",
    "0618042245",
    "9780261102415",
    "0618346252",
    "0345020200",
    "9780618260515",
    "0261102346",
    "8445070320",
    "0618260277",
    "9780618517657",
    "0395974682",
    "0618042237",
    "0007635613",
    "9780048230874",
    "9780618260591",
    "0048230871",
    "9780618260287",
    "9780007322596",
    "9780007172009",
    "0618346244",
    "9780261102385",
    "9780739408254",
    "9780048231499",
    "0345247868",
    "9788422616337",
    "9780395647400",
    "8422616335",
    "0618042202",
    "0618042229",
    "9780261102439",
    "0618037667",
    "9780345020208",
    "0261102958",
    "9780061952876",
    "9780618129027",
    "9788020409263",
    "0618129022",
    "J. R. R. Tolkien",
    "Lee, Alan, 1947-",
    "Rob Inglis (Narrator, Reader)",
    "Grathmer, Ingahild (Illustrator)",
    "Fraser, Eric (Illustrator)",
    "Tolkien, J. R. R. 1892-1973.",
    "Lee, Alan.",
    "57241599",
    "237889032",
    "50854192",
    "781923736",
    "947127014",
    "52751474",
    "221689614",
    "31385942",
    "751515201",
    "919902149",
    "41049708",
    "1487587",
    "42949158",
    "48130922",
    "lordofrings00tolk_1",
    "lordofringstrilo00jrrt",
    "lordofrings00tolk_3",
    "lordofrings00tolk_2",
    "lordofringsonevo00jrrt",
    "isbn_9780618640157",
    "lordofrings00tolk_0",
    "OL26320A",
    "English Fantasy fiction",
    "In library",
    "Protected DAISY",
    "Gandalf (Fictitious character)",
    "Middle Earth (Imaginary place)",
    "Baggins, Frodo (Personaje literario)",
    "Accessible book",
    "Fiction in English",
    "Tierra Media (Lugar imaginario)",
    "Fiction",
    "Frodo Baggins",
    "Frodo Baggins (Fictitious character)",
    "Open Library Staff Picks",
    "Fantasy fiction",
    "Ficci\u00f3n fant\u00e1stica inglesa",
    "Ficci\u00f3n",
    "Textual Criticism",
    "Internet Archive Wishlist",
    "Trilogy Gift Set",
    "The two towers.",
    "The Two Towers and the Return of the King(Exerpts)",
    " The Ring Sets Out; The Ring Goes South; The Treason of Isengard; The Ring Goes East; The War of the Ring; The End of the Third Age; Appendices",
    "The Lord of the Rings",
    "/works/OL27448W",
    "by J. R. R. Tolkien. With a new foreword by the author.",
    "J.R.R. Tolkien ; traducci\u00f3n de Luis Dom\u0144ech.",
    "J.R.R. Tolkien ; illustrated by Alan Lee.",
    "complete with index and full appendices ; by J.R.R. Tolkien.",
    "J.R.R. Tolkien ; illustrations by Ingahild Grathmer ; drawn by Eric Fraser.",
    "by J.R.R. Tolkien; with a new foreword by the author.",
    "J.R.R. Tolkien ; illustrations by Ingahild Grathmer, drawn by Eric Fraser.",
    "J.R.R. Tolkien.",
    "by J.R.R. Tolkien.",
    "J. R. R. Tolkien ; illustrated by A. Lee..",
    "by J. R. R. Tolkien.",
    "J. R. R. Tolkien ; illustrated by A. Lee.",
    "by J. R. H. Tolkien ; illustrated by Alan Lee.",
    "J. R. R. Tolkien.",
    "Houghton Mifflin Co.",
    "Allenand Unwin",
    "Allen & Unwin",
    "Folio Society",
    "Collins",
    "Book Club Association",
    "George Allen and Unwin",
    "Mlad\u00e1 fronta",
    "Grafton",
    "HarperCollins Publishers Ltd",
    "Der H\u00f6rverlag",
    "Circulo de Lectores",
    "Houghton Mifflin",
    "Allen and Unwin",
    "Listening Library",
    "Ballantine Books",
    "Minotauro",
    "Guild",
    "Recorded Books",
    "Easton Press",
    "Unwin Paperbacks",
    "Unwin Hyman",
    "Caedmon",
    "Methuen",
    "HarperCollins",
    "Treason of Isengard.",
    "The lord of the rings",
    "Der Herr der Ringe",
    "The Lord of theRings.",
    "War of the ring.",
    "The lord of the rings.",
    "Lord of the rings.",
    "Return of the king.",
    "Two towers.",
    "The Hobbit & The Lord of the Rings",
    "The lord of the Rings.",
    "El Se\u00f1or de los Anillos",
    "Comunidad del anillo",
    "Retorno del rey",
    "P\u00e1n prsten\u016f: Spole\u010dentvo prstenu",
    "THE LORD OF THE RINGS",
    "The Lord of the Rings ",
    "The Lord of the rings.",
    "Dos torres",
    "The Lord of the Rings & The Hobbit",
    "End of the Third Age.",
    "The fellowship of the ring.",
    "The lord of the Rings",
    "The Lord of the rings",
    "Ring goes east.",
    "The Ring Sets Out",
    "The return of the king.",
    "Ring goes south.",
    "Lord of the Rings",
    "The Lord of the Rings.",
    "El se\u00f1or de los anillos",
    "Fellowship of the ring.",
    "The two towers.",
    "2005020460",
    "76012275",
    "75308399",
    "67084547",
    "90215588",
    "2001271127",
    "99026007",
    "54036398",
    "2004541379",
    "2002726623",
    "2004275215",
    "67012274",
    "2002524228",
    "66000953",
    "91010298",
    "78873439",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein",
    "Merry",
    "Sam",
    "Shelob",
    "Frodo",
    "Pippin",
    "Gandalf",
    "Aragorn",
    "Cracks of Doom",
    "Isengard",
    "Hornburg",
    "Fangorn Forest",
    "Mordor",
    "Middle-earth in the end of the third age"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "contributor": [
    "Lee, Alan, 1947-",
    "Rob Inglis (Narrator, Reader)",
    "Grathmer, Ingahild (Illustrator)",
    "Fraser, Eric (Illustrator)",
    "Tolkien, J. R. R. 1892-1973.",
    "Lee, Alan."
   ],
   "ia_loaded_id": [
    "lordofrings00tolk_4",
    "lordofrings00tolk_1",
    "lordofrings00tolk_0",
    "lordofrings00tolk_3"
   ],
   "seed": [
    "/books/OL10681058M",
    "/books/OL10236416M",
    "/books/OL21217116M",
    "/books/OL22510662M",
    "/books/OL9559516M",
    "/books/OL7603320M",
    "/books/OL6165495M",
    "/books/OL13807949M",
    "/books/OL13761262M",
    "/books/OL17906645M",
    "/books/OL4883007M",
    "/books/OL5975400M",
    "/books/OL22406853M",
    "/books/OL17990125M",
    "/books/OL16539692M",
    "/books/OL23795326M",
    "/books/OL22815379M",
    "/books/OL5574175M",
    "/books/OL5535578M",
    "/books/OL4382055M",
    "/books/OL21318055M",
    "/books/OL20943851M",
    "/books/OL16791443M",
    "/books/OL21392110M",
    "/books/OL22470927M",
    "/books/OL5237526M",
    "/books/OL10682337M",
    "/books/OL23821472M",
    "/books/OL20200626M",
    "/books/OL22984886M",
    "/books/OL17885449M",
    "/books/OL22858420M",
    "/books/OL20943862M",
    "/books/OL20943868M",
    "/books/OL17912024M",
    "/books/OL1974942M",
    "/books/OL22836449M",
    "/books/OL1532643M",
    "/books/OL21217131M",
    "/books/OL25175074M",
    "/books/OL26450492M",
    "/books/OL22831274M",
    "/books/OL21217165M",
    "/books/OL22193052M",
    "/books/OL10236393M",
    "/books/OL22572775M",
    "/books/OL21058613M",
    "/books/OL19620537M",
    "/books/OL3966044M",
    "/books/OL8269996M",
    "/books/OL9444589M",
    "/books/OL7468970M",
    "/books/OL26418460M",
    "/books/OL7946403M",
    "/books/OL22820202M",
    "/books/OL9216449M",
    "/books/OL7261734M",
    "/books/OL3659520M",
    "/books/OL9216964M",
    "/books/OL7262249M",
    "/books/OL22819486M",
    "/books/OL3670214M",
    "/books/OL3380031M",
    "/books/OL22816363M",
    "/books/OL3321902M",
    "/books/OL3404981M",
    "/books/OL24278639M",
    "/books/OL24261347M",
    "/works/OL27448W",
    "/subjects/fiction",
    "/subjects/ficci\u00f3n",
    "/subjects/english_fantasy_fiction",
    "/subjects/middle_earth_(imaginary_place)",
    "/subjects/baggins_frodo_(personaje_literario)",
    "/subjects/tierra_media_(lugar_imaginario)",
    "/subjects/frodo_baggins_(fictitious_character)",
    "/subjects/ficci\u00f3n_fant\u00e1stica_inglesa",
    "/subjects/in_library",
    "/subjects/gandalf_(fictitious_character)",
    "/subjects/fantasy_fiction",
    "/subjects/accessible_book",
    "/subjects/fiction_in_english",
    "/subjects/frodo_baggins",
    "/subjects/open_library_staff_picks",
    "/subjects/protected_daisy",
    "/subjects/textual_criticism",
    "/subjects/internet_archive_wishlist",
    "/subjects/person:aragorn",
    "/subjects/person:frodo",
    "/subjects/person:sam",
    "/subjects/person:pippin",
    "/subjects/person:merry",
    "/subjects/person:gandalf",
    "/subjects/person:shelob",
    "/subjects/place:mordor",
    "/subjects/place:hornburg",
    "/subjects/place:isengard",
    "/subjects/place:cracks_of_doom",
    "/subjects/place:fangorn_forest",
    "/subjects/time:middle-earth_in_the_end_of_the_third_age",
    "/authors/OL26320A"
   ],
   "oclc": [
    "57241599",
    "237889032",
    "50854192",
    "781923736",
    "947127014",
    "52751474",
    "221689614",
    "31385942",
    "751515201",
    "919902149",
    "41049708",
    "1487587",
    "42949158",
    "48130922"
   ],
   "id_google": [
    "WYeYQgAACAAJ"
   ],
   "ia": [
    "lordofrings00tolk_1",
    "lordofringstrilo00jrrt",
    "lordofrings00tolk_3",
    "lordofrings00tolk_2",
    "lordofringsonevo00jrrt",
    "isbn_9780618640157",
    "lordofrings00tolk_0"
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "English Fantasy fiction",
    "In library",
    "Protected DAISY",
    "Gandalf (Fictitious character)",
    "Middle Earth (Imaginary place)",
    "Baggins, Frodo (Personaje literario)",
    "Accessible book",
    "Fiction in English",
    "Tierra Media (Lugar imaginario)",
    "Fiction",
    "Frodo Baggins",
    "Frodo Baggins (Fictitious character)",
    "Open Library Staff Picks",
    "Fantasy fiction",
    "Ficci\u00f3n fant\u00e1stica inglesa",
    "Ficci\u00f3n",
    "Textual Criticism",
    "Internet Archive Wishlist"
   ],
   "title": "The Lord of the Rings",
   "lending_identifier_s": "lordofringstrilo00jrrt",
   "ia_collection_s": "printdisabled;americana;internetarchivebooks;delawarecountydistrictlibrary;inlibrary;bannedbooks;china;openlibraries",
   "first_publish_year": 1954,
   "type": "work",
   "ebook_count_i": 7,
   "publish_place": [
    "Toronto",
    "Norwalk, Conn",
    "Boston, Mass",
    "New York, USA",
    "Boston, MA",
    "Boston",
    "Barcelona",
    "New York",
    "London",
    "London (etc.)",
    "Glasgow",
    "Spain",
    "Boston, USA"
   ],
   "ia_box_id": [
    "IA177301",
    "IA129901",
    "IA104013",
    "IA1156820",
    "IA176701",
    "IA177101",
    "IA180001"
   ],
   "edition_count": 68,
   "key": "/works/OL27448W",
   "id_goodreads": [
    "998763",
    "70996",
    "984752",
    "899781",
    "31",
    "795109",
    "2527331",
    "516989",
    "516970",
    "15336",
    "33",
    "54707",
    "899773",
    "899771",
    "32",
    "877730",
    "34",
    "1153955",
    "877731",
    "1337450",
    "5899",
    "93937",
    "15407",
    "15404",
    "1233420",
    "215343",
    "1233422",
    "3007740",
    "2298536",
    "15367",
    "7349",
    "2068966",
    "273437",
    "222954",
    "11793075",
    "340381",
    "877732",
    "899800",
    "899801",
    "35",
    "360973",
    "825248",
    "623517",
    "529015",
    "569465",
    "837605",
    "6215547",
    "3094606",
    "215342",
    "733999",
    "827763",
    "15366"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "public_scan_b": false,
   "id_overdrive": [
    "417C4314-2354-4092-96A7-DB3C12598E8A",
    "2CCA69FD-FE09-4C2C-8C91-84D55F4AA425"
   ],
   "publisher": [
    "Houghton Mifflin Co.",
    "Allenand Unwin",
    "Allen & Unwin",
    "Folio Society",
    "Collins",
    "Book Club Association",
    "George Allen and Unwin",
    "Mlad\u00e1 fronta",
    "Grafton",
    "HarperCollins Publishers Ltd",
    "Der H\u00f6rverlag",
    "Circulo de Lectores",
    "Houghton Mifflin",
    "Allen and Unwin",
    "Listening Library",
    "Ballantine Books",
    "Minotauro",
    "Guild",
    "Recorded Books",
    "Easton Press",
    "Unwin Paperbacks",
    "Unwin Hyman",
    "Caedmon",
    "Methuen",
    "HarperCollins"
   ],
   "id_canadian_national_library_archive": [
    "20600075"
   ],
   "language": [
    "spa",
    "cze",
    "ger",
    "eng"
   ],
   "lccn": [
    "2005020460",
    "76012275",
    "75308399",
    "67084547",
    "90215588",
    "2001271127",
    "99026007",
    "54036398",
    "2004541379",
    "2002726623",
    "2004275215",
    "67012274",
    "2002524228",
    "66000953",
    "91010298",
    "78873439"
   ],
   "last_modified_i": 1530505798,
   "lending_edition_s": "OL1532643M",
   "id_librarything": [
    "1386651",
    "4881",
    "636553",
    "1471210",
    "3203347"
   ],
   "cover_edition_key": "OL1532643M",
   "person": [
    "Merry",
    "Sam",
    "Shelob",
    "Frodo",
    "Pippin",
    "Gandalf",
    "Aragorn"
   ],
   "publish_year": [
    1968,
    1969,
    1981,
    1965,
    1966,
    1967,
    1999,
    1954,
    1982,
    1991,
    1990,
    1993,
    1992,
    1994,
    1978,
    1977,
    1998,
    1975,
    1974,
    1973,
    2002,
    2003,
    2001,
    2004,
    2005,
    2009
   ],
   "printdisabled_s": "OL1532643M;OL21058613M;OL3966044M;OL24261347M;OL7468970M;OL3659520M;OL3404981M",
   "place": [
    "Cracks of Doom",
    "Isengard",
    "Hornburg",
    "Fangorn Forest",
    "Mordor"
   ],
   "time": [
    "Middle-earth in the end of the third age"
   ],
   "publish_date": [
    "1997 November 3",
    "February 2001",
    "2003",
    "2001 August",
    "1968",
    "1969",
    "1981",
    "1965",
    "1966",
    "1967",
    "1970 September",
    "January 5, 1998",
    "November 2, 1998",
    "October 7, 2002",
    "1954",
    "1982",
    "1991",
    "1990",
    "1993",
    "1992",
    "1994",
    "1978",
    "1977",
    "1975",
    "1974",
    "1973",
    "2002",
    "1999",
    "2001",
    "2004",
    "2005",
    "2009",
    "1999 October"
   ],
   "id_wikidata": [
    "Q22122681"
   ]
  },
  {
   "title_suggest": "Lord of the Rings",
   "edition_key": [
    "OL9409698M",
    "OL10957365M",
    "OL10957364M",
    "OL9314653M",
    "OL9701406M"
   ],
   "cover_i": 1454705,
   "isbn": [
    "0768325293",
    "9780768374698",
    "9780768325782",
    "9780768325249",
    "9780768325294",
    "0768325242",
    "0768325234",
    "0768374693",
    "0768325781",
    "9780768325232"
   ],
   "has_fulltext": false,
   "text": [
    "OL9409698M",
    "OL10957365M",
    "OL10957364M",
    "OL9314653M",
    "OL9701406M",
    "0768325293",
    "9780768374698",
    "9780768325782",
    "9780768325249",
    "9780768325294",
    "0768325242",
    "0768325234",
    "0768374693",
    "0768325781",
    "9780768325232",
    "Cedco Publishing",
    "OL2853379A",
    "Journal # 4 (Lord of the Rings)",
    "Trilogy Edition 2006 Calendar (Cedco Mini Daily)",
    "Journal # 3 (Lord of the Rings)",
    "Lord of the Rings",
    "/works/OL8527426W",
    "Cedco Publishing Company",
    "The Lord of the Rings"
   ],
   "author_name": [
    "Cedco Publishing"
   ],
   "seed": [
    "/books/OL9409698M",
    "/books/OL10957365M",
    "/books/OL10957364M",
    "/books/OL9314653M",
    "/books/OL9701406M",
    "/works/OL8527426W",
    "/authors/OL2853379A"
   ],
   "author_key": [
    "OL2853379A"
   ],
   "title": "Lord of the Rings",
   "publish_date": [
    "August 30, 2005",
    "September 2002",
    "October 2001"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 5,
   "key": "/works/OL8527426W",
   "id_goodreads": [
    "130022",
    "5984308",
    "59318"
   ],
   "publisher": [
    "Cedco Publishing Company"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1282021198,
   "id_librarything": [
    "4607237"
   ],
   "cover_edition_key": "OL9701406M",
   "publish_year": [
    2002,
    2001,
    2005
   ],
   "first_publish_year": 2001
  },
  {
   "title_suggest": "Lords of the Ring",
   "edition_key": [
    "OL10317216M",
    "OL10317217M"
   ],
   "cover_i": 2353908,
   "isbn": [
    "0299204243",
    "9780299204242",
    "0299204200",
    "9780299204204"
   ],
   "has_fulltext": false,
   "text": [
    "OL10317216M",
    "OL10317217M",
    "0299204243",
    "9780299204242",
    "0299204200",
    "9780299204204",
    "Doug Moe",
    "54677827",
    "149469555",
    "OL317745A",
    "The Triumph and Tragedy of College Boxing's Greatest Team",
    "Lords of the Ring",
    "/works/OL2347684W",
    "University of Wisconsin Press"
   ],
   "author_name": [
    "Doug Moe"
   ],
   "seed": [
    "/books/OL10317216M",
    "/books/OL10317217M",
    "/works/OL2347684W",
    "/authors/OL317745A"
   ],
   "oclc": [
    "54677827",
    "149469555"
   ],
   "author_key": [
    "OL317745A"
   ],
   "title": "Lords of the Ring",
   "publish_date": [
    "September 14, 2005",
    "September 22, 2004"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL2347684W",
   "id_goodreads": [
    "442134",
    "883933"
   ],
   "publisher": [
    "University of Wisconsin Press"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1303896881,
   "id_librarything": [
    "4719431"
   ],
   "cover_edition_key": "OL10317217M",
   "publish_year": [
    2004,
    2005
   ],
   "first_publish_year": 2004
  },
  {
   "title_suggest": "Lord of the Rings",
   "edition_key": [
    "OL8773280M",
    "OL8773281M"
   ],
   "cover_i": 2111453,
   "isbn": [
    "1904764827",
    "1904764835",
    "9781904764823",
    "9781904764830"
   ],
   "has_fulltext": false,
   "text": [
    "OL8773280M",
    "OL8773281M",
    "1904764827",
    "1904764835",
    "9781904764823",
    "9781904764830",
    "Ernest Mathijs",
    "OL3091153A",
    "Popular Culture in Global Context",
    "Lord of the Rings",
    "/works/OL8937755W",
    "Wallflower Press"
   ],
   "author_name": [
    "Ernest Mathijs"
   ],
   "seed": [
    "/books/OL8773280M",
    "/books/OL8773281M",
    "/works/OL8937755W",
    "/authors/OL3091153A"
   ],
   "author_key": [
    "OL3091153A"
   ],
   "title": "Lord of the Rings",
   "publish_date": [
    "November 1, 2006"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL8937755W",
   "id_goodreads": [
    "222930",
    "1982337"
   ],
   "publisher": [
    "Wallflower Press"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1281432559,
   "id_librarything": [
    "3706961"
   ],
   "cover_edition_key": "OL8773280M",
   "publish_year": [
    2006
   ],
   "first_publish_year": 2006
  },
  {
   "title_suggest": "Lord of the rings",
   "publisher": [
    "Entertainment in video"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL16169368M"
   ],
   "last_modified_i": 1419577714,
   "title": "Lord of the rings",
   "seed": [
    "/books/OL16169368M",
    "/works/OL16169368M"
   ],
   "key": "/works/OL16169368M",
   "text": [
    "OL16169368M",
    "Return of the king.",
    "Lord of the rings",
    "/works/OL16169368M",
    "Entertainment in video"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lords of the Ring",
   "publisher": [
    "Pulse"
   ],
   "isbn": [
    "092101404X",
    "9780921014041"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL11445939M"
   ],
   "last_modified_i": 1419577496,
   "title": "Lords of the Ring",
   "id_librarything": [
    "5808468"
   ],
   "seed": [
    "/books/OL11445939M",
    "/works/OL11445939M"
   ],
   "first_publish_year": 1987,
   "publish_year": [
    1987
   ],
   "key": "/works/OL11445939M",
   "text": [
    "OL11445939M",
    "092101404X",
    "9780921014041",
    "Wrestling Stars",
    "Lords of the Ring",
    "/works/OL11445939M",
    "Pulse"
   ],
   "publish_date": [
    "1987"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lords of the Ring",
   "publisher": [
    "Hamlyn"
   ],
   "cover_i": 2539329,
   "isbn": [
    "060059520X",
    "9780600595205"
   ],
   "has_fulltext": false,
   "title": "Lords of the Ring",
   "edition_key": [
    "OL10918978M"
   ],
   "last_modified_i": 1272446784,
   "edition_count": 1,
   "author_name": [
    "Peter Arnold"
   ],
   "cover_edition_key": "OL10918978M",
   "seed": [
    "/books/OL10918978M",
    "/works/OL7284693W",
    "/authors/OL2133665A"
   ],
   "first_publish_year": 1998,
   "publish_year": [
    1998
   ],
   "key": "/works/OL7284693W",
   "text": [
    "OL10918978M",
    "060059520X",
    "9780600595205",
    "Peter Arnold",
    "OL2133665A",
    "The Greatest Fighters Since 1950",
    "Lords of the Ring",
    "/works/OL7284693W",
    "Hamlyn"
   ],
   "id_goodreads": [
    "883932"
   ],
   "publish_date": [
    "August 15, 1998"
   ],
   "author_key": [
    "OL2133665A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Rings",
   "edition_key": [
    "OL12367160M"
   ],
   "isbn": [
    "9781589940512",
    "1589940512"
   ],
   "has_fulltext": false,
   "text": [
    "OL12367160M",
    "9781589940512",
    "1589940512",
    "Reiner Knizia",
    "John Howe (Illustrator)",
    "OL2788774A",
    "Lord of the Rings",
    "/works/OL8372037W",
    "Fantasy Flight Games"
   ],
   "author_name": [
    "Reiner Knizia"
   ],
   "seed": [
    "/books/OL12367160M",
    "/works/OL8372037W",
    "/authors/OL2788774A"
   ],
   "contributor": [
    "John Howe (Illustrator)"
   ],
   "author_key": [
    "OL2788774A"
   ],
   "title": "Lord of the Rings",
   "publish_date": [
    "September 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL8372037W",
   "id_goodreads": [
    "15270"
   ],
   "publisher": [
    "Fantasy Flight Games"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1282048082,
   "id_librarything": [
    "7158386"
   ],
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003
  },
  {
   "title_suggest": "Lords of the ring",
   "edition_key": [
    "OL21409258M"
   ],
   "isbn": [
    "043473876X",
    "9780434738762"
   ],
   "has_fulltext": false,
   "text": [
    "OL21409258M",
    "043473876X",
    "9780434738762",
    "Harry Lansdown",
    "Spillius, Alex.",
    "24743033",
    "OL3399247A",
    "Marsh, Warren and the business of boxing",
    "Lords of the ring",
    "Harry Lansdown & Alex Spillius.",
    "/works/OL9356256W",
    "William Heinemann",
    "Frank Warren (1952-)",
    "Terry Marsh (1958-)"
   ],
   "author_name": [
    "Harry Lansdown"
   ],
   "seed": [
    "/books/OL21409258M",
    "/works/OL9356256W",
    "/subjects/person:frank_warren_(1952-)",
    "/subjects/person:terry_marsh_(1958-)",
    "/authors/OL3399247A"
   ],
   "oclc": [
    "24743033"
   ],
   "contributor": [
    "Spillius, Alex."
   ],
   "author_key": [
    "OL3399247A"
   ],
   "title": "Lords of the ring",
   "publish_date": [
    "1991"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "London"
   ],
   "edition_count": 1,
   "key": "/works/OL9356256W",
   "id_goodreads": [
    "883931"
   ],
   "publisher": [
    "William Heinemann"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1307533716,
   "person": [
    "Frank Warren (1952-)",
    "Terry Marsh (1958-)"
   ],
   "publish_year": [
    1991
   ],
   "first_publish_year": 1991
  },
  {
   "title_suggest": "Lord of the Rings",
   "publisher": [
    "Unwin Books"
   ],
   "isbn": [
    "0048231126",
    "9780048231123"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "edition_key": [
    "OL9228705M"
   ],
   "last_modified_i": 1419576537,
   "title": "Lord of the Rings",
   "id_librarything": [
    "3203347"
   ],
   "seed": [
    "/books/OL9228705M",
    "/works/OL9228705M"
   ],
   "first_publish_year": 1974,
   "publish_year": [
    1974
   ],
   "key": "/works/OL9228705M",
   "text": [
    "OL9228705M",
    "0048231126",
    "9780048231123",
    "The Fellowship of the Ring, The Two Towers, The Return of the King",
    "Lord of the Rings",
    "/works/OL9228705M",
    "Unwin Books"
   ],
   "id_goodreads": [
    "1451516"
   ],
   "publish_date": [
    "1974"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lords of the ring",
   "publisher": [
    "Cassell Australia"
   ],
   "isbn": [
    "9780726913952",
    "0726913952"
   ],
   "has_fulltext": false,
   "id_librarything": [
    "1180072"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL7866471M"
   ],
   "last_modified_i": 1281081785,
   "title": "Lords of the ring",
   "author_name": [
    "Peter Corris"
   ],
   "seed": [
    "/books/OL7866471M",
    "/works/OL1698390W",
    "/authors/OL193277A"
   ],
   "first_publish_year": 1980,
   "publish_year": [
    1980
   ],
   "key": "/works/OL1698390W",
   "text": [
    "OL7866471M",
    "9780726913952",
    "0726913952",
    "Peter Corris",
    "OL193277A",
    "Lords of the ring",
    "/works/OL1698390W",
    "Cassell Australia"
   ],
   "id_goodreads": [
    "3235512"
   ],
   "publish_date": [
    "1980"
   ],
   "author_key": [
    "OL193277A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the rings",
   "edition_key": [
    "OL22643577M"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "last_modified_i": 1260863666,
   "title": "Lord of the rings",
   "author_name": [
    "Jim Pendrill"
   ],
   "seed": [
    "/books/OL22643577M",
    "/works/OL12413029W",
    "/authors/OL5470710A"
   ],
   "key": "/works/OL12413029W",
   "text": [
    "OL22643577M",
    "Jim Pendrill",
    "OL5470710A",
    "Lord of the rings",
    "/works/OL12413029W",
    "Lord of the rings."
   ],
   "author_key": [
    "OL5470710A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the rings",
   "publisher": [
    "CHARISMA [CAS1059."
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL21964564M"
   ],
   "last_modified_i": 1260862632,
   "title": "Lord of the rings",
   "author_name": [
    "Bo Hansson"
   ],
   "seed": [
    "/books/OL21964564M",
    "/works/OL13508175W",
    "/authors/OL6376891A"
   ],
   "key": "/works/OL13508175W",
   "text": [
    "OL21964564M",
    "Bo Hansson",
    "OL6376891A",
    "Lord of the rings",
    "/works/OL13508175W",
    "CHARISMA [CAS1059."
   ],
   "author_key": [
    "OL6376891A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of Rings",
   "edition_key": [
    "OL10681579M"
   ],
   "isbn": [
    "0345214528",
    "9780345214522"
   ],
   "has_fulltext": false,
   "text": [
    "OL10681579M",
    "0345214528",
    "9780345214522",
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of Rings",
    "/works/OL14926051W",
    "Ballantine Books",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL10681579M",
    "/works/OL14926051W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of Rings",
   "publish_date": [
    "September 12, 1972"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL14926051W",
   "id_goodreads": [
    "877754"
   ],
   "publisher": [
    "Ballantine Books"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1282016354,
   "id_librarything": [
    "1386651"
   ],
   "publish_year": [
    1972
   ],
   "first_publish_year": 1972
  },
  {
   "title_suggest": "Lord of the rings",
   "edition_key": [
    "OL23126486M"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "last_modified_i": 1260865359,
   "title": "Lord of the rings",
   "author_name": [
    "jude Fisher"
   ],
   "seed": [
    "/books/OL23126486M",
    "/works/OL13754671W",
    "/authors/OL6595630A"
   ],
   "key": "/works/OL13754671W",
   "text": [
    "OL23126486M",
    "jude Fisher",
    "OL6595630A",
    "Lord of the rings",
    "/works/OL13754671W"
   ],
   "author_key": [
    "OL6595630A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the rings",
   "edition_key": [
    "OL2242338M"
   ],
   "has_fulltext": false,
   "text": [
    "OL2242338M",
    "Susan Rosenkranz",
    "Gebel-Williams, Gunther, 1934-",
    "OL1019020A",
    "Gunther Gebel-Williams",
    "Lord of the rings",
    "introduction by Kenneth Feld.",
    "Animal trainers",
    "Gebel-Williams, Gunther, 1934-",
    "Biography",
    "Gebel-Williams, Gunther,",
    "/works/OL4825661W",
    "Ringling Bros. and Barnum & Bailey Combined Shows",
    "Gunther Gebel-Williams.",
    "89114713",
    "United States"
   ],
   "author_name": [
    "Susan Rosenkranz"
   ],
   "seed": [
    "/books/OL2242338M",
    "/works/OL4825661W",
    "/subjects/animal_trainers",
    "/subjects/biography",
    "/subjects/gebel-williams_gunther",
    "/subjects/gebel-williams_gunther_1934-",
    "/subjects/place:united_states",
    "/authors/OL1019020A"
   ],
   "contributor": [
    "Gebel-Williams, Gunther, 1934-"
   ],
   "author_key": [
    "OL1019020A"
   ],
   "subject": [
    "Animal trainers",
    "Gebel-Williams, Gunther, 1934-",
    "Biography",
    "Gebel-Williams, Gunther,"
   ],
   "title": "Lord of the rings",
   "first_publish_year": 1988,
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "[Washington, D.C.] (3201 New Mexico Ave., N.W., Washington 20016)"
   ],
   "edition_count": 1,
   "key": "/works/OL4825661W",
   "publisher": [
    "Ringling Bros. and Barnum & Bailey Combined Shows"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "89114713"
   ],
   "last_modified_i": 1291483783,
   "publish_year": [
    1988
   ],
   "place": [
    "United States"
   ],
   "publish_date": [
    "1988"
   ]
  },
  {
   "title_suggest": "Lord of the Rings",
   "edition_key": [
    "OL9729713M"
   ],
   "cover_i": 1972472,
   "isbn": [
    "1590921372",
    "9781590921371"
   ],
   "has_fulltext": false,
   "text": [
    "OL9729713M",
    "1590921372",
    "9781590921371",
    "Betsy Gallup",
    "Cris DiMarco (Editor)",
    "OL3317161A",
    "The Best Websites",
    "Lord of the Rings",
    "/works/OL9262013W",
    "Lightning Rod, a Division of Windstorm Creative",
    "Read an assortment of alternative versions of Lord of the Rings (LOTR) written by George Lucas, Rudyard Kipling, and Meatloaf."
   ],
   "author_name": [
    "Betsy Gallup"
   ],
   "seed": [
    "/books/OL9729713M",
    "/works/OL9262013W",
    "/authors/OL3317161A"
   ],
   "contributor": [
    "Cris DiMarco (Editor)"
   ],
   "author_key": [
    "OL3317161A"
   ],
   "title": "Lord of the Rings",
   "publish_date": [
    "March 1, 2006"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL9262013W",
   "id_goodreads": [
    "15302"
   ],
   "publisher": [
    "Lightning Rod, a Division of Windstorm Creative"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1272448863,
   "cover_edition_key": "OL9729713M",
   "first_sentence": [
    "Read an assortment of alternative versions of Lord of the Rings (LOTR) written by George Lucas, Rudyard Kipling, and Meatloaf."
   ],
   "publish_year": [
    2006
   ],
   "first_publish_year": 2006
  },
  {
   "title_suggest": "Lord of the Rings",
   "publisher": [
    "MSI MUSIC"
   ],
   "isbn": [
    "6307245999",
    "9786307245993"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "edition_key": [
    "OL12789685M"
   ],
   "last_modified_i": 1339970513,
   "title": "Lord of the Rings",
   "author_alternative_name": [
    "Various Artists-Chil Cdmflp         73963",
    "Various Artists-Arno Cdmflp         78252",
    "Various Artists      Cdumme          1903",
    "Various Artists-Hall Cdpetr          9683",
    "Various Artists-Jewi Cdkhi         Put182",
    "Various Artists-Chil Cdmflp         73765",
    "Various Artists-Chri Cdsyw          86675",
    "Various Artists-Chri Cdsyw          86671",
    "Various Artists-Chil Csmflp         79842",
    "Various Artists-Rock Cdcolm         30283",
    "Various Artists-Duff Cd500        8607917",
    "Various Artists-Hall Cdpetr          9686",
    "Various Artists-Chil Csmflp         73766",
    "Various Artists-Chil Csmflp         73765",
    "Various Artists-Duff Cd500        8607912",
    "Various Artists-Clas Cdlase         14059",
    "Various Artists-Foxy Csktel          6973",
    "Various Artists-Foxy Csktel          6972",
    "Various Artists-Cold Cdatl          83588",
    "Various Artists-Midl Cd500        8607227",
    "Various Artists-Clas Cdlase         14054",
    "Various Artists-Nyro Cdcolm         30271",
    "Various Artists-Mexi Cd176        1600662",
    "Various artists-Printed in Malaysia- no publication date",
    "Various Artists-Subs Cdorh     6991071012",
    "Cdcolm         30274 Various Artists-Day",
    "Various artists.",
    "Various Artists-Chil Cdmada          2168",
    "Various Artists-Mila Cd500        8600972",
    "Various Artists-Radi Cdrdos         27602",
    "Various Artists-Chri Cdstce          3538",
    "Various Artists-Jazz Cdcolm         61439",
    "Various Artists-Chil Cdmflp         78223",
    "Various Artists-Pop  Cdefa           4404",
    "Various Artists-Gap  Csmflp         76087",
    "Various Artists-Chri Cd8627         40700",
    "Various Artists-East Cdagro     Crg140122",
    "Various Artists-Spok Cdmsim        203449",
    "Various Artists-Chil Cdmada          2195",
    "Various Artists-Chil Cdmada          2194",
    "Various Artists-Pop  Cd500        8600707",
    "Various Artists-Chil Cdmada          6058",
    "Various Artists-Chil Cdmflp         74339",
    "Various Artists-Dail Cd500        8607747",
    "Various Artists-Clas Cdteld         24802",
    "Various Artists-Brow Cdrhin         76703",
    "Various Artists-The  Cdorh     6991019332",
    "Various Artists-Chil Cdmflp         73964",
    "Various Artists-Garl Cdrhin         78323",
    "Various Artists-With Cdrhin         78262",
    "Various Artists-Dani Cdmflp         74341",
    "Various Artists-Gilb Cdnara        10366C",
    "Various Artists-Chil Csmflp         78223",
    "Various Artists-Chri Cddelt         46171",
    "Various Artists-Chri Csmada          4496",
    "Various Artists-TV s Cdrhin         74337",
    "Various Artists-Chil Cdmflp         78362",
    "Various Artists-Clas Cdpolc        010120",
    "Various Artists-Come Cdcolm         30192",
    "Various Artists-Hall Cdpetr          9688",
    "Various Artists-Jazz Cdcolm         30160",
    "Various Artists-Hall Cdpetr          9685",
    "Various Artists-Hall Cdpetr          9684",
    "Various Artists-Hall Cdpetr          9687",
    "Various Artists-Blue Cd500        8600837",
    "Various Artists.",
    "Various Artists-Hook Cdcolm         31134",
    "Various Artists-Chil Cd500        8607767",
    "Various Artists-Dust Cdsyw          63517",
    "Various Artists-Chil Cd500        8607762",
    "Various Artists-Lenn Cdmflp         78932",
    "Various Artists-Chil Cdmflp         75729",
    "Various Artists-Moro Cdstru           122",
    "Various Artists-Chri Cdmflp         75539",
    "Various Artists-Gap  Cdmflp         76087",
    "Various Artists-Hall Cdpetr          9690",
    "Various Artists-Hall Cdpetr          9691",
    "Various Artists-Worl Cdagro      Bud82264",
    "Various Artists-Chil Cdmada          6095",
    "Various Artists-Chil Cdmada          6096",
    "Various Artists-D'Le Cd500        8600937",
    "Various Artists-Wilc Cdrhin         78279",
    "Various Artists-Wyno Cd500        8607342",
    "Various Artists-Wyno Cd500        8607347",
    "Various Artists-Chri Cdmada          0698",
    "Various Artists-Chri Cdmada          0696",
    "Various Artists-Chri Cdmada          0697",
    "Various Artists-Chri Cdmada          0691",
    "Various Artists-Chri Cdmada          0692",
    "Various Artists-Chri Cdmada          0693",
    "Various Artists-Chil Cdmada          8240",
    "Various Artists-Gaye Cdrhin         78261",
    "Various Artists-Chri Cdbt           30072",
    "Various Artists-Chil Cdmflp         74260",
    "Various Artists-Chil Cdmflp         74261",
    "Various Artists-Chil Cdmflp         73936",
    "Various Artists-Chil Csmflp         74261",
    "Various Artists-Chri Cdmada          4499"
   ],
   "publish_year": [
    2002
   ],
   "seed": [
    "/books/OL12789685M",
    "/works/OL10069759W",
    "/authors/OL2659937A"
   ],
   "first_publish_year": 2002,
   "author_name": [
    "Various Artists"
   ],
   "key": "/works/OL10069759W",
   "text": [
    "OL12789685M",
    "6307245999",
    "9786307245993",
    "Various Artists",
    "OL2659937A",
    "Lord of the Rings",
    "/works/OL10069759W",
    "MSI MUSIC",
    "Various Artists-Chil Cdmflp         73963",
    "Various Artists-Arno Cdmflp         78252",
    "Various Artists      Cdumme          1903",
    "Various Artists-Hall Cdpetr          9683",
    "Various Artists-Jewi Cdkhi         Put182",
    "Various Artists-Chil Cdmflp         73765",
    "Various Artists-Chri Cdsyw          86675",
    "Various Artists-Chri Cdsyw          86671",
    "Various Artists-Chil Csmflp         79842",
    "Various Artists-Rock Cdcolm         30283",
    "Various Artists-Duff Cd500        8607917",
    "Various Artists-Hall Cdpetr          9686",
    "Various Artists-Chil Csmflp         73766",
    "Various Artists-Chil Csmflp         73765",
    "Various Artists-Duff Cd500        8607912",
    "Various Artists-Clas Cdlase         14059",
    "Various Artists-Foxy Csktel          6973",
    "Various Artists-Foxy Csktel          6972",
    "Various Artists-Cold Cdatl          83588",
    "Various Artists-Midl Cd500        8607227",
    "Various Artists-Clas Cdlase         14054",
    "Various Artists-Nyro Cdcolm         30271",
    "Various Artists-Mexi Cd176        1600662",
    "Various artists-Printed in Malaysia- no publication date",
    "Various Artists-Subs Cdorh     6991071012",
    "Cdcolm         30274 Various Artists-Day",
    "Various artists.",
    "Various Artists-Chil Cdmada          2168",
    "Various Artists-Mila Cd500        8600972",
    "Various Artists-Radi Cdrdos         27602",
    "Various Artists-Chri Cdstce          3538",
    "Various Artists-Jazz Cdcolm         61439",
    "Various Artists-Chil Cdmflp         78223",
    "Various Artists-Pop  Cdefa           4404",
    "Various Artists-Gap  Csmflp         76087",
    "Various Artists-Chri Cd8627         40700",
    "Various Artists-East Cdagro     Crg140122",
    "Various Artists-Spok Cdmsim        203449",
    "Various Artists-Chil Cdmada          2195",
    "Various Artists-Chil Cdmada          2194",
    "Various Artists-Pop  Cd500        8600707",
    "Various Artists-Chil Cdmada          6058",
    "Various Artists-Chil Cdmflp         74339",
    "Various Artists-Dail Cd500        8607747",
    "Various Artists-Clas Cdteld         24802",
    "Various Artists-Brow Cdrhin         76703",
    "Various Artists-The  Cdorh     6991019332",
    "Various Artists-Chil Cdmflp         73964",
    "Various Artists-Garl Cdrhin         78323",
    "Various Artists-With Cdrhin         78262",
    "Various Artists-Dani Cdmflp         74341",
    "Various Artists-Gilb Cdnara        10366C",
    "Various Artists-Chil Csmflp         78223",
    "Various Artists-Chri Cddelt         46171",
    "Various Artists-Chri Csmada          4496",
    "Various Artists-TV s Cdrhin         74337",
    "Various Artists-Chil Cdmflp         78362",
    "Various Artists-Clas Cdpolc        010120",
    "Various Artists-Come Cdcolm         30192",
    "Various Artists-Hall Cdpetr          9688",
    "Various Artists-Jazz Cdcolm         30160",
    "Various Artists-Hall Cdpetr          9685",
    "Various Artists-Hall Cdpetr          9684",
    "Various Artists-Hall Cdpetr          9687",
    "Various Artists-Blue Cd500        8600837",
    "Various Artists.",
    "Various Artists-Hook Cdcolm         31134",
    "Various Artists-Chil Cd500        8607767",
    "Various Artists-Dust Cdsyw          63517",
    "Various Artists-Chil Cd500        8607762",
    "Various Artists-Lenn Cdmflp         78932",
    "Various Artists-Chil Cdmflp         75729",
    "Various Artists-Moro Cdstru           122",
    "Various Artists-Chri Cdmflp         75539",
    "Various Artists-Gap  Cdmflp         76087",
    "Various Artists-Hall Cdpetr          9690",
    "Various Artists-Hall Cdpetr          9691",
    "Various Artists-Worl Cdagro      Bud82264",
    "Various Artists-Chil Cdmada          6095",
    "Various Artists-Chil Cdmada          6096",
    "Various Artists-D'Le Cd500        8600937",
    "Various Artists-Wilc Cdrhin         78279",
    "Various Artists-Wyno Cd500        8607342",
    "Various Artists-Wyno Cd500        8607347",
    "Various Artists-Chri Cdmada          0698",
    "Various Artists-Chri Cdmada          0696",
    "Various Artists-Chri Cdmada          0697",
    "Various Artists-Chri Cdmada          0691",
    "Various Artists-Chri Cdmada          0692",
    "Various Artists-Chri Cdmada          0693",
    "Various Artists-Chil Cdmada          8240",
    "Various Artists-Gaye Cdrhin         78261",
    "Various Artists-Chri Cdbt           30072",
    "Various Artists-Chil Cdmflp         74260",
    "Various Artists-Chil Cdmflp         74261",
    "Various Artists-Chil Cdmflp         73936",
    "Various Artists-Chil Csmflp         74261",
    "Various Artists-Chri Cdmada          4499"
   ],
   "id_goodreads": [
    "2688616"
   ],
   "publish_date": [
    "October 31, 2002"
   ],
   "author_key": [
    "OL2659937A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Rings",
   "publisher": [
    "Center for Learning"
   ],
   "edition_key": [
    "OL12120485M"
   ],
   "isbn": [
    "1560771372",
    "9781560771371"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "oclc": [
    "40279463"
   ],
   "last_modified_i": 1339477394,
   "title": "Lord of the Rings",
   "author_name": [
    "Carla Fritsch"
   ],
   "seed": [
    "/books/OL12120485M",
    "/works/OL9838681W",
    "/authors/OL3822898A"
   ],
   "first_publish_year": 2004,
   "publish_year": [
    2004
   ],
   "key": "/works/OL9838681W",
   "text": [
    "OL12120485M",
    "1560771372",
    "9781560771371",
    "Carla Fritsch",
    "40279463",
    "OL3822898A",
    "Lord of the Rings",
    "/works/OL9838681W",
    "Center for Learning"
   ],
   "id_goodreads": [
    "275085"
   ],
   "publish_date": [
    "February 28, 2004"
   ],
   "author_key": [
    "OL3822898A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Rings",
   "publisher": [
    "Scribd.com"
   ],
   "subtitle": "Apocalyptic Prophecies",
   "has_fulltext": false,
   "title": "Lord of the Rings",
   "edition_key": [
    "OL25646462M"
   ],
   "last_modified_i": 1487344641,
   "edition_count": 1,
   "author_name": [
    "E.A. Bucchianeri"
   ],
   "cover_edition_key": "OL25646462M",
   "seed": [
    "/books/OL25646462M",
    "/works/OL17076676W",
    "/authors/OL1480405A"
   ],
   "first_publish_year": 2014,
   "publish_year": [
    2014
   ],
   "key": "/works/OL17076676W",
   "text": [
    "OL25646462M",
    "Apocalyptic Prophecies",
    "E.A. Bucchianeri",
    "OL1480405A",
    "Lord of the Rings",
    "/works/OL17076676W",
    "Scribd.com",
    "Lord of the Rings: Apocalyptic Prophecies"
   ],
   "publish_date": [
    "December 8, 2014"
   ],
   "author_key": [
    "OL1480405A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Rings",
   "edition_key": [
    "OL1126026M"
   ],
   "subtitle": "official game secrets",
   "has_fulltext": false,
   "text": [
    "OL1126026M",
    "official game secrets",
    "Steven A. Schwartz",
    "32348637",
    "1559586753",
    "9781559586757",
    "OL407564A",
    "Lord of the Rings (Game)",
    "Lord of the Rings",
    "/works/OL2769862W",
    "Steve Schwartz.",
    "Prima Pub.",
    "94068401",
    "Steve Schwartz",
    "Steven Schwartz"
   ],
   "author_name": [
    "Steven A. Schwartz"
   ],
   "seed": [
    "/books/OL1126026M",
    "/works/OL2769862W",
    "/subjects/lord_of_the_rings_(game)",
    "/authors/OL407564A"
   ],
   "oclc": [
    "32348637"
   ],
   "isbn": [
    "1559586753",
    "9781559586757"
   ],
   "author_key": [
    "OL407564A"
   ],
   "subject": [
    "Lord of the Rings (Game)"
   ],
   "title": "Lord of the Rings",
   "publish_date": [
    "1995"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Rocklin, CA"
   ],
   "edition_count": 1,
   "key": "/works/OL2769862W",
   "id_goodreads": [
    "2640694"
   ],
   "publisher": [
    "Prima Pub."
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "94068401"
   ],
   "last_modified_i": 1303960628,
   "author_alternative_name": [
    "Steve Schwartz",
    "Steven Schwartz"
   ],
   "publish_year": [
    1995
   ],
   "first_publish_year": 1995
  },
  {
   "title_suggest": "Lord of the Rings",
   "edition_key": [
    "OL1126026M"
   ],
   "cover_i": 8166951,
   "subtitle": "Official Game Secrets",
   "has_fulltext": false,
   "text": [
    "OL1126026M",
    "Official Game Secrets",
    "Steven A. Schwartz",
    "32348637",
    "1559586753",
    "9781559586757",
    "OL407564A",
    "Lord of the Rings (Game)",
    "official game secrets",
    "Lord of the Rings",
    "/works/OL17863022W",
    "Steve Schwartz.",
    "Prima Pub.",
    "94068401",
    "Steve Schwartz",
    "Steven Schwartz"
   ],
   "author_name": [
    "Steven A. Schwartz"
   ],
   "seed": [
    "/books/OL1126026M",
    "/works/OL17863022W",
    "/subjects/lord_of_the_rings_(game)",
    "/authors/OL407564A"
   ],
   "oclc": [
    "32348637"
   ],
   "isbn": [
    "1559586753",
    "9781559586757"
   ],
   "author_key": [
    "OL407564A"
   ],
   "subject": [
    "Lord of the Rings (Game)"
   ],
   "title": "Lord of the Rings",
   "publish_date": [
    "1995"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Rocklin, CA"
   ],
   "edition_count": 1,
   "key": "/works/OL17863022W",
   "id_goodreads": [
    "2640694"
   ],
   "publisher": [
    "Prima Pub."
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "94068401"
   ],
   "last_modified_i": 1525185911,
   "author_alternative_name": [
    "Steve Schwartz",
    "Steven Schwartz"
   ],
   "publish_year": [
    1995
   ],
   "first_publish_year": 1995
  },
  {
   "title_suggest": "Lord of the Rings",
   "publisher": [
    "Unwin Books"
   ],
   "isbn": [
    "0048231126",
    "9780048231123"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "edition_key": [
    "OL7273996M"
   ],
   "last_modified_i": 1526377682,
   "title": "Lord of the Rings",
   "id_librarything": [
    "3203347"
   ],
   "cover_edition_key": "OL7273996M",
   "seed": [
    "/books/OL7273996M",
    "/works/OL7273996M"
   ],
   "first_publish_year": 1974,
   "publish_year": [
    1974
   ],
   "key": "/works/OL7273996M",
   "text": [
    "OL7273996M",
    "0048231126",
    "9780048231123",
    "The Fellowship of the Ring, The Two Towers, The Return of the King",
    "Lord of the Rings",
    "/works/OL7273996M",
    "Unwin Books"
   ],
   "id_goodreads": [
    "1451516"
   ],
   "publish_date": [
    "1974"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL25418754M",
    "OL25418753M",
    "OL15280670M",
    "OL9076613M",
    "OL9076577M",
    "OL22054291M",
    "OL23097541M",
    "OL9076578M",
    "OL12823904M"
   ],
   "isbn": [
    "3608936394",
    "3608933522",
    "9783608958553",
    "3608955364",
    "3608933514",
    "360895855X",
    "9783608936391",
    "9783608935448",
    "9783608955361",
    "9783608933529",
    "3608935444",
    "9783608933512"
   ],
   "has_fulltext": false,
   "text": [
    "OL25418754M",
    "OL25418753M",
    "OL15280670M",
    "OL9076613M",
    "OL9076577M",
    "OL22054291M",
    "OL23097541M",
    "OL9076578M",
    "OL12823904M",
    "3608936394",
    "3608933522",
    "9783608958553",
    "3608955364",
    "3608933514",
    "360895855X",
    "9783608936391",
    "9783608935448",
    "9783608955361",
    "9783608933529",
    "3608935444",
    "9783608933512",
    "J. R. R. Tolkien",
    "Carroux, Margaret.",
    "43202270",
    "OL26320A",
    "English Fantasy fiction",
    "Translations into German",
    "German Fantasy fiction",
    "Translations from English",
    "Die Gefahrten",
    "Die Zwei T\u00fcrme",
    "The Lord of the Rings",
    "/works/OL16245393W",
    "J.R.R. Tolkien ; [aus dem Englischen \u00fcbersetzt von Margaret Carroux].",
    "Collins",
    "Hobbit Presse",
    "Klett-Cotte",
    "J.G. Cotta'sche, Buchhandlung Nachfolger GmbH",
    "Klett-Cotta",
    "Der Herr der Ringe.",
    "Der Herr der Ringe",
    "The Lord of the Rings.",
    "Der Herr Der Ringe",
    "Lord of the rings.",
    "Lord of the Rings",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL25418754M",
    "/books/OL25418753M",
    "/books/OL15280670M",
    "/books/OL9076613M",
    "/books/OL9076577M",
    "/books/OL22054291M",
    "/books/OL23097541M",
    "/books/OL9076578M",
    "/books/OL12823904M",
    "/works/OL16245393W",
    "/subjects/english_fantasy_fiction",
    "/subjects/translations_into_german",
    "/subjects/german_fantasy_fiction",
    "/subjects/translations_from_english",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "contributor": [
    "Carroux, Margaret."
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "English Fantasy fiction",
    "Translations into German",
    "German Fantasy fiction",
    "Translations from English"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "1991",
    "March 12, 1999",
    "2002",
    "2001",
    "1950",
    "July 1, 2003",
    "October 31, 2001"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Stuttgart",
    "Klett-Cotta"
   ],
   "edition_count": 9,
   "key": "/works/OL16245393W",
   "id_goodreads": [
    "514235",
    "136774",
    "4543827",
    "136773",
    "136779",
    "136775"
   ],
   "publisher": [
    "Collins",
    "Hobbit Presse",
    "Klett-Cotte",
    "J.G. Cotta'sche, Buchhandlung Nachfolger GmbH",
    "Klett-Cotta"
   ],
   "language": [
    "ger"
   ],
   "last_modified_i": 1525543460,
   "id_librarything": [
    "1386651",
    "3203347",
    "3203350"
   ],
   "cover_edition_key": "OL9076613M",
   "publish_year": [
    1991,
    1999,
    2002,
    2003,
    2001,
    1950
   ],
   "first_publish_year": 1950,
   "oclc": [
    "43202270"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9131845M",
    "OL9137997M",
    "OL9131886M",
    "OL9131846M",
    "OL9179425M",
    "OL10943762M"
   ],
   "cover_i": 4927739,
   "isbn": [
    "9780606305648",
    "8445070320",
    "9505470665",
    "9788445070338",
    "9789706906533",
    "8445071769",
    "0606305645",
    "9706906533",
    "9788445071762",
    "9788445070321",
    "8445070339",
    "9789505470662"
   ],
   "has_fulltext": false,
   "text": [
    "OL9131845M",
    "OL9137997M",
    "OL9131886M",
    "OL9131846M",
    "OL9179425M",
    "OL10943762M",
    "9780606305648",
    "8445070320",
    "9505470665",
    "9788445070338",
    "9789706906533",
    "8445071769",
    "0606305645",
    "9706906533",
    "9788445071762",
    "9788445070321",
    "8445070339",
    "9789505470662",
    "J. R. R. Tolkien",
    "56605802",
    "OL26320A",
    "Internet Archive Wishlist",
    "el retorno del rey",
    "Las DOS Torres (Lord of the Rings)",
    "LA Comunidad Del Anillo",
    "El Retorno Del Rey Iii",
    "Las Dos Torres",
    "The Lord of the Rings",
    "/works/OL27494W",
    "Minotauro/Argentina",
    "Minotauro",
    "Turtleback Books Distributed by Demco Media",
    "El Senor De Los Anillos / the Lord of the Rings",
    "El Senor De Los Anillos/the Lord of the Rings",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL9131845M",
    "/books/OL9137997M",
    "/books/OL9131886M",
    "/books/OL9131846M",
    "/books/OL9179425M",
    "/books/OL10943762M",
    "/works/OL27494W",
    "/subjects/internet_archive_wishlist",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "Internet Archive Wishlist"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "March 2003",
    "March 2002",
    "February 1985",
    "April 30, 2004",
    "November 2001",
    "April 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 6,
   "key": "/works/OL27494W",
   "id_goodreads": [
    "984745",
    "984752",
    "63390",
    "63360",
    "15280"
   ],
   "publisher": [
    "Minotauro/Argentina",
    "Minotauro",
    "Turtleback Books Distributed by Demco Media"
   ],
   "language": [
    "spa"
   ],
   "last_modified_i": 1500045399,
   "id_librarything": [
    "3203347",
    "1386651",
    "3203356",
    "3203350"
   ],
   "cover_edition_key": "OL9179425M",
   "publish_year": [
    2002,
    2003,
    1985,
    2004,
    2001
   ],
   "first_publish_year": 1985,
   "oclc": [
    "56605802"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9117897M",
    "OL18462275M",
    "OL9131874M",
    "OL9179424M"
   ],
   "isbn": [
    "9788422690306",
    "9789706906519",
    "9706906517",
    "8445071408",
    "9788445071403",
    "8422690306"
   ],
   "has_fulltext": true,
   "id_dep\u00f3sito_legal": [
    "B472882001"
   ],
   "text": [
    "OL9117897M",
    "OL18462275M",
    "OL9131874M",
    "OL9179424M",
    "9788422690306",
    "9789706906519",
    "9706906517",
    "8445071408",
    "9788445071403",
    "8422690306",
    "J. R. R. Tolkien",
    "elsenordelosanil00jrrt",
    "OL26320A",
    "In library",
    "Accessible book",
    "Protected DAISY",
    "La Comunidad Del Anillo I",
    "LA Comunidad Del Anillo (Lord of the Rings)",
    "The Lord of the Rings",
    "/works/OL16245392W",
    "Minotauro/Argentina",
    "Minotauro",
    "Circulo de Lectores",
    "The lord of the rings.",
    "El senor de los anillos.",
    "El Senor De Los Anillos",
    "El Se\u00f1or De Los Anillos",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL9117897M",
    "/books/OL18462275M",
    "/books/OL9131874M",
    "/books/OL9179424M",
    "/works/OL16245392W",
    "/subjects/in_library",
    "/authors/OL26320A"
   ],
   "id_librarything": [
    "3203347"
   ],
   "ia": [
    "elsenordelosanil00jrrt"
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "In library",
    "Accessible book",
    "Protected DAISY"
   ],
   "title": "The Lord of the Rings",
   "lending_identifier_s": "elsenordelosanil00jrrt",
   "ia_collection_s": "printdisabled;bannedbooks;inlibrary;china;internetarchivebooks",
   "printdisabled_s": "OL9131874M",
   "type": "work",
   "ebook_count_i": 1,
   "publish_place": [
    "Barcelona, Espa\u00f1a",
    "Barcelona"
   ],
   "ia_box_id": [
    "IA1113422"
   ],
   "edition_count": 4,
   "first_publish_year": 1977,
   "key": "/works/OL16245392W",
   "id_goodreads": [
    "222947",
    "984757",
    "63387"
   ],
   "public_scan_b": false,
   "publisher": [
    "Minotauro/Argentina",
    "Minotauro",
    "Circulo de Lectores"
   ],
   "language": [
    "spa"
   ],
   "last_modified_i": 1525542850,
   "lending_edition_s": "OL9131874M",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL9117897M",
   "publish_year": [
    1977,
    2002,
    1982,
    2003
   ],
   "publish_date": [
    "1977",
    "March 2002",
    "April 2003",
    "1982"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL8018652M",
    "OL8018616M",
    "OL17943583M"
   ],
   "cover_i": 511001,
   "isbn": [
    "9780761553120",
    "9780761553922",
    "0761553126",
    "0761553924"
   ],
   "has_fulltext": false,
   "text": [
    "OL8018652M",
    "OL8018616M",
    "OL17943583M",
    "9780761553120",
    "9780761553922",
    "0761553126",
    "0761553924",
    "Eric Mylonas",
    "76962300",
    "OL1395518A",
    "The Battle for Middle-earth II (Prima Official Game Guide)",
    "the battle for Middle Earth : Prima official game guide",
    "The Battle for Middle-earth II (Xbox 360) (Prima Official Game Guide)",
    "The Lord of the Rings",
    "Eric ECM Mylonas.",
    "/works/OL5740146W",
    "Prima Games",
    "Lord of the rings",
    "Battle for Middle Earth :",
    "2006903650"
   ],
   "author_name": [
    "Eric Mylonas"
   ],
   "seed": [
    "/books/OL8018652M",
    "/books/OL8018616M",
    "/books/OL17943583M",
    "/works/OL5740146W",
    "/authors/OL1395518A"
   ],
   "oclc": [
    "76962300"
   ],
   "author_key": [
    "OL1395518A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "July 4, 2006",
    "2006",
    "February 28, 2006"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Roseville, CA"
   ],
   "edition_count": 3,
   "key": "/works/OL5740146W",
   "id_goodreads": [
    "15290",
    "877739"
   ],
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2006903650"
   ],
   "last_modified_i": 1303941283,
   "id_librarything": [
    "4402478"
   ],
   "cover_edition_key": "OL8018616M",
   "publish_year": [
    2006
   ],
   "first_publish_year": 2006
  },
  {
   "title_suggest": "The Lord of the rings",
   "edition_key": [
    "OL3670710M",
    "OL3670562M",
    "OL22034985M"
   ],
   "cover_i": 393986,
   "isbn": [
    "0007170564",
    "0618257365",
    "9780618257362",
    "9780007170562",
    "0618258116",
    "9780618258116"
   ],
   "has_fulltext": false,
   "text": [
    "OL3670710M",
    "OL3670562M",
    "OL22034985M",
    "0007170564",
    "0618257365",
    "9780618257362",
    "9780007170562",
    "0618258116",
    "9780618258116",
    "David Brawn",
    "Coad, Chris.",
    "Vinet, Pierre.",
    "50995977",
    "51006684",
    "OL1398136A",
    "the two towers : photo guide",
    "photo guide",
    "the two towers : creatures",
    "The Lord of the rings",
    "[text by David Brawn].",
    "text by David Brawn ; photography by Pierre Vinet and Chris Coad.",
    "Lord of the rings, the two towers (Motion picture)",
    "Lord of the rings, the return of the king (Motion picture)",
    "/works/OL5747799W",
    "Collins",
    "Houghton Mifflin",
    "Two towers photo guide",
    "The lord of the rings.",
    "Two towers creatures",
    "2002727063",
    "2002727306"
   ],
   "author_name": [
    "David Brawn"
   ],
   "seed": [
    "/books/OL3670710M",
    "/books/OL3670562M",
    "/books/OL22034985M",
    "/works/OL5747799W",
    "/subjects/lord_of_the_rings_the_return_of_the_king_(motion_picture)",
    "/subjects/lord_of_the_rings_the_two_towers_(motion_picture)",
    "/authors/OL1398136A"
   ],
   "oclc": [
    "50995977",
    "51006684"
   ],
   "contributor": [
    "Coad, Chris.",
    "Vinet, Pierre."
   ],
   "author_key": [
    "OL1398136A"
   ],
   "subject": [
    "Lord of the rings, the two towers (Motion picture)",
    "Lord of the rings, the return of the king (Motion picture)"
   ],
   "title": "The Lord of the rings",
   "publish_date": [
    "2002",
    "2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "New York",
    "London"
   ],
   "edition_count": 3,
   "key": "/works/OL5747799W",
   "id_goodreads": [
    "15327",
    "15335",
    "15266"
   ],
   "publisher": [
    "Collins",
    "Houghton Mifflin"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2002727063",
    "2002727306"
   ],
   "last_modified_i": 1291513732,
   "id_librarything": [
    "313188",
    "26037",
    "790603"
   ],
   "cover_edition_key": "OL3670562M",
   "publish_year": [
    2002,
    2003
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The lord of the rings",
   "edition_key": [
    "OL11759646M",
    "OL3953584M",
    "OL23247000M"
   ],
   "cover_i": 393721,
   "isbn": [
    "0618258000",
    "9780618195596",
    "9780618258000",
    "0618195599",
    "9781417605101",
    "0618260226",
    "9780618260225",
    "1417605103"
   ],
   "has_fulltext": true,
   "text": [
    "OL11759646M",
    "OL3953584M",
    "OL23247000M",
    "0618258000",
    "9780618195596",
    "9780618258000",
    "0618195599",
    "9781417605101",
    "0618260226",
    "9780618260225",
    "1417605103",
    "Brian Sibley",
    "Tolkien, J. R. R. 1892-1973.",
    "lordofringsmakin00sibl",
    "lordofringsinsid00sibl",
    "OL475982A",
    "English Fantasy fiction",
    "In library",
    "Middle Earth (Imaginary place)",
    "Accessible book",
    "History and criticism",
    "Handbooks, manuals",
    "Protected DAISY",
    "Fantasy fiction, English",
    "Handbooks, manuals, etc",
    "The Fellowship Of The Ring Insider's Guide",
    "insider's guide",
    "the making of the movie trilogy",
    "The lord of the rings",
    "/works/OL3062799W",
    "Brian Sibley.",
    "Houghton Mifflin Company",
    "Tandem Library",
    "Houghton Mifflin",
    "The lord of the rings.",
    "Lord Of The Rings",
    "2001051586",
    "J. R. R. Tolkien (1892-1973)"
   ],
   "author_name": [
    "Brian Sibley"
   ],
   "contributor": [
    "Tolkien, J. R. R. 1892-1973."
   ],
   "ia_loaded_id": [
    "lordofringsinsid00sibl"
   ],
   "seed": [
    "/books/OL11759646M",
    "/books/OL3953584M",
    "/books/OL23247000M",
    "/works/OL3062799W",
    "/subjects/english_fantasy_fiction",
    "/subjects/in_library",
    "/subjects/middle_earth_(imaginary_place)",
    "/subjects/history_and_criticism",
    "/subjects/handbooks_manuals",
    "/subjects/protected_daisy",
    "/subjects/fantasy_fiction_english",
    "/subjects/handbooks_manuals_etc",
    "/subjects/person:j._r._r._tolkien_(1892-1973)",
    "/authors/OL475982A"
   ],
   "ia": [
    "lordofringsmakin00sibl",
    "lordofringsinsid00sibl"
   ],
   "author_key": [
    "OL475982A"
   ],
   "subject": [
    "English Fantasy fiction",
    "In library",
    "Middle Earth (Imaginary place)",
    "Accessible book",
    "History and criticism",
    "Handbooks, manuals",
    "Protected DAISY",
    "Fantasy fiction, English",
    "Handbooks, manuals, etc"
   ],
   "title": "The lord of the rings",
   "lending_identifier_s": "lordofringsinsid00sibl",
   "ia_collection_s": "printdisabled;internetarchivebooks;inlibrary;china;browserlending",
   "printdisabled_s": "OL3953584M;OL23247000M",
   "type": "work",
   "ebook_count_i": 2,
   "publish_place": [
    "New York, N.Y",
    "Boston"
   ],
   "ia_box_id": [
    "IA1124908",
    "IA179701"
   ],
   "edition_count": 3,
   "first_publish_year": 2001,
   "key": "/works/OL3062799W",
   "id_goodreads": [
    "470271",
    "780852",
    "7351",
    "15390"
   ],
   "public_scan_b": false,
   "publisher": [
    "Houghton Mifflin Company",
    "Tandem Library",
    "Houghton Mifflin"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2001051586"
   ],
   "last_modified_i": 1500685912,
   "lending_edition_s": "OL3953584M",
   "id_librarything": [
    "76320",
    "181567"
   ],
   "cover_edition_key": "OL3953584M",
   "person": [
    "J. R. R. Tolkien (1892-1973)"
   ],
   "publish_year": [
    2002,
    2001
   ],
   "publish_date": [
    "2002",
    "2001",
    "November 2001"
   ]
  },
  {
   "title_suggest": "The lord of the rings",
   "edition_key": [
    "OL3949131M",
    "OL3670507M",
    "OL22074077M"
   ],
   "cover_i": 393983,
   "isbn": [
    "000711625X",
    "0618258027",
    "9780618258024",
    "9780007116256",
    "9780618154012",
    "0618154019"
   ],
   "has_fulltext": true,
   "text": [
    "OL3949131M",
    "OL3670507M",
    "OL22074077M",
    "000711625X",
    "0618258027",
    "9780618258024",
    "9780007116256",
    "9780618154012",
    "0618154019",
    "Jude Fisher",
    "Tolkien, J. R. R. 1892-1973.",
    "50917436",
    "lordofringsfello00fish",
    "OL1399851A",
    "Lord of the Rings: The two towers (Motion picture)",
    "In library",
    "Film and video adaptations",
    "Middle Earth (Imaginary place)",
    "Lord of the rings, the fellowship of the ring (Motion picture)",
    "Accessible book",
    "Lord of the rings, the two towers (Motion picture)",
    "Protected DAISY",
    "Illustrations",
    "Pictorial works",
    "the two towers : visual companion",
    "The two towers : visual companion",
    "the fellowship of the ring : visual companion",
    "The lord of the rings",
    "/works/OL5753836W",
    "Jude Fisher.",
    "HarperCollins",
    "Houghton Mifflin",
    "Two towers visual companion",
    "The Lord of the rings",
    "2002726993",
    "2001039533",
    "J. R. R. Tolkien (1892-1973)"
   ],
   "author_name": [
    "Jude Fisher"
   ],
   "contributor": [
    "Tolkien, J. R. R. 1892-1973."
   ],
   "ia_loaded_id": [
    "lordofringsfello00fish"
   ],
   "seed": [
    "/books/OL3949131M",
    "/books/OL3670507M",
    "/books/OL22074077M",
    "/works/OL5753836W",
    "/subjects/lord_of_the_rings:_the_two_towers_(motion_picture)",
    "/subjects/in_library",
    "/subjects/film_and_video_adaptations",
    "/subjects/middle_earth_(imaginary_place)",
    "/subjects/lord_of_the_rings_the_fellowship_of_the_ring_(motion_picture)",
    "/subjects/lord_of_the_rings_the_two_towers_(motion_picture)",
    "/subjects/protected_daisy",
    "/subjects/illustrations",
    "/subjects/pictorial_works",
    "/subjects/person:j._r._r._tolkien_(1892-1973)",
    "/authors/OL1399851A"
   ],
   "oclc": [
    "50917436"
   ],
   "ia": [
    "lordofringsfello00fish"
   ],
   "author_key": [
    "OL1399851A"
   ],
   "subject": [
    "Lord of the Rings: The two towers (Motion picture)",
    "In library",
    "Film and video adaptations",
    "Middle Earth (Imaginary place)",
    "Lord of the rings, the fellowship of the ring (Motion picture)",
    "Accessible book",
    "Lord of the rings, the two towers (Motion picture)",
    "Protected DAISY",
    "Illustrations",
    "Pictorial works"
   ],
   "title": "The lord of the rings",
   "lending_identifier_s": "lordofringsfello00fish",
   "ia_collection_s": "printdisabled;browserlending;china;inlibrary;internetarchivebooks",
   "publish_date": [
    "2002",
    "2001"
   ],
   "type": "work",
   "ebook_count_i": 1,
   "publish_place": [
    "Boston",
    "London"
   ],
   "ia_box_id": [
    "IA177101"
   ],
   "edition_count": 3,
   "first_publish_year": 2001,
   "key": "/works/OL5753836W",
   "id_goodreads": [
    "15222",
    "15221",
    "93936"
   ],
   "public_scan_b": false,
   "publisher": [
    "HarperCollins",
    "Houghton Mifflin"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2002726993",
    "2001039533"
   ],
   "last_modified_i": 1500721046,
   "lending_edition_s": "OL3949131M",
   "id_librarything": [
    "86479",
    "121443"
   ],
   "cover_edition_key": "OL3670507M",
   "person": [
    "J. R. R. Tolkien (1892-1973)"
   ],
   "publish_year": [
    2002,
    2001
   ],
   "printdisabled_s": "OL3949131M"
  },
  {
   "title_suggest": "The lord of the rings",
   "edition_key": [
    "OL1700996M",
    "OL3938088M",
    "OL22149857M"
   ],
   "cover_i": 583487,
   "isbn": [
    "9780805794410",
    "9780813190174",
    "080578571X",
    "0805794417",
    "9780805785715",
    "0813190177"
   ],
   "has_fulltext": true,
   "text": [
    "OL1700996M",
    "OL3938088M",
    "OL22149857M",
    "9780805794410",
    "9780813190174",
    "080578571X",
    "0805794417",
    "9780805785715",
    "0813190177",
    "Jane Chance",
    "lordofringst00chan",
    "isbn_9780813190174",
    "OL578238A",
    "English Fantasy fiction",
    "Politics and literature",
    "Middle Earth (Imaginary place)",
    "Literature and society",
    "Accessible book",
    "History and criticism",
    "Political fiction, English",
    "Myth in literature",
    "Political and social views",
    "English Political fiction",
    "Protected DAISY",
    "Fantasy fiction, English",
    "Power (Social sciences) in literature",
    "History",
    "the mythology of power",
    "The lord of the rings",
    "/works/OL3469307W",
    "Jane Chance.",
    "Twayne Publishers",
    "Maxwell Macmillan Canada",
    "University Press of Kentucky",
    "Maxwell Macmillan International",
    "92001402",
    "2001002583",
    "20012583",
    "J. R. R. Tolkien (1892-1973)",
    "Great Britain",
    "20th century"
   ],
   "author_name": [
    "Jane Chance"
   ],
   "ia_loaded_id": [
    "lordofringst00chan"
   ],
   "seed": [
    "/books/OL1700996M",
    "/books/OL3938088M",
    "/books/OL22149857M",
    "/works/OL3469307W",
    "/subjects/english_fantasy_fiction",
    "/subjects/english_political_fiction",
    "/subjects/fantasy_fiction_english",
    "/subjects/history",
    "/subjects/history_and_criticism",
    "/subjects/literature_and_society",
    "/subjects/middle_earth_(imaginary_place)",
    "/subjects/myth_in_literature",
    "/subjects/political_and_social_views",
    "/subjects/political_fiction_english",
    "/subjects/politics_and_literature",
    "/subjects/power_(social_sciences)_in_literature",
    "/subjects/protected_daisy",
    "/subjects/person:j._r._r._tolkien_(1892-1973)",
    "/subjects/place:great_britain",
    "/subjects/time:20th_century",
    "/authors/OL578238A"
   ],
   "ia": [
    "lordofringst00chan",
    "isbn_9780813190174"
   ],
   "author_key": [
    "OL578238A"
   ],
   "subject": [
    "English Fantasy fiction",
    "Politics and literature",
    "Middle Earth (Imaginary place)",
    "Literature and society",
    "Accessible book",
    "History and criticism",
    "Political fiction, English",
    "Myth in literature",
    "Political and social views",
    "English Political fiction",
    "Protected DAISY",
    "Fantasy fiction, English",
    "Power (Social sciences) in literature",
    "History"
   ],
   "title": "The lord of the rings",
   "ia_collection_s": "printdisabled;china;internetarchivebooks",
   "printdisabled_s": "OL22149857M;OL1700996M",
   "type": "work",
   "ebook_count_i": 2,
   "publish_place": [
    "Toronto",
    "New York",
    "Lexington"
   ],
   "ia_box_id": [
    "IA1129901",
    "IA158801",
    "IA145116"
   ],
   "edition_count": 3,
   "key": "/works/OL3469307W",
   "id_goodreads": [
    "54700",
    "1280690",
    "998764"
   ],
   "public_scan_b": false,
   "publisher": [
    "Twayne Publishers",
    "Maxwell Macmillan Canada",
    "University Press of Kentucky",
    "Maxwell Macmillan International"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "92001402",
    "2001002583",
    "20012583"
   ],
   "last_modified_i": 1506056146,
   "first_publish_year": 1992,
   "id_librarything": [
    "837759"
   ],
   "cover_edition_key": "OL1700996M",
   "person": [
    "J. R. R. Tolkien (1892-1973)"
   ],
   "publish_year": [
    1992,
    2001
   ],
   "publish_date": [
    "1992",
    "2001"
   ],
   "place": [
    "Great Britain"
   ],
   "time": [
    "20th century"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL12509252M",
    "OL8890612M",
    "OL8890596M"
   ],
   "cover_i": -1,
   "isbn": [
    "9782267011258",
    "9782266032483",
    "9782267013160",
    "2267013169",
    "2267011255",
    "2266032488"
   ],
   "has_fulltext": false,
   "text": [
    "OL12509252M",
    "OL8890612M",
    "OL8890596M",
    "9782267011258",
    "9782266032483",
    "9782267013160",
    "2267013169",
    "2267011255",
    "2266032488",
    "J. R. R. Tolkien",
    "OL26320A",
    "Lectures et morceaux choisis",
    "Litte rature fantastique",
    "Roman",
    "Franc \u02b9ais (langue)",
    "Science-fiction",
    "The Lord of the Rings",
    "/works/OL27507W",
    "Pocket",
    "Christian Bourgois",
    "Le Seigneur DES Anneaux",
    "Le Seigneur des Anneaux",
    "Le Seigneur des anneaux",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL12509252M",
    "/books/OL8890612M",
    "/books/OL8890596M",
    "/works/OL27507W",
    "/subjects/lectures_et_morceaux_choisis",
    "/subjects/litte_rature_fantastique",
    "/subjects/roman",
    "/subjects/franc_\u02b9ais_(langue)",
    "/subjects/science-fiction",
    "/authors/OL26320A"
   ],
   "id_librarything": [
    "1386651"
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "Lectures et morceaux choisis",
    "Litte rature fantastique",
    "Roman",
    "Franc \u02b9ais (langue)",
    "Science-fiction"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "December 31, 1995",
    "October 16, 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 3,
   "key": "/works/OL27507W",
   "id_goodreads": [
    "1597667",
    "1811086",
    "6768611"
   ],
   "publisher": [
    "Pocket",
    "Christian Bourgois"
   ],
   "language": [
    "fre"
   ],
   "last_modified_i": 1527104364,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL8890612M",
   "publish_year": [
    2002,
    1995
   ],
   "first_publish_year": 1995
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9217143M",
    "OL7262428M"
   ],
   "cover_i": 10796,
   "isbn": [
    "0007149131",
    "9780007149131"
   ],
   "has_fulltext": false,
   "text": [
    "OL9217143M",
    "OL7262428M",
    "0007149131",
    "9780007149131",
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL27449W",
    "HarperCollins",
    "The Lord of the Rings trilogy - one volume hardback (movie cover)",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL9217143M",
    "/books/OL7262428M",
    "/works/OL27449W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL27449W",
   "id_goodreads": [
    "273440"
   ],
   "publisher": [
    "HarperCollins"
   ],
   "last_modified_i": 1337898366,
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL7262428M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL3700728M",
    "OL25430694M"
   ],
   "cover_i": 393992,
   "isbn": [
    "0618258000",
    "9780618260225",
    "9780618258000",
    "0618260226",
    "9022533956",
    "9789022533956"
   ],
   "has_fulltext": false,
   "text": [
    "OL3700728M",
    "OL25430694M",
    "0618258000",
    "9780618260225",
    "9780618258000",
    "0618260226",
    "9022533956",
    "9789022533956",
    "Brian Sibley",
    "51196462",
    "OL475982A",
    "de verfilming van een meesterwerk",
    "The Lord of the Rings",
    "Brian Sibley.",
    "Lord of the rings, the two towers (Motion picture)",
    "Lord of the rings, the return of the king (Motion picture)",
    "Lord of the rings, the fellowship of the ring (Motion picture)",
    "/works/OL3062780W",
    "Uitgeverij M",
    "Houghton Mifflin Company",
    "The Lord of the Rings: The Making of the Movie Trilogy",
    "2003266645"
   ],
   "author_name": [
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL3700728M",
    "/books/OL25430694M",
    "/works/OL3062780W",
    "/subjects/lord_of_the_rings_the_fellowship_of_the_ring_(motion_picture)",
    "/subjects/lord_of_the_rings_the_return_of_the_king_(motion_picture)",
    "/subjects/lord_of_the_rings_the_two_towers_(motion_picture)",
    "/authors/OL475982A"
   ],
   "oclc": [
    "51196462"
   ],
   "author_key": [
    "OL475982A"
   ],
   "subject": [
    "Lord of the rings, the two towers (Motion picture)",
    "Lord of the rings, the return of the king (Motion picture)",
    "Lord of the rings, the fellowship of the ring (Motion picture)"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Boston",
    "Amsterdam, Netherlands"
   ],
   "edition_count": 2,
   "key": "/works/OL3062780W",
   "id_goodreads": [
    "780852",
    "7351"
   ],
   "publisher": [
    "Uitgeverij M",
    "Houghton Mifflin Company"
   ],
   "language": [
    "dut",
    "eng"
   ],
   "lccn": [
    "2003266645"
   ],
   "last_modified_i": 1378806406,
   "id_librarything": [
    "76320"
   ],
   "cover_edition_key": "OL3700728M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The lords of the rings",
   "edition_key": [
    "OL21090294M",
    "OL1471527M"
   ],
   "isbn": [
    "9780671711221",
    "0671711229",
    "0773726365",
    "9780773726369"
   ],
   "has_fulltext": false,
   "text": [
    "OL21090294M",
    "OL1471527M",
    "9780671711221",
    "0671711229",
    "0773726365",
    "9780773726369",
    "Vyv Simson",
    "Jennings, Andrew.",
    "OL738083A",
    "power, money, and drugs in the modern Olympics",
    "power, money and drugs in the modern Olympics",
    "The lords of the rings",
    "Vyv Simson & Andrew Jennings.",
    "Vyv Simon and Andrew Jennings.",
    "Mass media and sports",
    "Finance",
    "Corrupt practices",
    "Sports",
    "International Olympic Committee",
    "Olympics",
    "Political aspects of Olympics",
    "Political aspects",
    "/works/OL4005122W",
    "Stoddart",
    "Simon & Schuster",
    "93134306"
   ],
   "author_name": [
    "Vyv Simson"
   ],
   "seed": [
    "/books/OL21090294M",
    "/books/OL1471527M",
    "/works/OL4005122W",
    "/subjects/corrupt_practices",
    "/subjects/finance",
    "/subjects/international_olympic_committee",
    "/subjects/mass_media_and_sports",
    "/subjects/olympics",
    "/subjects/political_aspects",
    "/subjects/political_aspects_of_olympics",
    "/subjects/sports",
    "/authors/OL738083A"
   ],
   "contributor": [
    "Jennings, Andrew."
   ],
   "author_key": [
    "OL738083A"
   ],
   "subject": [
    "Mass media and sports",
    "Finance",
    "Corrupt practices",
    "Sports",
    "International Olympic Committee",
    "Olympics",
    "Political aspects of Olympics",
    "Political aspects"
   ],
   "title": "The lords of the rings",
   "publish_date": [
    "1992"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Toronto, Canada",
    "London"
   ],
   "edition_count": 2,
   "key": "/works/OL4005122W",
   "id_goodreads": [
    "1090327",
    "15362"
   ],
   "publisher": [
    "Stoddart",
    "Simon & Schuster"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "93134306"
   ],
   "last_modified_i": 1325062471,
   "id_librarything": [
    "6036356",
    "9826010"
   ],
   "publish_year": [
    1992
   ],
   "first_publish_year": 1992
  },
  {
   "title_suggest": "The lord of the rings",
   "publish_place": [
    "[2002?]"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 2,
   "edition_key": [
    "OL22373882M",
    "OL22373883M"
   ],
   "last_modified_i": 1264743054,
   "title": "The lord of the rings",
   "text": [
    "OL22373882M",
    "OL22373883M",
    "Fran Walsh",
    "Boyens, Philippa.",
    "Tolkien, J. R. R. 1892-1973.",
    "Jackson, Peter, 1961-",
    "OL6439810A",
    "the return of the king",
    "the fellowship of the ring",
    "The lord of the rings",
    "screenplay by Fran Walsh & Philippa Boyens & Peter Jackson ; based on the book by J.R.R. Tolkien.",
    "screenplay by Fran Walsh, Philippa Boyens & Peter Jackson ; based on the book by J.R.R. Tolkien.",
    "Drama",
    "Motion picture plays",
    "Fantasy films",
    "Middle Earth (Imaginary place)",
    "/works/OL13578274W",
    "Fellowship of the ring",
    "Return of the king",
    "Lord of the rings, the return of the king (Motion picture)",
    "Lord of the rings, the fellowship of the ring (Motion picture)",
    "2001-2010"
   ],
   "subject": [
    "Drama",
    "Motion picture plays",
    "Fantasy films",
    "Middle Earth (Imaginary place)"
   ],
   "publish_year": [
    2002,
    2003
   ],
   "seed": [
    "/books/OL22373882M",
    "/books/OL22373883M",
    "/works/OL13578274W",
    "/subjects/motion_picture_plays",
    "/subjects/drama",
    "/subjects/middle_earth_(imaginary_place)",
    "/subjects/fantasy_films",
    "/subjects/time:2001-2010",
    "/authors/OL6439810A"
   ],
   "first_publish_year": 2002,
   "author_name": [
    "Fran Walsh"
   ],
   "key": "/works/OL13578274W",
   "time": [
    "2001-2010"
   ],
   "contributor": [
    "Boyens, Philippa.",
    "Tolkien, J. R. R. 1892-1973.",
    "Jackson, Peter, 1961-"
   ],
   "publish_date": [
    "2002",
    "2003"
   ],
   "author_key": [
    "OL6439810A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL3700865M",
    "OL3328599M"
   ],
   "cover_i": 394161,
   "subtitle": "The Art of The Two Towers",
   "has_fulltext": false,
   "text": [
    "OL3700865M",
    "OL3328599M",
    "The Art of The Two Towers",
    "Gary Russell",
    "53997270",
    "51869993",
    "0618331301",
    "0618430296",
    "9780618331307",
    "9780618430291",
    "OL1401384A",
    "Motion pictures",
    "Middle Earth (Imaginary place)",
    "Lord of the rings, the two towers (Motion picture)",
    "Lord of the rings, the return of the king (Motion picture)",
    "Setting and scenery",
    "Characters and characteristics in motion pictures",
    "Pictorial works",
    "Internet Archive Wishlist",
    "the art of The return of the king",
    "The Lord of the Rings",
    "/works/OL5758765W",
    "Gary Russell.",
    "Houghton Mifflin",
    "Art of The two towers",
    "The  Lord of the Rings",
    "Art of The return of the king",
    "2003266852",
    "2004303379",
    "J. R. R. Tolkein (1892-1973)",
    "J. R. R. Tolkien (1892-1973)"
   ],
   "author_name": [
    "Gary Russell"
   ],
   "seed": [
    "/books/OL3700865M",
    "/books/OL3328599M",
    "/works/OL5758765W",
    "/subjects/motion_pictures",
    "/subjects/middle_earth_(imaginary_place)",
    "/subjects/lord_of_the_rings_the_two_towers_(motion_picture)",
    "/subjects/lord_of_the_rings_the_return_of_the_king_(motion_picture)",
    "/subjects/setting_and_scenery",
    "/subjects/characters_and_characteristics_in_motion_pictures",
    "/subjects/pictorial_works",
    "/subjects/internet_archive_wishlist",
    "/subjects/person:j._r._r._tolkein_(1892-1973)",
    "/subjects/person:j._r._r._tolkien_(1892-1973)",
    "/authors/OL1401384A"
   ],
   "oclc": [
    "53997270",
    "51869993"
   ],
   "isbn": [
    "0618331301",
    "0618430296",
    "9780618331307",
    "9780618430291"
   ],
   "author_key": [
    "OL1401384A"
   ],
   "subject": [
    "Motion pictures",
    "Middle Earth (Imaginary place)",
    "Lord of the rings, the two towers (Motion picture)",
    "Lord of the rings, the return of the king (Motion picture)",
    "Setting and scenery",
    "Characters and characteristics in motion pictures",
    "Pictorial works",
    "Internet Archive Wishlist"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2003",
    "2004"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Boston, Mass"
   ],
   "edition_count": 2,
   "key": "/works/OL5758765W",
   "id_goodreads": [
    "15242",
    "67514"
   ],
   "publisher": [
    "Houghton Mifflin"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2003266852",
    "2004303379"
   ],
   "last_modified_i": 1500013381,
   "id_librarything": [
    "186295",
    "186294"
   ],
   "cover_edition_key": "OL3700865M",
   "person": [
    "J. R. R. Tolkein (1892-1973)",
    "J. R. R. Tolkien (1892-1973)"
   ],
   "publish_year": [
    2003,
    2004
   ],
   "first_publish_year": 2003
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL24353781M",
    "OL25209450M"
   ],
   "isbn": [
    "9789027481979",
    "9027401683",
    "9027481970",
    "9789027401687"
   ],
   "has_fulltext": false,
   "text": [
    "OL24353781M",
    "OL25209450M",
    "9789027481979",
    "9027401683",
    "9027481970",
    "9789027401687",
    "J. R. R. Tolkien",
    "45573912",
    "OL26320A",
    "De Reisgenoten",
    "The Lord of the Rings",
    "/works/OL15367501W",
    "J.R.R. Tolkien ; [vert.: Max Schuchart]",
    "Het Spectrum",
    "In de Ban van de Ring I",
    "In de ban van de ring",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL24353781M",
    "/books/OL25209450M",
    "/works/OL15367501W",
    "/authors/OL26320A"
   ],
   "oclc": [
    "45573912"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "1975",
    "1979"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Antwerp, Belgium",
    "Utrecht [etc.]",
    "Utrecht, the Netherlands"
   ],
   "edition_count": 2,
   "key": "/works/OL15367501W",
   "publisher": [
    "Het Spectrum"
   ],
   "language": [
    "dut"
   ],
   "last_modified_i": 1525276568,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL24353781M",
   "publish_year": [
    1975,
    1979
   ],
   "first_publish_year": 1975
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9131848M",
    "OL25424621M"
   ],
   "isbn": [
    "9788445070352",
    "8445070355",
    "84-450-7375-3",
    "9788445073759"
   ],
   "has_fulltext": false,
   "text": [
    "OL9131848M",
    "OL25424621M",
    "9788445070352",
    "8445070355",
    "84-450-7375-3",
    "9788445073759",
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL16245357W",
    "Minotauro",
    "El Se\u00f1or de Los Anillos",
    "El se\u00f1or de los anillos",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL9131848M",
    "/books/OL25424621M",
    "/works/OL16245357W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "Barcelona, 2006",
    "July 1995"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL16245357W",
   "id_goodreads": [
    "3379781"
   ],
   "publisher": [
    "Minotauro"
   ],
   "language": [
    "spa"
   ],
   "last_modified_i": 1519835781,
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL9131848M",
   "publish_year": [
    1995,
    2006
   ],
   "first_publish_year": 1995
  },
  {
   "title_suggest": "Lord of the Rings, the",
   "edition_key": [
    "OL25418752M",
    "OL9850389M"
   ],
   "cover_i": 149274,
   "isbn": [
    "9780261103252",
    "0261103253"
   ],
   "has_fulltext": false,
   "text": [
    "OL25418752M",
    "OL9850389M",
    "9780261103252",
    "0261103253",
    "J. R. R. Tolkien",
    "OL26320A",
    "Fantasy",
    "OverDrive",
    "Fiction",
    "Lord of the Rings, the",
    "/works/OL14933439W",
    "Collins",
    "HarperCollins Publishers",
    "Lord of the Rings",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL25418752M",
    "/books/OL9850389M",
    "/works/OL14933439W",
    "/subjects/overdrive",
    "/subjects/fantasy",
    "/subjects/fiction",
    "/authors/OL26320A"
   ],
   "id_librarything": [
    "1386651"
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "Fantasy",
    "OverDrive",
    "Fiction"
   ],
   "title": "Lord of the Rings, the",
   "publish_date": [
    "August 1996",
    "1950"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL14933439W",
   "id_goodreads": [
    "15350"
   ],
   "publisher": [
    "Collins",
    "HarperCollins Publishers"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1523923363,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL9850389M",
   "publish_year": [
    1950,
    1996
   ],
   "first_publish_year": 1950,
   "id_wikidata": [
    "Q22122681"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7913930M",
    "OL7913929M"
   ],
   "subtitle": "The Two Towers: A Full-Cast Dramatization",
   "has_fulltext": false,
   "text": [
    "OL7913930M",
    "OL7913929M",
    "The Two Towers: A Full-Cast Dramatization",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "Dramatization (Narrator)",
    "9780739301180",
    "0739301195",
    "0739301187",
    "9780739301197",
    "OL26320A",
    "OL475982A",
    "Internet Archive Wishlist",
    "A Full-Cast Dramatization",
    "The Lord of the Rings",
    "/works/OL16245381W",
    "Random House Audio",
    "The Lord of the Rings: The Two Towers",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL7913930M",
    "/books/OL7913929M",
    "/works/OL16245381W",
    "/subjects/internet_archive_wishlist",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "id_librarything": [
    "3947494",
    "3203350"
   ],
   "contributor": [
    "Dramatization (Narrator)"
   ],
   "isbn": [
    "9780739301180",
    "0739301195",
    "0739301187",
    "9780739301197"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Internet Archive Wishlist"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "July 2, 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL16245381W",
   "id_goodreads": [
    "126754",
    "2914584"
   ],
   "publisher": [
    "Random House Audio"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1525877970,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL7913930M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "Realm of the Ring Lords",
   "edition_key": [
    "OL8478607M",
    "OL12268327M",
    "OL23015935M",
    "OL8803174M",
    "OL9216924M",
    "OL8803116M",
    "OL7262209M"
   ],
   "cover_i": 956526,
   "isbn": [
    "1903773172",
    "9780953768677",
    "1931412944",
    "0953768678",
    "9780007142934",
    "9781931412940",
    "1931412146",
    "9781931412148",
    "9781903773178",
    "0007142935"
   ],
   "has_fulltext": false,
   "text": [
    "OL8478607M",
    "OL12268327M",
    "OL23015935M",
    "OL8803174M",
    "OL9216924M",
    "OL8803116M",
    "OL7262209M",
    "1903773172",
    "9780953768677",
    "1931412944",
    "0953768678",
    "9780007142934",
    "9781931412940",
    "1931412146",
    "9781931412148",
    "9781903773178",
    "0007142935",
    "Laurence Gardner",
    "53808868",
    "50232910",
    "OL50039A",
    "Promotions",
    "Biblical teaching",
    "Management",
    "Folklore",
    "Work",
    "Rings",
    "Leadership",
    "Grail",
    "The Myth and Magic of the Grail Quest",
    "the myth and magic of the grail quest",
    "Beyond the Portal of the Twilight World",
    "Realm of the Ring Lords",
    "/works/OL646331W",
    "Laurence Gardner.",
    "MediaQuest",
    "Fair Winds Press (MA)",
    "HarperCollins Publishers Ltd",
    "Fair Winds Press",
    "Realm of the ring lords",
    "J. R. R. Tolkien's The Lord of The Rings is one of the most enchanting and successful tales of all time.",
    "Europe"
   ],
   "author_name": [
    "Laurence Gardner"
   ],
   "seed": [
    "/books/OL8478607M",
    "/books/OL12268327M",
    "/books/OL23015935M",
    "/books/OL8803174M",
    "/books/OL9216924M",
    "/books/OL8803116M",
    "/books/OL7262209M",
    "/works/OL646331W",
    "/subjects/biblical_teaching",
    "/subjects/folklore",
    "/subjects/grail",
    "/subjects/leadership",
    "/subjects/management",
    "/subjects/promotions",
    "/subjects/rings",
    "/subjects/work",
    "/subjects/place:europe",
    "/authors/OL50039A"
   ],
   "oclc": [
    "53808868",
    "50232910"
   ],
   "author_key": [
    "OL50039A"
   ],
   "subject": [
    "Promotions",
    "Biblical teaching",
    "Management",
    "Folklore",
    "Work",
    "Rings",
    "Leadership",
    "Grail"
   ],
   "title": "Realm of the Ring Lords",
   "publish_date": [
    "January 2003",
    "November 2000",
    "October 2001",
    "2002",
    "January 2002",
    "May 6, 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Gloucester, MA"
   ],
   "edition_count": 7,
   "key": "/works/OL646331W",
   "id_goodreads": [
    "883934",
    "883935",
    "1090324",
    "15328",
    "2039687"
   ],
   "publisher": [
    "MediaQuest",
    "Fair Winds Press (MA)",
    "HarperCollins Publishers Ltd",
    "Fair Winds Press"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1304164430,
   "id_librarything": [
    "153562"
   ],
   "cover_edition_key": "OL8803116M",
   "first_sentence": [
    "J. R. R. Tolkien's The Lord of The Rings is one of the most enchanting and successful tales of all time."
   ],
   "publish_year": [
    2002,
    2003,
    2000,
    2001
   ],
   "first_publish_year": 2000,
   "place": [
    "Europe"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7987631M"
   ],
   "isbn": [
    "0753508745",
    "9780753508749"
   ],
   "has_fulltext": false,
   "text": [
    "OL7987631M",
    "0753508745",
    "9780753508749",
    "Jim Smith",
    "J. Clive Matthews",
    "OL357812A",
    "OL2829513A",
    "The Films, the Books, the Radio Series (Virgin Film)",
    "The Lord of the Rings",
    "Pop Arts / Pop Culture",
    "Reference",
    "Performing Arts / Video / General",
    "General",
    "Fantasy",
    "Films, cinema",
    "Film & Video - General",
    "/works/OL7987631M",
    "Virgin Books"
   ],
   "author_name": [
    "Jim Smith",
    "J. Clive Matthews"
   ],
   "seed": [
    "/books/OL7987631M",
    "/works/OL7987631M",
    "/subjects/fantasy",
    "/subjects/films_cinema",
    "/subjects/pop_arts_/_pop_culture",
    "/subjects/reference",
    "/subjects/film_&_video_-_general",
    "/subjects/general",
    "/subjects/performing_arts_/_video_/_general",
    "/authors/OL357812A",
    "/authors/OL2829513A"
   ],
   "author_key": [
    "OL357812A",
    "OL2829513A"
   ],
   "subject": [
    "Pop Arts / Pop Culture",
    "Reference",
    "Performing Arts / Video / General",
    "General",
    "Fantasy",
    "Films, cinema",
    "Film & Video - General"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "September 1, 2004"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL7987631M",
   "id_goodreads": [
    "515854"
   ],
   "publisher": [
    "Virgin Books"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1419574808,
   "id_librarything": [
    "151644"
   ],
   "cover_edition_key": "OL7987631M",
   "publish_year": [
    2004
   ],
   "first_publish_year": 2004
  },
  {
   "title_suggest": "The Lord of the Rings",
   "publisher": [
    "Stoddart Pub. Co."
   ],
   "isbn": [
    "9780671711221",
    "0671711229"
   ],
   "has_fulltext": false,
   "id_librarything": [
    "6036356"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL7662927M"
   ],
   "last_modified_i": 1281067528,
   "title": "The Lord of the Rings",
   "author_name": [
    "Vyv and Andrew Jennings. Simson"
   ],
   "seed": [
    "/books/OL7662927M",
    "/works/OL8270320W",
    "/authors/OL2751521A"
   ],
   "first_publish_year": 1992,
   "publish_year": [
    1992
   ],
   "key": "/works/OL8270320W",
   "text": [
    "OL7662927M",
    "9780671711221",
    "0671711229",
    "Vyv and Andrew Jennings. Simson",
    "OL2751521A",
    "Power, Money and Drugs In the Modern Olympics.",
    "The Lord of the Rings",
    "/works/OL8270320W",
    "Stoddart Pub. Co."
   ],
   "id_goodreads": [
    "1090327"
   ],
   "publish_date": [
    "1992"
   ],
   "author_key": [
    "OL2751521A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9776467M"
   ],
   "cover_i": 149318,
   "isbn": [
    "9780261104037",
    "0261104039"
   ],
   "has_fulltext": false,
   "text": [
    "OL9776467M",
    "9780261104037",
    "0261104039",
    "Harpercoll",
    "J. R. R. Tolkien (Creator)",
    "57484284",
    "OL2622493A",
    "A Book of 20 Postcards (Postcard Books)",
    "The Lord of the Rings",
    "/works/OL7908921W",
    "Harpercollins Pub Ltd"
   ],
   "author_name": [
    "Harpercoll"
   ],
   "seed": [
    "/books/OL9776467M",
    "/works/OL7908921W",
    "/authors/OL2622493A"
   ],
   "oclc": [
    "57484284"
   ],
   "contributor": [
    "J. R. R. Tolkien (Creator)"
   ],
   "author_key": [
    "OL2622493A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "May 2000"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL7908921W",
   "id_goodreads": [
    "15355"
   ],
   "publisher": [
    "Harpercollins Pub Ltd"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1347099678,
   "id_librarything": [
    "786659"
   ],
   "cover_edition_key": "OL9776467M",
   "publish_year": [
    2000
   ],
   "first_publish_year": 2000
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL12307327M"
   ],
   "isbn": [
    "9781931334709",
    "1931334706"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "last_modified_i": 1272134414,
   "title": "The Lord of the Rings",
   "author_name": [
    "Wendy Conklin"
   ],
   "seed": [
    "/books/OL12307327M",
    "/works/OL8120484W",
    "/authors/OL2704059A"
   ],
   "key": "/works/OL8120484W",
   "text": [
    "OL12307327M",
    "9781931334709",
    "1931334706",
    "Wendy Conklin",
    "OL2704059A",
    "A Curriculum Guide",
    "The Lord of the Rings",
    "/works/OL8120484W"
   ],
   "id_goodreads": [
    "3007744"
   ],
   "author_key": [
    "OL2704059A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The lord of the rings.",
   "publish_place": [
    "Los Angeles"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL20098346M"
   ],
   "last_modified_i": 1419575049,
   "title": "The lord of the rings.",
   "publisher": [
    "Fotonovel Publications"
   ],
   "seed": [
    "/books/OL20098346M",
    "/works/OL20098346M"
   ],
   "first_publish_year": 1979,
   "publish_year": [
    1979
   ],
   "key": "/works/OL20098346M",
   "text": [
    "OL20098346M",
    "The lord of the rings.",
    "/works/OL20098346M",
    "Fotonovel Publications"
   ],
   "publish_date": [
    "1979"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings ",
   "edition_key": [
    "OL9924431M"
   ],
   "isbn": [
    "0007702752",
    "9780007702756"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "last_modified_i": 1419576451,
   "title": "The Lord of the Rings ",
   "id_librarything": [
    "3209063"
   ],
   "seed": [
    "/books/OL9924431M",
    "/works/OL9924431M"
   ],
   "key": "/works/OL9924431M",
   "text": [
    "OL9924431M",
    "0007702752",
    "9780007702756",
    "The Return of the Kings ; Special Deluxe Gift Edition",
    "The Lord of the Rings ",
    "/works/OL9924431M"
   ],
   "id_goodreads": [
    "73715"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of The Rings",
   "edition_key": [
    "OL7591511M"
   ],
   "isbn": [
    "9780458907700",
    "0458907707"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "last_modified_i": 1419575881,
   "title": "The Lord of The Rings",
   "id_librarything": [
    "3203356"
   ],
   "seed": [
    "/books/OL7591511M",
    "/works/OL7591511M"
   ],
   "oclc": [
    "44829562"
   ],
   "key": "/works/OL7591511M",
   "text": [
    "OL7591511M",
    "9780458907700",
    "0458907707",
    "44829562",
    "The Lord of The Rings",
    "/works/OL7591511M"
   ],
   "id_goodreads": [
    "564131"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The lord of the rings",
   "edition_key": [
    "OL3315530M"
   ],
   "isbn": [
    "0761547479",
    "9780761547471"
   ],
   "has_fulltext": true,
   "text": [
    "OL3315530M",
    "0761547479",
    "9780761547471",
    "57245819",
    "lordringsthirdag00grou",
    "Prima official game guide.",
    "The lord of the rings",
    "Protected DAISY",
    "Accessible book",
    "Video games",
    "Lord of the Rings (Game)",
    "/works/OL16943581W",
    "Prima Games",
    "The Lord of the Rings: the third age",
    "2004109805"
   ],
   "seed": [
    "/books/OL3315530M",
    "/works/OL16943581W",
    "/subjects/video_games",
    "/subjects/lord_of_the_rings_(game)"
   ],
   "oclc": [
    "57245819"
   ],
   "ia": [
    "lordringsthirdag00grou"
   ],
   "subject": [
    "Protected DAISY",
    "Accessible book",
    "Video games",
    "Lord of the Rings (Game)"
   ],
   "title": "The lord of the rings",
   "ia_collection_s": "printdisabled;librarygenesis",
   "first_publish_year": 2004,
   "type": "work",
   "ebook_count_i": 1,
   "publish_place": [
    "Roseville, CA"
   ],
   "printdisabled_s": "OL3315530M",
   "edition_count": 1,
   "key": "/works/OL16943581W",
   "id_goodreads": [
    "15248"
   ],
   "public_scan_b": false,
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2004109805"
   ],
   "last_modified_i": 1406594525,
   "id_librarything": [
    "53526"
   ],
   "cover_edition_key": "OL3315530M",
   "publish_year": [
    2004
   ],
   "publish_date": [
    "2004"
   ]
  },
  {
   "title_suggest": "The Lord of the Ring",
   "edition_key": [
    "OL8184572M"
   ],
   "cover_i": 1576186,
   "isbn": [
    "0830743278",
    "9780830743278"
   ],
   "has_fulltext": false,
   "text": [
    "OL8184572M",
    "0830743278",
    "9780830743278",
    "Phil Anderson",
    "74649012",
    "OL257300A",
    "The Lord of the Ring",
    "/works/OL2089932W",
    "Regal Books"
   ],
   "author_name": [
    "Phil Anderson"
   ],
   "seed": [
    "/books/OL8184572M",
    "/works/OL2089932W",
    "/authors/OL257300A"
   ],
   "oclc": [
    "74649012"
   ],
   "author_key": [
    "OL257300A"
   ],
   "title": "The Lord of the Ring",
   "publish_date": [
    "April 5, 2007"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL2089932W",
   "id_goodreads": [
    "15392"
   ],
   "publisher": [
    "Regal Books"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1303853859,
   "id_librarything": [
    "2041767"
   ],
   "cover_edition_key": "OL8184572M",
   "publish_year": [
    2007
   ],
   "first_publish_year": 2007
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL8018441M"
   ],
   "cover_i": 510809,
   "isbn": [
    "076154545X",
    "9780761545453"
   ],
   "has_fulltext": false,
   "text": [
    "OL8018441M",
    "076154545X",
    "9780761545453",
    "Bryan Stratton",
    "OL1396492A",
    "The Battle for Middle-earth (Prima Official Game Guide)",
    "The Lord of the Rings",
    "/works/OL5742945W",
    "Prima Games"
   ],
   "author_name": [
    "Bryan Stratton"
   ],
   "seed": [
    "/books/OL8018441M",
    "/works/OL5742945W",
    "/authors/OL1396492A"
   ],
   "author_key": [
    "OL1396492A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "December 14, 2004"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL5742945W",
   "id_goodreads": [
    "92006"
   ],
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1281130262,
   "id_librarything": [
    "3030910"
   ],
   "cover_edition_key": "OL8018441M",
   "publish_year": [
    2004
   ],
   "first_publish_year": 2004
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL21991871M"
   ],
   "isbn": [
    "0007144091",
    "9780007144099"
   ],
   "has_fulltext": false,
   "text": [
    "OL21991871M",
    "0007144091",
    "9780007144099",
    "David Brawn",
    "OL6382265A",
    "the two towers : creatures",
    "The Lord of the Rings",
    "[text by David Brawn].",
    "Adaptations",
    "/works/OL13513933W",
    "Collins",
    "J. R. R. Tolkien (1892-1973)"
   ],
   "author_name": [
    "David Brawn"
   ],
   "seed": [
    "/books/OL21991871M",
    "/works/OL13513933W",
    "/subjects/adaptations",
    "/subjects/person:j._r._r._tolkien_(1892-1973)",
    "/authors/OL6382265A"
   ],
   "author_key": [
    "OL6382265A"
   ],
   "subject": [
    "Adaptations"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "London"
   ],
   "edition_count": 1,
   "key": "/works/OL13513933W",
   "id_goodreads": [
    "1859716"
   ],
   "publisher": [
    "Collins"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1282177888,
   "id_librarything": [
    "790603"
   ],
   "person": [
    "J. R. R. Tolkien (1892-1973)"
   ],
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL3698865M"
   ],
   "cover_i": 481574,
   "isbn": [
    "9780744003499",
    "0744003490"
   ],
   "has_fulltext": false,
   "text": [
    "OL3698865M",
    "9780744003499",
    "0744003490",
    "Cohen, Mark",
    "54982741",
    "OL816088A",
    "war of the ring official strategy guide",
    "The Lord of the Rings",
    "by Mark Cohen.",
    "Video games",
    "/works/OL4245244W",
    "BradyGames",
    "Take your game further",
    "2003114104"
   ],
   "author_name": [
    "Cohen, Mark"
   ],
   "seed": [
    "/books/OL3698865M",
    "/works/OL4245244W",
    "/subjects/video_games",
    "/authors/OL816088A"
   ],
   "oclc": [
    "54982741"
   ],
   "author_key": [
    "OL816088A"
   ],
   "subject": [
    "Video games"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2004"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Indianapolis, IN"
   ],
   "edition_count": 1,
   "key": "/works/OL4245244W",
   "id_goodreads": [
    "15285"
   ],
   "publisher": [
    "BradyGames"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2003114104"
   ],
   "last_modified_i": 1304053246,
   "id_librarything": [
    "1260796"
   ],
   "cover_edition_key": "OL3698865M",
   "publish_year": [
    2004
   ],
   "first_publish_year": 2004
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9076563M"
   ],
   "isbn": [
    "9783608932225",
    "3608932224"
   ],
   "has_fulltext": false,
   "text": [
    "OL9076563M",
    "9783608932225",
    "3608932224",
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL15331152W",
    "Klett-Cotta",
    "Der Herr der Ringe. Die Gef\u00e4hrten / Die zwei T\u00fcrme / Die R\u00fcckkehr des K\u00f6nigs. Mit Anh\u00e4ngen und Register.",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL9076563M",
    "/works/OL15331152W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "January 1, 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL15331152W",
   "id_goodreads": [
    "671212"
   ],
   "publisher": [
    "Klett-Cotta"
   ],
   "language": [
    "ger"
   ],
   "last_modified_i": 1337897213,
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL9076563M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7827516M"
   ],
   "cover_i": 370481,
   "isbn": [
    "0553456539",
    "9780553456530"
   ],
   "has_fulltext": false,
   "text": [
    "OL7827516M",
    "0553456539",
    "9780553456530",
    "J. R. R. Tolkien",
    "Ian Holm (Narrator)",
    "Dramatization (Narrator)",
    "OL26320A",
    "Internet Archive Wishlist",
    "The Lord of the Rings",
    "/works/OL14926055W",
    "Random House Audio",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL7827516M",
    "/works/OL14926055W",
    "/subjects/internet_archive_wishlist",
    "/authors/OL26320A"
   ],
   "id_librarything": [
    "636553"
   ],
   "contributor": [
    "Ian Holm (Narrator)",
    "Dramatization (Narrator)"
   ],
   "author_key": [
    "OL26320A"
   ],
   "subject": [
    "Internet Archive Wishlist"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "December 1, 1999"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL14926055W",
   "id_goodreads": [
    "39"
   ],
   "publisher": [
    "Random House Audio"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1499986059,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL7827516M",
   "publish_year": [
    1999
   ],
   "first_publish_year": 1999
  },
  {
   "title_suggest": "The lord of the rings",
   "edition_key": [
    "OL8920312M"
   ],
   "cover_i": 6987479,
   "subtitle": "The Two Towers: The Lord of The Rings Strategy Game",
   "has_fulltext": true,
   "text": [
    "OL8920312M",
    "The Two Towers: The Lord of The Rings Strategy Game",
    "Talima Fox (Editor)",
    "Alexander Boyd (Illustrator)",
    "Mark Owen (Editor)",
    "David Gallagher (Illustrator)",
    "lordofringstwoto00cava",
    "1841542857",
    "9781841542850",
    "In library",
    "Accessible book",
    "Protected DAISY",
    "Rule Book",
    "Game",
    "Lord of the Rings (Game)",
    "The lord of the rings",
    "/works/OL16287785W",
    "Games Workshop",
    "The Lord of The Rings"
   ],
   "contributor": [
    "Talima Fox (Editor)",
    "Alexander Boyd (Illustrator)",
    "Mark Owen (Editor)",
    "David Gallagher (Illustrator)"
   ],
   "ia_loaded_id": [
    "lordofringstwoto00cava"
   ],
   "seed": [
    "/books/OL8920312M",
    "/works/OL16287785W",
    "/subjects/game",
    "/subjects/protected_daisy",
    "/subjects/rule_book",
    "/subjects/in_library",
    "/subjects/lord_of_the_rings_(game)"
   ],
   "ia": [
    "lordofringstwoto00cava"
   ],
   "isbn": [
    "1841542857",
    "9781841542850"
   ],
   "subject": [
    "In library",
    "Accessible book",
    "Protected DAISY",
    "Rule Book",
    "Game",
    "Lord of the Rings (Game)"
   ],
   "title": "The lord of the rings",
   "lending_identifier_s": "lordofringstwoto00cava",
   "ia_collection_s": "printdisabled;browserlending;china;inlibrary;internetarchivebooks",
   "printdisabled_s": "OL8920312M",
   "type": "work",
   "ebook_count_i": 1,
   "ia_box_id": [
    "IA125123"
   ],
   "edition_count": 1,
   "first_publish_year": 2003,
   "key": "/works/OL16287785W",
   "id_goodreads": [
    "899740"
   ],
   "public_scan_b": false,
   "publisher": [
    "Games Workshop"
   ],
   "last_modified_i": 1500687880,
   "lending_edition_s": "OL8920312M",
   "id_librarything": [
    "7916309"
   ],
   "cover_edition_key": "OL8920312M",
   "publish_year": [
    2003
   ],
   "publish_date": [
    "September 30, 2003"
   ]
  },
  {
   "title_suggest": "The Lord of the rings",
   "edition_key": [
    "OL24212888M"
   ],
   "subtitle": "the fellowship of the ring ; insiders' guide",
   "has_fulltext": true,
   "text": [
    "OL24212888M",
    "the fellowship of the ring ; insiders' guide",
    "Brian Sibley",
    "50526330",
    "lordofringsfello00siblrich",
    "0007131941",
    "9780007131945",
    "OL475982A",
    "Accessible book",
    "Protected DAISY",
    "In library",
    "Lord of the rings, the fellowship of the ring (Motion picture)",
    "The Lord of the rings",
    "/works/OL15145356W",
    "Brian Sibley.",
    "Collins"
   ],
   "author_name": [
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL24212888M",
    "/works/OL15145356W",
    "/subjects/accessible_book",
    "/subjects/lord_of_the_rings_the_fellowship_of_the_ring_(motion_picture)",
    "/subjects/in_library",
    "/subjects/protected_daisy",
    "/authors/OL475982A"
   ],
   "oclc": [
    "50526330"
   ],
   "ia": [
    "lordofringsfello00siblrich"
   ],
   "isbn": [
    "0007131941",
    "9780007131945"
   ],
   "author_key": [
    "OL475982A"
   ],
   "subject": [
    "Accessible book",
    "Protected DAISY",
    "In library",
    "Lord of the rings, the fellowship of the ring (Motion picture)"
   ],
   "title": "The Lord of the rings",
   "lending_identifier_s": "lordofringsfello00siblrich",
   "ia_collection_s": "printdisabled;inlibrary;browserlending;americana;internetarchivebooks",
   "printdisabled_s": "OL24212888M",
   "type": "work",
   "ebook_count_i": 1,
   "publish_place": [
    "London"
   ],
   "ia_box_id": [
    "IA105508"
   ],
   "edition_count": 1,
   "first_publish_year": 2001,
   "key": "/works/OL15145356W",
   "public_scan_b": false,
   "publisher": [
    "Collins"
   ],
   "last_modified_i": 1500705546,
   "lending_edition_s": "OL24212888M",
   "cover_edition_key": "OL24212888M",
   "publish_year": [
    2001
   ],
   "publish_date": [
    "2001"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7852599M"
   ],
   "isbn": [
    "0563528877",
    "9780563528876"
   ],
   "has_fulltext": false,
   "text": [
    "OL7852599M",
    "0563528877",
    "9780563528876",
    "J. R. R. Tolkien",
    "Stephen Thorne (Performer)",
    "John Le Mesurier (Performer)",
    "Simon Cadell (Performer)",
    "Ian Holm (Performer)",
    "Michael Hordern (Performer)",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL9085720W",
    "BBC Audiobooks",
    "The Lord of the Rings Trilogy (Radio Collection)",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL7852599M",
    "/works/OL9085720W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "contributor": [
    "Stephen Thorne (Performer)",
    "John Le Mesurier (Performer)",
    "Simon Cadell (Performer)",
    "Ian Holm (Performer)",
    "Michael Hordern (Performer)"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "October 7, 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL9085720W",
   "id_goodreads": [
    "130023"
   ],
   "publisher": [
    "BBC Audiobooks"
   ],
   "last_modified_i": 1525339345,
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL7852599M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL8018275M"
   ],
   "cover_i": 8167590,
   "subtitle": "The Fellowship of the Ring",
   "has_fulltext": false,
   "text": [
    "OL8018275M",
    "The Fellowship of the Ring",
    "Mark Cohen",
    "Debra McBride",
    "David Cassady",
    "51565698",
    "0761540873",
    "9780761540878",
    "OL2821360A",
    "OL1605109A",
    "OL244984A",
    "PlayStation 2",
    "Game Boy Advance",
    "GBA",
    "Electronic Entertainment",
    "Passtimes",
    "Strategy",
    "Video & Electronic - Nintendo",
    "PS2",
    "Gamebooks",
    "Computer Books: General",
    "Video & Electronic",
    "The Fellowship of the Ring",
    "The Hobbit",
    "PC",
    "Adventure",
    "RPG",
    "Videogames",
    "Role Playing Game",
    "Games/Puzzles",
    "Nintendo Games",
    "Personal Computer",
    "Video games",
    "Video & Electronic - Microsoft Xbox",
    "Xbox",
    "Video & Electronic - General",
    "J.R.R. Tolkien",
    "Games",
    "Hobbit",
    "Lord of the Rings (Game)",
    "Computer games",
    "Fellowship of the Ring",
    "Games / Video & Electronic",
    "The Lord of the Rings",
    "Hobbies",
    "Entertainment & Games - General",
    "Video & Electronic - Sony PlayStation 2",
    "Middle-earth",
    "Lord of the Rings",
    "Computers - Games",
    "Prima's Official Strategy Guide",
    "The Lord of the Rings",
    "/works/OL17863428W",
    "Prima Games",
    "The Lord of the Rings: The Fellowship of the Ring",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkien"
   ],
   "author_name": [
    "Mark Cohen",
    "Debra McBride",
    "David Cassady"
   ],
   "seed": [
    "/books/OL8018275M",
    "/works/OL17863428W",
    "/subjects/video_&_electronic_-_nintendo",
    "/subjects/video_&_electronic_-_general",
    "/subjects/games",
    "/subjects/computers_-_games",
    "/subjects/computer_books:_general",
    "/subjects/games/puzzles",
    "/subjects/video_&_electronic_-_sony_playstation_2",
    "/subjects/video_&_electronic_-_microsoft_xbox",
    "/subjects/entertainment_&_games_-_general",
    "/subjects/computer_games",
    "/subjects/games_/_video_&_electronic",
    "/subjects/lord_of_the_rings_(game)",
    "/subjects/video_&_electronic",
    "/subjects/gamebooks",
    "/subjects/personal_computer",
    "/subjects/pc",
    "/subjects/playstation_2",
    "/subjects/ps2",
    "/subjects/xbox",
    "/subjects/game_boy_advance",
    "/subjects/gba",
    "/subjects/video_games",
    "/subjects/videogames",
    "/subjects/strategy",
    "/subjects/passtimes",
    "/subjects/hobbies",
    "/subjects/electronic_entertainment",
    "/subjects/nintendo_games",
    "/subjects/j.r.r._tolkien",
    "/subjects/adventure",
    "/subjects/role_playing_game",
    "/subjects/rpg",
    "/subjects/the_hobbit",
    "/subjects/hobbit",
    "/subjects/the_lord_of_the_rings",
    "/subjects/lord_of_the_rings",
    "/subjects/the_fellowship_of_the_ring",
    "/subjects/fellowship_of_the_ring",
    "/subjects/middle-earth",
    "/subjects/person:j.r.r._tolkien",
    "/subjects/person:john_ronald_reuel_tolkien",
    "/authors/OL2821360A",
    "/authors/OL1605109A",
    "/authors/OL244984A"
   ],
   "oclc": [
    "51565698"
   ],
   "isbn": [
    "0761540873",
    "9780761540878"
   ],
   "author_key": [
    "OL2821360A",
    "OL1605109A",
    "OL244984A"
   ],
   "subject": [
    "PlayStation 2",
    "Game Boy Advance",
    "GBA",
    "Electronic Entertainment",
    "Passtimes",
    "Strategy",
    "Video & Electronic - Nintendo",
    "PS2",
    "Gamebooks",
    "Computer Books: General",
    "Video & Electronic",
    "The Fellowship of the Ring",
    "The Hobbit",
    "PC",
    "Adventure",
    "RPG",
    "Videogames",
    "Role Playing Game",
    "Games/Puzzles",
    "Nintendo Games",
    "Personal Computer",
    "Video games",
    "Video & Electronic - Microsoft Xbox",
    "Xbox",
    "Video & Electronic - General",
    "J.R.R. Tolkien",
    "Games",
    "Hobbit",
    "Lord of the Rings (Game)",
    "Computer games",
    "Fellowship of the Ring",
    "Games / Video & Electronic",
    "The Lord of the Rings",
    "Hobbies",
    "Entertainment & Games - General",
    "Video & Electronic - Sony PlayStation 2",
    "Middle-earth",
    "Lord of the Rings",
    "Computers - Games"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "October 29, 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17863428W",
   "id_goodreads": [
    "15257"
   ],
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1525344389,
   "id_librarything": [
    "1198541"
   ],
   "cover_edition_key": "OL8018275M",
   "person": [
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkien"
   ],
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL8018301M"
   ],
   "cover_i": 510611,
   "subtitle": "The Two Towers",
   "has_fulltext": true,
   "text": [
    "OL8018301M",
    "The Two Towers",
    "Dan Egger",
    "lordofrings00prim",
    "0761541942",
    "9780761541943",
    "OL1481503A",
    "In library",
    "Accessible book",
    "Protected DAISY",
    "Prima's Official Strategy Guide",
    "The Lord of the Rings",
    "/works/OL8495954W",
    "Prima Games",
    "The Lord of the Rings: The Two Towers"
   ],
   "author_name": [
    "Dan Egger"
   ],
   "seed": [
    "/books/OL8018301M",
    "/works/OL8495954W",
    "/subjects/in_library",
    "/authors/OL1481503A"
   ],
   "ia": [
    "lordofrings00prim"
   ],
   "isbn": [
    "0761541942",
    "9780761541943"
   ],
   "author_key": [
    "OL1481503A"
   ],
   "subject": [
    "In library",
    "Accessible book",
    "Protected DAISY"
   ],
   "title": "The Lord of the Rings",
   "lending_identifier_s": "lordofrings00prim",
   "ia_collection_s": "printdisabled;inlibrary;china;internetarchivebooks",
   "printdisabled_s": "OL8018301M",
   "type": "work",
   "ebook_count_i": 1,
   "publish_place": [
    "Roseville, CA"
   ],
   "ia_box_id": [
    "IA139801"
   ],
   "edition_count": 1,
   "first_publish_year": 2002,
   "key": "/works/OL8495954W",
   "id_goodreads": [
    "15283"
   ],
   "public_scan_b": false,
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1525348440,
   "lending_edition_s": "OL8018301M",
   "id_librarything": [
    "2666538"
   ],
   "cover_edition_key": "OL8018301M",
   "publish_year": [
    2002
   ],
   "publish_date": [
    "November 26, 2002"
   ]
  },
  {
   "title_suggest": "The Lord of the rings",
   "edition_key": [
    "OL3698160M"
   ],
   "cover_i": 510714,
   "isbn": [
    "0761543945",
    "9780761543947"
   ],
   "has_fulltext": false,
   "text": [
    "OL3698160M",
    "0761543945",
    "9780761543947",
    "Mario De Govia",
    "OL93017A",
    "Video games",
    "the return of the king : Prima's official strategy guide",
    "The Lord of the rings",
    "/works/OL1001224W",
    "Mario De Govia.",
    "Prima Games",
    "Prima's official strategy guide",
    "Return of the King",
    "2003111140"
   ],
   "author_name": [
    "Mario De Govia"
   ],
   "seed": [
    "/books/OL3698160M",
    "/works/OL1001224W",
    "/subjects/video_games",
    "/authors/OL93017A"
   ],
   "author_key": [
    "OL93017A"
   ],
   "subject": [
    "Video games"
   ],
   "title": "The Lord of the rings",
   "publish_date": [
    "2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Roseville, CA"
   ],
   "edition_count": 1,
   "key": "/works/OL1001224W",
   "id_goodreads": [
    "15258"
   ],
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2003111140"
   ],
   "last_modified_i": 1525351440,
   "id_librarything": [
    "2460463"
   ],
   "cover_edition_key": "OL3698160M",
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL3698160M"
   ],
   "cover_i": 8167609,
   "subtitle": "Return of the King",
   "has_fulltext": false,
   "text": [
    "OL3698160M",
    "Return of the King",
    "Mario De Govia",
    "0761543945",
    "9780761543947",
    "OL93017A",
    "Video & Electronic",
    "Game Boy Advance",
    "GBA",
    "Electronic Entertainment",
    "Passtimes",
    "Strategy",
    "PS2",
    "Gamebooks",
    "PlayStation 2",
    "The Hobbit",
    "PC",
    "Adventure",
    "RPG",
    "Videogames",
    "Role Playing Game",
    "J.R.R. Tolkien",
    "Nintendo Games",
    "Personal Computer",
    "Video games",
    "Xbox",
    "Video & Electronic - General",
    "Games",
    "Hobbit",
    "Lord of the Rings (Game)",
    "The Return of the King",
    "The Lord of the Rings",
    "Hobbies",
    "Middle-earth",
    "Lord of the Rings",
    "the return of the king : Prima's official strategy guide",
    "The Lord of the Rings",
    "/works/OL17863437W",
    "Mario De Govia.",
    "Prima Games",
    "The Lord of the rings",
    "Prima's official strategy guide",
    "Return of the King",
    "2003111140",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkien"
   ],
   "author_name": [
    "Mario De Govia"
   ],
   "seed": [
    "/books/OL3698160M",
    "/works/OL17863437W",
    "/subjects/lord_of_the_rings_(game)",
    "/subjects/games",
    "/subjects/video_&_electronic",
    "/subjects/gamebooks",
    "/subjects/personal_computer",
    "/subjects/pc",
    "/subjects/playstation_2",
    "/subjects/ps2",
    "/subjects/xbox",
    "/subjects/game_boy_advance",
    "/subjects/gba",
    "/subjects/video_games",
    "/subjects/videogames",
    "/subjects/strategy",
    "/subjects/passtimes",
    "/subjects/hobbies",
    "/subjects/electronic_entertainment",
    "/subjects/video_&_electronic_-_general",
    "/subjects/nintendo_games",
    "/subjects/j.r.r._tolkien",
    "/subjects/adventure",
    "/subjects/role_playing_game",
    "/subjects/rpg",
    "/subjects/the_hobbit",
    "/subjects/hobbit",
    "/subjects/the_lord_of_the_rings",
    "/subjects/lord_of_the_rings",
    "/subjects/the_return_of_the_king",
    "/subjects/middle-earth",
    "/subjects/person:j.r.r._tolkien",
    "/subjects/person:john_ronald_reuel_tolkien",
    "/authors/OL93017A"
   ],
   "isbn": [
    "0761543945",
    "9780761543947"
   ],
   "author_key": [
    "OL93017A"
   ],
   "subject": [
    "Video & Electronic",
    "Game Boy Advance",
    "GBA",
    "Electronic Entertainment",
    "Passtimes",
    "Strategy",
    "PS2",
    "Gamebooks",
    "PlayStation 2",
    "The Hobbit",
    "PC",
    "Adventure",
    "RPG",
    "Videogames",
    "Role Playing Game",
    "J.R.R. Tolkien",
    "Nintendo Games",
    "Personal Computer",
    "Video games",
    "Xbox",
    "Video & Electronic - General",
    "Games",
    "Hobbit",
    "Lord of the Rings (Game)",
    "The Return of the King",
    "The Lord of the Rings",
    "Hobbies",
    "Middle-earth",
    "Lord of the Rings"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Roseville, CA"
   ],
   "edition_count": 1,
   "key": "/works/OL17863437W",
   "id_goodreads": [
    "15258"
   ],
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "lccn": [
    "2003111140"
   ],
   "last_modified_i": 1525352406,
   "id_librarything": [
    "2460463"
   ],
   "cover_edition_key": "OL3698160M",
   "person": [
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkien"
   ],
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL16418946M"
   ],
   "isbn": [
    "8370799736",
    "9788370799731"
   ],
   "has_fulltext": false,
   "text": [
    "OL16418946M",
    "8370799736",
    "9788370799731",
    "J. R. R. Tolkien",
    "57687993",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL16245354W",
    "J. R. R. Tolkein.",
    "Literackie",
    "The Fellowship of the ring.",
    "Druzyna pierscienia",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL16418946M",
    "/works/OL16245354W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "2005"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Warszawa"
   ],
   "edition_count": 1,
   "key": "/works/OL16245354W",
   "id_goodreads": [
    "6534558"
   ],
   "publisher": [
    "Literackie"
   ],
   "language": [
    "pol"
   ],
   "last_modified_i": 1520099400,
   "id_librarything": [
    "3203356"
   ],
   "publish_year": [
    2005
   ],
   "first_publish_year": 2005,
   "oclc": [
    "57687993"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7591516M"
   ],
   "cover_i": 8889,
   "isbn": [
    "0458923400",
    "9780458923403"
   ],
   "has_fulltext": false,
   "text": [
    "OL7591516M",
    "0458923400",
    "9780458923403",
    "J. R. R. Tolkien",
    "OL26320A",
    "The Return of the King; with THE HOBBIT",
    "The Lord of the Rings",
    "/works/OL27470W",
    "Unwin Paperbacks",
    "THE LORD OF THE RINGS: Book (1) One: The Fellowship of the Ring; Book (2) Two: The Two Towers; Book (3) Three",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL7591516M",
    "/works/OL27470W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "1982"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL27470W",
   "id_goodreads": [
    "15382"
   ],
   "publisher": [
    "Unwin Paperbacks"
   ],
   "last_modified_i": 1526668721,
   "id_librarything": [
    "1386651"
   ],
   "publish_year": [
    1982
   ],
   "first_publish_year": 1982
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL9523430M"
   ],
   "isbn": [
    "9780563496144",
    "0563496142"
   ],
   "has_fulltext": false,
   "text": [
    "OL9523430M",
    "9780563496144",
    "0563496142",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "OL26320A",
    "OL475982A",
    "Fantasy - General",
    "Unabridged Audio - Fiction/General",
    "Radio Dramatization",
    "The Lord of the Rings",
    "/works/OL17871170W",
    "BBC Books",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL9523430M",
    "/works/OL17871170W",
    "/subjects/fantasy_-_general",
    "/subjects/unabridged_audio_-_fiction/general",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Fantasy - General",
    "Unabridged Audio - Fiction/General"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "January 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17871170W",
   "id_goodreads": [
    "3619846"
   ],
   "publisher": [
    "BBC Books"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1527105501,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7852600M"
   ],
   "cover_i": 375439,
   "isbn": [
    "0563528885",
    "9780563528883"
   ],
   "has_fulltext": false,
   "text": [
    "OL7852600M",
    "0563528885",
    "9780563528883",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "Stephen Thorne (Performer)",
    "John Le Mesurier (Performer)",
    "Simon Cadell (Performer)",
    "Ian Holm (Performer)",
    "Michael Hordern (Performer)",
    "OL26320A",
    "OL475982A",
    "Fantasy",
    "The Lord of the Rings",
    "/works/OL17871169W",
    "BBC Audiobooks",
    "The Lord of the Rings (BBC Radio Collection)",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL7852600M",
    "/works/OL17871169W",
    "/subjects/fantasy",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "id_librarything": [
    "636553"
   ],
   "contributor": [
    "Stephen Thorne (Performer)",
    "John Le Mesurier (Performer)",
    "Simon Cadell (Performer)",
    "Ian Holm (Performer)",
    "Michael Hordern (Performer)"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Fantasy"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "October 7, 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17871169W",
   "id_goodreads": [
    "15347"
   ],
   "publisher": [
    "BBC Audiobooks"
   ],
   "last_modified_i": 1527105407,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "cover_edition_key": "OL7852600M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL10636627M"
   ],
   "cover_i": 2520233,
   "isbn": [
    "0563494859",
    "9780563494850"
   ],
   "has_fulltext": false,
   "text": [
    "OL10636627M",
    "0563494859",
    "9780563494850",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "53971149",
    "OL26320A",
    "OL475982A",
    "Fantasy",
    "The Lord of the Rings",
    "/works/OL17871171W",
    "BBC Audiobooks",
    "The Lord of the Rings (Radio Collection)",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL10636627M",
    "/works/OL17871171W",
    "/subjects/fantasy",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Fantasy"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "October 6, 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17871171W",
   "id_goodreads": [
    "15369"
   ],
   "publisher": [
    "BBC Audiobooks"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1527105573,
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL10636627M",
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003,
   "oclc": [
    "53971149"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7851753M"
   ],
   "cover_i": 374871,
   "isbn": [
    "0563388129",
    "9780563388128"
   ],
   "has_fulltext": false,
   "text": [
    "OL7851753M",
    "0563388129",
    "9780563388128",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "Stephen Thorne (Performer)",
    "Mesurier John Le (Performer)",
    "Simon Cadell (Performer)",
    "Ian Holm (Performer)",
    "Michael Hordern (Performer)",
    "795498352",
    "OL26320A",
    "OL475982A",
    "Fantasy",
    "The Lord of the Rings",
    "/works/OL17871173W",
    "BBC Audiobooks",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL7851753M",
    "/works/OL17871173W",
    "/subjects/fantasy",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "oclc": [
    "795498352"
   ],
   "contributor": [
    "Stephen Thorne (Performer)",
    "Mesurier John Le (Performer)",
    "Simon Cadell (Performer)",
    "Ian Holm (Performer)",
    "Michael Hordern (Performer)"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Fantasy"
   ],
   "title": "The Lord of the Rings",
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17871173W",
   "id_goodreads": [
    "15306"
   ],
   "publisher": [
    "BBC Audiobooks"
   ],
   "last_modified_i": 1527105727,
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL7851753M",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "publish_date": [
    "1995 October 9"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "publisher": [
    "BBC Books"
   ],
   "edition_key": [
    "OL7852249M"
   ],
   "isbn": [
    "0563496134",
    "9780563496137"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "oclc": [
    "51859693"
   ],
   "last_modified_i": 1527105986,
   "title": "The Lord of the Rings",
   "id_librarything": [
    "636553"
   ],
   "seed": [
    "/books/OL7852249M",
    "/works/OL7852249M",
    "/subjects/fantasy_-_general",
    "/subjects/unabridged_audio_-_fiction/general"
   ],
   "first_publish_year": 2003,
   "publish_year": [
    2003
   ],
   "key": "/works/OL7852249M",
   "text": [
    "OL7852249M",
    "0563496134",
    "9780563496137",
    "51859693",
    "Fantasy - General",
    "Unabridged Audio - Fiction/General",
    "Radio Dramatization",
    "The Lord of the Rings",
    "/works/OL7852249M",
    "BBC Books"
   ],
   "id_goodreads": [
    "2582657"
   ],
   "publish_date": [
    "January 2003"
   ],
   "subject": [
    "Fantasy - General",
    "Unabridged Audio - Fiction/General"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "publisher": [
    "BBC Audiobooks"
   ],
   "isbn": [
    "0563209828",
    "9780563209829"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "edition_key": [
    "OL7851256M"
   ],
   "last_modified_i": 1527105299,
   "title": "The Lord of the Rings",
   "id_librarything": [
    "636553"
   ],
   "cover_edition_key": "OL7851256M",
   "seed": [
    "/books/OL7851256M",
    "/works/OL7851256M",
    "/subjects/fantasy"
   ],
   "publish_date": [
    "1991 October 7"
   ],
   "key": "/works/OL7851256M",
   "text": [
    "OL7851256M",
    "0563209828",
    "9780563209829",
    "Fantasy",
    "The Lord of the Rings",
    "/works/OL7851256M",
    "BBC Audiobooks"
   ],
   "id_goodreads": [
    "899736"
   ],
   "subject": [
    "Fantasy"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7851256M"
   ],
   "cover_i": 374616,
   "isbn": [
    "0563209828",
    "9780563209829"
   ],
   "has_fulltext": false,
   "text": [
    "OL7851256M",
    "0563209828",
    "9780563209829",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "OL26320A",
    "OL475982A",
    "Fantasy",
    "The Lord of the Rings",
    "/works/OL17871168W",
    "BBC Audiobooks",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL7851256M",
    "/works/OL17871168W",
    "/subjects/fantasy",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Fantasy"
   ],
   "title": "The Lord of the Rings",
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17871168W",
   "id_goodreads": [
    "899736"
   ],
   "publisher": [
    "BBC Audiobooks"
   ],
   "last_modified_i": 1527105291,
   "id_librarything": [
    "636553"
   ],
   "cover_edition_key": "OL7851256M",
   "publish_date": [
    "1991 October 7"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings",
   "edition_key": [
    "OL7852249M"
   ],
   "isbn": [
    "0563496134",
    "9780563496137"
   ],
   "has_fulltext": false,
   "text": [
    "OL7852249M",
    "0563496134",
    "9780563496137",
    "J. R. R. Tolkien",
    "Brian Sibley",
    "51859693",
    "OL26320A",
    "OL475982A",
    "Fantasy - General",
    "Unabridged Audio - Fiction/General",
    "Radio Dramatization",
    "The Lord of the Rings",
    "/works/OL17871177W",
    "BBC Books",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "seed": [
    "/books/OL7852249M",
    "/works/OL17871177W",
    "/subjects/fantasy_-_general",
    "/subjects/unabridged_audio_-_fiction/general",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "subject": [
    "Fantasy - General",
    "Unabridged Audio - Fiction/General"
   ],
   "title": "The Lord of the Rings",
   "publish_date": [
    "January 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL17871177W",
   "id_goodreads": [
    "2582657"
   ],
   "publisher": [
    "BBC Books"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1527106006,
   "id_librarything": [
    "636553"
   ],
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003,
   "oclc": [
    "51859693"
   ]
  },
  {
   "title_suggest": "The Lord of the Rings Trilogy (Lord of the Rings)",
   "publisher": [
    "Cedco Publishing Company"
   ],
   "isbn": [
    "0768370191",
    "9780768370195"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL8065495M"
   ],
   "last_modified_i": 1419575914,
   "title": "The Lord of the Rings Trilogy (Lord of the Rings)",
   "id_librarything": [
    "1386651"
   ],
   "cover_edition_key": "OL8065495M",
   "seed": [
    "/books/OL8065495M",
    "/works/OL8065495M",
    "/subjects/stationery_items",
    "/subjects/non-classifiable",
    "/subjects/calendars_-_personalities_&_entertainment",
    "/subjects/calendar",
    "/subjects/film_&_video_-_general"
   ],
   "first_publish_year": 2004,
   "publish_year": [
    2004
   ],
   "key": "/works/OL8065495M",
   "text": [
    "OL8065495M",
    "0768370191",
    "9780768370195",
    "The Lord of the Rings Trilogy (Lord of the Rings)",
    "Calendars - Personalities & Entertainment",
    "Stationery items",
    "Non-Classifiable",
    "Calendar",
    "Film & Video - General",
    "/works/OL8065495M",
    "Cedco Publishing Company"
   ],
   "publish_date": [
    "September 2004"
   ],
   "subject": [
    "Calendars - Personalities & Entertainment",
    "Stationery items",
    "Non-Classifiable",
    "Calendar",
    "Film & Video - General"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Rings Instrumental",
   "edition_key": [
    "OL10872494M",
    "OL8005697M",
    "OL9377247M"
   ],
   "cover_i": 2601070,
   "isbn": [
    "9780757923265",
    "9780757923289",
    "0757923267",
    "0757923275",
    "9780757923272",
    "0757923283"
   ],
   "has_fulltext": false,
   "text": [
    "OL10872494M",
    "OL8005697M",
    "OL9377247M",
    "9780757923265",
    "9780757923289",
    "0757923267",
    "0757923275",
    "9780757923272",
    "0757923283",
    "Howard Shore",
    "OL2834626A",
    "Horn in F (Book & CD)",
    "Piano Accompaniment (Book & CD)",
    "Trombone (Book & CD)",
    "Lord of the Rings Instrumental",
    "/works/OL8488047W",
    "Warner Bros. Publications"
   ],
   "author_name": [
    "Howard Shore"
   ],
   "seed": [
    "/books/OL10872494M",
    "/books/OL8005697M",
    "/books/OL9377247M",
    "/works/OL8488047W",
    "/authors/OL2834626A"
   ],
   "author_key": [
    "OL2834626A"
   ],
   "title": "Lord of the Rings Instrumental",
   "publish_date": [
    "August 2004"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 3,
   "key": "/works/OL8488047W",
   "id_goodreads": [
    "2091050",
    "2054334",
    "840091"
   ],
   "publisher": [
    "Warner Bros. Publications"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1282020078,
   "id_librarything": [
    "3033505",
    "1839597"
   ],
   "cover_edition_key": "OL10872494M",
   "publish_year": [
    2004
   ],
   "first_publish_year": 2004
  },
  {
   "title_suggest": "The Lord of the Rings",
   "cover_i": 510582,
   "subtitle": "The Fellowship of the Ring",
   "has_fulltext": false,
   "title": "The Lord of the Rings",
   "last_modified_i": 1525329011,
   "edition_count": 0,
   "author_name": [
    "Mark Cohen"
   ],
   "seed": [
    "/works/OL8456213W",
    "/authors/OL2821360A"
   ],
   "key": "/works/OL8456213W",
   "text": [
    "The Fellowship of the Ring",
    "Mark Cohen",
    "OL2821360A",
    "The Lord of the Rings",
    "/works/OL8456213W"
   ],
   "author_key": [
    "OL2821360A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1525338294,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL14926061W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL14926061W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL14926061W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "cover_i": -1,
   "has_fulltext": false,
   "title": "The Lord of the Rings",
   "last_modified_i": 1527105234,
   "edition_count": 0,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL262744W",
    "/authors/OL26320A",
    "/authors/OL475982A"
   ],
   "author_name": [
    "J. R. R. Tolkien",
    "Brian Sibley"
   ],
   "key": "/works/OL262744W",
   "text": [
    "J. R. R. Tolkien",
    "Brian Sibley",
    "OL26320A",
    "OL475982A",
    "The Lord of the Rings",
    "/works/OL262744W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A",
    "OL475982A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1526747108,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL12644217W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL12644217W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL12644217W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "cover_i": 980436,
   "has_fulltext": false,
   "title": "The Lord of the Rings",
   "last_modified_i": 1526747392,
   "edition_count": 0,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL14933493W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL14933493W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL14933493W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "cover_i": -1,
   "has_fulltext": false,
   "title": "The Lord of the Rings",
   "last_modified_i": 1527932070,
   "edition_count": 0,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL27493W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL27493W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL27493W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1527931875,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL16245358W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL16245358W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL16245358W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1527931594,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL16290346W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL16290346W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL16290346W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1527931659,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL16290339W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL16290339W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL16290339W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1527931789,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL16245365W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL16245365W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL16245365W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "has_fulltext": false,
   "edition_count": 0,
   "last_modified_i": 1527931936,
   "title": "The Lord of the Rings",
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL15331185W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL15331185W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL15331185W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "The Lord of the Rings",
   "cover_i": -1,
   "has_fulltext": false,
   "title": "The Lord of the Rings",
   "last_modified_i": 1527931514,
   "edition_count": 0,
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "seed": [
    "/works/OL15333183W",
    "/authors/OL26320A"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "key": "/works/OL15333183W",
   "text": [
    "J. R. R. Tolkien",
    "OL26320A",
    "The Lord of the Rings",
    "/works/OL15333183W",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Realm of the Ring Lord",
   "edition_key": [
    "OL74386M",
    "OL12268325M"
   ],
   "cover_i": 3045951,
   "isbn": [
    "1903773075",
    "9781903773079"
   ],
   "has_fulltext": false,
   "text": [
    "OL74386M",
    "OL12268325M",
    "1903773075",
    "9781903773079",
    "Laurence Gardner",
    "40482380",
    "OL50039A",
    "Lecture",
    "lettura junghiana di alcuni film d'autore",
    "Realm of the Ring Lord",
    "Andrea Enrile.",
    "Motion pictures",
    "Psychological aspects of Motion pictures",
    "Psychological aspects",
    "/works/OL646325W",
    "MediaQuest",
    "Minotauro",
    "Interiors",
    "99175960"
   ],
   "author_name": [
    "Laurence Gardner"
   ],
   "seed": [
    "/books/OL74386M",
    "/books/OL12268325M",
    "/works/OL646325W",
    "/subjects/motion_pictures",
    "/subjects/psychological_aspects",
    "/subjects/psychological_aspects_of_motion_pictures",
    "/authors/OL50039A"
   ],
   "oclc": [
    "40482380"
   ],
   "author_key": [
    "OL50039A"
   ],
   "subject": [
    "Motion pictures",
    "Psychological aspects of Motion pictures",
    "Psychological aspects"
   ],
   "title": "Realm of the Ring Lord",
   "publish_date": [
    "1998",
    "October 2001"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "publish_place": [
    "Roma"
   ],
   "edition_count": 2,
   "key": "/works/OL646325W",
   "id_goodreads": [
    "489110"
   ],
   "publisher": [
    "MediaQuest",
    "Minotauro"
   ],
   "language": [
    "ita"
   ],
   "lccn": [
    "99175960"
   ],
   "last_modified_i": 1291450942,
   "cover_edition_key": "OL12268325M",
   "publish_year": [
    1998,
    2001
   ],
   "first_publish_year": 1998
  },
  {
   "title_suggest": "Gollum (\"Lord of the Rings\")",
   "edition_key": [
    "OL9217767M",
    "OL7263052M"
   ],
   "cover_i": 11903,
   "isbn": [
    "9780007170579",
    "0007170572"
   ],
   "has_fulltext": false,
   "text": [
    "OL9217767M",
    "OL7263052M",
    "9780007170579",
    "0007170572",
    "Andy Serkis",
    "OL1400080A",
    "Gollum (\"Lord of the Rings\")",
    "/works/OL5754682W",
    "Collins"
   ],
   "author_name": [
    "Andy Serkis"
   ],
   "seed": [
    "/books/OL9217767M",
    "/books/OL7263052M",
    "/works/OL5754682W",
    "/authors/OL1400080A"
   ],
   "author_key": [
    "OL1400080A"
   ],
   "title": "Gollum (\"Lord of the Rings\")",
   "publish_date": [
    "December 1, 2003"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 2,
   "key": "/works/OL5754682W",
   "id_goodreads": [
    "477217"
   ],
   "publisher": [
    "Collins"
   ],
   "last_modified_i": 1281577706,
   "id_librarything": [
    "5792"
   ],
   "cover_edition_key": "OL9217767M",
   "publish_year": [
    2003
   ],
   "first_publish_year": 2003
  },
  {
   "title_suggest": "The Fellowship of the Ring",
   "edition_key": [
    "OL26452664M",
    "OL26452607M",
    "OL26452599M",
    "OL26452593M",
    "OL26452273M",
    "OL9131988M",
    "OL24591555M",
    "OL9179424M",
    "OL8171920M",
    "OL8890485M",
    "OL11037701M",
    "OL8890402M",
    "OL9595965M",
    "OL9076585M",
    "OL9076577M",
    "OL9137998M",
    "OL8890347M",
    "OL7603917M",
    "OL8840001M",
    "OL9131874M",
    "OL10686522M",
    "OL12034181M",
    "OL9076610M",
    "OL8171839M",
    "OL8889789M",
    "OL9678816M",
    "OL26450211M",
    "OL26450210M",
    "OL26450140M",
    "OL26450127M",
    "OL26450126M",
    "OL11346299M",
    "OL10684788M",
    "OL26450096M",
    "OL26449842M",
    "OL26449841M",
    "OL26449840M",
    "OL9131846M",
    "OL26449483M",
    "OL26449482M",
    "OL26449477M",
    "OL26449390M",
    "OL26449194M",
    "OL26449186M",
    "OL26449183M",
    "OL26449168M",
    "OL26448812M",
    "OL10236417M",
    "OL10236387M",
    "OL10681986M",
    "OL10681593M",
    "OL10682347M",
    "OL24206969M",
    "OL10682854M",
    "OL8969576M",
    "OL26448808M",
    "OL22266040M",
    "OL26448814M",
    "OL26449207M",
    "OL26448821M",
    "OL26449212M",
    "OL26449227M",
    "OL26449226M",
    "OL26449223M",
    "OL15350842M",
    "OL7465583M",
    "OL21428276M",
    "OL24212887M",
    "OL26449244M",
    "OL26452621M",
    "OL26449391M",
    "OL22835039M",
    "OL26449741M",
    "OL26449484M",
    "OL10682513M",
    "OL7591509M",
    "OL13893006M",
    "OL26449833M",
    "OL20943864M",
    "OL25209450M",
    "OL26449215M",
    "OL22837887M",
    "OL13103887M",
    "OL21485714M",
    "OL3828014M",
    "OL3848658M",
    "OL7466031M",
    "OL26450095M",
    "OL26449826M",
    "OL20942846M",
    "OL26449213M",
    "OL26450100M",
    "OL24373119M",
    "OL26450214M",
    "OL26159487M",
    "OL2083847M",
    "OL2082346M",
    "OL7465858M",
    "OL18299598M",
    "OL9370678M",
    "OL25966404M",
    "OL26450218M",
    "OL18928910M",
    "OL7467153M",
    "OL21478444M",
    "OL26450477M",
    "OL26450216M",
    "OL26452620M",
    "OL26452600M",
    "OL26452256M",
    "OL20784407M",
    "OL26450482M",
    "OL23077320M",
    "OL8889882M",
    "OL26450490M",
    "OL17238263M",
    "OL9076659M",
    "OL19685717M",
    "OL23124795M",
    "OL10236390M",
    "OL22814360M",
    "OL24584294M",
    "OL11461843M",
    "OL8171979M",
    "OL22106804M",
    "OL23097541M",
    "OL26451577M",
    "OL26451576M",
    "OL22054291M",
    "OL7261494M",
    "OL9216209M",
    "OL13320799M",
    "OL7261842M",
    "OL9216557M",
    "OL22469028M",
    "OL8529332M",
    "OL3969872M",
    "OL20932268M",
    "OL13569251M",
    "OL24206968M",
    "OL24737100M",
    "OL23041688M",
    "OL25483585M",
    "OL9158225M",
    "OL19112575M",
    "OL22050938M",
    "OL18905181M",
    "OL9149754M",
    "OL26383768M",
    "OL3777336M",
    "OL24374179M",
    "OL26451900M",
    "OL26451897M",
    "OL26450093M",
    "OL22069376M",
    "OL3682825M",
    "OL26452611M",
    "OL12541182M",
    "OL7605824M",
    "OL26451924M",
    "OL24298430M",
    "OL24293296M",
    "OL24281996M",
    "OL25420485M",
    "OL26452597M",
    "OL26452618M",
    "OL26452617M",
    "OL26384839M",
    "OL26450094M",
    "OL26452619M",
    "OL26452624M",
    "OL26452610M"
   ],
   "cover_i": 8200821,
   "isbn": [
    "8533615558",
    "0007171978",
    "3608107134",
    "9780261102354",
    "0808520768",
    "9780345332080",
    "9706906517",
    "9780007123827",
    "0618129030",
    "8202336406",
    "9027401683",
    "9780458907502",
    "9780395647387",
    "9789536166114",
    "9782070515790",
    "9780007488315",
    "0048231126",
    "9780828868990",
    "3608955364",
    "9780261102316",
    "0345008626",
    "0618260269",
    "0061952834",
    "9780345253439",
    "9460235301",
    "061826051X",
    "9780048231857",
    "1500410225",
    "9780547928210",
    "0345247868",
    "9780544448933",
    "9780061917677",
    "0965307751",
    "6020332268",
    "9780007149216",
    "0785907424",
    "8845290409",
    "0618002227",
    "8702093693",
    "9780345247865",
    "0544448936",
    "9782266070614",
    "000712970X",
    "004823155X",
    "9780061917684",
    "0345248279",
    "9789632809632",
    "9780618260515",
    "0345332083",
    "9780395312674",
    "0345253434",
    "9783899408867",
    "9780345015334",
    "9780965307758",
    "3608939814",
    "0786251786",
    "9632809637",
    "9780618002221",
    "9788483026830",
    "0828839816",
    "9780618153985",
    "360893541X",
    "9780788739576",
    "0061917680",
    "0395312671",
    "9785170264155",
    "9780788789816",
    "9780007171972",
    "0828810540",
    "9780345008626",
    "2266046497",
    "9780618134694",
    "0261102923",
    "8445071408",
    "2266128043",
    "9788533615557",
    "9782266115612",
    "1850894140",
    "0061917672",
    "9780345917430",
    "9788702093698",
    "3608933514",
    "9789753421638",
    "039564738X",
    "9789570823363",
    "9788439596196",
    "8439596197",
    "9780345339706",
    "9788445070338",
    "1556903219",
    "848302683X",
    "9780345296054",
    "9789706906519",
    "9782070612888",
    "2266120999",
    "0345015339",
    "9780061952838",
    "2070515796",
    "9780345248275",
    "9788439596189",
    "0606006508",
    "9783608934014",
    "8445000667",
    "9780618260263",
    "0828868999",
    "9789505470679",
    "0007488319",
    "9781594130076",
    "9780812415582",
    "0007123825",
    "9780048231550",
    "0345296052",
    "9782266107983",
    "8439596189",
    "9780261103573",
    "3899408861",
    "9783608955361",
    "9788580631012",
    "9788445071403",
    "8580631017",
    "9783608939811",
    "9780048230454",
    "9781850894148",
    "9505470673",
    "975342163X",
    "9780395082546",
    "9780395272237",
    "9789027401687",
    "0618574948",
    "9570823364",
    "9781500410223",
    "0261102354",
    "9788445075739",
    "2070612880",
    "3608934014",
    "9780828865654",
    "0048230456",
    "0261103571",
    "9780606006507",
    "0458907502",
    "8445070339",
    "0007149212",
    "9780786251780",
    "9780007129706",
    "9780606244237",
    "0812415582",
    "9780345272584",
    "0395489318",
    "9780828839815",
    "9782266046497",
    "146183614X",
    "9780345240323",
    "9536166119",
    "9780808520764",
    "8673480671",
    "9782266128049",
    "0788789813",
    "9780007117116",
    "9788202336400",
    "9780345215338",
    "0606244239",
    "0345240324",
    "0618134697",
    "034591743X",
    "0345235096",
    "9789721041028",
    "0618153985",
    "9783608952124",
    "9788673480671",
    "0547928211",
    "9780048231123",
    "0007322496",
    "8371502419",
    "9788845290404",
    "9780618574940",
    "844507573X",
    "0395082544",
    "0345272587",
    "9781556903212",
    "1594130078",
    "9788371502415",
    "9780618129034",
    "2266070614",
    "2266115618",
    "9780261102927",
    "0261102311",
    "0345215338",
    "953-6166-11-9",
    "0345339703",
    "9788445000663",
    "9782266120999",
    "978-2070612888",
    "5170264151",
    "9780395489314",
    "9786020332260",
    "9780007322497",
    "0048231851",
    "0788739573",
    "9783608107135",
    "9783608933512",
    "9780785907428",
    "9789460235306",
    "9780828810548",
    "0345020200",
    "9783608935417",
    "9780345235091",
    "0828865655",
    "0395272238",
    "9721041025",
    "3608952128",
    "9781461836148",
    "0007117116",
    "9780345020208",
    "2266107984"
   ],
   "has_fulltext": true,
   "id_dep\u00f3sito_legal": [
    "NA8962002"
   ],
   "text": [
    "OL26452664M",
    "OL26452607M",
    "OL26452599M",
    "OL26452593M",
    "OL26452273M",
    "OL9131988M",
    "OL24591555M",
    "OL9179424M",
    "OL8171920M",
    "OL8890485M",
    "OL11037701M",
    "OL8890402M",
    "OL9595965M",
    "OL9076585M",
    "OL9076577M",
    "OL9137998M",
    "OL8890347M",
    "OL7603917M",
    "OL8840001M",
    "OL9131874M",
    "OL10686522M",
    "OL12034181M",
    "OL9076610M",
    "OL8171839M",
    "OL8889789M",
    "OL9678816M",
    "OL26450211M",
    "OL26450210M",
    "OL26450140M",
    "OL26450127M",
    "OL26450126M",
    "OL11346299M",
    "OL10684788M",
    "OL26450096M",
    "OL26449842M",
    "OL26449841M",
    "OL26449840M",
    "OL9131846M",
    "OL26449483M",
    "OL26449482M",
    "OL26449477M",
    "OL26449390M",
    "OL26449194M",
    "OL26449186M",
    "OL26449183M",
    "OL26449168M",
    "OL26448812M",
    "OL10236417M",
    "OL10236387M",
    "OL10681986M",
    "OL10681593M",
    "OL10682347M",
    "OL24206969M",
    "OL10682854M",
    "OL8969576M",
    "OL26448808M",
    "OL22266040M",
    "OL26448814M",
    "OL26449207M",
    "OL26448821M",
    "OL26449212M",
    "OL26449227M",
    "OL26449226M",
    "OL26449223M",
    "OL15350842M",
    "OL7465583M",
    "OL21428276M",
    "OL24212887M",
    "OL26449244M",
    "OL26452621M",
    "OL26449391M",
    "OL22835039M",
    "OL26449741M",
    "OL26449484M",
    "OL10682513M",
    "OL7591509M",
    "OL13893006M",
    "OL26449833M",
    "OL20943864M",
    "OL25209450M",
    "OL26449215M",
    "OL22837887M",
    "OL13103887M",
    "OL21485714M",
    "OL3828014M",
    "OL3848658M",
    "OL7466031M",
    "OL26450095M",
    "OL26449826M",
    "OL20942846M",
    "OL26449213M",
    "OL26450100M",
    "OL24373119M",
    "OL26450214M",
    "OL26159487M",
    "OL2083847M",
    "OL2082346M",
    "OL7465858M",
    "OL18299598M",
    "OL9370678M",
    "OL25966404M",
    "OL26450218M",
    "OL18928910M",
    "OL7467153M",
    "OL21478444M",
    "OL26450477M",
    "OL26450216M",
    "OL26452620M",
    "OL26452600M",
    "OL26452256M",
    "OL20784407M",
    "OL26450482M",
    "OL23077320M",
    "OL8889882M",
    "OL26450490M",
    "OL17238263M",
    "OL9076659M",
    "OL19685717M",
    "OL23124795M",
    "OL10236390M",
    "OL22814360M",
    "OL24584294M",
    "OL11461843M",
    "OL8171979M",
    "OL22106804M",
    "OL23097541M",
    "OL26451577M",
    "OL26451576M",
    "OL22054291M",
    "OL7261494M",
    "OL9216209M",
    "OL13320799M",
    "OL7261842M",
    "OL9216557M",
    "OL22469028M",
    "OL8529332M",
    "OL3969872M",
    "OL20932268M",
    "OL13569251M",
    "OL24206968M",
    "OL24737100M",
    "OL23041688M",
    "OL25483585M",
    "OL9158225M",
    "OL19112575M",
    "OL22050938M",
    "OL18905181M",
    "OL9149754M",
    "OL26383768M",
    "OL3777336M",
    "OL24374179M",
    "OL26451900M",
    "OL26451897M",
    "OL26450093M",
    "OL22069376M",
    "OL3682825M",
    "OL26452611M",
    "OL12541182M",
    "OL7605824M",
    "OL26451924M",
    "OL24298430M",
    "OL24293296M",
    "OL24281996M",
    "OL25420485M",
    "OL26452597M",
    "OL26452618M",
    "OL26452617M",
    "OL26384839M",
    "OL26450094M",
    "OL26452619M",
    "OL26452624M",
    "OL26452610M",
    "8533615558",
    "0007171978",
    "3608107134",
    "9780261102354",
    "0808520768",
    "9780345332080",
    "9706906517",
    "9780007123827",
    "0618129030",
    "8202336406",
    "9027401683",
    "9780458907502",
    "9780395647387",
    "9789536166114",
    "9782070515790",
    "9780007488315",
    "0048231126",
    "9780828868990",
    "3608955364",
    "9780261102316",
    "0345008626",
    "0618260269",
    "0061952834",
    "9780345253439",
    "9460235301",
    "061826051X",
    "9780048231857",
    "1500410225",
    "9780547928210",
    "0345247868",
    "9780544448933",
    "9780061917677",
    "0965307751",
    "6020332268",
    "9780007149216",
    "0785907424",
    "8845290409",
    "0618002227",
    "8702093693",
    "9780345247865",
    "0544448936",
    "9782266070614",
    "000712970X",
    "004823155X",
    "9780061917684",
    "0345248279",
    "9789632809632",
    "9780618260515",
    "0345332083",
    "9780395312674",
    "0345253434",
    "9783899408867",
    "9780345015334",
    "9780965307758",
    "3608939814",
    "0786251786",
    "9632809637",
    "9780618002221",
    "9788483026830",
    "0828839816",
    "9780618153985",
    "360893541X",
    "9780788739576",
    "0061917680",
    "0395312671",
    "9785170264155",
    "9780788789816",
    "9780007171972",
    "0828810540",
    "9780345008626",
    "2266046497",
    "9780618134694",
    "0261102923",
    "8445071408",
    "2266128043",
    "9788533615557",
    "9782266115612",
    "1850894140",
    "0061917672",
    "9780345917430",
    "9788702093698",
    "3608933514",
    "9789753421638",
    "039564738X",
    "9789570823363",
    "9788439596196",
    "8439596197",
    "9780345339706",
    "9788445070338",
    "1556903219",
    "848302683X",
    "9780345296054",
    "9789706906519",
    "9782070612888",
    "2266120999",
    "0345015339",
    "9780061952838",
    "2070515796",
    "9780345248275",
    "9788439596189",
    "0606006508",
    "9783608934014",
    "8445000667",
    "9780618260263",
    "0828868999",
    "9789505470679",
    "0007488319",
    "9781594130076",
    "9780812415582",
    "0007123825",
    "9780048231550",
    "0345296052",
    "9782266107983",
    "8439596189",
    "9780261103573",
    "3899408861",
    "9783608955361",
    "9788580631012",
    "9788445071403",
    "8580631017",
    "9783608939811",
    "9780048230454",
    "9781850894148",
    "9505470673",
    "975342163X",
    "9780395082546",
    "9780395272237",
    "9789027401687",
    "0618574948",
    "9570823364",
    "9781500410223",
    "0261102354",
    "9788445075739",
    "2070612880",
    "3608934014",
    "9780828865654",
    "0048230456",
    "0261103571",
    "9780606006507",
    "0458907502",
    "8445070339",
    "0007149212",
    "9780786251780",
    "9780007129706",
    "9780606244237",
    "0812415582",
    "9780345272584",
    "0395489318",
    "9780828839815",
    "9782266046497",
    "146183614X",
    "9780345240323",
    "9536166119",
    "9780808520764",
    "8673480671",
    "9782266128049",
    "0788789813",
    "9780007117116",
    "9788202336400",
    "9780345215338",
    "0606244239",
    "0345240324",
    "0618134697",
    "034591743X",
    "0345235096",
    "9789721041028",
    "0618153985",
    "9783608952124",
    "9788673480671",
    "0547928211",
    "9780048231123",
    "0007322496",
    "8371502419",
    "9788845290404",
    "9780618574940",
    "844507573X",
    "0395082544",
    "0345272587",
    "9781556903212",
    "1594130078",
    "9788371502415",
    "9780618129034",
    "2266070614",
    "2266115618",
    "9780261102927",
    "0261102311",
    "0345215338",
    "953-6166-11-9",
    "0345339703",
    "9788445000663",
    "9782266120999",
    "978-2070612888",
    "5170264151",
    "9780395489314",
    "9786020332260",
    "9780007322497",
    "0048231851",
    "0788739573",
    "9783608107135",
    "9783608933512",
    "9780785907428",
    "9789460235306",
    "9780828810548",
    "0345020200",
    "9783608935417",
    "9780345235091",
    "0828865655",
    "0395272238",
    "9721041025",
    "3608952128",
    "9781461836148",
    "0007117116",
    "9780345020208",
    "2266107984",
    "J. R. R. Tolkien",
    "Somay, B\u00fclent.",
    "Ipek, \u00c7igdem Erkal.",
    "Fraser, Eric.",
    "Grathmer, Ingahild.",
    "Tolkien, J. R. R. 1892-1973.",
    "Zhu, Xueheng.",
    "Carroux, Margaret.",
    "Alan Lee (Illustrator)",
    "Lee, Alan.",
    "Moises Rodriguez Barcia (Translator)",
    "492489392",
    "874884502",
    "495926805",
    "59462836",
    "28820516",
    "813678154",
    "60198264",
    "859858656",
    "962899321",
    "925375894",
    "969606359",
    "1005936675",
    "892147306",
    "892822609",
    "12783233",
    "26074760",
    "53354229",
    "804341872",
    "473660275",
    "985367714",
    "490916277",
    "908106356",
    "866921295",
    "69306984",
    "314934465",
    "847522557",
    "1023784421",
    "891929385",
    "20911014",
    "608811797",
    "264943675",
    "867941362",
    "879331252",
    "863419832",
    "491629977",
    "858006243",
    "656925950",
    "972120209",
    "868151445",
    "1028304305",
    "59806314",
    "222286517",
    "800851830",
    "173617998",
    "221359042",
    "859053085",
    "840313694",
    "491308716",
    "644361719",
    "401668875",
    "28576179",
    "642408746",
    "5983481",
    "39786673",
    "818844233",
    "689998836",
    "422011972",
    "956677518",
    "1028428830",
    "828327601",
    "988608157",
    "441105273",
    "276705178",
    "1031627083",
    "59304971",
    "494437348",
    "300294295",
    "965313612",
    "50575811",
    "31385993",
    "840923271",
    "473321979",
    "999800269",
    "769331264",
    "59814092",
    "33231212",
    "690513322",
    "1003689208",
    "441644416",
    "973591950",
    "458615282",
    "18291996",
    "495787648",
    "812770728",
    "934791596",
    "887434322",
    "733661501",
    "265243763",
    "223368847",
    "955830033",
    "608874150",
    "813328089",
    "940043845",
    "924759492",
    "6801190",
    "733845192",
    "723113405",
    "51898813",
    "48034705",
    "50880827",
    "315256208",
    "820529069",
    "680126005",
    "679748755",
    "60788362",
    "718006258",
    "473636432",
    "671818954",
    "873088483",
    "401524066",
    "41736747",
    "38493843",
    "877421571",
    "869828061",
    "490283396",
    "936043149",
    "819931671",
    "1028305395",
    "76820597",
    "558815281",
    "832974849",
    "762217299",
    "925000280",
    "49652808",
    "993953990",
    "185439182",
    "812629789",
    "760005887",
    "71756740",
    "223428261",
    "438323741",
    "436317500",
    "39031400",
    "963195864",
    "779162993",
    "317867795",
    "59549292",
    "999367006",
    "473798507",
    "438980186",
    "1023727818",
    "889581762",
    "671852341",
    "69654933",
    "63157893",
    "473251806",
    "48863478",
    "228444755",
    "650243225",
    "278019019",
    "1014283774",
    "48896366",
    "33034923",
    "751933468",
    "68389399",
    "52828988",
    "48034344",
    "59483583",
    "473191796",
    "440837776",
    "742807522",
    "48491076",
    "493357569",
    "906673187",
    "222929817",
    "51652816",
    "432702929",
    "884060681",
    "1098874",
    "972118943",
    "491677922",
    "613265489",
    "810453057",
    "49597495",
    "22366207",
    "473216878",
    "60658001",
    "861657097",
    "148822151",
    "1005270888",
    "932188442",
    "931784385",
    "906720636",
    "51782682",
    "1028386230",
    "12228601",
    "1133027",
    "60598951",
    "416287693",
    "911216759",
    "918598176",
    "244128644",
    "780027833",
    "221067788",
    "773759305",
    "407039470",
    "810481073",
    "1027685857",
    "46387665",
    "441192718",
    "1035694988",
    "906893207",
    "fellowshipofring00tolk",
    "fellowshipofringtol00tolk",
    "lordofrings00jrrt",
    "fellowshipofring1973tolk",
    "elsenordelosanil00jrrt",
    "fellowshipofring01tolk",
    "fellowshipofring00tolkrich",
    "lordofrings00tolk",
    "mojieshoubuqumoj00tolk",
    "lordofringsco00jrrt",
    "fellowshipofrin00tolk",
    "isbn_9780965307758",
    "twotowersbeingse00tolk_0",
    "fellowshipofring00jrrt",
    "fellowshipofring00tolk_0",
    "OL26320A",
    "English Fantasy fiction",
    "In library",
    "Popular Print Disabled Books",
    "Open Library Staff Picks",
    "Accessible book",
    "The Lord of the Rings",
    "Fantastic fiction",
    "Fiction",
    "Fantasy",
    "Fantasy fiction",
    "Fairy tales",
    "adventure fiction",
    "Adventure stories",
    "Protected DAISY",
    "Ficci\u00f3n fant\u00e1stica inglesa",
    "Large type books",
    "Ficci\u00f3n",
    "Internet Archive Wishlist",
    "Being The First Part of the Lord of the Rings",
    "Being the First Part of The Lord of the Rings",
    "Being the First Part of the Lord of the Rings",
    "Sembilan Pembawa Cincin",
    "Being the first part of The Lord of the Rings",
    "being the first part of The Lord of the Rings",
    "\u9b54\u6212\u73fe\u8eab",
    "Prstenova dru\u017eina",
    "The Fellowship of the Ring",
    "/works/OL15331214W",
    "J. R. R. Tolkien zhu ; Alan Lee tu ; Zhu Xueheng yi.",
    "J.R.R. Tolkien ; with a new foreword by the author",
    "J. R. R. Tolkien ; Inglilizce'den \u00c7eviren: \u00c7igdem Erkal Ipek ; Siir \u00c7evirileri: B\u00fclent Somay. Birinci Kisim, Y\u00fcz\u00fck Kardesligi.",
    "J.R.R. Tolkien ; [aus dem Englischen \u00fcbersetzt von Margaret Carroux].",
    "with a new foreward by the author J.R.R. Tolkien",
    "J.R.R. Tolkien ; illustrated by Alan Lee.",
    "with a new foreword by the author, J.R.R. Tolkien.",
    "by J.R.R. Tolkien.",
    "by J.R.R. Tolkien",
    "by J. R. R. Tolkien.",
    "(by) J.R.R. Tolkien.",
    "traduit de l'anglais par F. Ledoux.",
    "illustrations by Ingahild Grathmer ; drawn by Eric Fraser.",
    "J.R.R. Tolkien",
    "J. R. R. Tolkien.",
    "Klett-Cotta",
    "French & European Pubns",
    "Gallimard Jeunesse",
    "Harper",
    "Allen & Unwin",
    "Houghton Mifflin Company",
    "Grafton",
    "Folio Society",
    "xx",
    "Houghton Mifflin Co.",
    "Martins Fontes",
    "Easton Press",
    "Collins",
    "Hobbit Presse",
    "George Allen and Unwin",
    "ISIS Large Print Books",
    "Harper Collins",
    "Christian Bourgois",
    "Thorndike Press",
    "Rubikon",
    "Quality Paperback Book Club",
    "AST",
    "Gyldendal Lyd",
    "HarperCollins Publishers Ltd",
    "Der H\u00f6rverlag",
    "Houghton Mifflin",
    "Pocket",
    "Folio Junior",
    "Unwin Books",
    "Del Rey (Random House)",
    "Xerias",
    "Allen and Unwin",
    "Houghton Mifflin Harcourt",
    "J.G. Cotta'sche, Buchhandlung Nachfolger GmbH",
    "Het Spectrum",
    "Ballantine Books",
    "Minotauro",
    "Algoritam",
    "Ace",
    "Zysk i S-ka",
    "Del Rey",
    "Barry Goldstein",
    "Europa-America",
    "Turtleback Books Distributed by Demco Media",
    "Bompiani",
    "Harper-Collins",
    "UITGEVERIJ MEULENHOFF",
    "Recorded Books",
    "Gondolat",
    "George Allen & Unwin",
    "Large Print Press",
    "Metis Yay\u0131nlar\u0131",
    "Linking Publishing",
    "Ballantine Books / Del Rey",
    "Perfection Learning",
    "Ediciones Minotauro",
    "HarperCollins",
    "Unwin Paperbacks",
    "Cappelen Damm Lydbok",
    "Turtleback Books",
    "Del Rey / Ballantine Books",
    "Methuen",
    "harpercollins",
    "Gramedia Pustaka Utama",
    "Ballentine Books",
    "Lian jing chu ban shi ye gong si",
    "HarperCollins Publishers",
    "Magnum Books",
    "Minotaur",
    "Ringens brorskap",
    "Y\u00fcz\u00fck Karde\u015fli\u011fi",
    "\u05d3\u05d9 \u05d7\u05d1\u05e8\u05d5\u05ea\u05d0 \u05e4\u05d5\u05df \u05d3\u05e2\u05dd \u05e4\u05d9\u05e0\u05d2\u05e2\u05e8\u05dc",
    "The Fellowship of The Ring",
    "The lord of the rings",
    "Mo jie xian shen",
    "La Compagnia dell'anello",
    "Khraniteli Kol'tsa",
    "La Comunidad Del Anillo",
    "\u9b54\u6212\u9996\u90e8\u66f2",
    "A Sociedade do Anel",
    "Lord of the rings.",
    "Bractwo pierscienia",
    "Gospodar prstenova (dio prvi)",
    "La Communaut\u00e9 de l'Anneau",
    "De Reisgenoten",
    "A Irmandade do Anel",
    "La compagnia dell'anello",
    "La communaut\u00e9 de l'anneau",
    "La Comunidad del Anillo",
    "Die Gefahrten",
    "Comunidad Anillo",
    "Le Communaute de L'Anneau",
    "The Lord of the Rings, Book 1, The Fellowship of the Rings.",
    "A Gyuru Szovetsege",
    "The fellowship of the ring.",
    "Lord of the rings, pt. 1.",
    "The Fellowship of the ring.",
    "the lord of the rings",
    "La Communeaute de l'Anneau",
    "Dru\u017eina prstena",
    "The Fellowship of the Rings",
    "Die Gef\u00e4hrten",
    "Return of the king",
    "La Communaute de l'Anneau",
    "Eventyret om Ringen",
    "The Lord of the Rings",
    "A sociedade do anel",
    "La Compagnia dell'Anello",
    "La comunidad del anillo",
    "La Communaute de L'Anneaux",
    "Fellowship of the ring.",
    "Mo jie shou bu xu : mo jie xian shen",
    "88120282",
    "2001276576",
    "81166135",
    "2003041673",
    "81139600",
    "67012274",
    "67-12274",
    "67-12275",
    "2003542569",
    "88122831",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein",
    "THIS BOOK is largely concerned with Hobbits, and from its pages a reader may discover much of their character and a little of their history.",
    "This book is largely concerned with Hobbits, and from its pages a reader may discover much of their character and a little of their history.",
    "Sauron",
    "Aragorn (Strider)",
    "Gandalf the Wizard",
    "Frodo Baggins",
    "Elrond",
    "Gimli",
    "Bilbo Baggins",
    "Samwise Gamgee",
    "Legolas",
    "Mordor",
    "Tierra Media",
    "Middle Earth",
    "Before the Age of Men"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "contributor": [
    "Somay, B\u00fclent.",
    "Ipek, \u00c7igdem Erkal.",
    "Fraser, Eric.",
    "Grathmer, Ingahild.",
    "Tolkien, J. R. R. 1892-1973.",
    "Zhu, Xueheng.",
    "Carroux, Margaret.",
    "Alan Lee (Illustrator)",
    "Lee, Alan.",
    "Moises Rodriguez Barcia (Translator)"
   ],
   "ia_loaded_id": [
    "mojieshoubuqumoj00tolk",
    "fellowshipofrin00tolk",
    "fellowshipofring00tolk_0"
   ],
   "seed": [
    "/books/OL26452664M",
    "/books/OL26452607M",
    "/books/OL26452599M",
    "/books/OL26452593M",
    "/books/OL26452273M",
    "/books/OL9131988M",
    "/books/OL24591555M",
    "/books/OL9179424M",
    "/books/OL8171920M",
    "/books/OL8890485M",
    "/books/OL11037701M",
    "/books/OL8890402M",
    "/books/OL9595965M",
    "/books/OL9076585M",
    "/books/OL9076577M",
    "/books/OL9137998M",
    "/books/OL8890347M",
    "/books/OL7603917M",
    "/books/OL8840001M",
    "/books/OL9131874M",
    "/books/OL10686522M",
    "/books/OL12034181M",
    "/books/OL9076610M",
    "/books/OL8171839M",
    "/books/OL8889789M",
    "/books/OL9678816M",
    "/books/OL26450211M",
    "/books/OL26450210M",
    "/books/OL26450140M",
    "/books/OL26450127M",
    "/books/OL26450126M",
    "/books/OL11346299M",
    "/books/OL10684788M",
    "/books/OL26450096M",
    "/books/OL26449842M",
    "/books/OL26449841M",
    "/books/OL26449840M",
    "/books/OL9131846M",
    "/books/OL26449483M",
    "/books/OL26449482M",
    "/books/OL26449477M",
    "/books/OL26449390M",
    "/books/OL26449194M",
    "/books/OL26449186M",
    "/books/OL26449183M",
    "/books/OL26449168M",
    "/books/OL26448812M",
    "/books/OL10236417M",
    "/books/OL10236387M",
    "/books/OL10681986M",
    "/books/OL10681593M",
    "/books/OL10682347M",
    "/books/OL24206969M",
    "/books/OL10682854M",
    "/books/OL8969576M",
    "/books/OL26448808M",
    "/books/OL22266040M",
    "/books/OL26448814M",
    "/books/OL26449207M",
    "/books/OL26448821M",
    "/books/OL26449212M",
    "/books/OL26449227M",
    "/books/OL26449226M",
    "/books/OL26449223M",
    "/books/OL15350842M",
    "/books/OL7465583M",
    "/books/OL21428276M",
    "/books/OL24212887M",
    "/books/OL26449244M",
    "/books/OL26452621M",
    "/books/OL26449391M",
    "/books/OL22835039M",
    "/books/OL26449741M",
    "/books/OL26449484M",
    "/books/OL10682513M",
    "/books/OL7591509M",
    "/books/OL13893006M",
    "/books/OL26449833M",
    "/books/OL20943864M",
    "/books/OL25209450M",
    "/books/OL26449215M",
    "/books/OL22837887M",
    "/books/OL13103887M",
    "/books/OL21485714M",
    "/books/OL3828014M",
    "/books/OL3848658M",
    "/books/OL7466031M",
    "/books/OL26450095M",
    "/books/OL26449826M",
    "/books/OL20942846M",
    "/books/OL26449213M",
    "/books/OL26450100M",
    "/books/OL24373119M",
    "/books/OL26450214M",
    "/books/OL26159487M",
    "/books/OL2083847M",
    "/books/OL2082346M",
    "/books/OL7465858M",
    "/books/OL18299598M",
    "/books/OL9370678M",
    "/books/OL25966404M",
    "/books/OL26450218M",
    "/books/OL18928910M",
    "/books/OL7467153M",
    "/books/OL21478444M",
    "/books/OL26450477M",
    "/books/OL26450216M",
    "/books/OL26452620M",
    "/books/OL26452600M",
    "/books/OL26452256M",
    "/books/OL20784407M",
    "/books/OL26450482M",
    "/books/OL23077320M",
    "/books/OL8889882M",
    "/books/OL26450490M",
    "/books/OL17238263M",
    "/books/OL9076659M",
    "/books/OL19685717M",
    "/books/OL23124795M",
    "/books/OL10236390M",
    "/books/OL22814360M",
    "/books/OL24584294M",
    "/books/OL11461843M",
    "/books/OL8171979M",
    "/books/OL22106804M",
    "/books/OL23097541M",
    "/books/OL26451577M",
    "/books/OL26451576M",
    "/books/OL22054291M",
    "/books/OL7261494M",
    "/books/OL9216209M",
    "/books/OL13320799M",
    "/books/OL7261842M",
    "/books/OL9216557M",
    "/books/OL22469028M",
    "/books/OL8529332M",
    "/books/OL3969872M",
    "/books/OL20932268M",
    "/books/OL13569251M",
    "/books/OL24206968M",
    "/books/OL24737100M",
    "/books/OL23041688M",
    "/books/OL25483585M",
    "/books/OL9158225M",
    "/books/OL19112575M",
    "/books/OL22050938M",
    "/books/OL18905181M",
    "/books/OL9149754M",
    "/books/OL26383768M",
    "/books/OL3777336M",
    "/books/OL24374179M",
    "/books/OL26451900M",
    "/books/OL26451897M",
    "/books/OL26450093M",
    "/books/OL22069376M",
    "/books/OL3682825M",
    "/books/OL26452611M",
    "/books/OL12541182M",
    "/books/OL7605824M",
    "/books/OL26451924M",
    "/books/OL24298430M",
    "/books/OL24293296M",
    "/books/OL24281996M",
    "/books/OL25420485M",
    "/books/OL26452597M",
    "/books/OL26452618M",
    "/books/OL26452617M",
    "/books/OL26384839M",
    "/books/OL26450094M",
    "/books/OL26452619M",
    "/books/OL26452624M",
    "/books/OL26452610M",
    "/works/OL15331214W",
    "/subjects/adventure_fiction",
    "/subjects/ficci\u00f3n",
    "/subjects/ficci\u00f3n_fant\u00e1stica_inglesa",
    "/subjects/internet_archive_wishlist",
    "/subjects/fantastic_fiction",
    "/subjects/the_lord_of_the_rings",
    "/subjects/english_fantasy_fiction",
    "/subjects/in_library",
    "/subjects/popular_print_disabled_books",
    "/subjects/open_library_staff_picks",
    "/subjects/accessible_book",
    "/subjects/protected_daisy",
    "/subjects/fiction",
    "/subjects/fantasy",
    "/subjects/fairy_tales",
    "/subjects/adventure_stories",
    "/subjects/fantasy_fiction",
    "/subjects/large_type_books",
    "/subjects/person:bilbo_baggins",
    "/subjects/person:gandalf_the_wizard",
    "/subjects/person:frodo_baggins",
    "/subjects/person:samwise_gamgee",
    "/subjects/person:aragorn_(strider)",
    "/subjects/person:legolas",
    "/subjects/person:gimli",
    "/subjects/person:elrond",
    "/subjects/person:sauron",
    "/subjects/place:middle_earth",
    "/subjects/place:mordor",
    "/subjects/place:tierra_media",
    "/subjects/time:before_the_age_of_men",
    "/authors/OL26320A"
   ],
   "oclc": [
    "492489392",
    "874884502",
    "495926805",
    "59462836",
    "28820516",
    "813678154",
    "60198264",
    "859858656",
    "962899321",
    "925375894",
    "969606359",
    "1005936675",
    "892147306",
    "892822609",
    "12783233",
    "26074760",
    "53354229",
    "804341872",
    "473660275",
    "985367714",
    "490916277",
    "908106356",
    "866921295",
    "69306984",
    "314934465",
    "847522557",
    "1023784421",
    "891929385",
    "20911014",
    "608811797",
    "264943675",
    "867941362",
    "879331252",
    "863419832",
    "491629977",
    "858006243",
    "656925950",
    "972120209",
    "868151445",
    "1028304305",
    "59806314",
    "222286517",
    "800851830",
    "173617998",
    "221359042",
    "859053085",
    "840313694",
    "491308716",
    "644361719",
    "401668875",
    "28576179",
    "642408746",
    "5983481",
    "39786673",
    "818844233",
    "689998836",
    "422011972",
    "956677518",
    "1028428830",
    "828327601",
    "988608157",
    "441105273",
    "276705178",
    "1031627083",
    "59304971",
    "494437348",
    "300294295",
    "965313612",
    "50575811",
    "31385993",
    "840923271",
    "473321979",
    "999800269",
    "769331264",
    "59814092",
    "33231212",
    "690513322",
    "1003689208",
    "441644416",
    "973591950",
    "458615282",
    "18291996",
    "495787648",
    "812770728",
    "934791596",
    "887434322",
    "733661501",
    "265243763",
    "223368847",
    "955830033",
    "608874150",
    "813328089",
    "940043845",
    "924759492",
    "6801190",
    "733845192",
    "723113405",
    "51898813",
    "48034705",
    "50880827",
    "315256208",
    "820529069",
    "680126005",
    "679748755",
    "60788362",
    "718006258",
    "473636432",
    "671818954",
    "873088483",
    "401524066",
    "41736747",
    "38493843",
    "877421571",
    "869828061",
    "490283396",
    "936043149",
    "819931671",
    "1028305395",
    "76820597",
    "558815281",
    "832974849",
    "762217299",
    "925000280",
    "49652808",
    "993953990",
    "185439182",
    "812629789",
    "760005887",
    "71756740",
    "223428261",
    "438323741",
    "436317500",
    "39031400",
    "963195864",
    "779162993",
    "317867795",
    "59549292",
    "999367006",
    "473798507",
    "438980186",
    "1023727818",
    "889581762",
    "671852341",
    "69654933",
    "63157893",
    "473251806",
    "48863478",
    "228444755",
    "650243225",
    "278019019",
    "1014283774",
    "48896366",
    "33034923",
    "751933468",
    "68389399",
    "52828988",
    "48034344",
    "59483583",
    "473191796",
    "440837776",
    "742807522",
    "48491076",
    "493357569",
    "906673187",
    "222929817",
    "51652816",
    "432702929",
    "884060681",
    "1098874",
    "972118943",
    "491677922",
    "613265489",
    "810453057",
    "49597495",
    "22366207",
    "473216878",
    "60658001",
    "861657097",
    "148822151",
    "1005270888",
    "932188442",
    "931784385",
    "906720636",
    "51782682",
    "1028386230",
    "12228601",
    "1133027",
    "60598951",
    "416287693",
    "911216759",
    "918598176",
    "244128644",
    "780027833",
    "221067788",
    "773759305",
    "407039470",
    "810481073",
    "1027685857",
    "46387665",
    "441192718",
    "1035694988",
    "906893207"
   ],
   "id_google": [
    "5sQ8DwAAQBAJ",
    "dicxLgEACAAJ",
    "lqHNugAACAAJ",
    "OyLzoNQ2vuEC",
    "TlYWqAAACAAJ",
    "Av6RMQEACAAJ",
    "7gJhHwAACAAJ",
    "FH44swEACAAJ",
    "ywDssgEACAAJ",
    "Zy3-QgAACAAJ",
    "TL6wAAAACAAJ",
    "3klWtQEACAAJ",
    "OGJqzw0Oo2UC",
    "nkD1QgAACAAJ",
    "LviqAAAACAAJ",
    "VSwDAAAACAAJ",
    "AMFZQAAACAAJ",
    "BunxAAAACAAJ",
    "q09yQgAACAAJ",
    "4sEvpZtowmAC",
    "Zw24wCYcF1EC",
    "GCOZQgAACAAJ",
    "H4-RfI4wiggC",
    "3flBjgEACAAJ",
    "ksTFy9UN6NcC",
    "Xzc76KsFrokC",
    "Av83swEACAAJ",
    "AaWwQwAACAAJ",
    "U1Ne2A916MkC",
    "qnsTtAEACAAJ",
    "elxQRwAACAAJ",
    "civqAAAACAAJ",
    "qy28tQEACAAJ",
    "L5ABrgEACAAJ",
    "l0hMjgEACAAJ",
    "aHPwAACAAJ",
    "9vsHmQEACAAJ",
    "xFr92V2k3PIC",
    "pK43Jn0RmTcC",
    "CMOhPwAACAAJ",
    "2R_9swEACAAJ",
    "4Py2swEACAAJ",
    "ILsWC2CLZLwC",
    "SeVg7tTw1ucC",
    "5sIZORTxFgMC",
    "fhhxSQAACAAJ",
    "DtOJTobDpx0C"
   ],
   "ia": [
    "fellowshipofring00tolk",
    "fellowshipofringtol00tolk",
    "lordofrings00jrrt",
    "fellowshipofring1973tolk",
    "elsenordelosanil00jrrt",
    "fellowshipofring01tolk",
    "fellowshipofring00tolkrich",
    "lordofrings00tolk",
    "mojieshoubuqumoj00tolk",
    "lordofringsco00jrrt",
    "fellowshipofrin00tolk",
    "isbn_9780965307758",
    "twotowersbeingse00tolk_0",
    "fellowshipofring00jrrt",
    "fellowshipofring00tolk_0"
   ],
   "id_amazon_ca_asin": [
    "B002RI9THI",
    "844507573X",
    "8845290409",
    "0785907424",
    "0606244239",
    "9721041025",
    "9505470673",
    "0828868999",
    "0828865655",
    "8445070339",
    "9570823364",
    "8371502419"
   ],
   "author_key": [
    "OL26320A"
   ],
   "id_amazon_it_asin": [
    "B00JR9Y42A",
    "2070612880",
    "8845290409",
    "0606244239",
    "0345332083"
   ],
   "subject": [
    "English Fantasy fiction",
    "In library",
    "Popular Print Disabled Books",
    "Open Library Staff Picks",
    "Accessible book",
    "The Lord of the Rings",
    "Fantastic fiction",
    "Fiction",
    "Fantasy",
    "Fantasy fiction",
    "Fairy tales",
    "adventure fiction",
    "Adventure stories",
    "Protected DAISY",
    "Ficci\u00f3n fant\u00e1stica inglesa",
    "Large type books",
    "Ficci\u00f3n",
    "Internet Archive Wishlist"
   ],
   "id_amazon_co_uk_asin": [
    "1500410225",
    "B00JR9Y42A",
    "B002RI9THI",
    "3899408861",
    "5170264151",
    "9706906517",
    "8439596197",
    "B009YK1DB2",
    "0785907424",
    "B0071MUY06",
    "9721041025",
    "9505470673",
    "2266115618",
    "1556903219",
    "0828865655",
    "9027401683",
    "9536166119",
    "0618260269",
    "9570823364",
    "8371502419"
   ],
   "title": "The Fellowship of the Ring",
   "lending_identifier_s": "elsenordelosanil00jrrt",
   "ia_collection_s": "printdisabled;americana;internetarchivebooks;delawarecountydistrictlibrary;inlibrary;bannedbooks;china;openlibraries",
   "first_publish_year": 1954,
   "id_amazon_de_asin": [
    "1500410225",
    "B00JR9Y42A",
    "3608939814",
    "0007488319",
    "8445000667",
    "B002RI9THI",
    "2070612880",
    "844507573X",
    "3899408861",
    "8845290409",
    "9706906517",
    "B002922PT6",
    "3608934014",
    "3608933514",
    "B002E1VNO0",
    "0048231851",
    "0007171978",
    "0618129030"
   ],
   "type": "work",
   "ebook_count_i": 15,
   "publish_place": [
    "Canada",
    "Klett-Cotta",
    "Utrecht, the Netherlands",
    "Penerbit, Indonesia",
    "Prince Frederick, MD, USA",
    "Norwalk, CT, USA",
    "Mem Martins",
    "Argentina",
    "Barcelona, Spain",
    "Glasgow",
    "Boston, USA",
    "Antwerp, Belgium",
    "Beograd, Serbia",
    "Poznan",
    "Amsterdam, The Netherlands",
    "New York, USA",
    "London, England",
    "Madrid, Espa\u00f1a",
    "Taipei Shi",
    "Waterville, ME, USA",
    "Zagreb, Croatia",
    "Milano, Italia",
    "S\u00e3o Paulo SP Brasil",
    "Istanbul, Turkey",
    "Boston, MA, USA",
    "Stuttgart, Germany"
   ],
   "ia_box_id": [
    "IA101514",
    "IA1149313",
    "IA178301",
    "IA142018",
    "IA125203",
    "IA1155322",
    "IA176501",
    "IA177001",
    "IA105914",
    "IA177101",
    "IA111510",
    "IA123705",
    "IA119501",
    "IA148207",
    "IA1113422"
   ],
   "edition_count": 172,
   "key": "/works/OL15331214W",
   "id_alibris_id": [
    "9780547928210",
    "9781461836148",
    "9781594130076",
    "9780965307758",
    "9780618002221",
    "9780395312674",
    "9780618153985",
    "9780345253439",
    "9780618129034"
   ],
   "id_nla": [
    "5961254",
    "6331275",
    "44702252"
   ],
   "id_goodreads": [
    "35346101",
    "27113752",
    "40198412",
    "23432814",
    "40198224",
    "22704890",
    "15923739",
    "40197832",
    "21963487",
    "13356706",
    "17206506",
    "32451004",
    "40197253",
    "26232453",
    "40193571",
    "3009630",
    "20492433",
    "63389",
    "1210342",
    "2049473",
    "3548172",
    "63387",
    "29775260",
    "15265",
    "16126249",
    "136779",
    "1246553",
    "317017",
    "2442908",
    "12757148",
    "15304",
    "30288873",
    "13488305",
    "22080664",
    "470272",
    "1632313",
    "136773",
    "1246552",
    "6309474",
    "1215385",
    "1152666",
    "227233",
    "580010",
    "40167797",
    "497347",
    "2693339",
    "1220578",
    "222947",
    "828401",
    "7848435",
    "481774",
    "6926618",
    "92663",
    "1070463",
    "15282",
    "92657",
    "423092",
    "2905845",
    "15706872",
    "2913945",
    "12517169",
    "16045693",
    "837605",
    "727798",
    "5941419",
    "222909",
    "70991",
    "77683",
    "37650935",
    "0395082544",
    "20837433",
    "580675",
    "6472595",
    "12955161",
    "165488",
    "9501245",
    "18488193",
    "40096946",
    "227232",
    "4797425",
    "273438",
    "54709",
    "1432618",
    "1223937",
    "63390",
    "35527790",
    "28022171",
    "38448120",
    "11493292",
    "1451516",
    "40124493",
    "40106851",
    "30235421",
    "20510284",
    "40114038",
    "40113797",
    "40109464",
    "40107058",
    "6022453",
    "40106758",
    "29847025",
    "40106640",
    "21899285",
    "22046704",
    "33624963",
    "25263165",
    "899777",
    "822620",
    "15331",
    "1367355",
    "937196",
    "460643",
    "39006385",
    "9866440",
    "39011274",
    "16173884",
    "11996612",
    "17903161",
    "838626",
    "18510",
    "929675",
    "1181600",
    "601134",
    "360973",
    "877730",
    "929674",
    "15294",
    "7759287"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "public_scan_b": false,
   "id_overdrive": [
    "C2A9A798-DB81-472E-B555-A7A3D6A04BF8",
    "DFDA6E54-C616-431D-89D2-0D3CA8CF5A46"
   ],
   "publisher": [
    "Klett-Cotta",
    "French & European Pubns",
    "Gallimard Jeunesse",
    "Harper",
    "Allen & Unwin",
    "Houghton Mifflin Company",
    "Grafton",
    "Folio Society",
    "xx",
    "Houghton Mifflin Co.",
    "Martins Fontes",
    "Easton Press",
    "Collins",
    "Hobbit Presse",
    "George Allen and Unwin",
    "ISIS Large Print Books",
    "Harper Collins",
    "Christian Bourgois",
    "Thorndike Press",
    "Rubikon",
    "Quality Paperback Book Club",
    "AST",
    "Gyldendal Lyd",
    "HarperCollins Publishers Ltd",
    "Der H\u00f6rverlag",
    "Houghton Mifflin",
    "Pocket",
    "Folio Junior",
    "Unwin Books",
    "Del Rey (Random House)",
    "Xerias",
    "Allen and Unwin",
    "Houghton Mifflin Harcourt",
    "J.G. Cotta'sche, Buchhandlung Nachfolger GmbH",
    "Het Spectrum",
    "Ballantine Books",
    "Minotauro",
    "Algoritam",
    "Ace",
    "Zysk i S-ka",
    "Del Rey",
    "Barry Goldstein",
    "Europa-America",
    "Turtleback Books Distributed by Demco Media",
    "Bompiani",
    "Harper-Collins",
    "UITGEVERIJ MEULENHOFF",
    "Recorded Books",
    "Gondolat",
    "George Allen & Unwin",
    "Large Print Press",
    "Metis Yay\u0131nlar\u0131",
    "Linking Publishing",
    "Ballantine Books / Del Rey",
    "Perfection Learning",
    "Ediciones Minotauro",
    "HarperCollins",
    "Unwin Paperbacks",
    "Cappelen Damm Lydbok",
    "Turtleback Books",
    "Del Rey / Ballantine Books",
    "Methuen",
    "harpercollins",
    "Gramedia Pustaka Utama",
    "Ballentine Books",
    "Lian jing chu ban shi ye gong si",
    "HarperCollins Publishers",
    "Magnum Books",
    "Minotaur"
   ],
   "id_amazon": [
    "1500410225",
    "0544448936",
    "8445000667",
    "B002RI9THI",
    "2070612880",
    "844507573X",
    "8845290409",
    "9706906517",
    "8439596197",
    "3608955364",
    "0828839816",
    "2266128043",
    "0785907424",
    "0606244239",
    "3608934014",
    "3608933514",
    "0007117116",
    "9721041025",
    "2266070614",
    "9505470673",
    "2266115618",
    "000712970X",
    "2070515796",
    "034591743X",
    "0965307751",
    "0828868999",
    "1556903219",
    "360893541X",
    "0828865655",
    "0828810540",
    "2266046497",
    "039564738X",
    "0345008626",
    "B0074VCEU2",
    "3608952128",
    "0345339703",
    "9632809637",
    "8445070339",
    "0261103571",
    "0261102311",
    "B0028IF5SO",
    "0606006508",
    "0345235096",
    "0395082544",
    "1850894140",
    "9570823364",
    "8371502419"
   ],
   "id_paperback_swap": [
    "0345008626"
   ],
   "language": [
    "ger",
    "fre",
    "eng",
    "chi",
    "dan",
    "hrv",
    "tur",
    "ita",
    "gag",
    "pol",
    "yid",
    "por",
    "rus",
    "ind",
    "spa",
    "dut",
    "hun",
    "nor",
    "scr"
   ],
   "lccn": [
    "88120282",
    "2001276576",
    "81166135",
    "2003041673",
    "81139600",
    "67012274",
    "67-12274",
    "67-12275",
    "2003542569",
    "88122831"
   ],
   "last_modified_i": 1530691990,
   "id_bcid": [
    "12802787"
   ],
   "lending_edition_s": "OL9131874M",
   "id_librarything": [
    "3203347",
    "1386651",
    "8739375"
   ],
   "cover_edition_key": "OL26452664M",
   "first_sentence": [
    "THIS BOOK is largely concerned with Hobbits, and from its pages a reader may discover much of their character and a little of their history.",
    "This book is largely concerned with Hobbits, and from its pages a reader may discover much of their character and a little of their history."
   ],
   "person": [
    "Sauron",
    "Aragorn (Strider)",
    "Gandalf the Wizard",
    "Frodo Baggins",
    "Elrond",
    "Gimli",
    "Bilbo Baggins",
    "Samwise Gamgee",
    "Legolas"
   ],
   "publish_year": [
    1974,
    2003,
    1986,
    1987,
    1984,
    1982,
    1983,
    1980,
    1981,
    1965,
    1966,
    1967,
    1989,
    2018,
    2014,
    2010,
    2013,
    2012,
    1954,
    1968,
    1959,
    1991,
    1990,
    1993,
    1992,
    1995,
    1994,
    1979,
    1996,
    1999,
    1976,
    1978,
    1972,
    1970,
    2002,
    1977,
    2000,
    2001,
    2006,
    2007,
    2004,
    2009
   ],
   "printdisabled_s": "OL24212887M;OL7261842M;OL18299598M;OL8529332M;OL9216557M;OL24206969M;OL24206968M;OL24373119M;OL10682854M;OL24374179M;OL24737100M;OL10236417M;OL9131874M;OL20932268M;OL13569251M;OL10236390M;OL9149754M;OL22814360M",
   "place": [
    "Mordor",
    "Tierra Media",
    "Middle Earth"
   ],
   "time": [
    "Before the Age of Men"
   ],
   "publish_date": [
    "1974 March",
    "2000 Novembre",
    "1979 June",
    "2018",
    "2014",
    "1999 July 5",
    "2010",
    "2013",
    "2012",
    "2003 March",
    "2001 October",
    "1954",
    "2002 November 7",
    "1977 July",
    "1959",
    "1975 April",
    "1987 July",
    "2000 September",
    "1972 August",
    "1975 September",
    "1983 January",
    "1991 September",
    "2006 June 30",
    "1986",
    "1986 July",
    "1980 October",
    "2003 April",
    "2001 November",
    "1980",
    "1976 March",
    "2000 April 13",
    "1997 November 3",
    "1973 March",
    "2001 October 1",
    "1956 December",
    "1991 June",
    "1973 September",
    "1974 September",
    "1987",
    "1984",
    "1982",
    "1983",
    "2001 October 31",
    "1981",
    "2001 June",
    "1989",
    "1990 March",
    "2010 February 22",
    "1991",
    "1990",
    "1993",
    "1992",
    "1995",
    "1994",
    "1996",
    "1999",
    "1998 November 2",
    "2001 May",
    "1988 September",
    "2012 July",
    "2002 January 1",
    "1968",
    "1965 October",
    "1965",
    "1966",
    "1967",
    "1981 April",
    "2006",
    "1966 August",
    "2016 August",
    "1985 July",
    "2018 March 02",
    "1966 September",
    "2003 November 13",
    "2011 May 01",
    "1979",
    "1978",
    "1977",
    "1976",
    "1974",
    "1972",
    "1970",
    "2002",
    "2003",
    "2000",
    "2001",
    "1993 January",
    "2007",
    "2004",
    "2009",
    "1977 October"
   ],
   "id_british_national_bibliography": [
    "GB7428478"
   ]
  },
  {
   "title_suggest": "Realm of the Ring Lords",
   "publisher": [
    "MediaQuest"
   ],
   "isbn": [
    "0953768694",
    "9780953768691"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "edition_key": [
    "OL11620056M"
   ],
   "last_modified_i": 1419577629,
   "title": "Realm of the Ring Lords",
   "author_name": [
    "Laurence Gardner",
    "Adrian Wagner"
   ],
   "cover_edition_key": "OL11620056M",
   "seed": [
    "/books/OL11620056M",
    "/works/OL11620056M",
    "/authors/OL50039A",
    "/authors/OL3684075A"
   ],
   "first_publish_year": 2001,
   "publish_year": [
    2001
   ],
   "key": "/works/OL11620056M",
   "text": [
    "OL11620056M",
    "0953768694",
    "9780953768691",
    "Laurence Gardner",
    "Adrian Wagner",
    "OL50039A",
    "OL3684075A",
    "Beyond the Portal of the Twilight World",
    "Realm of the Ring Lords",
    "/works/OL11620056M",
    "MediaQuest"
   ],
   "id_goodreads": [
    "660939"
   ],
   "publish_date": [
    "February 28, 2001"
   ],
   "author_key": [
    "OL50039A",
    "OL3684075A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Rings Enhanced",
   "edition_key": [
    "OL12579408M"
   ],
   "isbn": [
    "5555630115",
    "9785555630117"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "last_modified_i": 1272134736,
   "title": "Lord of the Rings Enhanced",
   "author_name": [
    "Interplay"
   ],
   "seed": [
    "/books/OL12579408M",
    "/works/OL9870213W",
    "/authors/OL3853219A"
   ],
   "key": "/works/OL9870213W",
   "text": [
    "OL12579408M",
    "5555630115",
    "9785555630117",
    "Interplay",
    "OL3853219A",
    "Lord of the Rings Enhanced",
    "/works/OL9870213W"
   ],
   "id_goodreads": [
    "6669620"
   ],
   "author_key": [
    "OL3853219A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the Living Ring",
   "edition_key": [
    "OL8489393M"
   ],
   "cover_i": 1811146,
   "isbn": [
    "142088526X",
    "9781420885262"
   ],
   "has_fulltext": false,
   "text": [
    "OL8489393M",
    "142088526X",
    "9781420885262",
    "Beldeu Singh",
    "OL2992550A",
    "Lord of the Living Ring",
    "/works/OL8781438W",
    "Authorhouse"
   ],
   "author_name": [
    "Beldeu Singh"
   ],
   "seed": [
    "/books/OL8489393M",
    "/works/OL8781438W",
    "/authors/OL2992550A"
   ],
   "author_key": [
    "OL2992550A"
   ],
   "title": "Lord of the Living Ring",
   "publish_date": [
    "October 31, 2005"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL8781438W",
   "id_goodreads": [
    "1788092"
   ],
   "publisher": [
    "Authorhouse"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1272448156,
   "cover_edition_key": "OL8489393M",
   "publish_year": [
    2005
   ],
   "first_publish_year": 2005
  },
  {
   "title_suggest": "Realm of the Ring Lords",
   "publisher": [
    "MediaQuest"
   ],
   "edition_key": [
    "OL12268324M"
   ],
   "isbn": [
    "1903773008",
    "9781903773000"
   ],
   "has_fulltext": false,
   "edition_count": 1,
   "oclc": [
    "50427308"
   ],
   "last_modified_i": 1419576406,
   "title": "Realm of the Ring Lords",
   "author_name": [
    "Laurence Gardner",
    "Adrian Wagner"
   ],
   "cover_edition_key": "OL12268324M",
   "seed": [
    "/books/OL12268324M",
    "/works/OL12268324M",
    "/authors/OL50039A",
    "/authors/OL3684075A"
   ],
   "first_publish_year": 2001,
   "publish_year": [
    2001
   ],
   "key": "/works/OL12268324M",
   "text": [
    "OL12268324M",
    "1903773008",
    "9781903773000",
    "Laurence Gardner",
    "Adrian Wagner",
    "50427308",
    "OL50039A",
    "OL3684075A",
    "Beyond the Portal of the Twilight World",
    "Realm of the Ring Lords",
    "/works/OL12268324M",
    "MediaQuest"
   ],
   "id_goodreads": [
    "2416127"
   ],
   "publish_date": [
    "February 28, 2001"
   ],
   "author_key": [
    "OL50039A",
    "OL3684075A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord Gnome of the rings",
   "publish_place": [
    "London"
   ],
   "isbn": [
    "023396827X",
    "9780233968278"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL20645257M"
   ],
   "last_modified_i": 1419576650,
   "title": "Lord Gnome of the rings",
   "publisher": [
    "A. Deutsch",
    "Private Eye Productions"
   ],
   "id_librarything": [
    "1995530"
   ],
   "seed": [
    "/books/OL20645257M",
    "/works/OL20645257M",
    "/subjects/english_wit_and_humor.",
    "/subjects/english_wit_and_humor_pictorial."
   ],
   "first_publish_year": 1976,
   "publish_year": [
    1976
   ],
   "key": "/works/OL20645257M",
   "text": [
    "OL20645257M",
    "023396827X",
    "9780233968278",
    "the best of Private eye.",
    "Lord Gnome of the rings",
    "English wit and humor.",
    "English wit and humor, Pictorial.",
    "/works/OL20645257M",
    "A. Deutsch",
    "Private Eye Productions",
    "Private eye."
   ],
   "id_goodreads": [
    "3235505"
   ],
   "publish_date": [
    "1976"
   ],
   "subject": [
    "English wit and humor.",
    "English wit and humor, Pictorial."
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "War lords of the ring.",
   "publish_place": [
    "London"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL15476075M"
   ],
   "last_modified_i": 1419577391,
   "title": "War lords of the ring.",
   "publisher": [
    "Gemini Vision"
   ],
   "seed": [
    "/books/OL15476075M",
    "/works/OL15476075M",
    "/subjects/wrestling."
   ],
   "key": "/works/OL15476075M",
   "text": [
    "OL15476075M",
    "War lords of the ring.",
    "Wrestling.",
    "/works/OL15476075M",
    "Gemini Vision"
   ],
   "subject": [
    "Wrestling."
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord of the gas rings.",
   "publisher": [
    "Bright books."
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL20505368M"
   ],
   "last_modified_i": 1419575747,
   "title": "Lord of the gas rings.",
   "seed": [
    "/books/OL20505368M",
    "/works/OL20505368M"
   ],
   "key": "/works/OL20505368M",
   "text": [
    "OL20505368M",
    "Lord of the gas rings.",
    "/works/OL20505368M",
    "Bright books."
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Lord Gnome of the Rings",
   "publish_place": [
    "London"
   ],
   "has_fulltext": false,
   "language": [
    "eng"
   ],
   "edition_count": 1,
   "edition_key": [
    "OL19882552M"
   ],
   "last_modified_i": 1264401896,
   "title": "Lord Gnome of the Rings",
   "publisher": [
    "A Deutsch/Private Eye"
   ],
   "author_name": [
    "PRIVATE EYE."
   ],
   "seed": [
    "/books/OL19882552M",
    "/works/OL12919947W",
    "/authors/OL5849386A"
   ],
   "first_publish_year": 1976,
   "publish_year": [
    1976
   ],
   "key": "/works/OL12919947W",
   "text": [
    "OL19882552M",
    "PRIVATE EYE.",
    "OL5849386A",
    "the best of \"Private Eye\".",
    "Lord Gnome of the Rings",
    "/works/OL12919947W",
    "A Deutsch/Private Eye"
   ],
   "publish_date": [
    "1976"
   ],
   "author_key": [
    "OL5849386A"
   ],
   "type": "work",
   "ebook_count_i": 0
  },
  {
   "title_suggest": "Hobbit Lord of the Rings",
   "edition_key": [
    "OL8080254M"
   ],
   "cover_i": 7020407,
   "isbn": [
    "0774032979",
    "9780774032971"
   ],
   "has_fulltext": false,
   "text": [
    "OL8080254M",
    "0774032979",
    "9780774032971",
    "J. R. R. Tolkien",
    "OL26320A",
    "Hobbit Lord of the Rings",
    "/works/OL14933384W",
    "Coles Pub Group Ltd",
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_name": [
    "J. R. R. Tolkien"
   ],
   "seed": [
    "/books/OL8080254M",
    "/works/OL14933384W",
    "/authors/OL26320A"
   ],
   "author_alternative_name": [
    "J. R. R. Tolkein",
    "John Ronald Reuel Tolkien",
    "J.R.R. Tolkein"
   ],
   "author_key": [
    "OL26320A"
   ],
   "title": "Hobbit Lord of the Rings",
   "publish_date": [
    "June 1979"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL14933384W",
   "id_goodreads": [
    "222946"
   ],
   "publisher": [
    "Coles Pub Group Ltd"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1327780502,
   "id_librarything": [
    "4881"
   ],
   "publish_year": [
    1979
   ],
   "first_publish_year": 1979
  },
  {
   "title_suggest": "The Lord of the Rings - The Fellowship of the Ring",
   "edition_key": [
    "OL10905390M"
   ],
   "cover_i": 2605854,
   "isbn": [
    "0761540881",
    "9780761540885"
   ],
   "has_fulltext": false,
   "text": [
    "OL10905390M",
    "0761540881",
    "9780761540885",
    "Scruffy Productions",
    "OL2838674A",
    "The Lord of the Rings - The Fellowship of the Ring",
    "/works/OL8496085W",
    "Prima Games"
   ],
   "author_name": [
    "Scruffy Productions"
   ],
   "seed": [
    "/books/OL10905390M",
    "/works/OL8496085W",
    "/authors/OL2838674A"
   ],
   "author_key": [
    "OL2838674A"
   ],
   "title": "The Lord of the Rings - The Fellowship of the Ring",
   "publish_date": [
    "October 2002"
   ],
   "type": "work",
   "ebook_count_i": 0,
   "edition_count": 1,
   "key": "/works/OL8496085W",
   "id_goodreads": [
    "470270"
   ],
   "publisher": [
    "Prima Games"
   ],
   "language": [
    "eng"
   ],
   "last_modified_i": 1293241488,
   "cover_edition_key": "OL10905390M",
   "publish_year": [
    2002
   ],
   "first_publish_year": 2002
  }
 ]
}"""

# TODO Refactor tests.

def test_base_panel_calculate_price():
    p = Panel()
    with pytest.raises(NotImplementedError):
        p.calculate_price()

def test_panel_one_url():
    p = PanelOne()
    assert 'http://time.com', p.url

def test_panel_two_url():
    p = PanelTwo()
    test_url = 'http://openlibrary.org/earch.json?q=the+lord+of+the+rings'
    assert test_url, p.url

def test_panel_three_url():
    p = PanelThree()
    assert 'http://time.com', p.url

def test_panel_one_price():
    p = PanelOne()
    p.url_content = HTML
    assert 0.88, p.calculate_price()

#  TODO panel two class and test
# def test_panel_two_price():
#     p = PanelTwo()
#     p.url_content = data
#     assert 0, p.calculate_price()


def test_panel_three_price():
    p = PanelThree()
    p.url_content = HTML
    assert 0.01, p.calculate_price()