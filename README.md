# Dragon's Dogma: Dark Arisen Save Game Affinity Editor
#### 2023-10-11
nowahNOwah @ https://www.nexusmods.com/dragonsdogma/mods/957
https://github.com/RamKromberg/DDDA_Save_Game_Affinity_Editor

###### A GUI to modify DDDA save games' NPCs' affinities, the NPC that was ring-bonded and the NPC that was caught.

##### Requirements:
	1. Python ( https://www.python.org/downloads/windows/ )
	2. lxml (run "pip install lxml" in the cmd after installing python)

##### Optional Requirements:
	1. sv_ttk (run "pip install sv_ttk" in the cmd after installing python)
	2. DDsavetool ( http://www.fluffyquack.com/tools/DDsavetool.rar )

##### Installation:
	1. Install python
	2. Start -> "Command Prompt"
	3. Run "pip install lxml"
	4. (Optional for Dark Mode) Run "pip install sv_ttk"
	5. (Optional in case internal .sav handling is buggy) Unpack DDsavetool.exe where you have DDDA.sav stored
	6. Unpack DDDA_Save_Game_Affinity_Editor.pyw where you'll have DDsavetool's output DDDA.sav.xml stored

##### Usage (no DDsavetool):
	0. Make backups...
	1. Run "DDDA_Save_Game_Affinity_Editor.pyw" by double-clicking it in explorer or the command-line
	2. Click the button labeled "Load..." and toggle the file type to .sav before selecting DDDA.sav
	3. Modify stuff...
	4. Click the button labeled "Save..." and toggle the file type to .sav before overwriting DDDA.sav

##### Usage (assuming DDsavetool):
	0. Make backups...
	1. Unpack your save with "DDsavetool.exe -u DDDA.sav"
	2. Run "DDDA_Save_Game_Affinity_Editor.pyw" by double-clicking it in explorer or the command-line
	3. Click the button labeled "Load..." and select DDDA.sav.xml
	4. Modify stuff...
	5. Click the button labeled "Save..." and select to overwrite DDDA.sav.xml
	6. Use "DDsavetool.exe -r DDDA.sav.xml" to repack DDDA.sav

##### Notes:
	1. Doesn't touch the checkpoint slot / only modifies the quick-save slot
	2. Was only tested on the GOG version
	3. (linux) Uses the windows pre-packaged Tkinter library
	4. The support for direct .sav saving and loading is experimental
	5. Some credits in the source...

##### ChangeLog:
	2023-10-11: Treeview for affinities; .sav support.
	2023-10-04: Sorted the names; Added a basic search to the combobox.
	2023-09-29: Release.
