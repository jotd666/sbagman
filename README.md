# Super Bagman (68K)

Super Bagman remake by JOTD in 2023

Original game by Valadon Automation (c) 1984
ROM strings show that it has been coded by Jacques Brisse (still head of Valadon in 2015 at least)

Game uses 99% of the transcoded original code for better accuracy.

Some memory read bugs & text typos have been fixed, some not. 
Music never loses the tempo.
Sound use samples.
Game still has original bugs left

History: 

2023: Amiga version using real game code transcoded to 68000 (should run on A500)
2010-2023: Bagman


### PROGRESS:

#### TRANSCODE


#### AMIGA

- fully playable with sound
- still bugs
- missing features

#### NEO GEO

- not planned ATM ...

### FEATURES:

#### CREDITS:

- Jean-Francois Fabre (aka jotd): Z80 reverse engineering, Z80 to 68k transcode, Amiga code and assets
- no9: remade amiga tunes
- DanyPPC: icons
- DamienD: floppy menus
- phx: ptplayer sound/music replay Amiga code
- Valadon Automation: original game :)

#### SPECIAL THANKS:

- Toni Wilen for WinUAE
- Mark Mc Dougall for converting me to the global idea of transcoding the things,
  the C graphical rip format he created and that I'm using from now, and also
  the nice e-mail conversations that we have.

#### MENU CONTROLS (Amiga: joystick required):

- fire/5 key: insert coin (from menu)
- up/1 key: start game
- down/1 key: start 2P game

#### GAME CONTROLS:

- directions: move bagman
- fire/ctrl: pick/release object/jump
- space/left-alt/2nd button: shoot
- P key: pause

## REBUILDING FROM SOURCES:

### AMIGA:

#### Prerequesites:

- Bebbo's amiga gcc compiler
- Windows
- python
- sox
- "bitplanelib.py" (asset conversion tool needs it) at https://github.com/jotd666/amiga68ktools.git

#### Build process:

- install above tools & adjust python paths
- make -f makefile.am

### NEO GEO:

#### Prerequesites:

- Windows
- NeoDev kit (Fabrice Martinez, Jeff Kurtz, et al)  
  https://wiki.neogeodev.org/index.php?title=Development_tools

#### Build process:

- install NeoDev and set path accordingly
- clone repository
- make -f makefile.ng OUTPUT={cart|cd}
  - (OUTPUT defaults to cart)
  
#### Install process (MAME):

- make -f makefile.ng OUTPUT={cart|cd} MAMEDIR={mamedir} install
  - (mamedir defaults to '.')
- paste sbagman.xml into MAME's hash/neogeo.xml file

#### To run in MAME:

- cart : 'mame neogeo sbagman'
- cd : 'mame neocdz -cdrom roms/neocdz/sbagman.iso'
  
