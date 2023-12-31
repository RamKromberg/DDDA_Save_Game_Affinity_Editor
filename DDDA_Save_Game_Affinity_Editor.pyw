#!/usr/bin/env python

# Dragon's Dogma: Dark Arisen Save Game Affinity Editor
# 2023-10-11
# nowahNOwah @ https://www.nexusmods.com/users/183050388
#
# depends on "pip install lxml sv_ttk"
# https://lxml.de/
# https://github.com/rdbende/Sun-Valley-ttk-theme/

from lxml import etree
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import StringVar
import tkinter.font as tkFont
import math

try:
	import sv_ttk
except ImportError:
	sv_ttk=False

#gamesrule1124 @ http://fluffyquack.com/DD/txt/npc-list.txt (reformated & alphabetically sorted)
ddda_npc_ids = {"255": "Abram", "001": "Adaro", "102": "Aelinore", "102_01": "Aelinore (hair down)", "102_02": "Aelinore (post-game Beloved)", "220": "Aemelie", "010": "Aestella", "216": "Agnes", "433": "Akim (pawn merchant in Everfall post-game)", "852": "Alastor", "105": "Aldous", "031": "Alejo", "043": "Alejo (injured; before Floral Delivery quest; strangely, has Jaquan's character model)", "018": "Alethea", "019": "Alita", "398": "Alon", "434": "Alonso", "110": "Ambrose", "596": "Amity", "537": "Anbros", "343": "Anelace", "328": "Anri", "126": "Ansell", "840": "Antony", "190": "Aric", "028": "Arnot", "154": "Arsmith", "147": "Asalam", "785": "Ashe", "527": "Asthea (Salvation member)", "362": "Aurene", "038": "Auster", "169": "Austine", "595": "Baden", "702": "Balsac", "157": "Barnaby", "784": "Barroch", "015": "Barten", "341": "Basilard", "215": "Baudric", "258": "Bawdwyn", "008": "Benita", "363": "Betiah", "847": "Bonneau", "160": "Brice", "555": "Burgess", "187": "Cale", "151": "Camellia", "345": "Caravel", "172": "Carel", "528": "Carmel (Salvation member)", "605": "Carya", "149": "Caxton", "823": "Cedric", "361": "Cele", "331": "Charlene", "034": "Chas", "027": "Chaves", "524": "Cicero", "838": "Clarke", "327": "Clarus", "340": "Claymore", "020": "Clemente", "556": "Cobalt", "732": "Condor", "173": "Conwey", "831": "Cordovan", "192": "Cornelius", "501": "Cortese", "706": "Cortese", "835": "Corti", "526": "Cristofer", "338": "Culverin", "387": "Cutting", "397": "Danell", "185": "Danton", "729": "Darkness", "358": "Dasya", "432": "Delec (pawn merchant)", "153": "Devyn", "700": "Dillan", "107": "Domenique", "392": "Dragonforged", "825": "Drew", "101": "Duke Edmun Dragonsbane", "610": "Duke Edmun Dragonsbane (old)", "101_01": "Duke Edmun Dragonsbane (unidentified variation)", "404": "Ecbal", "129": "Edgar", "016": "Elonzo", "017": "Elvar", "611": "Elysion", "022": "Ema", "040": "Ema (again)", "195": "Emme", "832": "Emzie", "480": "Enric", "708": "Esme", "115": "Esperaunce", "033": "Estevon", "505": "Estoni", "166": "Eugen", "845": "Ewald", "781": "Faircrest", "335": "Falchion", "136": "Fancey", "352": "Fayth", "106": "Fedel", "483": "Ferris", "103": "Feste", "179": "Flavian", "558": "Florian", "525": "Fonio", "133": "Fournival", "026": "Fredro", "256": "Frost", "833": "Garrett", "171": "Garvin", "583": "Gatte", "592": "Gatte", "127": "Geffrey", "726": "Ghost", "344": "Glaive", "521": "Graham", "035": "Grecio", "786": "Grette", "189": "Guston", "150": "Gwine", "334": "Hammer", "128": "Haslett", "731": "Hawk", "253": "Hender", "710": "Hera", "009": "Heraldo", "221": "Hewrey", "131": "Hilde", "217": "Hobert", "357": "Holle", "356": "Honna", "167": "Howlen", "168": "Humphrauy", "329": "Ilona", "012": "Inez", "011": "Iola", "260": "Isabel", "024": "Janielle", "042": "Janielle (again)", "330": "Janne", "025": "Jaquan", "180": "Jasper", "399": "Jayce", "263": "Jean", "218": "Jenlyns", "606": "Johann", "720": "Johnathan", "262": "Jolette", "349": "Jonna", "707": "Jorgen", "118": "Josephine", "213": "Josias", "182": "Josua", "582": "Jouwn", "591": "Jouwn", "412": "Joye", "413": "Joye", "414": "Joye", "415": "Joye", "416": "Joye", "417": "Joye", "418": "Joye", "419": "Joye", "420": "Joye", "421": "Joye", "422": "Joye", "423": "Joye", "424": "Joye", "425": "Joye", "426": "Joye", "427": "Joye", "428": "Joye", "429": "Joye", "430": "Joye", "713": "Joye", "749": "Joye", "788": "Joye", "789": "Joye", "411": "Joye (a pawn merchant in post-game Everfall. different clothes when chosen as Caught NPC; shop function doesn't work; resembles a Cassardi villager who is killed in the dragon attack)", "791": "Joye (his NPC may be a place holder for NPCs that are not supposed to be edited or seen outside of their normal area)", "741": "Joye (possibly Ser Caraway)", "746": "Joye (possibly Ser Flint)", "745": "Joye (possibly Ser Pierre)", "748": "Joye (possibly Ser Ritter)", "747": "Joye (possibly Ser Siegel)", "740": "Joye (possibly the Seneschal)", "431": "Joye (the actual one with normal clothing and functioning shop)", "790": "Joye (yet again)", "152": "Judith", "104_02": "Julien (around the Duke's Demesne)", "104": "Julien (full armor and helmet during Seeking Salvation quest)", "104_04": "Julien (normal clothing; while in dungeon or post-game Beloved)", "104_01": "Julien (unknown variation)", "104_03": "Julien (unknown variation)", "481": "Karina", "196": "Kassie", "178": "Katlyn", "851": "Keenan", "824": "Kellen", "569": "Kent", "614": "Klemt", "337": "Lance", "837": "Landon", "032": "Lazoro", "044": "Lazoro (again)", "608": "Lelou", "161": "Lena", "029": "Lesia", "005": "Lewes", "570": "Lowane", "214": "Lucie", "346": "Mace", "007": "Madeleine", "522": "Manning", "520": "Marcelo", "523": "Margaritte (Salvation member)", "116": "Margery", "164": "Marla", "177": "Martha", "030": "Marthena", "158": "Mason", "159": "Mathewe", "400": "Mathias", "332": "Maul", "165": "Maurin", "130": "Maxson", "004": "Mayra", "135": "Mellard", "301": "Mercedes", "333": "Mercygiver", "148": "Meridith", "003": "Merin", "183": "Merrick", "175": "Milberowe", "482": "Miles", "132": "Milly", "117": "Mirabelle", "117_01": "Mirabelle (no character changes noticed after multiple playthroughs or setting as post-game Beloved; maybe for the Blighted Manse cutscene)", "571": "Moditt", "174": "Morys", "156": "Mountebank", "612": "Murphey", "572": "Nabarough", "359": "Nelle", "709": "Nessa", "155": "Nettie", "705": "Nicolas", "181": "Nils", "385": "Nilson", "734": "Noir", "584": "Odnall", "593": "Odnall", "360": "Ola", "783": "Olra (Cassardi Docks & Bitterblack Isle)", "787": "Olra (pawn)", "348": "Ophis", "554": "Orlmer", "113": "Orsay", "163": "Osip", "844": "Otzi", "006": "Pablos", "607": "Patt", "112": "Pering", "176": "Pernill", "604": "Perrin", "725": "Phantom", "222": "Philippa", "503": "Piell", "347": "Pike", "194": "Pip", "259": "Pipa", "036": "Poll", "615": "Pom", "354": "Purnell", "002": "Quina", "002_01": "Quina (Abbey)", "750": "Quince (Everfall)", "827": "Ralph", "023": "Ramon", "041": "Ramon (again)", "111": "Randell", "336": "Ranseur", "114": "Raulin", "730": "Raven", "304": "Reynard", "502": "Rickard", "386": "Robyn", "782": "Rochelle", "037": "Rojay", "504": "Rook", "013": "Rorric", "733": "Rouge", "396": "Rowland", "839": "Russet", "184": "Rychard", "544": "Salomet", "803": "Salomet's Bandits (Magick user)", "801": "Salomet's Bandits (warrior)", "802": "Salomet's Bandits (warrior)", "613": "Samara", "557": "Sandor", "186": "Sara", "375": "Selene", "807": "Seneschal (possibly? game crashes when set as Caught NPC)", "355": "Sens", "021": "Sentena", "039": "Sentena (again)", "389": "Ser Abell", "381": "Ser Adem", "264": "Ser Adraenn", "201": "Ser Aerick", "810": "Ser Airhart (possibly? one of the knights that help with rescuing Aelinore from the Blighted Manse; purple clothing around armor; long hair)", "372": "Ser Alastair", "492": "Ser Alden", "476": "Ser Alfonso", "490": "Ser Alisander", "637": "Ser Aloyis", "198": "Ser Alvert", "559": "Ser Andorf", "367": "Ser Anso", "509": "Ser Antonio", "577": "Ser Apera", "586": "Ser Apera", "548": "Ser Arachis", "625": "Ser Arbel", "307": "Ser Arman", "510": "Ser Ashrore", "639": "Ser Auber", "519": "Ser Audric", "197": "Ser Auguste", "821": "Ser Azarel", "560": "Ser Bacell", "478": "Ser Baird", "624": "Ser Balter", "848": "Ser Basius", "635": "Ser Bastian", "580": "Ser Bax", "589": "Ser Bax", "211": "Ser Bayard", "493": "Ser Belus", "303": "Ser Berne", "312": "Ser Bernis", "640": "Ser Borone", "542": "Ser Brigante", "515": "Ser Brinden", "326": "Ser Bryan", "575": "Ser Burrell", "535": "Ser Burton", "829": "Ser Byrt", "828": "Ser Caesey", "648": "Ser Callister", "205": "Ser Camillus", "830": "Ser Carrot", "506": "Ser Cashew", "365": "Ser Castor", "541": "Ser Chandra", "374": "Ser Chesleigh", "629": "Ser Clyde", "854": "Ser Colby", "384": "Ser Constans", "531": "Ser Covan", "561": "Ser Cronnel", "603": "Ser Curtis", "402": "Ser Cutbert", "212": "Ser Cyriac", "267": "Ser Cyril", "305": "Ser Cyrus", "364": "Ser Daerio", "310": "Ser Datson", "633": "Ser Defloe", "623": "Ser Dennep", "120": "Ser Deric", "308": "Ser Devers", "562": "Ser Diggan", "545": "Ser Dill", "121": "Ser Dirke", "602": "Ser Dorgann", "649": "Ser Dornkirk", "578": "Ser Downing", "587": "Ser Downing", "642": "Ser Duncan", "370": "Ser Edmonde", "643": "Ser Edwardo", "711": "Ser Elmest", "849": "Ser Elrend", "265": "Ser Elthar", "563": "Ser Estoma", "395": "Ser Ethen", "391": "Ser Ewart", "616": "Ser Eyst", "564": "Ser Faerma", "533": "Ser Falken", "138": "Ser Fedor", "144": "Ser Folke", "538": "Ser Ford", "200": "Ser Forden", "579": "Ser Fowald", "588": "Ser Fowald", "401": "Ser Francis", "638": "Ser Frants", "378": "Ser Frederick", "366": "Ser Gabrian", "543": "Ser Gammon", "631": "Ser Gaspar", "628": "Ser Gauche", "208": "Ser Gauwyn", "302": "Ser Georg", "565": "Ser Gerrick", "536": "Ser Gettys", "373": "Ser Gordan", "142": "Ser Gregor", "574": "Ser Grynt", "108": "Ser Gyles", "546": "Ser Hardy", "137": "Ser Henning", "146": "Ser Hewrey", "566": "Ser Holtor", "547": "Ser Hoyt", "567": "Ser Iga", "203": "Ser Ivo", "125": "Ser Jakob", "143": "Ser Jakys", "139": "Ser Jareth", "853": "Ser Jayce", "627": "Ser Jerremy", "321": "Ser Jerrome", "622": "Ser Jet", "568": "Ser Jirco", "394": "Ser Josiah", "636": "Ser Josidd", "145": "Ser Jovan", "630": "Ser Julius", "600": "Ser Kain", "311": "Ser Keene", "644": "Ser Kennis", "403": "Ser Kester", "202": "Ser Kestril", "540": "Ser Kyte", "621": "Ser Lanferd", "309": "Ser Larch", "199": "Ser Laurent", "390": "Ser Lenn", "626": "Ser Lore", "576": "Ser Lotar", "513": "Ser Lysther", "512": "Ser Macklyn", "843": "Ser Malkovich", "206": "Ser Marcas", "516": "Ser Marco", "646": "Ser Marlon", "209": "Ser Mathys", "141": "Ser Maximillian", "371": "Ser Mirek", "552": "Ser Morrison", "380": "Ser Mycal", "641": "Ser Naplay", "477": "Ser Nathaniel", "507": "Ser Nevitt", "140": "Ser Nichol", "634": "Ser Nikolas", "618": "Ser Noal", "475": "Ser Octavio", "511": "Ser Palotti", "369": "Ser Peregrine", "645": "Ser Petryo", "123": "Ser Pol", "620": "Ser Publius", "585": "Ser Quintus", "594": "Ser Quintus", "204": "Ser Raffe", "539": "Ser Ramaen", "109": "Ser Raster", "210": "Ser Raulin", "549": "Ser Ravenn", "573": "Ser Redd", "820": "Ser Reed", "323": "Ser Rickart", "388": "Ser Robert", "324": "Ser Roderick", "322": "Ser Ronell", "601": "Ser Ross", "551": "Ser Rustom", "518": "Ser Rylen", "266": "Ser Ryndall", "809": "Ser Sago (possibly? one of the knights that help with rescuing Aelinore from the Blighted Manse; purple clothing around armor; blonde hair; high ponytail)", "597": "Ser Sairus", "383": "Ser Samwe", "368": "Ser Sandro", "325": "Ser Serdic", "529": "Ser Shakil", "850": "Ser Sharlen", "712": "Ser Snowdredge", "619": "Ser Sossan", "842": "Ser Sterling", "530": "Ser Tascan", "377": "Ser Tavin", "124": "Ser Tedrick", "517": "Ser Terrance", "382": "Ser Thurstance", "514": "Ser Timius", "379": "Ser Tobin", "703": "Ser Tolth", "553": "Ser Tulius", "599": "Ser Tyrone", "532": "Ser Viceroth", "122": "Ser Vinson", "534": "Ser Vitlay", "207": "Ser Vyctor", "647": "Ser Warwick", "550": "Ser Welkland", "306": "Ser Westley", "617": "Ser Weston", "598": "Ser Whitby", "822": "Ser Wyckes", "632": "Ser Yohem", "508": "Ser York", "491": "Ser Zamir", "609": "Sienna", "162": "Simond", "826": "Sion", "339": "Sling", "581": "Smyth", "590": "Smyth", "376": "Sofiah", "727": "Soul", "728": "Spirits", "191": "Steffen", "841": "Stone", "188": "Sylvie", "134": "Symone", "701": "Tagert", "393": "The Fool", "836": "Thwan", "351": "Tilda", "353": "Tomazin", "193": "Tomlin", "223": "Unfinished character (possibly? only 214kb; game crashes when set as Caught NPC)", "014": "Valmiro", "254": "Vander", "261": "Vanna", "342": "Voulge", "846": "Walker", "219": "Walter", "350": "Wenda", "170": "Wilhem", "257": "Willhem", "834": "Wilson", "119": "Winifride", "704": "Wyndar", "808": "You (NPC Seneschal makes; False Peace ending)", "800": "Yves (possibly? Salomet's bandits in the Stone Quarry; Strider with short hair and beard; can't interact to see name since game crashes)", "735": "Zero"}

#windows wizardy to get the dpi right and suppress the console.
#under linux just having the extension as .pyw instead of .py should work.
import os
import ctypes
if os.name == 'nt':
	ctypes.windll.shcore.SetProcessDpiAwareness(True)
	kernel32 = ctypes.WinDLL('kernel32')
	user32 = ctypes.WinDLL('user32')
	SW_HIDE = 0
	hWnd = kernel32.GetConsoleWindow()
	user32.ShowWindow(hWnd, SW_HIDE)

#RamKromberg & FluffyQuack @ https://github.com/RamKromberg/pyDDDAsavetool
from dataclasses import dataclass
import struct
import zlib

@dataclass
class DDDASaveHeader:
	"""DDDA save header"""
	version: int = None
	unCompressedSize: int = None
	compressedSize: int = None
	u1: int = 860693325
	u2: int = 0
	u3: int = 860700740
	hash: int = None #crc32 of compressed save data
	u4: int = 1079398965
	littleEndian = True
	headerLength = 32
	def __init__(self, rawHeader=None):
		if rawHeader != None:
			self.parse(rawHeader)
	def parse(self, rawHeader):
		if len(rawHeader) != self.headerLength:
			raise ValueError("parse requires a buffer of 32 bytes" % rawHeader)
		version, unCompressedSize, compressedSize, u1, u2, u3, hash, u4 = struct.unpack('< I I I I I I I I', rawHeader)
		if version != 21:
			#TODO: incomplete and untested
			version, unCompressedSize, compressedSize, u1, u2, u3, hash, u4 = struct.unpack('> I I I I I I I I', rawHeader)
			littleEndian = False
		if (u1 != self.u1 or u2 != self.u2 or u3 != self.u3 or u4 != self.u4):
			raise ValueError("Invalid DDDASaveHeader" % rawHeader)
		else:
			self.version, self.unCompressedSize, self.compressedSize, self.hash = version, unCompressedSize, compressedSize, hash
	def serialize(self):
		if self.littleEndian:
			stuct = struct.pack('< I I I I I I I I', self.version, self.unCompressedSize, self.compressedSize, self.u1, self.u2, self.u3, self.hash, self.u4)
		else:
			stuct = struct.pack('> I I I I I I I I', self.version, self.unCompressedSize, self.compressedSize, self.u1, self.u2, self.u3, self.hash, self.u4)
		return stuct
	def __getitem__(self, item):
		if self.littleEndian:
			match item:
				case 0:
					return self.version
				case 1:
					return self.unCompressedSize
				case 2:
					return self.compressedSize
				case 3:
					return self.u1
				case 4:
					return self.u2
				case 5:
					return self.u3
				case 6:
					return self.hash
				case 7:
					return self.u4
				case int():
					raise IndexError("index \"%s\" out of range" % item)
				case str():
					try:
						return getattr(self, item)
					except:
						raise KeyError ("key \"%s\" out of range" % item)
				case _:
					raise TypeError('Unsupported type' % item)
		else:
			match item:
				case 0:
					return self.u4
				case 1:
					return self.hash
				case 2:
					return self.u3
				case 3:
					return self.u2
				case 4:
					return self.u1
				case 5:
					return self.compressedSize
				case 6:
					return self.unCompressedSize
				case 7:
					return self.version
				case int():
					raise IndexError("index \"%s\" out of range" % item)
				case str():
					try:
						return getattr(self, item)
					except:
						raise KeyError ("key \"%s\" out of range" % item)
				case _:
					raise TypeError('Unsupported type' % item)
	def __str__(self):
		if self.version == 21:
			return "Dragon's Dogma: Dark Arisen save header"
		elif self.version == 5:
			return "Dragon's Dogma original console save header"
		else:
			return str(type(self))

class DDDASave:
	header = DDDASaveHeader()
	data = None
	fileLength = 524288
	def __init__(self, buffer=None):
		if buffer != None:
			peek=buffer.peek(1)[0]
			match peek:
				case 21:
					self.openSav(buffer)
				case 5:
					#TODO: untested
					self.openSav(buffer)
				case 60:
					self.openXml(buffer)
				case _:
					raise ValueError ("magick byte %s unsupported" % peek)
	def openSav(self, buffer):
		self.header.parse(buffer.read(self.header.headerLength))
		data_compressed = buffer.read(self.fileLength-self.header.headerLength)
		self.data = zlib.decompress(data_compressed)
	def openXml(self, buffer):
		self.data = buffer.read()
		self.header.version = 21
	def compress(self, data=None):
		data = self.data if data==None else data
		return zlib.compress(data, 3) #h78 h5E = b01111000 = zlib level 4
	def checksum(self, data_compressed=None):
		data_compressed = self.compress() if data_compressed==None else data_compressed
		hash = (zlib.crc32(data_compressed) ^ -1) % (1<<32)
		return hash
	def checksize(self, data_compressed=None):
		data_compressed = self.compress() if data_compressed==None else data_compressed
		data_compressed_size = len(data_compressed)
		return data_compressed_size
	def unpack(self, data=None):
		#xml output
		data = self.data if data==None else data
		return data.decode('utf-8')
	def __str__(self, data=None):
		data = self.data if data==None else data
		return self.unpack(data)
	def convert(self, data=None):
		#TODO: endian and pc-to-console-to-pc stuff...
		data = self.data if data==None else data
		if data.decode('utf-8')[-9:] == "</class>\n":
			print("PC save")
	def pack(self, data=None):
		#compress the new data
		data_compressed = self.compress() if data==None else self.compress(data)
		#update the header
		self.header.unCompressedSize = len(self.data) if data==None else len(data)
		self.header.compressedSize = self.checksize(data_compressed)
		self.header.hash = self.checksum(data_compressed)
		#put the updated header and compressed data together in a pre-padded bytearray and return it for write out
		compBuffer = bytearray(b'\0' * self.fileLength)
		for i, c in enumerate(self.header.serialize()):
			compBuffer[i] = c
		for i, c in enumerate(data_compressed):
			compBuffer[i+32] = c
		return(compBuffer)

#takes string file path
#returns lxml etree
def load_sav(file):
	f = open(file,"rb")
	save_str = DDDASave(f).unpack()
	save_str = save_str[save_str.find('\n'):] #lxml.etree.fromstring() doens't work with the first line's xml decleration
	tree = etree.fromstring(save_str)
	f.close()
	return tree

import io
#takes lxml etree, string file path
def save_sav(tree, file):
	tree_bytesio = io.BytesIO(etree.tostring(tree, xml_declaration=False, encoding="utf-8", doctype='<?xml version="1.0" encoding="utf-8"?>')+b"\n")
	tree_bytesio.seek(0)
	tree_bufferedreader = io.BufferedReader(tree_bytesio)
	save = DDDASave(tree_bufferedreader)
	file=open(file,'wb')
	file.write(save.pack())
	file.close()

#takes string file path
#returns lxml etree
def load_xml(file):
	f = open(file,"r")
	tree = etree.parse(f)
	f.close()
	return tree

#takes lxml etree, string file path
def save_xml(tree, file):
	file=open(file,'wb')
	out = etree.tostring(tree, xml_declaration=False, encoding="utf-8", doctype='<?xml version="1.0" encoding="utf-8"?>')+b"\n"
	file.write(out)
	file.close()

#wraps up all the node operations while keeping the various lists in-sync
class DDDASaveTree:
	_ddda_npc_ids = ddda_npc_ids
	tree = None
	_npcs_elements = ()
	npcs = ()
	npcs_ids = ()
	npcs_affinities = ()
	_caught_element = None
	_caught = None
	_caught_id = None
	_ring_element = None
	_ring = None
	_ring_id = None
	def __init__(self, tree):
		self.tree=tree
		self._get_npcs()
		self._get_caught()
		self._get_ring()
	def _get_npcs(self):
		#u/CyncoV @ https://www.reddit.com/r/DragonsDogma/comments/oejjqf/modmodding_tool_to_be_able_to_edit_npc_affinity/h4770xz/
		#quick save: <class name="mPlayerDataManual" type="sSave::playerData">
		#checkpoint: <class name="mPlayerDataBase" type="sSave::playerData">
		___npcs_elements=tuple(self.tree.findall(".//class[@name='mPlayerDataManual']//s16[@name='mFriendPoint']"))
		__npcs_elements, _npcs_ids, _npcs, _npcs_affinities = [], [], [], []
		for idx, npc in enumerate(___npcs_elements):
			idx_str=f'{idx:03d}' #pads zeros so a "1" becomes a "001"
			if idx_str in self._ddda_npc_ids:
				_npcs_ids.append(idx)
				_npcs.append(self._ddda_npc_ids[idx_str])
				_npcs_affinities.append(npc.attrib['value'])
				__npcs_elements.append(npc)
		npcs_zipped = zip(_npcs_ids, _npcs, _npcs_affinities, __npcs_elements)
		npcs_zipped_sorted = sorted(npcs_zipped, key = lambda x: x[1])
		#npcs_zipped_sorted = sorted(npcs_zipped, key = operator.itemgetter(1)) #cProfile looks roughly the same
		self.npcs_ids, self.npcs, self.npcs_affinities, self._npcs_elements = zip(*npcs_zipped_sorted)
	def _get_pos_by_id(self, id):
		if isinstance(id, str):
			id=int(id)
		return self.npcs_ids.index(id)
	def get_npc(self,id):
		pos=self._get_pos_by_id(id)
		return self.npcs[pos]
	def get_affinity(self, id):
		pos=self._get_pos_by_id(id)
		return self.npcs_affinities[pos]
	def set_affinity(self, id, value):
		pos=self._get_pos_by_id(id)
		self._npcs_elements[pos].attrib['value'] = value
		self._get_npcs()

	def _get_caught(self):
		#u/SordidDreams @ https://www.reddit.com/r/DragonsDogma/comments/48kkfp/changing_your_kidnapped_beloved_by_editing_the/
		#<s32 name="mCaughtNpcId" value="-1"/>
		#<s32 name="mRingNpcId" value="-1"/>
		self._caught_element=self.tree.findall(".//class[@name='mPlayerDataManual']//s32[@name='mCaughtNpcId']")[0]
		self._caught_id=int(self._caught_element.attrib['value'])
		if self._caught_id == -1:
			self._caught = "-None-"
		elif self._caught_id in self.npcs_ids:
			self._caught = self.get_npc(self._caught_id)
		else:
			self._caught = "№"+str(self._caught_id)
	@property
	def caught(self):
		return self._caught
	@property
	def caught_id(self):
		return self._caught_id
	@caught_id.setter
	def caught_id(self, id):
		self._caught_id = id
		if id == -1:
			self._caught_element.attrib['value'] = "-1"
			self._caught = "-None-"
		else:
			self._caught_element.attrib['value'] = str(self._caught_id)
			if id in self.npcs_ids:
				self._caught = self.get_npc(self._caught_id)
			else:
				self._caught = "№"+str(self._caught_id)
	def _get_ring(self):
		self._ring_element=self.tree.findall(".//class[@name='mPlayerDataManual']//s32[@name='mRingNpcId']")[0]
		self._ring_id=int(self._ring_element.attrib['value'])
		if self._ring_id == -1:
			self._ring = "-None-"
		elif self._ring_id in self.npcs_ids:
			self._ring = self.get_npc(self._ring_id)
		else:
			self._ring = "№"+str(self._ring_id)
	@property
	def ring(self):
		return self._ring
	@property
	def ring_id(self):
		return self._ring_id
	@ring_id.setter
	def ring_id(self, id):
		self._ring_id = id
		if id == -1:
			self._ring_element.attrib['value'] = "-1"
			self._ring = "-None-"
		else:
			self._ring_element.attrib['value'] = str(self._ring_id)
			if id in self.npcs_ids:
				self._ring = self.get_npc(self._ring_id)
			else:
				self._ring = "№"+str(self._ring_id)

#just jumps to the first letter
#TODO: full search...
class BasicSearchCombobox(ttk.Combobox):
	def __init__(self, master, **kwargs):
		ttk.Combobox.__init__(self, master, **kwargs)
		self['state']='readonly'
		self.bind('<KeyPress>', self.onBox)
		self._bind(('bind', self.listbox()),"<KeyRelease>", self.onPopdown, None)
	def popdown(self, **kwargs):
		return self.tk.call('ttk::combobox::PopdownWindow', self)
	def listbox(self, **kwargs):
		return self.popdown(**kwargs)+'.f.l'
	def onPopdown(self, evt):
		key = evt.keysym.capitalize()
		curPos=self.master.tk.eval(self.listbox()+' curselection')
		cur=self.master.tk.eval(self.listbox()+' get '+curPos)
		vals = self['values']
		self.current(curPos)
		if key != cur[0].capitalize():
			for val in vals:
				if key == val[0].capitalize():
					pos = vals.index(val)
					pos = str(pos)
					self.master.tk.eval(self.listbox()+' selection clear 0 end')
					self.master.tk.eval(self.listbox()+' selection set '+pos)
					self.master.tk.eval(self.listbox()+' activate '+pos)
					self.master.tk.eval(self.listbox()+' see '+pos)
					self.current(pos)
					break
		self.select_range(0, tk.END)
	def onBox(self, evt):
		key = evt.keysym.capitalize()
		cur = self.get()
		vals = self['values']
		if cur != "":
			if key != cur[0].capitalize():
				for val in vals:
					if key == val[0].capitalize():
						pos = vals.index(val)
						self.current(pos)
						break
		self.select_range(0, tk.END)

#DONE: editable entries, column sort, basic by-first-letter search
#TODO: full search...
class Treeview(ttk.Treeview):
	# customized https://stackoverflow.com/questions/18562123/how-to-make-ttk-treeviews-rows-editable
	def __init__(self, master, editable_columns=(), descending=(), sort_type=(), *args, **kwargs):
		self.editable_columns=editable_columns
		self.descending=descending
		self.sort_type=sort_type
		super().__init__(master, *args, **kwargs)
		self.bind("<Double-1>", lambda event: self.onDoubleClick(event))
		self.bind("<ButtonRelease-1>", lambda event: self.onSingleClickRelease(event))
		self.bind("<KeyPress>", lambda event: self.onKeyPress(event))
		self.bind("<<TreeviewSelect>>", lambda event: self.onTreeviewSelect(event))
		self.event_add('<<TreeViewRecordChange>>', 'None')

	#destroy existing entries on selection changes
	def onTreeviewSelect(self, event):
		try:
			self.entryPopup.destroy()
		except AttributeError:
			pass

	#entry popup
	def onDoubleClick(self, event):
		row = self.identify_row(event.y)
		col = self.identify_column(event.x)

		if not row:
			return

		if col not in self.editable_columns:
			return

		x,y,width,height = self.bbox(row, col)

		pady = height // 2

		text = self.item(row, 'values')[int(col[1:])-1]
		self.entryPopup = EntryPopup(self, row, int(col[1:])-1, text)
		self.entryPopup.place(x=x, y=y+pady, width=width, height=height+2, anchor='w')

	#search
	#just jumps to the first letter
	#TODO: full search...
	def onKeyPress(self, event):
		vals = []
		for iid in self.get_children():
			vals.append(self.item(iid, "values")[0])
		key = event.keysym.capitalize()
		for val in vals:
			if key == val[0].capitalize():
				pos = vals.index(val)
				self.yview(pos)
				break

	#sort on column click
	def onSingleClickRelease(self, event):
		row = self.identify_row(event.y)
		col = self.identify_column(event.x)
		if not row:
			if col and self.identify("region", event.x, event.y) == "heading":
				self.sort(int(col[1:])-1)
			return
	def sort(self, col):
		if len(self.descending) >= col+1:
			descend=self.descending[col]
		else:
			descend=False
		if len(self.sort_type) >= col+1:
			sort_type=self.sort_type[col]
		else:
			sort_type=str

		data = [(self.set(item, col), item) for item in self.get_children('')]
		if sort_type==int:
			data.sort(reverse=descend, key=lambda x: int(x[0]))
		else:
			data.sort(reverse=descend)

		for index, (val, item) in enumerate(data):
			self.move(item, '', index)
		self.descending=[not x for x in self.descending]

class EntryPopup(ttk.Entry):
	def __init__(self, master, iid, column, text, **kw):
		ttk.Style().configure('pad.TEntry', padding='1 1 1 1')
		super().__init__(master, style='pad.TEntry', **kw)
		self.tv = master
		self.iid = iid
		self.column = column

		self.insert(0, text)
		self['exportselection'] = False

		self.focus_force()
		self.select_all()
		self.bind("<Return>", self.on_return)
		self.bind("<Control-a>", self.select_all)
		self.bind("<Escape>", lambda *ignore: self.destroy())

	def on_return(self, event):
		rowid = self.tv.focus()
		vals = self.tv.item(rowid, 'values')
		vals = list(vals)
		vals[self.column] = self.get()
		self.tv.item(rowid, values=vals)
		self.tv.event_generate("<<TreeViewRecordChange>>");
		self.destroy()

	def select_all(self, *ignore):
		self.selection_range(0, 'end')
		return 'break'

	def destroy(self):
		ttk.Entry.destroy(self)

class AffinitiesTab(ttk.Frame):
	def __init__(self, container):
		super().__init__(container)

		self.tree=None
		self.master.master.master.master.bind('<<TreeLoaded>>', self.load_tree)

		affinitiesframe = ttk.Frame(self, style='Card.TFrame')
		self.treeview_affinities_scrollbar = ttk.Scrollbar(affinitiesframe, orient ="vertical")
		self.treeview_affinities = Treeview(affinitiesframe, columns=('c1', 'c2'), editable_columns=('#2'), descending=(True,False), sort_type=(str,int), show='headings', selectmode ='browse', height=25)
		self.treeview_affinities_scrollbar.config(command = self.treeview_affinities.yview)
		self.treeview_affinities.heading('c1', text='Name')
		self.treeview_affinities.heading('c2', text='Affinity')
		self.treeview_affinities.column('c2', minwidth=70)
		self.treeview_affinities.column('c1', minwidth=320)
		self.treeview_affinities.config(yscrollcommand=self.treeview_affinities_scrollbar.set)
		self.treeview_affinities.bind('<<TreeViewRecordChange>>', self.treeview_affinities_callback)

		caughtframe = ttk.Frame(self, style='Card.TFrame')
		self.combobox_caught_value = StringVar()
		self.combobox_caught_value.trace_add('write', self.combobox_caught_callback)
		label_caught = ttk.Label(caughtframe, style='TLabel', text = "Caught:")
		self.combobox_caught = BasicSearchCombobox(caughtframe, style='TCombobox', state='readonly', textvariable = self.combobox_caught_value, name="box_caught")

		ringframe = ttk.Frame(self, style='Card.TFrame')
		self.combobox_ring_value = StringVar()
		self.combobox_ring_value.trace_add('write', self.combobox_ring_callback)
		label_ring = ttk.Label(ringframe, style='TLabel', text = "Ring:")
		self.combobox_ring = BasicSearchCombobox(ringframe, style='TCombobox', state='readonly', textvariable = self.combobox_ring_value, name="box_ring")

		#layout
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		affinitiesframe.pack(fill="both",pady=2)
		self.treeview_affinities.pack(side="left",fill="both",padx=1)
		self.treeview_affinities_scrollbar.pack(side="right",fill="y",padx=1)
		caughtframe.pack(side="bottom",fill="both",pady=2,padx=2)
		label_caught.pack(side="left")
		self.combobox_caught.pack(side="right",fill="both")
		self.combobox_caught.configure(width=35)
		ringframe.pack(side="bottom",fill="both",pady=2,padx=2)
		label_ring.pack(side="left")
		self.combobox_ring.pack(side="right",fill="both")
		self.combobox_ring.configure(width=35)

	def treeview_affinities_callback(self, *event):
		iid=int(self.treeview_affinities.focus())
		entry=self.treeview_affinities.item(iid, "values")[1]
		if entry == "":
			entry = 0
		elif entry.isnumeric():
			entry = int(entry)
			if entry > 1000:
				entry = 1000
		else:
			entry = self.tree.npcs_affinities[int(iid)]
		self.treeview_affinities.set(iid, column="#2", value=entry)
		self.tree.set_affinity(self.tree.npcs_ids[iid], str(entry))

	def combobox_ring_callback(self, var, index, mode):
		cur = self.combobox_ring.current()
		if cur == 0:
			ring_value = -1
		else:
			curStr = self.combobox_ring.get()
			if curStr[0] == "№":
				ring_value = int(curStr[1:])
			else:
				ring_value = self.tree.npcs_ids[cur-1]
		self.tree.ring_id = ring_value

	def combobox_caught_callback(self, var, index, mode):
		cur = self.combobox_caught.current()
		if cur == 0:
			caught_value = -1
		else:
			curStr = self.combobox_caught.get()
			if curStr[0] == "№":
				caught_value = int(curStr[1:])
			else:
				caught_value = self.tree.npcs_ids[cur-1]
		self.tree.caught_id = caught_value

	def load_tree(self, *event):
		self.tree=self.master.master.master.master.tree
		self.treeview_affinities.delete(*self.treeview_affinities.get_children())
		for idx, npc in enumerate(self.tree.npcs):
			self.treeview_affinities.insert('', tk.END, iid=str(idx), values=(npc, self.tree.npcs_affinities[idx]))

		if self.tree.caught[0] == "№":
			self.combobox_caught['values'] = ['-None-']+list(self.tree.npcs)+[self.tree.caught]
		else:
			self.combobox_caught['values'] = ['-None-']+list(self.tree.npcs)
		self.combobox_caught.set(self.tree.caught)

		if self.tree.ring[0] == "№":
			self.combobox_ring['values'] = ['-None-']+list(self.tree.npcs)+[self.tree.ring]
		else:
			self.combobox_ring['values'] = ['-None-']+list(self.tree.npcs)
		self.combobox_ring.set(self.tree.ring)

class App(tk.Tk):
	tree = None
	def __init__(self):
		super().__init__()

		title = "DDDA Save Affinity Editor"
		self.title(title)
		self.resizable(height = False, width = False)
		frame = ttk.Frame(self, style='Card.TFrame')
		tabCtrl = ttk.Notebook(frame, style='TNotebook')
		affinitiesTab = ttk.Frame(tabCtrl, style='TNotebook.Tab')
		tabCtrl.add(affinitiesTab, text ='Affinities')

		affinitiesframe = AffinitiesTab(affinitiesTab)

		saveloadframe = ttk.Frame(frame, style='Card.TFrame')
		load_button=ttk.Button(saveloadframe, style='Accent.TButton', text='Load...', width=7, command=self.load_file)
		save_button=ttk.Button(saveloadframe, style='Accent.TButton', text='Save...', width=7, command=self.save_file)

		#layout
		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)
		frame.pack(padx=1, pady=1)
		tabCtrl.pack(padx=1, pady=1)
		affinitiesframe.pack(padx=1, pady=1)

		saveloadframe.pack(padx=2, pady=2)
		load_button.pack(side="left", padx=2, pady=2)
		save_button.pack(side="left", padx=2, pady=2)

		if sv_ttk:
			sv_ttk.set_theme("dark")
			font_nameprefix="SunValley"
			font_names = ("Caption", "Body", "BodyStrong", "BodyLarge", "Subtitle", "Title", "TitleLarge", "Display")
			font_scale_add = 1.2
		else:
			font_nameprefix="Tk"
			font_names = ("Default", "Text", "Fixed", "Menu", "Heading", "Caption", "SmallCaption", "Icon", "Tooltip")
			font_scale_add = 1.1
		for font in font_names:
			font = tkFont.nametofont(f"{font_nameprefix}{font}Font")
			size = font.cget("size")
			font.configure(size=math.ceil(int(size)*font_scale_add))
		ttk.Style().configure("Accent.TButton", padding=2)
		ttk.Style().configure("TCombobox", padding=2)
		ttk.Style().configure("TNotebook", padding=1)
		ttk.Style().configure("TNotebook.Tab", padding=1, width=8)
		self.mainloop()

	def load_file(self):
		filetypes = (
			('DDDA unpacked save', '*.sav.xml'),
			('DDDA save', '*.sav'),
			('All types', '*.*')
		)
		filename = filedialog.askopenfilename(
			title='Open a save file xml/sav',
			initialdir='./',
			filetypes=filetypes)
		if filename!="":
			if filename[-3:]=="sav":
				try:
					self.tree = DDDASaveTree(load_sav(filename))
				except:
					messagebox.showerror(title="Pawn 9000", message="I'm sorry, Ser " + os.getlogin() + ", I'm afraid I can't do that.")
			else:
				try:
					self.tree = DDDASaveTree(load_xml(filename))
				except:
					messagebox.showerror(title="Pawn 9000", message="I'm sorry, Ser " + os.getlogin() + ", I'm afraid I can't do that.")
		self.event_generate("<<TreeLoaded>>");

	def save_file(self):
		if self.tree == None:
			messagebox.showerror(title="Pawn 9000", message="I'm sorry, Ser " + os.getlogin() + ", I'm afraid I can't do that.")
			return
		filetypes = (
			('DDDA unpacked save', '*.sav.xml'),
			('DDDA save', '*.sav'),
			('All types', '*.*')
		)
		filename = filedialog.asksaveasfilename(
			title='Write a DDDA save file xml',
			initialdir='./',
			filetypes=filetypes,
			defaultextension=".xml")
		if filename:
			if filename[-3:]=="sav":
				save_sav(self.tree.tree, filename)
			else:
				save_xml(self.tree.tree, filename)

def main():
	app = App()
	app.mainloop()

if __name__ == '__main__':
	main()
