#!/usr/bin/env python

# Dragon's Dogma: Dark Arisen Save Game Affinity Editor
# 2023-09-29
# nowahNOwah @ https://www.nexusmods.com/users/183050388
#
# depends on "pip install lxml sv_ttk"
# https://lxml.de/
# https://github.com/rdbende/Sun-Valley-ttk-theme/

from lxml import etree
import tkinter as tk
from tkinter import ttk
from tkinter import Entry
from tkinter import filedialog
from tkinter import messagebox
from tkinter import StringVar
from tkinter.ttk import Combobox
import sv_ttk

#gamesrule1124 @ http://fluffyquack.com/DD/txt/npc-list.txt
ddda_npc_ids = {"001": "Adaro", "002": "Quina", "002_01": "Quina (At the Abbey)", "003": "Merin", "004": "Mayra", "005": "Lewes", "006": "Pablos", "007": "Madeleine", "008": "Benita", "009": "Heraldo", "010": "Aestella", "011": "Iola", "012": "Inez", "013": "Rorric", "014": "Valmiro", "015": "Barten", "016": "Elonzo", "017": "Elvar", "018": "Alethea", "019": "Alita", "020": "Clemente", "021": "Sentena ", "022": "Ema", "023": "Ramon", "024": "Janielle", "025": "Jaquan", "026": "Fredro", "027": "Chaves", "028": "Arnot", "029": "Lesia", "030": "Marthena", "031": "Alejo", "032": "Lazoro", "033": "Estevon", "034": "Chas", "035": "Grecio", "036": "Poll", "037": "Rojay", "038": "Auster", "039": "Sentena again", "040": "Ema again", "041": "Ramon again", "042": "Janielle again", "043": "Alejo (Injured, before Floral Delivery quest. Strangely, has Jaquan's Character Model) ", "044": "Lazoro again", "101": "Duke Edmun Dragon's Bane", "101_01": "Duke Edmun Dragon's Bane (Unidentified Variation)", "102": "Aelinore", "102_01": "Aelinore (Hair down)", "102_02": "Aelinore (Post game beloved)", "103": "Feste", "104": "Julien (Full Armor and Helmet during Seeking Salvation quest)", "104_01": "Julien (Unknown Variation)", "104_02": "Julien (Around the Duke's Demesne)", "104_03": "Julien (Unknown Variation)", "104_04": "Julien (Normal Clothing; While in Dungeon or Post Game Beloved)", "105": "Aldous", "106": "Fedel", "107": "Domenique", "108": "Ser Gyles", "109": "Ser Raster", "110": "Ambrose", "111": "Randell", "112": "Pering", "113": "Orsay", "114": "Raulin", "115": "Esperaunce", "116": "Margery", "117": "Mirabelle", "117_01": "Mirabelle (No character changes noticed after multiple playthroughs or setting as Post Game Beloved, may be for the Blighted Manse Cutscene)", "118": "Josephine", "119": "Winifride", "120": "Ser Deric", "121": "Ser Dirke", "122": "Ser Vinson", "123": "Ser Pol", "124": "Ser Tedrick", "125": "Ser Jakob", "126": "Ansell", "127": "Geffrey", "128": "Haslett", "129": "Edgar", "130": "Maxson", "131": "Hilde", "132": "Milly", "133": "Fournival", "134": "Symone", "135": "Mellard", "136": "Fancey", "137": "Ser Henning", "138": "Ser Fedor", "139": "Ser Jareth", "140": "Ser Nichol", "141": "Ser Maximillian", "142": "Ser Gregor", "143": "Ser Jakys", "144": "Ser Folke", "145": "Ser Jovan", "146": "Ser Hewrey", "147": "Asalam", "148": "Meridith", "149": "Caxton", "150": "Gwine", "151": "Camellia", "152": "Judith", "153": "Devyn", "154": "Arsmith", "155": "Nettie", "156": "Mountebank", "157": "Barnaby", "158": "Mason", "159": "Mathewe", "160": "Brice", "161": "Lena", "162": "Simond", "163": "Osip", "164": "Marla", "165": "Maurin", "166": "Eugen", "167": "Howlen", "168": "Humphrauy", "169": "Austine", "170": "Wilhem", "171": "Garvin", "172": "Carel", "173": "Conwey", "174": "Morys", "175": "Milberowe", "176": "Pernill", "177": "Martha", "178": "Katlyn", "179": "Flavian", "180": "Jasper", "181": "Nils", "182": "Josua", "183": "Merrick", "184": "Rychard", "185": "Danton", "186": "Sara", "187": "Cale", "188": "Sylvie", "189": "Guston", "190": "Aric", "191": "Steffen", "192": "Cornelius", "193": "Tomlin", "194": "Pip", "195": "Emme", "196": "Kassie", "197": "Ser Auguste", "198": "Ser Alvert", "199": "Ser Laurent", "200": "Ser Forden", "201": "Ser Aerick", "202": "Ser Kestril", "203": "Ser Ivo", "204": "Ser Raffe", "205": "Ser Camillus", "206": "Ser Marcas", "207": "Ser Vyctor", "208": "Ser Gauwyn", "209": "Ser Mathys", "210": "Ser Raulin", "211": "Ser Bayard", "212": "Ser Cyriac", "213": "Josias", "214": "Lucie", "215": "Baudric", "216": "Agnes", "217": "Hobert", "218": "Jenlyns", "219": "Walter", "220": "Aemelie", "221": "Hewrey", "222": "Philippa", "223": "Possibly Unfinished Character, only 214kb. Crashes game when set as Caught NPC.", "253": "Hender", "254": "Vander", "255": "Abram", "256": "Frost", "257": "Willhem", "258": "Bawdwyn", "259": "Pipa", "260": "Isabel", "261": "Vanna", "262": "Jolette", "263": "Jean", "264": "Ser Adraenn", "265": "Ser Elthar", "266": "Ser Ryndall", "267": "Ser Cyril", "301": "Mercedes", "302": "Ser Georg", "303": "Ser Berne", "304": "Reynard", "305": "Ser Cyrus", "306": "Ser Westley", "307": "Ser Arman", "308": "Ser Devers", "309": "Ser Larch", "310": "Ser Datson", "311": "Ser Keene", "312": "Ser Bernis", "321": "Ser Jerrome", "322": "Ser Ronell", "323": "Ser Rickart", "324": "Ser Roderick", "325": "Ser Serdic", "326": "Ser Bryan", "327": "Clarus", "328": "Anri", "329": "Ilona", "330": "Janne", "331": "Charlene", "332": "Maul", "333": "Mercygiver", "334": "Hammer", "335": "Falchion", "336": "Ranseur", "337": "Lance", "338": "Culverin", "339": "Sling", "340": "Claymore", "341": "Basilard", "342": "Voulge", "343": "Anelace", "344": "Glaive", "345": "Caravel", "346": "Mace", "347": "Pike", "348": "Ophis", "349": "Jonna", "350": "Wenda", "351": "Tilda", "352": "Fayth", "353": "Tomazin", "354": "Purnell", "355": "Sens", "356": "Honna", "357": "Holle", "358": "Dasya", "359": "Nelle", "360": "Ola", "361": "Cele", "362": "Aurene", "363": "Betiah", "364": "Ser Daerio", "365": "Ser Castor", "366": "Ser Gabrian", "367": "Ser Anso", "368": "Ser Sandro", "369": "Ser Peregrine", "370": "Ser Edmonde", "371": "Ser Mirek", "372": "Ser Alastair", "373": "Ser Gordan", "374": "Ser Chesleigh", "375": "Selene", "376": "Sofiah", "377": "Ser Tavin", "378": "Ser Frederick", "379": "Ser Tobin", "380": "Ser Mycal", "381": "Ser Adem", "382": "Ser Thurstance", "383": "Ser Samwe", "384": "Ser Constans", "385": "Nilson", "386": "Robyn", "387": "Cutting", "388": "Ser Robert", "389": "Ser Abell", "390": "Ser Lenn", "391": "Ser Ewart", "392": "Dragonforged", "393": "The Fool", "394": "Ser Josiah", "395": "Ser Ethen", "396": "Rowland", "397": "Danell", "398": "Alon", "399": "Jayce", "400": "Mathias", "401": "Ser Francis", "402": "Ser Cutbert", "403": "Ser Kester", "404": "Ecbal", "411": "Joye, a pawn merchant in Post Game Everfall. Different clothes when chosen as Caught NPC, shop function doesn't work. Resembles a Cassardi villager who is killed in the Dragon attack.", "412": "Joye", "413": "Joye", "414": "Joye", "415": "Joye", "416": "Joye", "417": "Joye", "418": "Joye", "419": "Joye", "420": "Joye", "421": "Joye", "422": "Joye", "423": "Joye", "424": "Joye", "425": "Joye", "426": "Joye", "427": "Joye", "428": "Joye", "429": "Joye", "430": "Joye", "431": "Joye (The actual one with normal clothing and functioning shop)", "432": "Delec (Pawn Merchant)", "433": "Akim (Pawn Merchant in Everfall Post Game)", "434": "Alonso", "475": "Ser Octavio", "476": "Ser Alfonso", "477": "Ser Nathaniel", "478": "Ser Baird", "480": "Enric", "481": "Karina", "482": "Miles", "483": "Ferris", "490": "Ser Alisander", "491": "Ser Zamir", "492": "Ser Alden", "493": "Ser Belus", "501": "Cortese", "502": "Rickard", "503": "Piell", "504": "Rook", "505": "Estoni", "506": "Ser Cashew", "507": "Ser Nevitt", "508": "Ser York", "509": "Ser Antonio", "510": "Ser Ashrore", "511": "Ser Palotti", "512": "Ser Macklyn", "513": "Ser Lysther", "514": "Ser Timius", "515": "Ser Brinden", "516": "Ser Marco", "517": "Ser Terrance", "518": "Ser Rylen", "519": "Ser Audric", "520": "Marcelo", "521": "Graham", "522": "Manning", "523": "Margaritte (Salvation Member)", "524": "Cicero", "525": "Fonio", "526": "Cristofer", "527": "Asthea (Salvation Member)", "528": "Carmel (Salvation Member)", "529": "Ser Shakil", "530": "Ser Tascan", "531": "Ser Covan", "532": "Ser Viceroth", "533": "Ser Falken", "534": "Ser Vitlay", "535": "Ser Burton", "536": "Ser Gettys", "537": "Anbros", "538": "Ser Ford", "539": "Ser Ramaen", "540": "Ser Kyte", "541": "Ser Chandra", "542": "Ser Brigante", "543": "Ser Gammon", "544": "Salomet", "545": "Ser Dill ", "546": "Ser Hardy", "547": "Ser Hoyt", "548": "Ser Arachis", "549": "Ser Ravenn", "550": "Ser Welkland", "551": "Ser Rustom", "552": "Ser Morrison", "553": "Ser Tulius", "554": "Orlmer", "555": "Burgess", "556": "Cobalt", "557": "Sandor", "558": "Florian", "559": "Ser Andorf", "560": "Ser Bacell", "561": "Ser Cronnel", "562": "Ser Diggan", "563": "Ser Estoma", "564": "Ser Faerma", "565": "Ser Gerrick", "566": "Ser Holtor", "567": "Ser Iga", "568": "Ser Jirco", "569": "Kent", "570": "Lowane", "571": "Moditt", "572": "Nabarough", "573": "Ser Redd", "574": "Ser Grynt", "575": "Ser Burrell", "576": "Ser Lotar", "577": "Ser Apera", "578": "Ser Downing", "579": "Ser Fowald", "580": "Ser Bax", "581": "Smyth", "582": "Jouwn", "583": "Gatte", "584": "Odnall", "585": "Ser Quintus", "586": "Ser Apera", "587": "Ser Downing", "588": "Ser Fowald", "589": "Ser Bax", "590": "Smyth", "591": "Jouwn", "592": "Gatte", "593": "Odnall", "594": "Ser Quintus", "595": "Baden", "596": "Amity", "597": "Ser Sairus", "598": "Ser Whitby", "599": "Ser Tyrone", "600": "Ser Kain", "601": "Ser Ross", "602": "Ser Dorgann", "603": "Ser Curtis", "604": "Perrin", "605": "Carya", "606": "Johann", "607": "Patt", "608": "Lelou", "609": "Sienna", "610": "Duke Edmun Dragonsbane (Old)", "611": "Elysion", "612": "Murphey", "613": "Samara", "614": "Klemt", "615": "Pom ", "616": "Ser Eyst", "617": "Ser Weston", "618": "Ser Noal", "619": "Ser Sossan", "620": "Ser Publius", "621": "Ser Lanferd", "622": "Ser Jet", "623": "Ser Dennep", "624": "Ser Balter", "625": "Ser Arbel", "626": "Ser Lore", "627": "Ser Jerremy", "628": "Ser Gauche", "629": "Ser Clyde", "630": "Ser Julius", "631": "Ser Gaspar", "632": "Ser Yohem", "633": "Ser Defloe", "634": "Ser Nikolas", "635": "Ser Bastian", "636": "Ser Josidd", "637": "Ser Aloyis", "638": "Ser Frants", "639": "Ser Auber", "640": "Ser Borone ", "641": "Ser Naplay", "642": "Ser Duncan", "643": "Ser Edwardo", "644": "Ser Kennis", "645": "Ser Petryo", "646": "Ser Marlon", "647": "Ser Warwick", "648": "Ser Callister", "649": "Ser Dornkirk", "700": "Dillan", "701": "Tagert", "702": "Balsac", "703": "Ser Tolth", "704": "Wyndar", "705": "Nicolas", "706": "Cortese", "707": "Jorgen", "708": "Esme", "709": "Nessa", "710": "Hera", "711": "Ser Elmest", "712": "Ser Snowdredge", "713": "Joye", "720": "Johnathan", "725": "Phantom", "726": "Ghost", "727": "Soul", "728": "Spirits", "729": "Darkness", "730": "Raven", "731": "Hawk", "732": "Condor", "733": "Rouge", "734": "Noir", "735": "Zero", "740": "Joye (The Seneschal?)", "741": "Joye (Ser Caraway?)", "745": "Joye (Ser Pierre?)", "746": "Joye (Ser Flint?)", "747": "Joye (Ser Siegel?)", "748": "Joye (Ser Ritter?)", "749": "Joye", "750": "Quince (Everfall)", "781": "Faircrest", "782": "Rochelle", "783": "Olra (Cassardi Docks & Bitterblack Isle)", "784": "Barroch", "785": "Ashe", "786": "Grette", "787": "Olra (Pawn)", "788": "Joye", "789": "Joye", "790": "Joye, yet again.", "791": "Joye, his NPC may be a place holder for NPC's that are not supposed to be edited or seen outside of their normal area.", "800": "Yves? One of Salomet's bandits in the Stone Quarry, Strider with short hair and beard. Can't interact to see name, Game Crashes.", "801": "One of Salomet's Bandits, a Warrior.", "802": "One of Salomet's Bandits, a Warrior", "803": "One of Salomet's Bandits, The Magick user.", "807": "Possibly Seneschal? Game Crashes whenset as Caught NPC", "808": "You (NPC Seneschal makes, False Peace Ending)", "809": "Ser Sago? One of the knights that help with rescuing Aelinore from the Blighted manse. Purple clothing around armor. Blonde Hair. High Ponytail.", "810": "Ser Airhart? One of the knights that help with rescuing Aelinore from the Blighted manse. Purple clothing around armor. Long Hair.", "820": "Ser Reed", "821": "Ser Azarel", "822": "Ser Wyckes", "823": "Cedric", "824": "Kellen", "825": "Drew", "826": "Sion", "827": "Ralph", "828": "Ser Caesey", "829": "Ser Byrt", "830": "Ser Carrot", "831": "Cordovan", "832": "Emzie", "833": "Garrett", "834": "Wilson", "835": "Corti", "836": "Thwan", "837": "Landon", "838": "Clarke", "839": "Russet", "840": "Antony", "841": "Stone", "842": "Ser Sterling", "843": "Ser Malkovich", "844": "Otzi", "845": "Ewald", "846": "Walker", "847": "Bonneau", "848": "Ser Basius", "849": "Ser Elrend", "850": "Ser Sharlen", "851": "Keenan", "852": "Alastor", "853": "Ser Jayce", "854": "Ser Colby"}

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

#pure
#takes string file path
#returns lxml etree
def load_tree(file):
	f = open(file,"r")
	tree = etree.parse(f)
	f.close()
	return tree

#pure
#takes the etree
#returns 3 lists of ints, strs and strs for the xml position, matching npc name and matching npc affinity value
def survey_friends(tree):
	#u/CyncoV @ https://www.reddit.com/r/DragonsDogma/comments/oejjqf/modmodding_tool_to_be_able_to_edit_npc_affinity/h4770xz/
	#quick save: <class name="mPlayerDataManual" type="sSave::playerData">
	#checkpoint: <class name="mPlayerDataBase" type="sSave::playerData">
	friends=tree.findall(".//class[@name='mPlayerDataManual']//s16[@name='mFriendPoint']")
	save_idx = []
	npcs = []
	affinities = []
	for idx, friend in enumerate(friends):
		idx_str=f'{idx:03d}' #pads zeros so a "1" becomes a "001".
		if idx_str in ddda_npc_ids:
			save_idx.append(idx)
			npcs.append(ddda_npc_ids[idx_str])
			affinities.append(friend.attrib['value'])
	return save_idx, npcs, affinities

#pure
#takes the tree
#return the etree elements for the caught and ring nodes
def survey_beloved(tree):
	#u/SordidDreams @ https://www.reddit.com/r/DragonsDogma/comments/48kkfp/changing_your_kidnapped_beloved_by_editing_the/
	#<s32 name="mCaughtNpcId" value="-1"/>
	#<s32 name="mRingNpcId" value="-1"/>
	caught=tree.findall(".//class[@name='mPlayerDataManual']//s32[@name='mCaughtNpcId']")[0]
	ring=tree.findall(".//class[@name='mPlayerDataManual']//s32[@name='mRingNpcId']")[0]
	return caught, ring

#impure
#takes the comboboxes refrences and filename
#modifies state of comboboxes
#returns etree and 3 lists of ints, strs and strs for the xml position, matching npc name and matching npc affinity value
def load_combobox(combo_box, combo_box_caught, combo_box_ring, filename):
	try:
		tree=load_tree(filename)
	except:
		messagebox.showerror(title="Pawn 9000", message="I'm sorry, Ser " + os.getlogin() + ", I'm afraid I can't do that.")
	else:
		save_idx, npcs, affinities=survey_friends(tree)
		combo_box['values'] = npcs

		caught_idx, ring_idx = survey_beloved(tree)
		caught_idx_value=int(caught_idx.attrib['value'])
		if caught_idx_value != -1:
			if caught_idx_value in save_idx:
				combo_box_caught['values'] = ['None']+npcs
				pos = save_idx.index(caught_idx_value)
				combo_box_caught.set(combo_box_caught['values'][pos+1])
			else:
				combo_box_caught['values'] = ['None']+npcs+["№"+str(caught_idx_value)]
				combo_box_caught.set("№"+str(caught_idx_value))
		else:
			combo_box_caught['values'] = ['None']+npcs
			combo_box_caught.set('None')
		ring_idx_value=int(ring_idx.attrib['value'])
		if ring_idx_value != -1:
			if ring_idx_value in save_idx:
				combo_box_ring['values'] = ['None']+npcs
				pos = save_idx.index(ring_idx_value)
				combo_box_ring.set(combo_box_ring['values'][pos+1])
			else:
				combo_box_ring['values'] = ['None']+npcs+["№"+str(ring_idx_value)]
				combo_box_ring.set("№"+str(ring_idx_value))
		else:
			combo_box_ring['values'] = ['None']+npcs
			combo_box_ring.set('None')

		return tree, save_idx, npcs, affinities

#impure
#takes the widgets
#asks the user for input file
#modifies widgets state
def load_select_file(entrybox_value, combo_box, combo_box_caught, combo_box_ring, tree, save_idx, npcs, affinities):
	filetypes = (
		('DDDA unpacked save', '*.sav.xml'),
		('All types', '*.*')
	)
	filename = filedialog.askopenfilename(
		title='Open a save file xml',
		initialdir='./',
		filetypes=filetypes)
	if filename!="":
		tree_in, save_idx_in, npcs_in, affinities_in = load_combobox(combo_box, combo_box_caught, combo_box_ring, filename)
		tree.append(tree_in)
		save_idx.append(save_idx_in)
		npcs.append(npcs_in)
		affinities.append(affinities_in)

#impure
#takes the tree, 3 lists of ints, strs and strs for the xml position, matching npc name and matching npc affinity value and strs of the caught and ring npcs
#asks the user for output file
#writes out the file
def save_select_file(tree, save_idx, npcs, affinities, caught, ring):
	if tree == []:
		messagebox.showerror(title="Pawn 9000", message="I'm sorry, Ser " + os.getlogin() + ", I'm afraid I can't do that.")
		return
	tree, save_idx, npcs, affinities = tree[0], save_idx[0], npcs[0], affinities[0]

	caught_node=tree.findall(".//class[@name='mPlayerDataManual']//s32[@name='mCaughtNpcId']")[0]
	if caught == "None":
		caught_value = "-1"
	elif caught[0] == "№":
		caught_value = f'{int(caught[1:]):03d}'
	else:
		caught_value = f'{save_idx[npcs.index(caught)]:03d}'
	caught_node.attrib['value'] = caught_value

	ring_node=tree.findall(".//class[@name='mPlayerDataManual']//s32[@name='mRingNpcId']")[0]
	if ring == "None":
		ring_value = "-1"
	elif ring[0] == "№":
		ring_value = f'{int(ring[1:]):03d}'
	else:
		ring_value = f'{save_idx[npcs.index(ring)]:03d}'
	ring_node.attrib['value'] = ring_value

	friends=tree.findall(".//class[@name='mPlayerDataManual']//s16[@name='mFriendPoint']")
	for idx, friend in enumerate(friends):
		if idx in save_idx:
			pos = save_idx.index(idx)
			friend.attrib['value'] = affinities[pos]
	##Quina
	#print(ddda_npc_ids["002"], friends[2].attrib['value'])
	##Clarus
	#print(ddda_npc_ids["327"], friends[327].attrib['value'])
	##Mason
	#print(ddda_npc_ids["158"], friends[158].attrib['value'])

	filetypes = (
		('DDDA unpacked save', '*.sav.xml'),
		('All types', '*.*')
	)
	filename = filedialog.asksaveasfilename(
		title='Write a DDDA save file xml',
		initialdir='./',
		filetypes=filetypes,
		defaultextension=".xml")
	if filename:
		file=open(filename,'wb')
		out = etree.tostring(tree, xml_declaration=False, encoding="utf-8", doctype='<?xml version="1.0" encoding="utf-8"?>')+b"\n"
		file.write(out)
		file.close()

def main():
	def entrybox_callback(var, index, mode):
		entry_box['state'] = 'normal'
		#sanitizing input
		entry = entrybox_value.get()
		entry = ''.join(c for c in entry if c.isdigit())
		if entry == "":
			entry = 0
			entry_box.insert(0, '0')
			entry_box.select_range(0, tk.END)
			entry_box.icursor(0)
			root.update()
		elif int(entry) > 1000:
			entry = 1000
			entry_box.select_range(0, tk.END)
		entrybox_value.set(entry)
		#putting the number back into the list
		pos = npcs[0].index(combo_box.get())
		affinities[0][pos] = str(entry)
	def combobox_callback(var, index, mode):
		pos = npcs[0].index(combo_box.get())
		entrybox_value.set(affinities[0][pos])
	root = tk.Tk()
	title = "DDDA Save Affinity Editor"
	root.title(title)
	frame = ttk.Frame(root, style='Card.TFrame')
	frame.grid(row = 0, column = 0, padx=5, pady=5, sticky = 'ew')
	entrybox_value = StringVar()
	entrybox_value.trace_add('write', entrybox_callback)
	combobox_value = StringVar()
	combobox_value.trace_add('write', combobox_callback)
	affinitiesframe = ttk.LabelFrame(frame, text="Affinities:", style='TLabelframe')
	entry_box = ttk.Entry(affinitiesframe, style='TEntry', state='readonly', textvariable = entrybox_value, width=5)
	combo_box = ttk.Combobox(affinitiesframe, style='TCombobox', textvariable=combobox_value, state='readonly', width=40)
	caughtframe = ttk.Frame(frame, style='Card.TFrame')
	label_caught = ttk.Label(caughtframe, style='TLabel', text = "Caught:")
	combo_box_caught = ttk.Combobox(caughtframe, style='TCombobox', state='readonly', width=40)
	ringframe = ttk.Frame(frame, style='Card.TFrame')
	label_ring = ttk.Label(ringframe, style='TLabel', text = "Ring:")
	combo_box_ring = ttk.Combobox(ringframe, style='TCombobox', state='readonly', width=42)
	buttonsframe = ttk.Frame(frame, style='Card.TFrame')
	tree, save_idx, npcs, affinities = [], [], [], []
	load_button=ttk.Button(buttonsframe, style='Accent.TButton', text='Load DDDA.sav.xml...', width=20, command=lambda : load_select_file(entrybox_value, combo_box, combo_box_caught, combo_box_ring, tree, save_idx, npcs, affinities))
	save_button=ttk.Button(buttonsframe, style='Accent.TButton', text='Save...', width=7, command=lambda : save_select_file(tree, save_idx, npcs, affinities, combo_box_caught.get(), combo_box_ring.get()))
	affinitiesframe.grid(row = 0, columnspan = 2, padx=5, pady=5, sticky = 'ew')
	combo_box.grid(row = 0, column=0, padx=5, pady=5)
	entry_box.grid(row = 0, column=1, padx=5, pady=5)
	caughtframe.grid(row = 1, columnspan = 2, padx=5, pady=5, sticky = 'ew')
	label_caught.grid(row = 0, column=0, padx=5, pady=5)
	combo_box_caught.grid(row = 0, column=1, padx=5, pady=5)
	ringframe.grid(row = 2, columnspan = 2, padx=5, pady=5, sticky = 'ew')
	label_ring.grid(row = 0, column=0, padx=5, pady=5)
	combo_box_ring.grid(row = 0, column=1, padx=5, pady=5)
	buttonsframe.grid(row = 3, columnspan = 2, padx=5, pady=5)
	load_button.grid(row = 0, column = 0, padx=5, pady=5)
	save_button.grid(row = 0, column = 1, padx=5, pady=5)
	sv_ttk.set_theme("dark")
	ttk.Style().configure("Accent.TButton", padding=2)
	ttk.Style().configure("TEntry", padding=2)
	ttk.Style().configure("TCombobox", padding=2)
	ttk.Style().configure("TFrame", padding=2)
	ttk.Style().configure('TLabelframe.Label', foreground='white', padding=1)
	root.mainloop()

if __name__ == '__main__':
	main()
