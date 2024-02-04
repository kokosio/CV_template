from fpdf import FPDF

fntgen = 'Cambria'

pdf = FPDF()
pdf.add_font(fntgen, '', '/path/to/font/font.ttf', uni=True)
pdf.add_font(fntgen, 'I', '/path/to/font/font.ttf', uni=True)
pdf.add_font(fntgen, 'B', '/path/to/font/font.ttf', uni=True)
pdf.add_font(fntgen, 'BI', '/path/to/font/font.ttf', uni=True)

pdf.add_page()

#_______________________________
# ELEMENT FUNCTIONS
#_______________________________

def structure():
    # HEADER
    pdf.set_font(fntgen, 'I', 18)
    pdf.set_text_color(120,120,120)
    pdf.text(73, 30, 'Curriculum Vitae')
    pdf.set_text_color(0,83,71)
    pdf.set_font(fntgen, 'B', 28)
    pdf.text(73, 22, 'Name Surname')
        # portrait
    pdf.image("/path/to/picture/avatar.PNG", x = 0.3, y = 5, w = 60, h = 36,)
        # big rectangle
    pdf.set_fill_color(0,83,71) 
    pdf.rect(-1, 50, 62, 300, style = 'F')

def technical(begining):
    # USAGE: 

    # SECTION TITLE
    pdf.set_fill_color(0,57,46)
    pdf.rect(4, begining, 53, 10, style = 'F')               # 44.5
    pdf.set_font(fntgen, '', 11)
    pdf.set_text_color(255,255,255)
    pdf.text(8, begining + 6.5, 'TECHNICAL SKILLS')          # 51

    #empty skill bars
    pdf.set_fill_color(166,166,166)       
    pdf.rect(8, begining + 24.5, 45, 1, style = 'F')         # 69
    pdf.rect(8, begining + 39.5, 45, 1, style = 'F')         # 84
    pdf.rect(8, begining + 54.5, 45, 1, style = 'F')         # 99
    pdf.rect(8, begining + 69.5, 45, 1, style = 'F')         # 114
    pdf.rect(8, begining + 84.5, 45, 1, style = 'F')         # 129
    #pdf.rect(8, begining + 99.5, 45, 1, style = 'F')         # 144

    #partial skill bars
    pdf.set_fill_color(255,255,255)      
    pdf.set_text_color(255,255,255)
    pdf.text(8, begining + 19.5, 'Skill 1')                      # 64
    pdf.rect(8, begining + 24.5, 24, 1, style = 'F')         # 69
    pdf.text(8, begining + 34.5, 'Skill 2')                   # 79
    pdf.rect(8, begining + 39.5, 24, 1, style = 'F')         # 84
    pdf.text(8, begining + 49.5, 'Skill 3')               # 94
    pdf.rect(8, begining + 54.5, 24, 1, style = 'F')         # 99
    pdf.text(8, begining + 64.5, 'Skill 4')                     # 109
    pdf.rect(8, begining + 69.5, 24, 1, style = 'F')       # 114
    pdf.text(8, begining + 79.5, 'Skill 5')                   # 124
    pdf.rect(8, begining + 84.5, 24, 1, style = 'F')         # 129

def languages(begining):
    # USAGE:

    # SECTION TITLE
    pdf.set_fill_color(0,57,46) 
    pdf.rect(4, begining, 53, 10, style = 'F')    # 162.5  
    pdf.set_text_color(255,255,255)       
    pdf.text(8, begining + 6.5, 'LANGUAGES')      # 169
    
    # LANGUAGE BARS

    # native language
    pdf.set_fill_color(255,255,255)           
    pdf.set_text_color(255,255,255)

    pdf.text(8, begining + 19.5, 'Language 1 -- Proficiency')     # 182
    pdf.rect(8, begining + 24.5, 45, 1, style = 'F')        # 187

    # language1    
    pdf.set_text_color(255,255,255)
    pdf.text(8, begining + 34.5, 'Language 2 -- Proficiency')	  	    # 197

        # empty language bar
    pdf.set_fill_color(166,166,166)                
    pdf.rect(8, begining + 39.5, 45 , 1, style = 'F')       # 202
          
        # partial language bar 
    pdf.set_fill_color(255,255,255)
    pdf.rect(8, begining + 39.5, 44, 1, style = 'F')        # 202

def personal(begining):
    # USAGE:

    # TEXT
    text = [
    "NAME: Name Surname,",
    "LOCATION: City, Country",
    "MOBILE: +xxx xx xxx xxx",
    "E-MAIL:", 
    "name_surname@domain.com",
    "DATE OF BIRTH: MM/YYYY",
    "NATIONALITY: Nationality"
    ]

    # SECTION TITLE
    pdf.set_fill_color(0,57,46) #british racing green
    pdf.rect(4, begining, 53, 10, style = 'F')           # 221
    pdf.set_text_color(255,255,255)
    pdf.text(8, begining + 6.5, 'PERSONAL DETAILS')          # 227.5

    # SECTION BODY
    pdf.text(8, begining + 18, text[0])               # 239
    pdf.text(8, begining + 24.5, text[1])             # 245.5
    pdf.text(8, begining + 31, text[2])               # 252
    pdf.text(8, begining + 37.5, text[3])             # 258.5
    pdf.text(8, begining + 43, text[4])               # 264   
    pdf.text(8, begining + 50.5, text[5])             # 271.5 
    pdf.text(8, begining + 57, text[6])               # 278

def work(begining):
    # USAGE:

    # TEXT
    wrkexp2 = [
    "Professional Experience 1",                    # 0
    "Institution/Company of emplyment 1 / MM.YYYY - MM.YYYY",   # 1
    "Job description 1;",                           # 2
    "Job description 2;",                           # 3
    "Job description 3.",                           # 4

    "Professional Experience 2",                                                 # 5
    "Institution/Company of emplyment 2 / MM.YYYY - MM.YYYY",   # 6
    "Job description 1;",                           # 7
    "Job description 2;",                           # 8
    "Job description 3.",                           # 9

    "Professional Experience 3",                    # 10
    "Institution/Company of emplyment 3 / MM.YYYY - MM.YYYY",   # 11
    "Job description 1;",                           # 12
    "Job description 2.",                           # 13
    ]

    # SECTION TITLE                                                 #position
    pdf.set_fill_color(0,83,71)                         
    pdf.rect(70, begining, 141, 10, style = 'F')                    # 44.5
    pdf.set_text_color(255,255,255)
    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 6.5, 'EXPERIENCE')                      # 51

    # SECTION BODY
    pdf.set_text_color(0,0,0)
    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 19.5, wrkexp2[0])            # 64
    pdf.set_font(fntgen, 'B', 11)
    pdf.text(73, begining + 26, wrkexp2[1])              # 70.5
    pdf.text(80, begining + 32.5, wrkexp2[2])            # 77
    pdf.text(80, begining + 39, wrkexp2[3])              # 83.5
    pdf.text(80, begining + 45.5, wrkexp2[4])            # 90

    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 54.5, wrkexp2[5])            # 99
    pdf.set_font(fntgen, 'B', 11)
    pdf.text(73, begining + 61, wrkexp2[6])              # 105.5
    pdf.text(80, begining + 67.5, wrkexp2[7])            # 112
    pdf.text(80, begining + 74, wrkexp2[8])              # 118.5 
    pdf.text(80, begining + 80.5, wrkexp2[9])            # 125

    pdf.set_font(fntgen, 'B', 13)       
    pdf.text(73, begining + 89.5, wrkexp2[10])           # 134
    pdf.set_font(fntgen, 'B', 11)           
    pdf.text(73, begining + 96, wrkexp2[11])             # 140.5
    pdf.text(80, begining + 102.5, wrkexp2[12])          # 147
    pdf.text(80, begining + 109, wrkexp2[13])            # 153.5

    # BULLET POINTS
    pdf.set_fill_color(0,83,71)
    pdf.ellipse(75, begining + 30.5, 1.5, 1.5, style = 'F')      # 75
    pdf.ellipse(75, begining + 37, 1.5, 1.5, style = 'F')        # 81.5
    pdf.ellipse(75, begining + 43.5, 1.5, 1.5, style = 'F')      # 88

    pdf.ellipse(75, begining + 65.5, 1.5, 1.5, style = 'F')     # 110
    pdf.ellipse(75, begining + 72, 1.5, 1.5, style = 'F')   # 116.5
    pdf.ellipse(75, begining + 78.5, 1.5, 1.5, style = 'F')     # 123

    pdf.ellipse(75, begining + 100.5, 1.5, 1.5, style = 'F')     # 145
    pdf.ellipse(75, begining + 107, 1.5, 1.5, style = 'F')   # 151.5

def education(begining):
    # USAGE: 

    # TEXT
    edu = [
    "Degree 1 in Major",
    "Alma mater / MM.YYYY - MM.YYYY",
    "Degree 2 in Major",
    "Alma mater / MM.YYYY - MM.YYYY",
    "Thesis work;",
    "Subjects mastered."
    ]

    # SECTION TITLE                                  # position
    pdf.set_fill_color(0,83,71)
    pdf.rect(70, begining, 141, 10, style = 'F')     # 162.5
    pdf.set_text_color(255,255,255)
    pdf.set_font(fntgen, 'B', 13)                   
    pdf.text(73,begining + 6.5, "EDUCATION")         # 169
    
    # SECTION BODY
    pdf.set_text_color(0,0,0)
    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 18, edu[0])              # 180.5
    pdf.set_font(fntgen, '', 11)
    pdf.text(73, begining + 24.5, edu[1])            # 187
    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 33.5, edu[2])            # 196   
    pdf.set_font(fntgen, '', 11)
    pdf.text(73, begining + 40, edu[3])              # 202.5
    pdf.text(80, begining + 46.5, edu[4])            # 209
    pdf.text(80, begining + 53, edu[5])              # 215.5

    # BULLET POINTS
    pdf.ellipse(75, begining + 44.5, 1.5, 1.5, style = 'F')       # 207
    pdf.ellipse(75, begining + 51, 1.5, 1.5, style = 'F')     # 213.5

def extracurricular(begining):
    # USAGE:

    # TITLE
    extra = [
        "Extracurricular experience 1",
        "Institution/Company of employment / MM.YYYY - MM.YYYY",
        "Assembled and calibrated experimental setups;",
        "Job description 1;",
        "Job description 2.",
    ]

    # SECTION TITLE
    pdf.set_fill_color(0,83,71)
    pdf.rect(70, begining, 141, 10, style = 'F')                     # 221

    pdf.set_text_color(255,255,255)
    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 6.5, "EXTRACURRICULAR EXPERIENCE")            # 227.5

    # SECTION BODY
    pdf.set_text_color(0,0,0)                   
    pdf.set_font(fntgen, 'B', 13)
    pdf.text(73, begining + 18, extra[0])                            # 239
    pdf.set_font(fntgen, '', 11)
    pdf.text(73, begining + 24.5, extra[1])                          # 245.5
    pdf.text(80, begining + 31, extra[2])                            # 252
    pdf.text(80, begining + 37.5, extra[3])                          # 258.5
    pdf.text(80, begining + 44, extra[4])                            # 265                        # 287

    # BULLET POINTS     
    pdf.ellipse(75, begining + 29, 1.5, 1.5, style = 'F')             # 250
    pdf.ellipse(75, begining + 35.5, 1.5, 1.5, style = 'F')           # 256.5
    pdf.ellipse(75, begining + 42, 1.5, 1.5, style = 'F')             # 263

#_______________________________

# LAYOUT   
structure()

#------------------
# left
#------------------

# TECHNICAL SKILLS
technical(44.5)

# LANGUAGES
languages(162.5)

# PERSONAL PARAGRAPH
personal(221)

#------------------
# right 
#------------------

# WORK PARAGRAPH
work(44.5)          

# EXTRACURRICULAR ACTIVITIES PARAGRAPH
extracurricular(162.5)    

# EDUCATION PARAGRAPH
education(221)        

#------------------

# GENERATE
pdf.output('cv_template.pdf', 'F')
