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

#just jumps to the first letter
#TODO: full search...
class BasicSearchCombobox(ttk.Combobox):
	def __init__(self, master=None, **kwargs):
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
#returns a zip of ints, strs and strs for the xml position, matching npc name and matching npc affinity value
def survey_friends(tree):
	#u/CyncoV @ https://www.reddit.com/r/DragonsDogma/comments/oejjqf/modmodding_tool_to_be_able_to_edit_npc_affinity/h4770xz/
	#quick save: <class name="mPlayerDataManual" type="sSave::playerData">
	#checkpoint: <class name="mPlayerDataBase" type="sSave::playerData">
	friends_elements=tree.findall(".//class[@name='mPlayerDataManual']//s16[@name='mFriendPoint']")
	save_idx = []
	npcs = []
	affinities = []
	for idx, friend in enumerate(friends_elements):
		idx_str=f'{idx:03d}' #pads zeros so a "1" becomes a "001".
		if idx_str in ddda_npc_ids:
			save_idx.append(idx)
			npcs.append(ddda_npc_ids[idx_str])
			affinities.append(friend.attrib['value'])
	friends_zipped = zip(save_idx, npcs, affinities)
	friends_zipped_sorted = sorted(friends_zipped, key = lambda x: x[1])
	return friends_zipped_sorted

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
		save_idx, npcs, affinities = zip(*survey_friends(tree))
		save_idx, npcs, affinities = list(save_idx), list(npcs), list(affinities)
		combo_box['values'] = npcs
		combo_box.current(0)

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
		selection = combo_box.get()
		if npcs != [] and selection != "item":
			pos = npcs[0].index(selection)
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
	combo_box = BasicSearchCombobox(affinitiesframe, style='TCombobox', textvariable=combobox_value, state='readonly', width=40,name="box_affinities")

	caughtframe = ttk.Frame(frame, style='Card.TFrame')
	label_caught = ttk.Label(caughtframe, style='TLabel', text = "Caught:")
	combo_box_caught = BasicSearchCombobox(caughtframe, style='TCombobox', state='readonly', width=40,name="box_caught")

	ringframe = ttk.Frame(frame, style='Card.TFrame')
	label_ring = ttk.Label(ringframe, style='TLabel', text = "Ring:")
	combo_box_ring = BasicSearchCombobox(ringframe, style='TCombobox', state='readonly', width=42,name="box_ring")

	buttonsframe = ttk.Frame(frame, style='Card.TFrame')
	tree, save_idx, npcs, affinities = [], [], [], []
	load_button=ttk.Button(buttonsframe, style='Accent.TButton', text='Load DDDA.sav.xml...', width=20, command=lambda : load_select_file(entrybox_value, combo_box, combo_box_caught, combo_box_ring, tree, save_idx, npcs, affinities))
	save_button=ttk.Button(buttonsframe, style='Accent.TButton', text='Save...', width=7, command=lambda : save_select_file(tree, save_idx, npcs, affinities, combo_box_caught.get(), combo_box_ring.get()))

	#layout
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
