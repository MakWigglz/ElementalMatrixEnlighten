''' This is a Program which tells Details of Elements 
of Periodic Table. When a user inputs Name of the element
or Symbol of the element or Atomic Number the user recieves 
details of the element respecitve of what user has entered  '''

import easygui

while True:       
    y = easygui.enterbox("Enter Name or Symbol or Atomic Number of the Element:-")
    x = y.lower()
    
    if x == "hydrogen" or x == '1' or x == 'h':
        easygui.msgbox('''Element :- HYDROGEN
Symbol :- H
Atomic Number :- 1
Atomic Mass :- 1.00784 amu 
Atomic Size :- (Calculated 53 pm) & (Vander Waals 120 or 110 pm)
Electronic Configuration :- 1s1 
Found In :- Group-1 And Period-1 
Discovered By :- Henry Cavendish in 1766
Valence Electron :- 1 
Isotopes :- Protium, Deuterium, Tritium
Type :- Natural and Non-Metal
Family :- Does Not Belongs To Any Family
Properties :- Tasteless, Odourless, Colourless Gas.''')
         
              
    elif x == "helium" or x == '2' or x == 'he':
        easygui.msgbox('''Element :- HELIUM
Symbol :- He
Atomic Number :- 2 
Atomic Mass :- 4.002602 amu
Atomic Size :- (Calculated 31 pm) & (Vander Waals 140 pm)
Electronic Configuration :- 1s2
Found In :- Group-18 And Period-1
Discovered By :- William Ramsay in 1895
Valence Electron :- 2
Isotopes :- Helium-2, Helium-3, Helium-4
Type :- Natural and Non-Metal
Family :- Noble Gas
Properties :- Odourless, Colourless, Inert.''')
         

    elif x == "lithium" or x == '3' or x == 'li':
        easygui.msgbox('''Element :- LITHIUM
Symbol :- Li
Atomic Number :- 3
Atomic Mass :- 6.941 amu
Atomic Size :- (Calculated 167 pm) & (Vander Waals 182 pm)
Electronic Configuration :- 1s1 2s1
Found In :- Group-1 And Period-2
Discovered By :- Johan August Arfvedson in 1817
Valence Electron :- 1
Isotopes :- Lithium-6 And Lithium-7
Type :- Natural and Metal
Family :- Alkali Metals
Properties :- Low Viscosity, Very Low Density, High Specific Heat.''')
         

    elif x == "beryllium" or x == '4' or x == 'be':
         easygui.msgbox('''Element :- BERYLLIUM
Symbol :- Be
Atomic Number :- 4
Atomic Mass :- 9.012 amu
Atomic Size :- (Calculated 112 pm) & (Vander Waals 153 pm)
Electronic Configuration :- [He] 2s2
Found In :- Group-2 And Period-2
Discovered By :- Nicholas Louis Vauquelin in 1797
Valence Electron :- 2
Isotopes :- Beryllium-9
Type :- Natural and Metal
Family :- Alkaline Earth Metal
Characteristics Properties :- Soft, Low Density.''')
         

    elif x == "boron" or x == '5' or x == 'b':
         easygui.msgbox('''Element :- BORON
Symbol :- B
Atomic Number :- 5
Atomic Mass :- 10.811 amu
Atomic Size :- (Calculated 85 pm) & (Vander Waals 192 pm)
Electronic Configuration :- [He] 2s2 2p1
Found In :- Group-13 And Period-2
Discovered By :- Gay-Lussac, Humphry Davy, Louis Jacques Thenard in 1808
Valence Electron :- 3
Isotopes :- Boron-10 and Boron-11
Type :- Natural and Metalloid
Family :- Boron Family
Properties :- Black, Lustrous Semiconductor.''')
         
       
    elif x == "carbon" or x == '6' or x == 'c':
         easygui.msgbox('''Element :- CARBON
Symbol :- C
Number :- 6
Mass :- 12.011 amu
Atomic Size :- (Calculated 70 pm) & (Vander Waals 170 pm)
Electronic Configuration :- [He] 2s2 2p2
Found In :- Group-14 And Period-2
Discovered By :- Antoine Lavoisier in 1789
Valence Electron :- 4
Isotopes :- Carbon-12, Carbon-13, Carbon-14
Type :- Natural and Non-Metal
Family :- Carbon Family
Properties :- Abundant, Forms Strong Covalent Bond.''')
         

    elif x == "nitrogen" or x == '7' or x == 'n':
         easygui.msgbox('''Element :- NITROGEN
Symbol :- N
Atomic Number :- 7
Atomic Mass :- 14.007 amu
Atomic Size :- (Calculated 56 pm) & (Vander Waals 155 pm)
Electronic Configuration :- [He] 2s2 2p3
Found In :- Group-15 And Period-2
Discovered By :- Daniel Rutherford in 1772
Valence Electron :- 5
Isotopes :- Nitrogen-14, Nitrogen-15
Type :- Natural and Non-Metal
Family :- Pnictogens Family
Properties :- Colourless, Odourless.''')
         


    elif x == "oxygen" or x == '8' or x == 'o':
         easygui.msgbox('''Element :- OXYGEN
Symbol :- O
Atomic Number :- 8
Atomic Mass :- 15.999 amu
Atomic Size :- (Calculated 48 pm) & (Vander Waals 152 pm)
Electronic Configuration :- [He] 2s2 2p4
Found In :- Group-16 And Period-2
Discovered By :- Joseph Priestley, Antoine Lavoisier, Carl Wilhelm Scheele in 1722
Valence Electron :- 6
Isotopes :- Oxygen-16, Oxygen-17, Oxygen-18
Type :- Natural and Non-Metal
Family :- Chalcogens Family
Properties :- Colourless, Odourless, Paramagnetic, Essential Gas For Living Organism.''')
         

    elif x == "fluorine" or x == '9' or x == 'f':
         easygui.msgbox('''Element :- FLUORINE
Symbol :- F
Atomic Number :- 9
Atomic Mass :- 18.998 amu
Atomic Size :- (Calculated 42 pm) & (Vander Waals 147 pm)
Electronic Configuration :- [He] 2s2 2p5
Found In :- Group-17 And Period-2
Discovered By :- Carl Wilhelm Scheele in 1886
Valence Electron :- 7
Isotopes :- Fluorine-19
Type :- Natural and Non-Metal
Family :- Halogens Family
Properties :- Faintly Yellow, Irritating Odour .''')
         

    elif x == "neon" or x == '10' or x == 'ne':
         easygui.msgbox('''Element :- NEON
Symbol :- Ne
Atomic Number :- 10
Atomic Mass :- 20.180 amu
Atomic Size :- (Calculated 38 pm) & (Vander Waals 154 pm)
Electronic Configuration :- [He] 2s2 2p6
Found In :- Group-18 And Period-2
Discovered By :- William Ramsay, Morris W. Travers in 1898
Valence Electron :- 8
Isotopes :- Neon-20, Neon-21, Neon-22
Type :- Natural and Non-Metal
Family :- Noble Family
Properties :- Colourless, Tasteless, Reddish Orange Colour in Vaccume Tube.''')
         

    elif x == "sodium" or x == '11' or x == 'na':
         easygui.msgbox('''Element :- SODIUM
Symbol :- Na
Atomic Number :- 11
Atomic Mass :- 22.99 amu
Atomic Size :- (Calculated 190 pm) & (Vander Waals 227 pm)
Electronic Configuration :- [Ne] 3s1
Found In :- Group-1 And Period-3
Discovered By :- Humphry Davy in 1807
Valence Electron :- 1
Isotopes :- Sodium-23
Type :- Natural and Metal
Family :- Alkali Metals
Properties :- Soft Metal,Low Melting Point, Highly Reactive.''')
         

    elif x == "magnesium" or x == '12' or x == 'mg':
         easygui.msgbox('''Element :- MAGNESIUM 
Symbol :- Mg
Atomic Number :- 12
Atomic Mass :- 9.012 amu
Atomic Size :- (Calculated 145 pm) & (Vander Waals 173 pm)
Electronic Configuration :- [Ne] 3s2
Found In :- Group-2 And Period-3
Discovered By :- Joseph Black, Humphry Davy in 1755
Valance Electron :- 2
Isotopes :- Magnesium-24, Magnesium-25, Magnesium-26
Type :- Natural and Metal 
Family :- Alkaline Earth Metal
Properties :- Ignites Easily, Burns With White Flame.''')
         

    elif x == "aluminum" or x == '13' or x == 'al':
         easygui.msgbox('''Element :- ALUMINUM
Symbol :- Al 
Atomic Number :- 13
Atomic Mass :- 26.982 amu
Atomic Size :- (Calculated 118 pm) & (Vander Waals 184 pm)
Electronic Configuration :- [Ne] 3s2 3p1
Found In :- Group-13 And Period-3
Discovered By :- Hans Christian Orsted in 1825
Valence Electron :- 3
Isotopes :- Aluminium-27 
Type :- Natural and Metal
Family :- Boron Family
Properties :- Low Density, Non-Toxic, High Thermal Conductivity.''')
         

    elif x == "silicon" or x == '14' or x == 'si':
         easygui.msgbox('''Element :- SILICON
Symbol :- Si
Atomic Number :- 14
Atomic Mass :- 28.086 amu
Atomic Size :- (Calculated 111 pm) & (Vander Waals 210 pm)
Electronic Configuration :- [Ne] 3s2 3p2 
Found In :- Group-14 And Period-3
Discovered By :- Antoine Lavoisier, Jons Jacob Berzelius in 1823
Valence Electron :- 4
Isotopes :-  Silicon-28, Silicon-29, Silicon-30
Type :- Natural and Metalloid
Family :- Carbon Family
Properties :- Used As Semiconductor, Very Brittle.''')
         

    elif x == "phosphorus" or x == '15' or x == 'p':
         easygui.msgbox('''Element :- PHOSPHORUS
Symbol :- P
Atomic Number :- 15
Atomic Mass :- 30.974 amu
Atomic Size :- (Calculated 98 pm) & (Vander Waals 180 pm)
Electronic Configuration :- [Ne] 3s2 3p3
Found In :- Group-15 And Period-3
Discovered By :- Hennig Brandt in 1669
Valence Electron :- 5
Isotopes :- Phosphorus-31
Type :- Natural and Non-Metal
Family :- Nitrogen Family
Properties :- Colourless, Semitransparent, Soft, Waxy Solid That Glows In The Dark.''')
         
        
    elif x == "sulfur" or x == '16' or x == 's':
         easygui.msgbox('''Element :- SULFUR
Symbol :- S
Atomic Number :- 16
Atomic Mass :- 32.066 amu
Atomic Size :- (Calculated 88 pm) & (Vander Waals 180 pm)
Electronic Configuration :- [Ne] 3s2 3p4
Found In :- Group-16 And Period-3
Discovered By :- Antoine Lavoiser in 1777
Valence Electron :- 6
Isotopes :- Sulphur-32, Sulphur-33, Sulphur-34, Sulphur-36
Type :- Natural and Non-Metal
Family :- Chalcogen Family
Properties :- Tasteless, Odourless, Pale Yellow Colour.''')
         

    elif x == "chlorine" or x == '17' or x == 'cl':
         easygui.msgbox('''Element :- CHLORINE
Symbol :- Cl
Atomic Number :- 17
Atomic Mass :- 35.453 amu
Atomic Size :- (Calculated 79 pm) & (Vander Waals 175 pm)
Electronic Configuration :- [Ne] 3s2 3p5
Found In :- Group-17 And Period-3
Discovered By :- Carl Wilhelm Scheele in 1774
Valence Electron :- 7
Isotopes :- Chlorine-35, Chlorine-37
Type :- Natural and Non-Metal
Family :- Halogen
Properties :- Greenish Yellow Gas At Room Temprature And Atmospheric Pressure.''')
                   
          
    elif x == "argon" or x == '18' or x == 'ar':
         easygui.msgbox('''Element :- ARGON
Symbol :- Ar
Atomic Number :- 18
Atomic Mass :- 39.948 amu
Atomic Size :- (Calculated 71 pm) & (Vander Waals 188 pm)
Electronic Configuration :- [Ne] 3s2 3p6
Found In :- Group-18 And Period-3
Discovered By :- William Ramsay in 1894
Valence Electron :- 8
Isotopes :- Argon-36, Argon-38, Argon-40
Type :- Natural and Non-Metal
Family :- Noble Gas
Properties :- Nonflammable, Nontoxic, Odorless, Colourless.''')
         

    elif x == "potassium" or x == '19' or x == 'k':
         easygui.msgbox('''Element :-POTASSIUM 
Symbol :- K
Atomic Number :- 19
Atomic Mass :- 39.098 amu
Atomic Size :- (Calculated 243 pm) & (Vander Waals 275 pm)
Electronic Configuration :- [Ar] 4s1
Found In :- Group-1 And Period-4
Discovered By :- Humphry Davy in 1807
Valence Electron :- 1
Isotopes :- Potassium-39, Potassium-40, Potassium-41
Type :- Natural and Metal
Family :- The Alkali Metals
Properties :- Soft and White with a silvery lustre, Has a low melting point.''')
         

    elif x == "calcium" or x == '20' or x == 'ca':
         easygui.msgbox('''Element :- CALCIUM
Symbol :- Ca
Atomic Number :- 20
Atomic Mass :- 40.078 amu
Atomic Size :- (Calculated 194 pm) & (Vander Waals 231 pm)
Electronic Configuration :- [Ar] 4s2 
Found In :- Group-2 And Period-4
Discovered By :- Humphry Davy in 1808
Valence Electron :- 2
Isotopes :- Calcium-40, Calcium-42, Calcium-43, Calcium-44, Calcium-46, Calcium-48
Type :- Natural and Metal
Family :- Alkaline Earth Metals
Properties :- Silvery-white metallic, Relatively Soft Metal, Capable of being shaped or bent.''')
         


    elif x == "scandium" or x == '21' or x == 'sc':
         easygui.msgbox('''Element :- SCANDIUM
Symbol :- Sc
Atomic Number :- 21
Atomic Mass :- 44.956 amu
Atomic Size :- (Calculated 184 pm) & (Vander Waals 211 pm)
Electronic Configuration :- [Ar] 3d1 4s2
Found In :- Group-3 And Period-4
Discovered By :- Lars Frederik Nilson in 1879
Valence Electron :- 3
Isotopes :- Scandium-45
Type :- Natural and Metal
Family :- Scandium Family (Trasition Metals)
Characteristics Properties :- Becomes slightly tinged with yellow or pink when exposed to Air.''')
         

    elif x == "titanium" or x == '22' or x == 'ti':
         easygui.msgbox('''Element :- TITANIUM
Symbol :- Ti
Atomic Number :- 22
Atomic Mass :- 47.867 amu
Atomic Size :- (Calculated 176 pm) & (Vander Waals 215 pm)
Electronic Configuration :- [Ar] 3d2 4s2
Found In :- Group-4 And Period-4
Discovered By :- William Gregor in 1791
Valence Electron :-4 
Isotopes :- Titanium-46, Titanium-47, Titanium-48, Titanium-49, Titanium-50
Type :- Natural and Metal
Family :- Titanium Family (Transition Metal)
Characteristics Properties :- Strong and Light, Low Density, High Melting Point.''')
         

    elif x == "vanadium" or x == '23' or x == 'v':
         easygui.msgbox('''Element :- VANADIUM
Symbol :- V
Atomic Number :- 23
Atomic Mass :- 50.942 amu
Atomic Size :- (Calculated 171 pm)
Electronic Configuration :- [Ar] 2d3 4s2
Found In :- Group-5 And Period-a
Discovered By :- Andrés Manuel del Rio in 1801
Valence Electron :- 5
Isotopes :- Vanadium-50, Vanadium-51
Type :- Natural and Metal
Family :- Vanadium Family (Transition Metal)
Characteristics Properties :- Soft and Ductile, Silver-Grey Metal.''')
         

    elif x == "chromium" or x == '24' or x == 'cr':
         easygui.msgbox('''Element :- CHROMIUM
Symbol :- Cr
Atomic Number :- 24
Atomic Mass :- 51.996 amu
Atomic Size :- (Calculated 166 pm)
Electronic Configuration :- [Ar] 3d5 4s1
Found In :- Group-6 And Period-4
Discovered By :- Louis Nicolas Vauquelin in 1797
Valence Electron :- 6
Isotopes :- Chromium-50, Chromium-52, Chromium-53, Chromium-54
Type :- Natural and Metal
Family :- Chromium Family (Transition Metal)
Characteristics Properties :- Lustrous, Brittle, Hard Metal.''')
         

    elif x == "manganese" or x == '25' or x == 'mn':
         easygui.msgbox('''Element :- MANGANESE
Symbol :- Mn
Atomic Number :- 25
Atomic Mass :- 54.938 amu
Atomic Size :- (Calculated 161 pm)
Electronic Configuration :- [Ar] 3d5 4s2
Found In :- Group-7 And Period-4
Discovered By :- Johan Gottlieb Gahn in 1774 
Valence Electron :- 7 
Isotopes :- Manganese-55
Type :- Natural and Metal
Family :- Manganese Family (Transition Metal)
Characteristics Properties :- Pinkinsh-Gray, Chemically Active Element.''')
         

    elif x == "iron" or x == '26' or x == 'fe':
         easygui.msgbox('''Element :- IRON
Symbol :- Fe
Atomic Number :- 26
Atomic Mass :- 55.845 amu
Atomic Size :- (Calculated 156 pm)
Electronic Configuration :- [Ar] 3d6 4s2 
Found In :- Group-8 And Period-4
Discovered By :- The Hittites (Before 5000 BC)
Valence Electron :- 8
Isotopes :- Iron-54, Iron-56, Iron-57, Iron-58
Type :- Natural and Metal
Family :- Iron Family (Transition Metal)
Characteristics Properties :- Lustrous, Ductile, Malleable, Silver-Gray Metal.''')
         

    elif x == "cobalt" or x == '27' or x == 'co':
         easygui.msgbox('''Element :- COBALT
Symbol :- Co
Atomic Number :- 27
Atomic Mass :- 58.933 amu
Atomic Size :- (Calculated 152 pm)
Electronic Configuration :- [Ar] 3d7 4s2
Found In :- Group-9 And Period-4
Discovered By :- Georg Brandt in 1735
Valence Electron :- 9
Isotopes :- Cobalt-59
Type :- Natural and Metal
Family :- Cobalt Family (Transition Metal)
Characteristics Properties :- Hard Ferromagnetic, Silver-White, Hard, Lustrous, Brittle Element.''')
         

    elif x == "nickel" or x == '28' or x == 'ni':
         easygui.msgbox('''Element :- NICKEL
Symbol :- Ni
Atomic Number :- 28
Atomic Mass :- 58.693 amu
Atomic Size :- (Calculated 149 pm) & (Vander Waals 163 pm)
Electronic Configuration :- [Ar] 3d8 4s2
Found In :- Group-10 And Period-4
Discovered By :- Axel Fredrik Cronstedt
Valence Electron :- 10
Isotopes :- Nickel-58, Nickel-60, Nickel-61, Nickel-62, Nickel-64 
Type :- Natural and Metal
Family :- Nickel Family (Transition Metal)
Characteristics Properties :- Hard, Malleable, Ductile Metal.''')
         

    elif x == "copper" or x == '29' or x == 'cu':
         easygui.msgbox('''Element :- COPPER
Symbol :- Cu
Atomic Number :- 29
Atomic Mass :- 63.546 amu
Atomic Size :- (Calculated 145 pm) & (Vander Waals 140 pm)
Electronic Configuration :- [Ar] 3d10 4s1 
Found In :- Group-11 And Period-4
Discovered By :- The Sumerians and the Chaldeans (Nearly 9000 BC)
Valence Electron :- 11
Isotopes :- Copper-63, Copper-65
Type :- Natural and Metal
Family :- Copper Family (Transition Metal)
Characteristics Properties :- Copper is a reddish metal with a face-centered cubic crystalline structure.''')
         
        
    elif x == "zinc" or x == '30' or x == 'zn':
         easygui.msgbox('''Element :- ZINC
Symbol :- Zn
Atomic Number :- 30
Atomic Mass :- 65.38 amu
Atomic Size :- (Calculated 142 pm) & (Vander Waals 139 pm)
Electronic Configuration :- [Ar] 3d10 4s2
Found In :- Group-12 And Period-4
Discovered By :- Andreas Marggraf in 1746
Valence Electron :- 12 
Isotopes :- Zinc-64, Zinc-66, Zinc-67, Zinc-68, Zinc-70
Type :- Natural and Metal
Family :- Zinc Family (Transition Metal)
Characteristics Properties :- Lustrous Bluish-White Metal, Brittle, Crystalline.''')
         


    elif x == "gallium" or x == '31' or x == 'ga':
         easygui.msgbox('''Element :- GALLIUM
Symbol :- Ga
Atomic Number :- 31
Atomic Mass :- 69.723 amu
Atomic Size :- (Calculated 136 pm) & (Vander Waals 187 pm)
Electronic Configuration :- [Ar] 3d10 4s2 4p1
Found In :- Group-13 And Period-4
Discovered By :- Paul-Émile Lecoq de Boisbaudran in 1875
Valence Electron :- 3 
Isotopes :- Gallium-69, Gallium-71
Type :- Elemental gallium is not found in nature, but it is easily obtained by smelting and it is metal
Family :- Boron Family
Characteristics Properties :- Silvery white, Soft, Can be cut with Knife.''')
         
        
    elif x == "germanium" or x == '32' or x == 'ge':
         easygui.msgbox('''Element :- GERMANIUM
Symbol :- Ge
Atomic Number :- 32
Atomic Mass :- 72.922 amu
Atomic Size :- (Calculated 125 pm) & (Vander Waals 211 pm)
Electronic Configuration :- [Ar] 3d10 4s2 4p2
Found In :- Group-14 And Period-4
Discovered By :- Clemens A. Winkler in 1886 
Valence Electron :- 4 
Isotopes :- Germanium-70, Germanium-72, Germanium-73, Germanium-74, Germanium-76
Type :- Natural and Metalloid
Family :- Carbon Family
Characteristics Properties :- Hard, Lustrous, Gray-White, Brittle.''')


    elif x == "arsenic" or x == '33' or x == 'as':
         easygui.msgbox('''Element :- ARSENIC
Symbol :- As
Atomic Number :- 33
Atomic Mass :- 74.922 amu
Atomic Size :- (Calculated 114 pm) & (Vander Waals 185 pm)
Electronic Configuration :- [Ar] 3d10 4s2 4p3
Found In :- Group-15 And Period-4
Discovered By :- Albertus Magnus (1250)
Valence Electron :- 5
Isotopes :- Arsenic-75
Type :- Natural and Metalloid
Family :- Notrogen Group
Characteristics Properties :- Semi-Metal, Silver-Grey, Brittle.''')

         
    elif x == "selenium" or x == '34' or x == 'se':
         easygui.msgbox('''Element :- SELENIUM
Symbol :- Se
Atomic Number :- 34
Atomic Mass :- 78.971 amu
Atomic Size :- (Calculated 103 pm) & (Vander Waals 190 pm)
Electronic Configuration :- [Ar] 3d10 4s2 4p4
Found In :- Group-16 And Period-4
Discovered By :- Jöns Jacob Berzelius in 1817
Valence Electron :- 6 
Isotopes :- Selenium-74, Selenium-76, Selenium-77, Selenium-78, Selenium-80
Type :- Natural and A Nonmetal and more rarely a Metalloid.
Family :- The Chalcogens
Characteristics Properties :- Red-Gray with Metallic Luster, Good Potovoltaic and Photoconductive Properties.''')
         

    elif x == "bromine" or x == '35' or x == 'br':
         easygui.msgbox('''Element :- BROMINE
Symbol :- Br
Atomic Number :- 35
Atomic Mass :- 79.904 amu
Atomic Size :- (Calculated 94 pm) & (Vander Waals 185 pm)
Electronic Configuration :- [Ar] 3d10 4s2 4p5
Found In :- Group-17 And Period-4
Discovered By :-  Antoine-Jérôme Balard in 1826
Valence Electron :- 7
Isotopes :- Bromine-79, Bromine-81
Type :- Natural and Non-Metal
Family :- The Halogens
Characteristics Properties :- Reddish Brown Liquid.''')

         
    elif x == "krypton" or x == '36' or x == 'kr':
         easygui.msgbox('''Element :- KRYPTON
Symbol :- Kr
Atomic Number :- 36
Atomic Mass :- 83.789 amu
Atomic Size :- (Calculated 88 pm) & (Vander Waals 202 pm)
Electronic Configuration :- [Ar] 3d10 4s2 4p6
Found In :- Group-18 And Period-4
Discovered By :- William Ramsay and Morris Travers in 1898 
Valence Electron :- 8
Isotopes :- Krypton-84, Krypton-86, Krypton-82, Krypton-83, Krypton-80, Krypton-78
Type :- Natural and Non-Metal (Noble Gas)
Family :- The Noble Gas 
Characteristics Properties :- Colourless, Odourless, Tasteless and Monoatomic.''')
         

    elif x == "rubidium" or x == '37' or x == 'rb':
         easygui.msgbox('''Element :- RUBIDIUM
Symbol :- Rb
Atomic Number :- 37
Atomic Mass :- 85.468 amu
Atomic Size :- (Calculated 265 pm) & (Vander Waals 303 pm)
Electronic Configuration :- [Kr] 5s1
Found In :- Group-1 And Period-5
Discovered By :- Gustav Kirchhoff and Robert Bunsen in 1861
Valence Electron :- 1
Isotopes :- Rubidium-85
Type :- Natural and Metal
Family :- Alkali Metals
Characteristics Properties :- Soft, Silvery-White Colour, Highly Inflammable.''')
         

    elif x == "strontium" or x == '38' or x == 'sr':
         easygui.msgbox('''Element :- STRONTIUM
Symbol :- Sr
Atomic Number :- 38
Atomic Mass :- 87.62 amu
Atomic Size :- (Calculated 219 pm) & (Vander Waals 249 pm)
Electronic Configuration :- [Kr] 5s2
Found In :- Group-2 And Period-5
Discovered By :- Adair Crawford and William Cruickshank and Humphry Davy in 1790
Valence Electron :- 2
Isotopes :- Strontium-84, Strontium-86, Strontium-81, Strontium-88
Type :- Natural and Metal
Family :- Alkaline Earth Metals
Characteristics Properties :- Soft, Silver-Yellow Colour, Reacts with Water.''')
         

    elif x == "yttrium" or x == '39' or x == 'y':
         easygui.msgbox('''Element :- YTTRIUM
Symbol :- Y
Atomic Number :- 39
Atomic Mass :- 88.906 amu
Atomic Size :- (Calculated 212 pm)
Electronic Configuration :- [Kr] 4d1 5s2
Found In :- Group-3 And Period-5
Discovered By :- Johan Gadolin in 1794
Valence Electron :- 3
Isotopes :- Yttrium-89
Type :- Never found in nature as a free element and it is a Metal
Family :- Scandium Family (Transition Metal)
Characteristics Properties :- Silvery White Colour, Moderately soft, Ductile Metal.''')
         

    elif x == "zirconium" or x == '40' or x == 'zr':
         easygui.msgbox('''Element :- ZIRCONIUM
Symbol :- Zr
Atomic Number :- 40
Atomic Mass :- 91.224 amu
Atomic Size :- (Calculated 206 pm)
Electronic Configuration :- [Kr] 4d2 5s2
Found In :- Group-4 And Period-5
Discovered By :- Martin Heinrich Klaproth in 1789
Valence Electron :- 4
Isotopes :- Zirconium-90, Zirconium-91, Zirconium-92, Zirconium-94, Zirconium-96
Type :- Natural and Metal
Family :- Titanium Family (Transition Metal)
Characteristics Properties :- Very Strong, Malleable, Ductile, Lustrous Silver-Gray Metal.''')
         

    elif x == "niobium" or x == '41' or x == 'nb':
         easygui.msgbox('''Element :- NIOBIUM 
Symbol :- Nb
Atomic Number :- 41
Atomic Mass :- 92.906 amu
Atomic Size :- (Calculated 198 pm)
Electronic Configuration :- [Kr] 4d4 5s1
Found In :- Group-5 And Period-5
Discovered By :- Charles Hatchett in 1801
Valence Electron :- 5
Isotopes :- Niobium-94
Type :- Natural and Metal
Family :- Vanadium Family (Transition Metal)
Characteristics Properties :- Rare, Soft, Malleable, Ductile, Gray-White Metal.''')
         

    elif x == "molybdenum" or x == '42' or x == 'mo':
         easygui.msgbox('''Element :- MOLYBDENUM
Symbol :- Mo
Atomic Number :- 42
Atomic Mass :- 95.95 amu
Atomic Size :- (Calculated 190 pm)
Electronic Configuration :- [Kr] 4d5 5s1
Found In :- Group-6 And Period-5
Discovered By :- Carl Welhelm Scheele in 1778
Valence Electron :- 6
Isotopes :-  Molybdenum-92, Molybdenum-94, Molybdenum-95, Molybdenum-96, Molybdenum-97, Molybdenum-98, Molybdenum-100
Type :- It is not found free in nature and It is a Metal
Family :- Chromium Family (Transition Metal)
Characteristics Properties :- Ductile and Highly Resistant to Corrosion.''')
         

    elif x == "technetium" or x == '43' or x == 'tc':
         easygui.msgbox('''Element :- TECHNETIUM
Symbol :- Tc
Atomic Number :- 43
Atomic Mass :- 98.907 amu
Atomic Size :- (Calculated 183 pm)
Electronic Configuration :- [Kr] 4d5 5s2
Found In :- Group-7 And Period-5
Discovered By :- Emilio Segrè in 1937
Valence Electron :- 7
Isotopes :- Technetium-98
Type :- Found Naturally but in small Amount and It is a Metal
Family :- Manganese Family (Transition Metal)
Characteristics Properties :- Rare, Silver-Gray metal, Tarnishes slowly in Moist Air.''')
         

    elif x == "ruthenium" or x == '44' or x == 'ru':
         easygui.msgbox('''Element :- RUTHENIUM
Symbol :- Ru
Atomic Number :- 44
Atomic Mass :- 101.07 amu
Atomic Size :- (Calculated 178 pm)
Electronic Configuration :- [Kr] 4d7 5s1
Found In :- Group-8 And Period-5
Discovered By :- Karl Ernst Claus in 1844
Valence Electron :- 8
Isotopes :- Ruthenium-96, Ruthenium-98, Ruthenium-99, Ruthenium-100, Ruthenium-101, Ruthenium-102, Ruthenium-104
Type :- It is found in Ores and It is a Metal
Family :- Iron Family (Transition Metal)
Characteristics Properties :- Very Rare, Lustrous, Brittle, Does not tarnish at Room Temprature.''')
         

    elif x == "rhodium" or x == '45' or x == 'rh':
         easygui.msgbox('''Element :- RHODIUM
Symbol :- Rh
Atomic Number :- 45
Atomic Mass :- 102.906 amu
Atomic Size :- (Calculated 173 pm)
Electronic Configuration :- [Kr] 4d8 5s1
Found In :- Group-9 And Period-5
Discovered By :- William Hyde Wollaston in 1803
Valence Electron :- 9
Isotopes :- Rhodium-103
Type :- Natural and Metal
Family :- Cobalt Family (Transition Metal)
Characteristics Properties :- It has a high reflectance and is hard and durable, Upon heating it turns to the oxide.''')
         

    elif x == "palladium" or x == '46' or x == 'pd':
         easygui.msgbox('''Element :- PALLADIUM
Symbol :- Pd
Atomic Number :- 46
Atomic Mass :- 106.42 amu
Atomic Size :- (Calculated 169 pm) & (Vander Waals 163 pm)
Electronic Configuration :- [Kr] 4d10
Found In :- Group-10 And Period-5
Discovered By :- William Hyde Wollaston in 1803
Valence Electron :- 10
Isotopes :- Palladium-102, Palladium-104, Palladium-105, Palladium-106, Palladium-108, Palladium-110
Type :- Natural and Metal
Family :- Nickel Family (Transition Metal)
Characteristics Properties :- Highly Dense, Malleable, Ductile.''')
         

    elif x == "silver" or x == '47' or x == 'ag':
         easygui.msgbox('''Element :- SILVER
Symbol :- Ag
Atomic Number :- 47
Atomic Mass :- 107.868 amu
Atomic Size :- (Calculated 165 pm) & (Vander Waals 172 pm)
Electronic Configuration :- [Kr] 4d10 5s1
Found In :- Group-11 And Period-5
Discovered By :- The Chaldeans (Approx 3000 BC)
Valence Electron :- 11
Isotopes :- Silver-107, Silver-109
Type :- Natural and Metal
Family :- Copper Family (Transition Metal)
Characteristics Properties :- Nearly White, Lustrous, Soft, Excellent Conductor.''')
         

    elif x == "cadmium" or x == '48' or x == 'cd':
         easygui.msgbox('''Element :- CADMIUM
Symbol :- Cd
Atomic Number :- 48
Atomic Mass :- 112.414 amu
Atomic Size :- (Calculated 161 pm) & (Vander Waals 158 pm)
Electronic Configuration :- [Kr] 4d10 5s2
Found In :- Group-12 And Period-5
Discovered By :- Friedrich Stromeyer in 1817
Valence Electron :- 12 
Isotopes :- Cadmium-110, Cadmium-111, Cadmium-112
Type :- Natural and Metal
Family :- Zinc Group
Characteristics Properties :- Bluish-Tinge Surface, Ductile, Malleable Metal.''')
         

    elif x == "indium" or x == '49' or x == 'in':
         easygui.msgbox('''Element :- INDIUM
Symbol :- In
Atomic Number :- 49
Atomic Mass :- 114.818amu
Atomic Size :- (Calculated 156 pm) & (Vander Waals 193 pm)
Electronic Configuration :- [Kr] 4d10 5s2 5p1
Found In :- Group-13 And Period-5
Discovered By :- Ferdinand Reich in 1863
Valence Electron :- 3
Isotopes :- Indium-113, Indium-115
Type :- Natural and Metal
Family :- Zinc Family (Transition Metal)
Characteristics Properties :- Soft, Malleable, Ductile, Lustrous.''')
         

    elif x == "tin" or x == '50' or x == 'sn':
         easygui.msgbox('''Element :- TIN
Symbol :- Sn
Atomic Number :- 50
Atomic Mass :- 118.711 amu
Atomic Size :- (Calculated 145 pm) & (Vander Waals 217 pm)
Electronic Configuration :- [Kr] 4d10 5s2 5p2
Found In :- Group-14 And Period-5
Discovered By :- - (Approx 2100 BC)
Valence Electron :- 4
Isotopes :- Tin-120
Type :- Natural and Metal
Family :- Carbon Family
Characteristics Properties :- Soft, Pliable, Silvery-White Metal.''')
        

    elif x == "antimony" or x == '51' or x == 'sb':
         easygui.msgbox('''Element :- ANITMONY
Symbol :- Sb
Atomic Number :- 51
Atomic Mass :- 121.760 amu
Atomic Size :- (Calculated 133 pm) & (Vander Waals 206 pm)
Electronic Configuration :- [Kr] 4d10 5s2 5p3
Found In :- Group-15 And Period-5
Discovered By :- Nicolas Lémery in 1707
Valence Electron :- 5
Isotopes :- Antimony-123
Type :- Natural and Semi-Metal
Family :- Nitrogen Group
Characteristics Properties :- Metallic Form is bright, Hard, Brittle.''')
         

    elif x == "tellurium" or x == '52' or x == 'te':
         easygui.msgbox('''Element :- TELLURIUM
Symbol :- Te
Atomic Number :- 52
Atomic Mass :- 127.6 amu
Atomic Size :- (Calculated 123 pm) & (Vander Waals 206 pm)
Electronic Configuration :- [Kr] 4d10 5s2 5p4
Found In :- Group-16 And Period-5
Discovered By :- Franz Joseph Müller von Reichenstein in 1783
Valence Electron :- 6
Isotopes :- Tellurium-120, Tellurium-122, Tellurium-123, Tellurium-124, Tellurium-125, Tellurium-126, Tellurium-128, Tellurium-130
Type :- Present in Earth Crust only and It is a Metalloids
Family :- The Chalcogen
Characteristics Properties :- Lustrous, Crystalline, Brittle.''')
         

    elif x == "iodine" or x == '53' or x == 'i':
         easygui.msgbox('''Element :- IODINE
Symbol :- I
Atomic Number :- 53
Atomic Mass :- 126.904 amu
Atomic Size :- (Calculated 115 pm) & (Vander Waals 198 pm)
Electronic Configuration :- [Kr] 4d10 5s2 5p5
Found In :- Group-17 And Period-5
Discovered By :- Bernard Courtois in 1811
Valence Electron :- 7
Isotopes :- Iodine-127
Type :- Natural and Non-Metal
Family :- The Halogens
Characteristics Properties :- Dark-Gray/Purple-Black, Solid, Lustrous.''')
         

    elif x == "xenon" or x == '54' or x == 'xe':
         easygui.msgbox('''Element :- XENON
Symbol :- Xe
Atomic Number :- 54
Atomic Mass :- 131.294 amu
Atomic Size :- (Calculated 108 pm) & (Vander Waals 216 pm)
Electronic Configuration :- [Kr] 4d10 5s2 5p5
Found In :- Group-18 And Period-5
Discovered By :- William Ramsay and Morris Travers in 1898
Valence Electron :- 8
Isotopes :- Xenon-124, Xenon-125, Xenon-128, Xenon-129, Xenon-130, Xenon-131, Xenon-132, Xenon-134, Xenon-136
Type :- Natural and Non-Metal
Family :- Noble Gas Family
Characteristics Properties :- Rare, Odorless, Colourless, Tasteless, Chemically unreactive Gas.''')
         

    elif x == "cesium" or x == '55' or x == 'cs':
         easygui.msgbox('''Element :- CESIUM
Symbol :- Cs
Atomic Number :- 55
Atomic Mass :- 132.905 amu
Atomic Size :- (Calculated 298 pm) & (Vander Waals 343 pm)
Electronic Configuration :- [Xe] 6s1
Found In :- Group-1 And Period-6
Discovered By :- Gustav Kirchhoff and Robert Bunsen in 1860
Valence Electron :- 1 
Isotopes :- Cesium-133
Type :- Natural and Metal
Family :- The Alkali Metals
Characteristics Properties :- Silvery-Gold, Soft, Ductile.''')
         

    elif x == "barium" or x == '56' or x == 'ba':
         easygui.msgbox('''Element :- BARIUM
Symbol :- Ba
Atomic Number :- 56
Atomic Mass :- 137.328amu
Atomic Size :- (Calculated 253 pm) & (Vander Waals 268 pm)
Electronic Configuration :- [Xe] 6s2
Found In :- Group-2 And Period-6
Discovered By :- Humphry Davy in 1808
Valence Electron :- 2
Isotopes :- Barium-138, Barium-137, Barium-136, Barium-135, Barium-134, Barium-132
Type :- Natural and Metal
Family :- Alkaline Earth Metals
Characteristics Properties :- Soft,  Silvery Metal that rapidly Tarnishes in Air and Reacts with Water.''')
         

    elif x == "lanthanum" or x == '57' or x == 'la':
         easygui.msgbox('''Element :-LANTHANUM 
Symbol :- La
Atomic Number :- 57
Atomic Mass :- 138.905amu
Atomic Size :- (Calculated 226 pm)
Electronic Configuration :- [Xe] 5d1 6s2
Found In :- Group-3 and Period-6
Discovered By :- Carl Gustav Mosander in 1839
Valence Electron :- 3
Isotopes :- Lanthanum-138, Lanthanum-139
Type :- Natural and Metal
Family :- Lanthanoids Family
Characteristics Properties :- Ductile, Malleable, Silvery-White, Can be cut with Knife.''')

         
    elif x == "cerium" or x == '58' or x == 'ce':
         easygui.msgbox('''Element :- CERIUM
Symbol :- Ce
Atomic Number :- 58
Atomic Mass :- 140.116 amu
Atomic Size :- (Calculated 210 pm)
Electronic Configuration :- [Xe] 4f1 5d1 6s2 
Found In :- Period-6
Discovered By :- Jöns Jacob Berzelius and Wilhelm Hisinger in 1803
Valence Electron :- 4
Isotopes :- Cerium-136, Cerium-138, Cerium-140, Cerium-142
Type :- Natural and Metal
Family :- Lanthanoid Family
Characteristics Properties :- Malleable, Soft, Ductile, Iron-Grey, Harder than Lead.''')
         

    elif x == "praseodymium" or x == '59' or x == 'pr':
         easygui.msgbox('''Element :- PRASEODYMIUM
Symbol :- Pr
Atomic Number :- 59
Atomic Mass :- 140.908amu
Atomic Size :- (Calculated 247 pm)
Electronic Configuration :- [Xe] 4f3 6s2
Found In :- Period-6
Discovered By :- Carl Auer von Welsbach in 1885 
Valence Electron :- 5
Isotopes :- Praseodymium-141
Type :- Natural and Metal
Family :- Rare Earth Metal
Characteristics Properties :- Soft, Silvery, Malleable, Ductile.''')
         

    elif x == "neodymium" or x == '60' or x == 'nd':
         easygui.msgbox('''Element :- NEODYMIUM
Symbol :- Nd
Atomic Number :- 60
Atomic Mass :- 144.243 amu
Atomic Size :- (Calculated 206 pm)
Electronic Configuration :- [Xe] 4f4 6s2
Found In :- Period-6
Discovered By :- Carl Auer von Welsbach in 1885
Valence Electron :- 6
Isotopes :- Neodymium-142, Neodymium-143, Neodymium-145, Neodymium-146, Neodymium-148
Type :- It is found in minerals that include all lanthanide minerals, such as monazite and bastnasite and It is a Metal
Family :- Rare Earth Metals
Characteristics Properties :- Ductile, Malleablr, Silvery-White, Oxidises Readily in Air.''')
         

    elif x == "Promethium" or x == '61' or x == 'pm':
         easygui.msgbox('''Element :- PROMETHIUM
Symbol :- Pm
Atomic Number :- 61
Atomic Mass :- 144.913 amu
Atomic Size :- (Calculated 205 pm)
Electronic Configuration :- [Xe] 4f5 6s2
Found In :- Period-6
Discovered By :- Jacob .A. Marinsky and Lawrence E. Glendenin and Charles D. Coryell in 1945
Valence Electron :- 7
Isotopes :- Promrthium-145
Type :- Man-Made and Metal
Family :- Lanthanides
Characteristics Properties :- Emits Beta Radiation, Salts have a red or pink colour.''')
         

    elif x == "samarium" or x == '62' or x == 'sm':
         easygui.msgbox('''Element :- SAMARIUM
Symbol :- Sm
Atomic Number :- 62
Atomic Mass :- 150.36 amu
Atomic Size :- (Calculated 238 pm)
Electronic Configuration :- [Xe] 4f6 6s2
Found In :- Period-6
Discovered By :- Paul-Émile Lecoq de Boisbaudran in 1879
Valence Electron :- 8
Isotopes :- Samarium-144, Samarium-149, Samarium-150,  Samarium-152, Samarium-154
Type :- Natural and Metal
Family :- Lanthanide
Characteristics Properties :- Silvery-White Metal, Used in Optical Lasers, Used as a Neutron absorber in Nuclear reactors.''')
         

    elif x == "europium" or x == '63' or x == 'eu':
         easygui.msgbox('''Element :- EUROPIUM
Symbol :- Eu
Atomic Number :- 63
Atomic Mass :- 151.964 amu
Atomic Size :- (Calculated 231 pm)
Electronic Configuration :- [Xe] 4f7 6s2
Found In :- Period-6
Discovered By :- Eugène-Anatole Demarçay in 1901
Valence Electron :- 9
Isotopes :- Europium-151, Europium-153
Type :- Natural and Metal
Family :- Lanthanide
Characteristics Properties :- Soft, Silvery, Highly Reactive, Ductile.''')
         

    elif x == "gadolinium" or x == '64' or x == 'gd':
         easygui.msgbox('''Element :- GADOLINIUM
Symbol :- Gd
Atomic Number :- 64
Atomic Mass :- 157.25 amu
Atomic Size :- (Calculated 233 pm)
Electronic Configuration :- [Xe] 4f7 5d1 6s2
Found In :- Period-6
Discovered By :- Charles Galissard de Marignac at Geneva in 1880
Valence Electron :- 10
Isotopes :- Gadolinium-154, Gadolinium-155, Gadolinium-156, Gadolinium-157, Gadolinium-158, Gadolinium-160
Type :- Natural and Metal
Family :- Lanthanide
Characteristics Properties :- Soft, Shiny, Ductile, Silvery Metal.''')
         

    elif x == "terbium" or x == '65' or x == 'tb':
         easygui.msgbox('''Element :- TERBIUM
Symbol :- Tb
Atomic Number :- 65
Atomic Mass :- 158.925 amu
Atomic Size :- (Calculated 225 pm)
Electronic Configuration :- [Xe] 4f9 6s2
Found In :- Period-6
Discovered By :- Carl Gustaf Mosander in 1843
Valence Electron :- 11
Isotopes :- Terbium-159
Type :- Natural amd Metal
Family :- Lanthanides
Characteristics Properties :- Soft, Malleable, Ductile, Silver-Gray Metal.''')
                 

    elif x == "dysprosium" or x == '66' or x == 'dy':
         easygui.msgbox('''Element :- DYSPROSIUM
Symbol :- Dy
Atomic Number :- 66
Atomic Mass :- 162.500 amu
Atomic Size :- (Calculated 228 pm)
Electronic Configuration :- [Xe] 4f10 6s2
Found In :- Period-6
Discovered By :- Paul Émile Lecoq de Boisbaudran in 1886
Valence Electron :- 12
Isotopes :- Dysprosium-156, Dysprosium-158, Dysprosium-160, Dysprosium-161, Dysprosium-162, Dysprosium-163, Dysprosium-164
Type :- Natural and Metal
Family :- Rare-Earth (Lanthanides)
Characteristics Properties :- Lustrous, Very Soft, Silvery Metal.''')
         

    elif x == "holmium" or x == '67' or x == 'ho':
         easygui.msgbox('''Element :- HOLMIUM
Symbol :- Ho
Atomic Number :- 67
Atomic Mass :- 164.930 amu
Atomic Size :- (Calculated 226 pm) 
Electronic Configuration :- [Xe] 4f11 6s2
Found In :- Period-6
Discovered By :- Marc Delafontaine and Louis Soret and Per Teodor Cleve in 1878
Valence Electron :- 13
Isotopes :- Holmium-165
Type :- Not naturally found as a free element and it is a Metal
Family :- Rare-Earth (Lanthanide)
Characteristics Properties :- Melleable, Soft, Lustrous, Silvery Colour.''')
         

    elif x == "erbium" or x == '68' or x == 'er':
         easygui.msgbox('''Element :- ERBIUM
Symbol :- Er
Atomic Number :- 68
Atomic Mass :- 167.259 amu
Atomic Size :- (Calculated 226 pm) 
Electronic Configuration :- [Xe] 4f12 6s2
Found In :- Period-6
Discovered By :- Carl-Gustav Mosander in 1843
Valence Electron :- 14
Isotopes :- Erbium-166, Erbium-168, Erbium-167, Erbium-170, Erbium-164, Erbium-162
Type :- Natural and Metal
Family :- Rare-Earth (Lanthanide)
Characteristics Properties :- Soft, Malleable, Lustrous, Silvery Colour.''')
         

    elif x == "Thulium" or x == '69' or x == 'tm':
         easygui.msgbox('''Element :- THULIUM
Symbol :- Tm
Atomic Number :- 69
Atomic Mass :- 168.934 amu
Atomic Size :- (Calculated 222 pm) 
Electronic Configuration :- [Xe] 4f13 6s2
Found In :- Period-6
Discovered By :- Per Teodor Cleve in 1879
Valence Electron :- 15
Isotopes :- Thulium-169
Type :- The element is never found in nature in pure form and it is a Metal
Family :- Lanthanide
Characteristics Properties :- Bright Silver-Gray Lusture, Can be cut with Knife.''')
         

    elif x == "ytterbium" or x == '70' or x == 'yb':
         easygui.msgbox('''Element :- YTTERBIUM
Symbol :- Yb
Atomic Number :- 70
Atomic Mass :- 173.055 amu
Atomic Size :- (Calculated 222 pm)
Electronic Configuration :- [Xe] 4f14 6s2
Found In :- Period-6
Discovered By :- Jean Charles Galissard de Marignac in 1878
Valence Electron :- 16
Isotopes :- Ytterbium-174, Ytterbium-172, Ytterbium-173, Ytterbium-171, Ytterbium-176, Ytterbium-170, Ytterbium-168
Type :- Natural and Metal
Family :- Rare-Earth (lanthanide)
Characteristics Properties :- Soft, Malleable, Ductile, Bright Silvery Lusture.''')
         

    elif x == "lutetium" or x == '71' or x == 'lu':
         easygui.msgbox('''Element :- LUTETIUM
Symbol :- Lu
Atomic Number :- 71
Atomic Mass :- 174.967 amu
Atomic Size :- (Calculated 217 pm) 
Electronic Configuration :- [Xe] 4f14 5d1 6s2
Found In :- Period-6
Discovered By :- Georges Urbain	in 1907
Valence Electron :- 3
Isotopes :- Lutetium-175, Lutetium-176
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Silvery-White, Soft and Ductile, Stable in Air, Harder and Denser than all Lanthanides.''')
         

    elif x == "hafnium" or x == '72' or x == 'hf':
         easygui.msgbox('''Element :- HAFNIUM
Symbol :- Hf
Atomic Number :- 72
Atomic Mass :- 178.49 amu
Atomic Size :- (Calculated 208 pm) 
Electronic Configuration :- [Xe] 4f14 5d2 6s2
Found In :- Group-4 and Period-6
Discovered By :- Dirk Coster and Charles de Hevesy in 1923
Valence Electron :- 4
Isotopes :- Hafnium-174, Hafnium-176, Hafnium-177, Hafnium-178, Hafnium-179, Hafnium-180
Type :- Natural (But obtained from zirconium) and Metal
Family :- Transition Element
Characteristics Properties :- Shiny-Silvery Metal, Corrosion Resistant, Ductile.''')
         

    elif x == "tantalum" or x == '73' or x == 'ta':
         easygui.msgbox('''Element :- TANTALUM
Symbol :- Ta
Atomic Number :- 73
Atomic Mass :- 180.948 amu
Atomic Size :- (Calculated 200 pm)
Electronic Configuration :- [Xe] 4f14 5d3 6s2
Found In :- Group-5 and Period-6
Discovered By :- Anders Gustaf Ekenberg	1802
Valence Electron :- 5
Isotopes :- Tantalum-180, Tantalum-181
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- High Density, Extremely High Melting Point, Excellent Resistance to all Acids.''')
         

    elif x == "tungsten" or x == '74' or x == 'w':
         easygui.msgbox('''Element :- TUNGSTEN
Symbol :- W
Atomic Number :- 74
Atomic Mass :- 183.84 amu
Atomic Size :- (Calculated 193 pm) 
Electronic Configuration :- [Xe] 4f14 5d4 6s2
Found In :- Group-6 and Period-6
Discovered By :- Juan José and Fausto Elhuyar in 1783
Valence Electron :- 6
Isotopes :- Tungsten-180, Tungsten-182, Tungsten-183, Tungsten-184, Tungsten-186
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Nickel-While to Grayish Lusture, Melting Point-3410°C, Low Coefficient of Linear Thermal Expansion.''')
         

    elif x == "rhenium" or x == '75' or x == 're':
         easygui.msgbox('''Element :- RHENIUM
Symbol :- Re
Atomic Number :- 75
Atomic Mass :- 186.207 amu
Atomic Size :- (Calculated 188 pm)
Electronic Configuration :- [Xe] 4f14 5d5 6s2
Found In :- Group-7 and Period-6
Discovered By :- Ida Tacke-Noddack and Walter Noddack and Otto Carl Berg in 1925
Valence Electron :- 7
Isotopes :- Rhenium-185, Rhenium-187
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Silvery-White, Extremely Hard, Highest Melting Points of the Elements.''')
         

    elif x == "osmium" or x == '76' or x == 'os':
         easygui.msgbox('''Element :- OSMIUM
Symbol :- Os
Atomic Number :- 76
Atomic Mass :- 190.23 amu
Atomic Size :- (Calculated 185 pm)
Electronic Configuration :- [Xe] 4f14 5d6 6s2
Found In :- Group-8 and Period-6
Discovered By :- Smithson Tennant in 1803
Valence Electron :- 8
Isotopes :- Osmium-184, Osmium-186, Osmium-187, Osmium-188, Osmium-189, Osmium-190, Osmium-192
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Very Hard, Brittle, Difficult to work, even at High Temperature.''')
         

    elif x == "iridium" or x == '77' or x == 'ir':
         easygui.msgbox('''Element :- IRIDIUM
Symbol :- Ir
Atomic Number :- 77
Atomic Mass :- 192.217 amu
Atomic Size :- (Calculated 180 pm)
Electronic Configuration :- [Xe] 4f14 5d7 6s2
Found In :- Group-9 and Period-6
Discovered By :- Smithson Tennant in 1803
Valence Electron :- 9
Isotopes :- Iridium-191, Iridium-193
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Hard, Silvery Metal, Unreactive as Gold.''')
         

    elif x == "platinum" or x == '78' or x == 'pt':
         easygui.msgbox('''Element :- PLATINUM
Symbol :- Pt
Atomic Number :- 78
Atomic Mass :- 195.085 amu
Atomic Size :- (Calculated 177 pm) & (Vander Waals 175 pm)
Electronic Configuration :- [Xe] 4f14 5d9 6s1
Found In :- Group-10 and Period-6
Discovered By :- Known to pre-Columbian Indians , Antonio de Ulloa in 1735
Valence Electron :- 10
Isotopes :- Platinum-190, Platinum-192, Platinum-194, Platinum-195, Platinum-196, Platinum-198
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Very Heavy, Precious, Silver-White, Soft, Ductile.''')
         

    elif x == "gold" or x == '79' or x == 'au':
         easygui.msgbox('''Element :- GOLD
Symbol :- Au
Atomic Number :- 79
Atomic Mass :- 196.967 amu
Atomic Size :- (Calculated 174 pm) & (Vander Waals 166 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s1
Found In :- Group-11 and Period-6
Discovered By :- Know to the Ancients
Valence Electron :- 11
Isotopes :- Gold-197
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Ductile, Highly Reflective, Conducts Heat and Electricity, Malleable.''')

         
    elif x == "mercury" or x == '80' or x == 'hg':
         easygui.msgbox('''Element :- MERCURY
Symbol :- Hg
Atomic Number :- 80
Atomic Mass :- 200.592 amu
Atomic Size :- (Calculated 171 pm) & (Vander Waals 155 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2
Found In :- Group-12 and Period-6
Discovered By :- Known since ancient times
Valence Electron :- 12
Isotopes :- Mercury-196, Mercury-198, Mercury-199, Mercury-200, Mercury-201, Mercury-202, Mercury-204
Type :- Natural and Metal
Family :- Transition Element
Characteristics Properties :- Fair conductor of Electricity, Poor conductor of Heat, Highest Volatility of any Metal.''')
         

    elif x == "thallium" or x == '81' or x == 'tl':
         easygui.msgbox('''Element :- THALLIUM
Symbol :- Tl
Atomic Number :- 81
Atomic Mass :- 204.383 amu
Atomic Size :- (Calculated 156 pm) & (Vander Waals 196 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2 6p1
Found In :- Group-13 and Period-6
Discovered By :- Sir William Crookes in 1861
Valence Electron :- 3
Isotopes :- Thallium-203, Thallium-205
Type :- Natural and Metalloid
Family :- Alluminum Family
Characteristics Properties :- Soft, Low-Melting, Low Tensile Strength.''')
         

    elif x == "lead" or x == '82' or x == 'pb':
         easygui.msgbox('''Element :- LEAD
Symbol :- Pb
Atomic Number :- 82
Atomic Mass :- 207.2 amu
Atomic Size :- (Calculated 154 pm) & (Vander Waals 202 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2 6p2
Found In :- Group-14 and Period-6
Discovered By :- Known since ancient times
Valence Electron :- 4
Isotopes :- Lead-204, Lead-206, Lead-207, Lead-208
Type :- Natural and Metal
Family :- Carbon Family
Characteristics Properties :- Very Malleable, Ductile, Dense, Poor Conductor of Electricity.''')
         

    elif x == "bismuth" or x == '83' or x == 'bi':
         easygui.msgbox('''Element :- BISMUTH
Symbol :- Bi
Atomic Number :- 83
Atomic Mass :- 208.980 amu
Atomic Size :- (Calculated 143 pm) & (Vander Waals 207 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2 6p3
Found In :- Group-15 and Period-6
Discovered By :- Claude Geoffroy the Younger in 1753
Valence Electron :- 5
Isotopes :- Bismuth-209
Type :- Natural and Metal
Family :- Nitrogen Family
Characteristics Properties :- High Density, Silvery, Pink-Tinged Metal, Brittle.''')
         

    elif x == "polonium" or x == '84' or x == 'po':
         easygui.msgbox('''Element :- POLONIUM
Symbol :- Po
Atomic Number :- 84
Atomic Mass :- 208.982 amu
Atomic Size :- (Calculated 135 pm) & (Vander Waals 197 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2 6p4
Found In :- Group-16 and Period-6
Discovered By :- Marie Sklodowska Curie in 1898
Valence Electron :- 6
Isotopes :- Polonium-209, Polonium-210
Type :- Natural and Metalloid
Family :- Chalcogen Family
Characteristics Properties :- Radioactive, Extremely rare semi-metal.''')
         

    elif x == "astatine" or x == '85' or x == 'at':
         easygui.msgbox('''Element :- ASTATINE
Symbol :- At
Atomic Number :- 85
Atomic Mass :- 209.987 amu
Atomic Size :- (Calculated 127 pm) & (Vander Waals 202 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2 6p5
Found In :- Group-17 and Period-6
Discovered By :- Dale R. Carson and K.R. MacKenzie and Emilio Segrè in 1940
Valence Electron :- 7
Isotopes :- Astatine-210, Astatine-211
Type :- Natural and Non-Metal
Family :- Halogen Family
Characteristics Properties :- Dangerously Radioactive Element.''')
         

    elif x == "radon" or x == '86' or x == 'rn':
         easygui.msgbox('''Element :- RADON
Symbol :- Rn
Atomic Number :- 86
Atomic Mass :- 222.018 amu
Atomic Size :- (Calculated 120 pm) & (Vander Waals 220 pm)
Electronic Configuration :- [Xe] 4f14 5d10 6s2 6p6
Found In :- Group-18 and Period-6
Discovered By :- Friedrich Ernst Dorn in 1900
Valence Electron :- 8
Isotopes :- Radon-211, Radon-220, Radon-222
Type :- Natural and Non-Metal
Family :- Nobel Gas Family
Characteristics Properties :- Colourless Gas, 7.5 times Heavier that Air, 100 time Heavies than Hydrogen.''')
         

    elif x == "francium" or x == '87' or x == 'fr':
         easygui.msgbox('''Element :- FRANCIUM
Symbol :- Fr
Atomic Number :- 87
Atomic Mass :- 223.020 amu
Atomic Size :- (Vander Waals 348 pm)
Electronic Configuration :- [Rn] 7s1
Found In :- Group-1 and Period-7
Discovered By :- Marguerite Catherine Perey	1939
Valence Electron :- 1
Isotopes :- Francium-223
Type :- Natural and Metal
Family :- Alkali Metal
Characteristics Properties :- Heavy, Unstable, Radioactive, 22 Minutes of Half-Life.''')
         

    elif x == "radium" or x == '88' or x == 'ra':
         easygui.msgbox('''Element :- RADIUM
Symbol :- Ra
Atomic Number :- 88
Atomic Mass :- 226.025 amu
Atomic Size :- (Vander Waals 283 pm)
Electronic Configuration :- [Rn] 7s2
Found In :- Group-2 and Period-7
Discovered By :- Marie Sklodowska Curie and Pierre Curie in 1898
Valence Electron :- 2
Isotopes :- Radium-223, Radium-224, Radium-226, Radium-228
Type :- Natural and Metal
Family :- Alkaline Earth Metal
Characteristics Properties :- Silvery, Lustrous, Soft, Intensely Radioactive.''')
         

    elif x == "actinium" or x == '89' or x == 'ac':
         easygui.msgbox('''Element :- ACTINIUM
Symbol :- Ac
Atomic Number :- 89
Atomic Mass :- 227.028 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 6d1 7s2
Found In :- Group-3 and Period-7
Discovered By :- André-Louis Debierne in 1899
Valence Electron :- 3
Isotopes :- Actinium-227
Type :- Natural and Metal
Family :- The Actinides Family
Characteristics Properties :- Soft, Silvery-White, Radioactive.''')
         

    elif x == "thorium" or x == '90' or x == 'th':
         easygui.msgbox('''Element :- THORIUM
Symbol :- Th
Atomic Number :- 90
Atomic Mass :- 232.038 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 6d2 7s2
Found In :- Period-7
Discovered By :- Jöns Jacob Berzelius in 1828
Valence Electron :- 4
Isotopes :- Thorium-230, Thorium-232
Type :- Natural and Metal
Family :- The Actinides Family
Characteristics Properties :- Silvery, Tarnishes Black when it is exposed to Air, Moderately Soft, Malleable.''')
         

    elif x == "protactinium" or x == '91' or x == 'pa':
         easygui.msgbox('''Element :- PROTACTINIUM
Symbol :- Pa
Atomic Number :- 91
Atomic Mass :- 231.036 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f2 6d1 7s2
Found In :- Period-7
Discovered By :- Kasimir Fajans and O.H. Göhring in 1913
Valence Electron :- 5
Isotopes :- Protactinium-231
Type :- Natural and Metal
Family :- The Actinides Family
Characteristics Properties :- Malleable, Shiny, Silver-Gray, Radioactive.''')
         

    elif x == "uranium" or x == '92' or x == 'u':
         easygui.msgbox('''Element :- URANIUM
Symbol :- U
Atomic Number :- 92
Atomic Mass :- 238.029 amu
Atomic Size :- (Vander Waals 186 pm)
Electronic Configuration :- [Rn] 5f3 6d1 7s2
Found In :- Period-7
Discovered By :- Martin Heinrich Klaproth in 1789
Valence Electron :- 6
Isotopes :- Uranium-233, Uranium-234, Uranium-235, Uranium-236, Uranium-238
Type :- Natural and Metal
Family :- The Actinides Family
Characteristics Properties :- Heavy, Silvery-White, Malleable, Ductile, Softer than Steel.''')
         

    elif x == "neptunium" or x == '93' or x == 'np':
         easygui.msgbox('''Element :- NEPTUNIUM
Symbol :- Np
Atomic Number :- 93
Atomic Mass :- 237.048 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f4 6d1 7s2
Found In :- Period-7
Discovered By :- Edwin M. McMillian and Philip H. Abelson in 1940
Valence Electron :- 7
Isotopes :- Neptunium-236, Neptunium-237
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Ductile, Silvery, Radioactive.''')
         

    elif x == "plutonium" or x == '94' or x == 'pu':
         easygui.msgbox('''Element :- PLUTONIUM
Symbol :- Pu
Atomic Number :- 94
Atomic Mass :- 244.064 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f6 7s2
Found In :- Period-7
Discovered By :- Glenn T. Seaborg and Joseph W. Kennedy and Edward M. McMillan and Arthur C. Wohl in 1941
Valence Electron :- 8
Isotopes :- Plutonium-238, Plutonium-239, Plutonium-240, Plutonium-241, Plutonium-242, Plutonium-244
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Silvery Apperance, Yellow Tarnish appears when Slightly Oxidized.''')
         

    elif x == "americium" or x == '95' or x == 'am':
         easygui.msgbox('''Element :- AMERICIUM
Symbol :- Am
Atomic Number :- 95
Atomic Mass :- 243.061 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f7 7s2
Found In :- Period-7
Discovered By :- Glenn T. Seaborg and Ralph A. James and Leon O. Morgan and Albert Ghiorso in 1944
Valence Electron :- 9
Isotopes :- Americium-241, Americium-243
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Silvery-White, Highly Radioactive.''')
         

    elif x == "curium" or x == '96' or x == 'cm':
         easygui.msgbox('''Element :- CURIUM
Symbol :- Cm
Atomic Number :- 96
Atomic Mass :- 247.070 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f7 6d1 7s2
Found In :- Period-7
Discovered By :- Glenn T. Seaborg and Ralph A. James and Albert Ghiorso and 1944
Valence Electron :- 10
Isotopes :- Curium-243, Curium-244, Curium-245, Curium-246, Curium-247, Curium-248
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Hard, Brittle, Silvery, Radioactive''')
         

    elif x == "berkelium" or x == '97' or x == 'bk':
         easygui.msgbox('''Element :- BERKELIUM
Symbol :- Bk
Atomic Number :- 97
Atomic Mass :- 247.070 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f9 7s2
Found In :- Period-7
Discovered By :- Stanley G. Thompson and Glenn T. Seaborg and Kenneth Street, Jr.and Albert Ghiorso in 1949
Valence Electron :- 11
Isotopes :- Berkelium-247, Berkelium-249
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Soft, Silvery-White, Radioactive''')
         

    elif x == "californium" or x == '98' or x == 'cf':
         easygui.msgbox('''Element :- CALIFORNIUM
Symbol :- Cf
Atomic Number :- 98
Atomic Mass :- 251.080 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f10 7s2
Found In :- Period-7
Discovered By :- Stanley G. Thompson and Glenn T. Seaborg and Kenneth Street, Jr. and Albert Ghiorso in 1950
Valence Electron :- 12
Isotopes :- Californium-249, Californium-250, Californium-251, Californium-252
Type :- 
Family :- The Actinides Family
Characteristics Properties :- Silvery-White, Melting Point-900°C, Boiling Point-1470°C.''')

         
    elif x == "einsteinium" or x == '99' or x == 'es':
         easygui.msgbox('''Element :- EINSTEINIUM
Symbol :- Es
Atomic Number :- 99
Atomic Mass :- 254 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f11 7s2
Found In :- Period-7
Discovered By :- Albert Ghiorso et. al. in 1952
Valence Electron :- 13
Isotopes :- Einsteinium-252
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Metallic, Radioactive, No known uses.''')
         

    elif x == "fermium" or x == '100' or x == 'fm':
         easygui.msgbox('''Element :- FERMIUM
Symbol :- Fm
Atomic Number :- 100
Atomic Mass :- 257.095 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f12 7s2
Found In :- Period-7
Discovered By :- Albert Ghiorso et. al.	in 1952
Valence Electron :- 14
Isotopes :- Fermium-257
Type :- Man-Maade and Metal
Family :- The Actinides Family
Characteristics Properties :- Synthetic, Radioactive''')
         


    elif x == "mendelevium" or x == '101' or x == 'md':
         easygui.msgbox('''Element :- MENDELEVIUM
Symbol :- Md
Atomic Number :- 101
Atomic Mass :- 258.1 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f13 7s2
Found In :- Period-7
Discovered By :- Stanley G. Thompson and Glenn T. Seaborg and Bernard G. Harvey and Gregory R. Choppin and Albert Ghiorso in 1955
Valence Electron :- 15
Isotopes :- Mendelevium-258, Mendelevium-260
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Moderately stable divalent state in addition to a trivalent state, Radioactive.''')
         

    elif x == "nobelium" or x == '102' or x == 'no':
         easygui.msgbox('''Element :- NOBELIUM
Symbol :- No
Atomic Number :- 102
Atomic Mass :- 259.101 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f14 7s2
Found In :- Period-7
Discovered By :- Albert Ghiorso and Glenn T. Seaborg and Torbørn Sikkeland and John R. Walton in 1958
Valence Electron :- 16
Isotopes :- Nobelium-259
Type :- Man-Made and Metal
Family :- The Actinides Family
Characteristics Properties :- Synthetic, Highly Radioactive, Divalent ion in Aqueous Solution.''')
         

    elif x == "lawrencium" or x == '103' or x == 'lr':
         easygui.msgbox('''Element :- LAWRENCIUM
Symbol :- Lr
Atomic Number :- 103
Atomic Mass :- 262 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f14 7s2 7p1
Found In :- Period-7
Discovered By :- Albert Ghiorso and Torbjørn Sikkeland and Almon E. Larsh and Robert M. Latimer in 1961
Valence Electron :- 3
Isotopes :- Lawrencium-262
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Synthetic, Radioactive''')
         

    elif x == "rutherfordium" or x == '104' or x == 'rf':
         easygui.msgbox('''Element :- RUTHERFORDIUM
Symbol :- Rf
Atomic Number :- 104
Atomic Mass :- 261 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- [Rn] 5f14 6d2 7s2
Found In :- Group-4 and Period-7
Discovered By :- Scientists at Dubna, Russia in 1964 and Albert Ghiorso et. al. in 1969
Valence Electron :- 4
Isotopes :- Rutherfordium-267
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Highly Radioactive''')
         

    elif x == "dubnium" or x == '105' or x == 'db':
         easygui.msgbox('''Element :- DUBNIUM
Symbol :- Db
Atomic Number :- 105
Atomic Mass :- 262 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d3 7s2
Found In :- Group-5 and Period-7
Discovered By :- Scientists at Dubna, Russia in 1967 and Lawrence Berkeley Laboratory in 1970
Valence Electron :- 5
Isotopes :- Dubnium-268
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Longest-Lived Isotope, Synthetic''')
         

    elif x == "seaborgium" or x == '106' or x == 'sg':
         easygui.msgbox('''Element :- SEABORGIUM
Symbol :- Sg
Atomic Number :- 106
Atomic Mass :- 266 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d4 7s2
Found In :- Group-6 and Period-7
Discovered By :- Albert Ghiorso et. al. in 1974
Valence Electron :- 6
Isotopes :- Seaborgium-271
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Silvery-White or Metallic Gray apperance.''')
         

    elif x == "bohrium" or x == '107' or x == 'bh':
         easygui.msgbox('''Element :- BOHRIUM
Symbol :- Bh
Atomic Number :- 107
Atomic Mass :- 264 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d5 7s2
Found In :- Group-7 and Period-7
Discovered By :- Scientists at Dubna, Russia in 1976
Valence Electron :- 7
Isotopes :- Bohrium-272
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Soft, Silvery Metal, Tarnishes in Air, Reacts with water.''')
         

    elif x == "hassium" or x == '108' or x == 'hs':
         easygui.msgbox('''Element :- HASSIUM
Symbol :- Hs
Atomic Number :- 108
Atomic Mass :- 269 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d6 7s2
Found In :- Group-8 and Period-7
Discovered By :- Peter Armbruster and Gottfried Münzenber in 1984
Valence Electron :- 8
Isotopes :- Hassium-270
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Silvery-White or Metallic Gray colour.''')
         

    elif x == "meitnerium" or x == '109' or x == 'mt' :
         easygui.msgbox('''Element :- MEITNERIUM
Symbol :- Mt
Atomic Number :- 109
Atomic Mass :- 278 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d7 7s2
Found In :- Group-9 and Period-7
Discovered By :- Peter Armbruster and Gottfried Münzenber in 1982
Valence Electron :- 9
Isotopes :- Meiterium-276
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Synthetic, Radioactive.''')
         

    elif x == "darmstadtium" or x == '110' or x == 'ds':
         easygui.msgbox('''Element :- DARMSTADTIUM
Symbol :- Ds
Atomic Number :- 110
Atomic Mass :- 281 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d9 7s1
Found In :- Group-10 and Period-7
Discovered By :- Peter Armbruster and Gottfried Münzenber in 1994
Valence Electron :- 10
Isotopes :- Darmstadtium-281
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Highly Radioactive, Synthetic.''')
         

    elif x == "roentgenium" or x == '111' or x == 'rg':
         easygui.msgbox('''Element :- ROENTGENIUM
Symbol :- Rg
Atomic Number :- 111
Atomic Mass :- 280 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s1
Found In :- Group-11 and Period-7
Discovered By :- Peter Armbruster and Gottfried Münzenber in 1994
Valence Electron :- 11
Isotopes :- Roentgenium-280
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Extremely Unstable, Radioactive.''')
         

    elif x == "copernicium" or x == '112' or x == 'cn':
         easygui.msgbox('''Element :- COPERNICIUM
Symbol :- Cn
Atomic Number :- 112
Atomic Mass :- 285 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2
Found In :- Group-12 and Period-7
Discovered By :- Peter Armbruster and Gottfried Münzenber in 1996
Valence Electron :- 12
Isotopes :- Copernicium-285
Type :- Man-Made and Metal
Family :- Transition Element
Characteristics Properties :- Radioactive, Unreactive.''')
         

    elif x == "nihonium" or x == '113' or x == 'nh':
         easygui.msgbox('''Element :- NIHONIUM
Symbol :- Nh
Atomic Number :- 113
Atomic Mass :- 286 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2 7p1
Found In :- Group-13 and Period-7
Discovered By :- Y. T. Oganessian et. al. in 2004
Valence Electron :- 3
Isotopes :- Nihonium-284
Type :- Man-Made and Metal
Family :- Boron Family
Characteristics Properties :- Radioactive, Synthetic.''')
         

    elif x == "flerovium" or x == '114' or x == 'fl':
         easygui.msgbox('''Element :- FLEROVIUM
Symbol :- Fl
Atomic Number :- 114
Atomic Mass :- 289 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2 7p2
Found In :- Group-14 and Period-7
Discovered By :- Scientists at Dubna, Russia with Scientists from Lawrence Livermore National Laboratory in 1998
Valence Electron :- 4
Isotopes :- Flerovium-289
Type :- Man-Made and Metal
Family :- Carbon Family
Characteristics Properties :- Superheavy, Radioactive, Synthetic''')

         
    elif x == "moscovium" or x == '115' or x == 'mc':
         easygui.msgbox('''Element :- MOSCOVIUM
Symbol :- Mc
Atomic Number :- 115
Atomic Mass :- 286 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2 7p3
Found In :- Group-15 and Period-7
Discovered By :- Y. T. Oganessian et. al. in 2004
Valence Electron :- 5
Isotopes :- Moscovium-288
Type :- Man-Made and Metal
Family :- Nitrogen Family
Characteristics Properties :- Dense, High atomic weight.''')
         

    elif x == "livermorium" or x == '116' or x == 'lv':
         easygui.msgbox('''Element :- LIVERMORIUM
Symbol :- Lv
Atomic Number :- 116
Atomic Mass :- 293 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2 7p4
Found In :- Group-16 and Period-7
Discovered By :- Scientists at Dubna, Russia with Scientists from Lawrence Livermore National Laboratory in 2001
Valence Electron :- 6
Isotopes :- Livermorium-293
Type :- Man-Made and Metal
Family :- Chalcogens Family
Characteristics Properties :- Highly Radioactive, Synthetic.''')
         

    elif x == "tennessine" or x == '117' or x == 'ts':
         easygui.msgbox('''Element :- TENNESSINE
Symbol :- Ts
Atomic Number :- 117
Atomic Mass :- 294 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2 7p5
Found In :- Group-17 and Period-7
Discovered By :- Y. T. Oganessian et. al. in 2010
Valence Electron :- 7
Isotopes :- Tennessine-292
Type :- Man-Made and Metal
Family :- Halogen Family
Characteristics Properties :- Harmful, Radioactive, Synthetic.''')
        

    elif x == "oganesson" or x == '118' or x == 'og':
         easygui.msgbox('''Element :- OGANESSON
Symbol :- Og
Atomic Number :- 118
Atomic Mass :- 294 amu
Atomic Size :- Data Unavailable
Electronic Configuration :- *[Rn] 5f14 6d10 7s2 7p6
Found In :- Group-18 and Period-7
Discovered By :- Y. T. Oganessian et. al. in 2006
Valence Electron :- 8
Isotopes :- Oganesson-294
Type :- Man-Made and Metal
Family :- Nobel Gas Family
Characteristics Properties :- Radioactive, Synthetic.''')
         

    elif x == "exit" or "":
         easygui.msgbox("Thank You For Using This.")	
         break
    else:
         easygui.msgbox ("Element Not Found")
         
