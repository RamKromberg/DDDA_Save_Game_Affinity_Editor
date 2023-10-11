Dragon's Dogma: Dark Arisen Save Game Affinity Editor
2023-09-29
nowahNOwah @ https://www.nexusmods.com/dragonsdogma/mods/957

A GUI to modify DDDA save games' NPCs' affinities, the NPC that was ring-bonded and the NPC that was caught.

Requirements:
    1. Python ( https://www.python.org/downloads/windows/ )
    2. lxml (run "pip install lxml" in the cmd after installing python)
    3. sv_ttk (run "pip install sv_ttk" in the cmd after installing python)
    4. DDsavetool ( http://www.fluffyquack.com/tools/DDsavetool.rar )

Installation:
	1. Install python.
	2. Start -> "Command Prompt"
	3. Run "pip install lxml sv_ttk"
	4. Unpack DDsavetool.exe where you have DDDA.sav stored
	5. Unpack DDDA_Save_Game_Affinity_Editor.pyw where you'll have DDsavetool's output DDDA.sav.xml stored

Usage:
	0. Make backups...
	1. Unpack your save with "DDsavetool.exe -u DDDA.sav"
	2. Run "DDDA_Save_Game_Affinity_Editor.pyw" by double-clicking it in explorer or the command-line
	3. Click the button labeled "Load DDDA.sav.xml..." and select DDDA.sav.xml
	4. Modify stuff...
	5. Click the button labeled "Save..." and select to overwrite DDDA.sav.xml
	6. Use "DDsavetool.exe -r DDDA.sav.xml" to repack DDDA.sav

Note:
	1. Doesn't touch the checkpoint slot / only modifies the quick-save slot
	2. Was only tested on the GOG version
	3. (linux) Uses the windows pre-packaged Tkinter library
	4. Some credits in the source...
