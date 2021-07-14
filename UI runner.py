#user interface runner

import pygame, pickle
from os import listdir 

from file_path_converter import convert_path
from schedule import get_schedule
from months_in_order import get_month_number
from months_in_order import get_days_in_a_month
from months_in_order import get_number_month

pi = True

pygame.init()
pygame.font.init()

myfont = pygame.font.SysFont('Currier', 25)

myfont2 = pygame.font.SysFont('Currier', 50)

myfont3 = pygame.font.SysFont('Currier', 15)

display = pygame.display.set_mode((792, 612))

pygame.display.set_caption('Project')

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
key_color = (58, 166, 221)
gray = (229, 229, 229, 255)
light_blue = (58, 166, 221, 255)

#Load Database and stuff

print('Loading')

if pi :
    arsenal = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Arsenal.dat'), 'rb'))
    aston_villa = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Aston Villa.dat'), 'rb'))
    brighton_and_hove_albion = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Brighton & Hove Albion.dat'), 'rb'))
    burnley = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Burnley.dat'), 'rb'))
    chelsea = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Chelsea.dat'), 'rb'))
    crystal_palace = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Crystal Palace.dat'), 'rb'))
    everton = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Everton.dat'), 'rb'))
    fulham = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Fulham.dat'), 'rb'))
    leeds_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leeds United.dat'), 'rb'))
    leicester_city = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leicester City.dat'), 'rb'))
    liverpool = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Liverpool.dat'), 'rb'))
    manchester_city = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester City.dat'), 'rb'))
    manchester_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester United.dat'), 'rb'))
    newcastle_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Newcastle United.dat'), 'rb'))
    sheffield_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Sheffield United.dat'), 'rb'))
    southampton = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Southampton.dat'), 'rb'))
    tottenham_hotspur = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Tottenham Hotspur.dat'), 'rb'))
    west_bromwich_albion = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Bromwich Albion.dat'), 'rb'))
    west_ham_united = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Ham United.dat'), 'rb'))
    wolverhampton_wanderers = pickle.load(open(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Wolverhampton Wanderers.dat'), 'rb'))
else :
    arsenal = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Arsenal.dat', 'rb'))
    aston_villa = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Aston Villa.dat', 'rb'))
    brighton_and_hove_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Brighton & Hove Albion.dat', 'rb'))
    burnley = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Burnley.dat', 'rb'))
    chelsea = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Chelsea.dat', 'rb'))
    crystal_palace = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Crystal Palace.dat', 'rb'))
    everton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Everton.dat', 'rb'))
    fulham = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Fulham.dat', 'rb'))
    leeds_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leeds United.dat', 'rb'))
    leicester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Leicester City.dat', 'rb'))
    liverpool = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Liverpool.dat', 'rb'))
    manchester_city = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester City.dat', 'rb'))
    manchester_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Manchester United.dat', 'rb'))
    newcastle_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Newcastle United.dat', 'rb'))
    sheffield_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Sheffield United.dat', 'rb'))
    southampton = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Southampton.dat', 'rb'))
    tottenham_hotspur = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Tottenham Hotspur.dat', 'rb'))
    west_bromwich_albion = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Bromwich Albion.dat', 'rb'))
    west_ham_united = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\West Ham United.dat', 'rb'))
    wolverhampton_wanderers = pickle.load(open('C:\\Users\\rhyde23\\Desktop\\Project\\Team Database\\Wolverhampton Wanderers.dat', 'rb'))

print('done')

#######################################################################################################################################

#Saves Screen Stuff

#######################################################################################################################################

save_number = 0

def get_save_image(save_number) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Images\\', 'Save', str(save_number), '.png'])
    if pi :
        path = convert_path(path)
    return pygame.image.load(path).convert()

save_background_images = []
for i in range(10) :
    current_save_image = get_save_image(i+1)
    save_background_images.append(current_save_image)

current_save_image = save_background_images[save_number]

save_names = []
for i in range(10) :
    path = ''.join(['C:\\Users\\rhyde23\\Desktop\\Project\\Saves\\', 'File', str(i+1), 'BasicInfo.dat'])
    if pi :
        path = convert_path(path)
    basic_info = pickle.load(open(path, 'rb'))
    save_names.append(basic_info['SaveName'])

save_names_texts = []
for save_name in save_names :
    save_names_texts.append(myfont.render(save_name, True, (0, 0, 0)))
    
clicker_mode = False
current_clicked = (0, 0)


y_difference = 37
x_start, x_end = 43, 761
buttons = []
for i in range(10) :
    first_y = 154+(i*y_difference)
    second_y = first_y+y_difference
    buttons.append([first_y, second_y])

print(buttons)

offset = [12, 13, 14, 16, 17, 19, 20, 22, 23, 25]


save_selected = None

#######################################################################################################################################

#Name Save Stuff

#######################################################################################################################################

if not pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png').convert(),
        pygame.K_n:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png').convert(),
        pygame.K_b:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png').convert(),
        pygame.K_v:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png').convert(),
        pygame.K_c:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png').convert(),
        pygame.K_x:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png').convert(),
        pygame.K_z:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png').convert(),
        pygame.K_l:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png').convert(),
        pygame.K_k:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png').convert(),
        pygame.K_j:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png').convert(),
        pygame.K_h:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png').convert(),
        pygame.K_g:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png').convert(),
        pygame.K_f:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png').convert(),
        pygame.K_d:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png').convert(),
        pygame.K_s:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png').convert(),
        pygame.K_a:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png').convert(),
        pygame.K_p:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png').convert(),
        pygame.K_o:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png').convert(),
        pygame.K_i:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png').convert(),
        pygame.K_u:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png').convert(),
        pygame.K_y:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png').convert(),
        pygame.K_t:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png').convert(),
        pygame.K_r:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png').convert(),
        pygame.K_e:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png').convert(),
        pygame.K_w:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png').convert(),
        pygame.K_q:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png').convert(),
        pygame.K_BACKSPACE:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png').convert(),
        pygame.K_0:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png').convert(),
        pygame.K_9:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png').convert(),
        pygame.K_8:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png').convert(),
        pygame.K_7:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png').convert(),
        pygame.K_6:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png').convert(),
        pygame.K_5:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png').convert(),
        pygame.K_4:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png').convert(),
        pygame.K_3:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png').convert(),
        pygame.K_2:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png').convert(),
        pygame.K_1:pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png').convert(),
    }
    
if pi :
    keyboard_order = {
        pygame.K_m:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-002.png')).convert(),
        pygame.K_n:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-003.png')).convert(),
        pygame.K_b:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-004.png')).convert(),
        pygame.K_v:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-005.png')).convert(),
        pygame.K_c:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-006.png')).convert(),
        pygame.K_x:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-007.png')).convert(),
        pygame.K_z:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-008.png')).convert(),
        pygame.K_l:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-009.png')).convert(),
        pygame.K_k:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-010.png')).convert(),
        pygame.K_j:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-011.png')).convert(),
        pygame.K_h:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-012.png')).convert(),
        pygame.K_g:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-013.png')).convert(),
        pygame.K_f:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-014.png')).convert(),
        pygame.K_d:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-015.png')).convert(),
        pygame.K_s:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-016.png')).convert(),
        pygame.K_a:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-017.png')).convert(),
        pygame.K_p:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-018.png')).convert(),
        pygame.K_o:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-019.png')).convert(),
        pygame.K_i:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-020.png')).convert(),
        pygame.K_u:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-021.png')).convert(),
        pygame.K_y:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-022.png')).convert(),
        pygame.K_t:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-023.png')).convert(),
        pygame.K_r:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-024.png')).convert(),
        pygame.K_e:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-025.png')).convert(),
        pygame.K_w:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-026.png')).convert(),
        pygame.K_q:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-027.png')).convert(),
        pygame.K_BACKSPACE:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-028.png')).convert(),
        pygame.K_0:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-029.png')).convert(),
        pygame.K_9:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-030.png')).convert(),
        pygame.K_8:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-031.png')).convert(),
        pygame.K_7:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-032.png')).convert(),
        pygame.K_6:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-033.png')).convert(),
        pygame.K_5:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-034.png')).convert(),
        pygame.K_4:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-035.png')).convert(),
        pygame.K_3:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-036.png')).convert(),
        pygame.K_2:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-037.png')).convert(),
        pygame.K_1:pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-038.png')).convert(),
    }

keyboard_letters = {
    pygame.K_m:'M',
    pygame.K_n:'N',
    pygame.K_b:'B',
    pygame.K_v:'V',
    pygame.K_c:'C',
    pygame.K_x:'X',
    pygame.K_z:'Z',
    pygame.K_l:'L',
    pygame.K_k:'K',
    pygame.K_j:'J',
    pygame.K_h:'H',
    pygame.K_g:'G',
    pygame.K_f:'F',
    pygame.K_d:'D',
    pygame.K_s:'S',
    pygame.K_a:'A',
    pygame.K_p:'P',
    pygame.K_o:'O',
    pygame.K_i:'I',
    pygame.K_u:'U',
    pygame.K_y:'Y',
    pygame.K_t:'T',
    pygame.K_r:'R',
    pygame.K_e:'E',
    pygame.K_w:'W',
    pygame.K_q:'Q',
    pygame.K_0:'0',
    pygame.K_9:'9',
    pygame.K_8:'8',
    pygame.K_7:'7',
    pygame.K_6:'6',
    pygame.K_5:'5',
    pygame.K_4:'4',
    pygame.K_3:'3',
    pygame.K_2:'1',
    pygame.K_1:'1',
}

def get_x_value(width) :
    return int((792-width)/2)

current_typed = ""
current_typed_text = myfont2.render(current_typed, True, light_blue)
current_typed_x = get_x_value(current_typed_text.get_width())

if pi :
    default_typed_screen = pygame.image.load(convert_path('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png')).convert()

if not pi :
    default_typed_screen = pygame.image.load('C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Page-001.png').convert()

current_typed_screen = default_typed_screen

space_bar_down = False

enter_extension_string = "the Save"
string2 = "save"

name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
name_save_header_x = get_x_value(name_save_header.get_width())

too_many_chars_text = myfont.render("You've reached the max amount of characters!", True, red)
too_many_chars_x = get_x_value(too_many_chars_text.get_width())

too_many_chars = False

enter_or_submit = True
over_submit = False

new_save_name = ''

entering_save = True

#######################################################################################################################################

#Calendar Screen

#Temporary Save Stuff

current_data = {
    'TeamName':'Arsenal',
    'ManagerName':'Reggie Hyde',
    'CurrentLineup':['Bernd Leno', 'Hector Bellerin', 'David Luiz', 'Gabriel', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Gabriel Martinelli', 'Martin Odegaard', 'Alexandre Lacazette'],
    'CurrentFormation':'4-2-3-1 (Wide)',
    'CurrentBudget':100000000,
    'CurrentTeamOverall':79,
    'DaysAdvanced':0,
    'CurrentDate':'June 25 2020',
    'CurrentEmails':['Welcome to Arsenal, Manager Hyde. Here is your email inbox where you will receive important messages. Be sure to check your email to stay updated on the Premier League.'],
    'UnreadEmails':0,
    'CurrentStandings':{},
    'CurrentStandingsInOrder':[],
    'TopScorers':{},
    'TopScorersInOrder':[],
    'TopAssistors':{},
    'TopAssistorsInOrder':[],
    'Arsenal_Players':{},
    'Arsenal_Formation':'4-2-3-1 (Wide)',
    'Arsenal_Lineup':['Bernd Leno', 'Hector Bellerin', 'David Luiz', 'Gabriel', 'Kieran Tierney', 'Thomas Partey', 'Granit Xhaka', 'Bukayo Saka', 'Gabriel Martinelli', 'Martin Odegaard', 'Alexandre Lacazette'],
    'Aston Villa_Players':{},
    'Aston Villa_Formation':'4-2-3-1 (Wide)',
    'Aston Villa_Lineup':['Emiliano Martinez', 'Matty Cash', 'Ezri Konsa', 'Tyrone Mings', 'Matt Targett', 'Douglas Luiz', 'John McGinn', 'Bertrand Traore', 'Anwar El Ghazi', 'Jack Grealish', 'Ollie Watkins'],
}

red_cover = pygame.Surface((71,71))  # the size of your rect
red_cover.set_alpha(128)                # alpha level
red_cover.fill((255,0,0))           # this fills the entire surface


"""
while calendar :
    display.fill(white)
    display.blit(current_calendar_screen, (0, 0))
    display.blit(red_cover, (day_x, day_y))
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN :
            coords = pygame.mouse.get_pos()
            print(coords)
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_RIGHT :
                day_x += 1
            elif event.key == pygame.K_LEFT :
                day_x -= 1
            elif event.key == pygame.K_DOWN :
                day_y += 1
            elif event.key == pygame.K_UP :
                day_y -= 1
            elif event.key == pygame.K_RETURN :
                coords_of_days[current_date] = [day_x, day_y]
                current_date, change_screen = advance_one_day(current_date)
                if change_screen :
                    print(coords_of_days)
                    quit()
                day_x, day_y = guess_coords_of_day(current_date)
    pygame.display.update()
"""

coords_of_days = {
    'June 1 2020': (55, 190),
    'June 2 2020': (127, 190),
    'June 3 2020': (199, 190),
    'June 4 2020': (271, 190),
    'June 5 2020': (343, 190),
    'June 6 2020': (415, 190),
    'June 7 2020': (487, 190),
    'June 8 2020': (56, 262),
    'June 9 2020': (128, 262),
    'June 10 2020': (200, 262),
    'June 11 2020': (272, 262),
    'June 12 2020': (344, 262),
    'June 13 2020': (416, 262),
    'June 14 2020': (487, 262),
    'June 15 2020': (56, 335),
    'June 16 2020': (128, 335),
    'June 17 2020': (200, 335),
    'June 18 2020': (272, 335),
    'June 19 2020': (344, 335),
    'June 20 2020': (416, 335),
    'June 21 2020': (487, 335),
    'June 22 2020': (56, 407),
    'June 23 2020': (128, 407),
    'June 24 2020': (200, 407),
    'June 25 2020': (272, 407),
    'June 26 2020': (344, 407),
    'June 27 2020': (416, 407),
    'June 28 2020': (487, 407),
    'June 29 2020': (56, 479),
    'June 30 2020': (128, 479)
}



def unpack_date(date) :
    splitted = date.split(' ') 
    return [splitted[0], int(splitted[1]), int(splitted[2])]

def build_date(month, day, year) :
    return ' '.join([month, str(day), str(year)])

def advance_one_day(date) :
    month, day, year = unpack_date(date)
    month_number = get_month_number(month)
    change_screen = False
    if day == get_days_in_a_month(month) :
        if month == 'December' :
            month, day, year = 'January', 1, year+1
        else :
            month, day, year = get_number_month(month_number+1), 1, year
        change_screen = True
    else :
        month, day, year = month, day+1, year
    return build_date(month, day, year), change_screen

def guess_coords_of_day(date) :
    month, day, year = unpack_date(date)
    mod = day % 7
    if mod == 0 :
        down, right = int((day-mod)/7)-1, 7
    else :
        down, right = int((day-mod)/7), mod
    return ((right-1)*73)+55, (down*73)+190


calendar_screens = []

for i in range(12) :
    path = 'C:\\Users\\rhyde23\\Desktop\\Project\\Images\\Month-'+str(i+1)+'.png'
    if pi :
        path = convert_path(path)
    calendar_screens.append(pygame.image.load(path).convert())

current_date = current_data['CurrentDate']
month, day, year = unpack_date(current_date)
month_number = get_month_number(month)
current_calendar_screen = calendar_screens[month_number]
day_x, day_y = guess_coords_of_day(current_date)



#######################################################################################################################################

manager_loop = True
saves_menu = False
name_save = False
calendar = True



while manager_loop :
    while calendar :
        display.fill(white)
        display.blit(current_calendar_screen, (0, 0))
        display.blit(red_cover, coords_of_days[current_date])
        pygame.display.update()
    while saves_menu :
        display.fill(white)
        display.blit(current_save_image, (0, 0))
        display.set_at(current_clicked, red)
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if clicker_mode :
                    current_clicked = coords
                save_selected = save_number
                print(save_selected)
                saves_menu = False
                name_save = True
                
        
        for i, save_name_text in enumerate(save_names_texts) :
            text_y = buttons[i][0]+offset[i]
            display.blit(save_name_text, (100, text_y))
            
        if x >= x_start and x <= x_end :
            for i, button in enumerate(buttons) :
                if y >= button[0] and y <= button[1] :
                    save_number = i
                    current_save_image = save_background_images[save_number]
        pygame.display.update()
        
        
    while name_save :
        display.fill(white)
        display.blit(current_typed_screen, (0, 0))
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get() :
            if event.type == pygame.MOUSEBUTTONDOWN :
                coords = pygame.mouse.get_pos()
                if over_submit :
                    if entering_save :
                        new_save_name = current_typed
                        current_typed = ""
                        current_typed_text = myfont2.render(current_typed, True, light_blue)
                        current_typed_x = get_x_value(current_typed_text.get_width())
                        current_typed_screen = default_typed_screen

                        space_bar_down = False

                        enter_extension_string = "your Manager"
                        string2 = "manager"

                        name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
                        name_save_header_x = get_x_value(name_save_header.get_width())

                        too_many_chars = False

                        enter_or_submit = True
                        over_submit = False

                        entering_save = False
                    else :
                        new_manager_name = current_typed
                        quit()
            if event.type == pygame.KEYDOWN :
                try :
                    key = event.key
                    if key == pygame.K_SPACE :
                        if len(current_typed) < 20 :
                            space_bar_down = True
                            current_typed += ' '
                        else :
                            too_many_chars = True
                    elif key == pygame.K_BACKSPACE :
                        current_typed = current_typed[:-1]
                        current_typed_screen = keyboard_order[key]
                        too_many_chars = False
                    else :
                        if len(current_typed) < 20 :
                            current_typed_screen = keyboard_order[key]
                            current_typed += keyboard_letters[key]
                        else :
                            too_many_chars = True
                    current_typed_text = myfont2.render(current_typed, True, light_blue)
                    current_typed_x = get_x_value(current_typed_text.get_width())
                except :
                    pass
                if current_typed != '' and enter_or_submit :
                    name_save_header = myfont2.render("Click here to submit "+string2+" name", True, light_blue)
                    name_save_header_x = get_x_value(name_save_header.get_width())
                    enter_or_submit = False
                if current_typed == '' and not enter_or_submit :
                    name_save_header = myfont2.render("Enter a Name for "+enter_extension_string, True, light_blue)
                    name_save_header_x = get_x_value(name_save_header.get_width())
                    enter_or_submit = True
                    over_submit = False
            if event.type == pygame.KEYUP :
                if key == pygame.K_SPACE :
                    space_bar_down = False
                current_typed_screen = default_typed_screen
        
        if x >= 42 and x <= 745 and y >= 51 and y <= 109 and (not enter_or_submit) and (not over_submit) :
            over_submit = True
            name_save_header = myfont2.render("Click here to submit "+string2+" name", True, gray)
        if over_submit and not (x >= 42 and x <= 745 and y >= 51 and y <= 109) :
            over_submit = False
            name_save_header = myfont2.render("Click here to submit "+string2+" name", True, light_blue)
        if space_bar_down :
            pygame.draw.rect(display, key_color, pygame.Rect(240, 505, 315, 50))
        else :
            pygame.draw.rect(display, white, pygame.Rect(240, 505, 315, 50))
        if over_submit :
            pygame.draw.rect(display, light_blue, pygame.Rect(42, 51, 703, 58))
        else :
            pygame.draw.rect(display, gray, pygame.Rect(42, 51, 703, 58))
        display.blit(name_save_header, (name_save_header_x, 60))
        display.blit(current_typed_text, (current_typed_x, 160))
        if too_many_chars :
            display.blit(too_many_chars_text, (too_many_chars_x, 575))
        pygame.display.update()

