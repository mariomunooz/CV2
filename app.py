from pathlib import Path

import streamlit as st
from PIL import Image



def add_job_section(job_data):
    col1, col2 = st.columns([1, 5], gap="small")
    with col1:
        st.image(job_data['image'], width=100)

    with col2:
        st.write(job_data['title'])
        st.write(job_data['duration'])

        description = job_data['description'].split('|')

        for paragraph in description:
            st.write(paragraph)


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic2.jpg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mario Muñoz Serrano"
PAGE_ICON = ":wave:"
NAME = "Mario Muñoz Serrano"
DESCRIPTION = """
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
EMAIL = "mariomunozserrano@gmail.com"
PHONE = '+34 664 633 542'
SOCIAL_MEDIA = {
    "YouTube": "",
    "LinkedIn": "",
    "GitHub": "",
    "Twitter": "",
}
PROJECTS = {
    "🏆 1st place Award public procurement Hackaton": "https://governobert.gencat.cat/ca/detalls/article/Open-Frau-i-ContraKtacio-idees-guanyadores-de-la-IdeatoDadesObertes-de-contractacio-publica",
    "🥈 2nd place U14 Spanish Championship ": "https://www.penya.com/es/inicio/noticias/1426-el-infantil-a-subcampeon-de-espana",
    "🏆 1st place U14 Catalan Championship ": "https://www.penya.com/es/inicio/noticias/1415-el-infantil-a-campeon-de-catalunya",

}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)
    # st.write("📱", PHONE)

# --- SOCIAL LINKS ---


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas, Numpy, Matplotlib, Scipy), SQL, R, C, C++, Java
- 💻💻 Parallel Programming: AWS, OpenMP API, OpenACC, CUDA
- 📊 Data Visualization: PowerBi, MS Excel, matplotlib, ggplot2, rayshader
- 📚 Web Scrapping: Scrappy, Selenium, Beautiful Soup, Requests
- 🗄️ Databases: MySQL
Among others...

"""
)

jobs_pics = [Image.open(current_dir / "assets" / "job_pics" / f"{image}.jpg") for image in range(0, 8)]

# --- EDUCATION ---
st.write('\n')
st.subheader("EDUCATION")
st.write("---")

pics_for_edu = [jobs_pics[6], jobs_pics[7]]
edu_titles = [
    '**Bachelor of enginerring (BEng) • Math engineering in data science (English) | Pompeu Fabra University**',
    '**Bachelor degree (BA) • Political and Administration Science | University of Barcelona**'
    ]
dates_edu = ['2019-Now', '2011-2015']

for edu in range(len(pics_for_edu)):
    job_data = {'image': pics_for_edu[edu],
                'emoji': None,
                'title': edu_titles[edu],
                'duration': dates_edu[edu],
                'description': ''}
    add_job_section(job_data)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# The pic i is the pic of job i
pics_for_job = [jobs_pics[0],
                jobs_pics[1], jobs_pics[1],
                jobs_pics[2], jobs_pics[2], jobs_pics[2], jobs_pics[2], jobs_pics[2],
                jobs_pics[3]
                ]

emojis = ["💻💳", "💻", "💻", "💻🏀", "💻🏀", "💻🏀", "💻🏀", "💻🏀", "💻🏀"]

titles = ["**Data Analyst | Comercia Global Payments**",
          "**Data Analyst | L'Hospitalet City Council**",
          "**ICT Technician | L'Hospitalet City Council**",
          "**U12 Assistant Coach & Scout Analyst | Club Joventut Badalona**",
          "**U12 Mini C Head coach & Scout Analyst | Club Joventut Badalona**",
          "**U14 Assistant Coach & Analyst | Club Joventut Badalona**",
          "**U13 Assistant Coach & Analyst | Club Joventut Badalona**",
          "**Youth Basketball Coach| Club Joventut Badalona**",
          "**Volunteers Office Coordinator (Basketball world cup 2014) | Spanish Basketball Federation**"
          ]

dates = ["07/2021 - 04/2022", "03/2019 - 05/2020", "02/2018 - 03/2019", "08/2018 - 07/2019", "08/2017 - 07/2018",
         "08/2016 - 07/2017", "08/2015 - 07/2016", "08/2012 - 07/2015", "07/2014 - 10/2014"
         ]

descriptions = [
    """
- ► Used Python, R and SQL to redefine and track KPIs.
- ► Creation of MS Excel KPI templates that can be used for non programmers .
- ► Improving the detection capacity of our fraud detection system using Data Mining and Machine Learning algorithms
- ► At the same time, we implement different evidence-based rules to reduce fraud operations
""",

    """
- ► Used Python, Power BI and MS Excel to analyze data about key actions in the different neighborhoods and they possible impacts.
- ► Used Power BI, Python and Cartodb to make visualizations and strategic reports on the city of L’Hospitalet de Llobregat.
""",

    """
- ► Creation of a specific website to make easier the access to relevant information by the social entities of L’Hospitalet
- ► Proposal of new functionalities inside of the Metadecidim community.
- ► Support for training on the Decidim digital platform for the technical staff of the city council.
- ► Support and advice on new technologies.
""",

    """I deliver effective support during training sessions that follow a seasonal training block specific to the 
    Youth Development Phase while also working as an scout analyst. This includes watching different games every week 
    to find youth prospects that could be interesting and add them to our database. As well as other tasks, like: 

- ► Recording some games for the ACB first team.
- ► Scorer and timer in some friendly games of the ACB first team.
- ► Refereeing youth friendly games.

""",
    """I deliver effective training sessions that follow a seasonal training block specific to the Youth Development 
    Phase while also working as an scout analyst. This includes watching different games every week to find youth 
    prospects that could be interesting and add them to our database. """,

    """Assisted the Head Coach by providing analysis of individual and team performance. This includes filming, 
    coding, collating, and analyzing match/training video using longomatch, python, excel and playsight. 

Champions of Catalonia, runners-up of Spain and participation in the ACB Minicopa
""",

    """Assisted the Head Coach by providing analysis of individual and team performance. This includes filming, 
    coding, collating, and analyzing match/training video using longomatch, python, excel and playsight. """,

    """
Tasks at Club Joventut Badalona School:
Basketball coaching, statistical analysis, video analysis and scouting, among others.
""",

    """My obligations here were. Collaborate in the volunteer selection processes. The planning of the different 
resources of the office and the coordination of a volunteers team of 150 people according to the needs of the 
different departments (marketing, press, competition, technologies, protocol ...). As well as support for the 
Slovenian national team for various practices, among others. 

First in Barcelona during round of 16, quarterfinals and semifinals and after in Madrid during the third and fourth 
place and the world cup final. """

]

for job in range(len(pics_for_job)):
    job_data = {'image': pics_for_job[job],
                'emoji': emojis[job],
                'title': titles[job],
                'duration': dates[job],
                'description': descriptions[job]}
    add_job_section(job_data)

# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")

# --- Volunteering ---
st.write('\n')
st.subheader("Volunteering")
st.write("---")

pics_for_vol = [jobs_pics[4], jobs_pics[3], jobs_pics[5]]

vol_titles = [
    "**Volunteer (Final of Endesa League 2012 and King's Cup 2012 and 2019)| ACB (Association of Basketball Clubs)**",
    '**Volunteer (Olympic Games 2012 Preparation Tournament)| Spanish Basketball Federation**',
    '**Volunteer (Dallas Mavericks and F.C. Barcelona) | National Basketball Association (NBA)**'
    ]

dates_vol = ['In Barcelona February and June  2012',
             '06/2012-06/2012',
             '10/2012-10/2012 ']

vol_descriptions = ["""In the 2019 Basketball King's Cup helping the organization of the U14 tournament in Madrid and trophy ceremony.

Previous experiences:
- ► In the 2012 Final of Endesa League. Helping to the organization of the trophy ceremony.
- ► In the 2012 Basketball King's Cup helping the organization of the U14 tournament in Barcelona.""",

                    """Volunteer in the Olympic Games 2012 Preparation Tournament in Barcelona between the National Teams of Spain, 
Argentina and USA. Helping the press department of the tournament. """,

                    """Volunteer in the friendly game between Dallas Mavericks and F.C. Barcelona. Helping the marketing department."""
                    ]

for vol in range(len(pics_for_vol)):
    job_data = {'image': pics_for_vol[vol],
                'emoji': None,
                'title': vol_titles[vol],
                'duration': dates_vol[vol],
                'description': vol_descriptions[vol]}
    add_job_section(job_data)

st.write('\n')
st.subheader("PROJECTS")
st.write("---")

st.write('\n')
st.subheader("Project 1: 2D and 3D Shotchart Visualisation")

'''shots = pd.read_csv('Projects\\Project  1\\shots_data.csv')
st.write('INPUT DATA')
st.dataframe(data=shots)'''

st.write(
    """With this df we can compute the Shooting percentage and the Effective field goal percentage using the following code""")

with st.expander('See Code (compute_stats.R)'):
    code = """#FUNCTIONS TO COMPUTE STATS

# Assign a zone to each shot
divide_shots_by_zone <- function(df){
  
  #Create variables is_C3, is_NC3 and is_2PT
  
  df <- df %>%
    mutate(is_C3 = if_else( (y <= 7.8 & (x > 22 | x < -22)),TRUE, FALSE )
    )
  
  df <- df %>%
    mutate(is_NC3 = if_else( (y > 7.8 & sqrt(x^2 + y^2) > 23.75)
                             ,TRUE, FALSE)
    )
  
  df <- df %>%
    mutate(is_2PT = if_else( !(is_C3 | is_NC3) ,TRUE, FALSE)
    )
  
  df
  
}

#Computes team number of shots attempted, made or missed per zone 
compute_num_team_shots <- function(inputdf, t_team, shot_t){
  
  
  inputdf <- filter(inputdf, team == t_team)
  
  if(shot_t == 'made') inputdf <- filter(inputdf, fgmadeLogic)
  if(shot_t == 'missed') inputdf <- filter(inputdf, !fgmadeLogic)
  
  #count num of shots per zone
  C3_shots  <- inputdf %>% count(is_C3)
  NC3_shots <- inputdf %>% count(is_NC3)
  PT2_shots <- inputdf %>% count(is_2PT)
  
  C3_shots  <- C3_shots$n[2]
  NC3_shots <- NC3_shots$n[2]
  PT2_shots <- PT2_shots$n[2]
  
  
  
  team_shots <- list(C3_shots ,NC3_shots, PT2_shots )
  team_shots
  
}
#Computes number of shots attempted, made or missed per zone by both teams
compute_num_shots <- function(inputdf, shot_t){
  
  if(shot_t == 'made') inputdf <- filter(inputdf, fgmadeLogic)
  if(shot_t == 'missed') inputdf <- filter(inputdf, !fgmadeLogic)
  
  number_shots <- inputdf %>% count(team)
  
  
  shotsA <- compute_num_team_shots(inputdf, 'Team A',shot_t)
  shotsB <- compute_num_team_shots(inputdf, 'Team B',shot_t)
  
  
  number_shots$C3 <- c(shotsA[1], shotsB[1])
  number_shots$NC3 <- c(shotsA[2], shotsB[2])
  number_shots$PT2 <- c(shotsA[3], shotsB[3])
  number_shots <- number_shots[, c(1,3,4,5,2)]
  
  number_shots
  
}



#Computes shoting percentage and efg per zone returns a list of three df
compute_stats <- function(inputdf, stats){
  
  # Number of shots attempted per zone
  number_shots <- compute_num_shots(inputdf, 'attempted')
  
  # Number of shots made per zone
  number_shots_made <- compute_num_shots(inputdf, 'made')
  
  
  zones = c('C3', 'NC3', 'PT2')
  
  fgm = -10000
  threesM = -10000
  fga = -10000
  for(zone in zones){
    
    # Compute shot percentage of each zone
    shot_percentage = as.numeric(unlist(number_shots[zone])) / as.numeric(unlist(number_shots['n']))
    stats[paste('shot%_', zone, sep='')] = shot_percentage * 100
    
    # Compute effective field goal percentage
    # efg% = (FGM + 0.5*3PM)/ FGA
    
    if(zone =='C3'|zone =='NC3'){
      fgm = as.numeric(unlist(number_shots_made[zone]))
      threesM = as.numeric(unlist(number_shots_made[zone]))
      fga = as.numeric(unlist(number_shots[zone]))
      
    }
    else{
      fgm = as.numeric(unlist(number_shots_made[zone]))
      threesM = 0
      fga = as.numeric(unlist(number_shots[zone]))
      
    }
    
    efg_percentage = ((fgm + 0.5*threesM)/fga)*100
    stats[paste('eFG%_', zone, sep='')] = efg_percentage
  }
  
  fgm = as.numeric(unlist(number_shots_made['n']))
  threesM = as.numeric(unlist(number_shots_made['C3'])) + as.numeric(unlist(number_shots_made['NC3']))
  fga = as.numeric(unlist(number_shots['n']))
  
  stats[paste('eFG%_', 'total', sep='')] = ((fgm + 0.5*threesM)/fga)*100
  
  
  
  return(list(attempted = number_shots, made = number_shots_made, stats = stats))
  
}

# creates shooting stats
create_shot_stats <- function(inputdf){
  
  #Initialize output df
  columns = c("team", "shot%_C3" ,"shot%_NC3","shot%_PT2",
              "eFG%_C3","eFG%_NC3","eFG%_PT2")
  
  stats = data.frame(matrix(nrow = 2, ncol = 0))
  stats[columns] <- NA
  stats$team <- c('Team A', 'Team B')
  
  #Compute Stats
  tablesdf <- compute_stats(inputdf, stats)
  
  tablesdf
  
}

# Assign to each shot their zone stats
shots_add_stats <- function(df, stats){
  
  df <- df %>%
    mutate( efg = case_when(
      is_C3   & team == 'Team A'  ~ stats[1,'eFG%_C3' ] ,
      is_NC3  & team == 'Team A'  ~ stats[1,'eFG%_NC3'],
      is_2PT  & team == 'Team A'  ~ stats[1,'eFG%_PT2'],
      is_C3   & team == 'Team B'  ~ stats[2,'eFG%_C3' ],
      is_NC3  & team == 'Team B'  ~ stats[2,'eFG%_NC3'],
      is_2PT  & team == 'Team B'  ~ stats[2,'eFG%_PT2']
      
    )
    
    )
  
  df <- df %>%
    mutate( usage = case_when(
      is_C3   & team == 'Team A'  ~ stats[1,'shot%_C3' ] ,
      is_NC3  & team == 'Team A'  ~ stats[1,'shot%_NC3'],
      is_2PT  & team == 'Team A'  ~ stats[1,'shot%_PT2'],
      is_C3   & team == 'Team B'  ~ stats[2,'shot%_C3' ],
      is_NC3  & team == 'Team B'  ~ stats[2,'shot%_NC3'],
      is_2PT  & team == 'Team B'  ~ stats[2,'shot%_PT2']
      
    )
    
    )
  
  df
  
}"""
    st.code(code, language='R')

st.write("""Then we can display the stats computed on the court with the following code """)

with st.expander('See Code (create_court.R)'):
    code2 = """
#FUNCTIONS TO PLOT THE COURT

# Construct_court creates the list of dataframes 
# with the coordinates of each element in the court

construct_court <- function() {
  
  
  ###outside box:
  outside_box <- data.frame(
    x=c(-25,-25,25,25,-25),
    y=c(0,47,47,0,0),
    type = 'outside box'
    
  )
  
  ###solid FT semicircle above FT line:
  solid_FT <- data.frame(
    x=c(-6000:(-1)/1000,1:6000/1000),
    y=c(19+sqrt(6^2-c(-6000:(-1)/1000,1:6000/1000)^2)),
    type = 'solid ft'
  )
  
  ###dashed FT semicircle below FT line:
  dashed_FT <- data.frame(
    x=c(-6000:(-1)/1000,1:6000/1000),
    y=c(19-sqrt(6^2-c(-6000:(-1)/1000,1:6000/1000)^2)),
    type = 'dashed ft'
  )
  
  ###key:
  key <- data.frame(
    x=c(-8,-8,8,8,-8),
    y=c(0,19,19,0,0),
    type = 'key'
  )
  
  ###box inside the key:
  box_inKey <- data.frame(
    x=c(-6,-6,6,6,-6),
    y=c(0,19,19,0,0),
    type = 'box in key'
  )
  ###restricted area semicircle:
  restrictedArea <- data.frame(
    x=c(-4000:(-1)/1000,1:4000/1000),
    y=c(5.25+sqrt(4^2-c(-4000:(-1)/1000,1:4000/1000)^2)),
    type = 'restricted area'
  )
  
  ###halfcourt semicircle:
  halfcourt_semic <- data.frame(
    x=c(-6000:(-1)/1000,1:6000/1000),
    y=c(47-sqrt(6^2-c(-6000:(-1)/1000,1:6000/1000)^2)),
    type = 'halfcourt semic'
  )
  
  ###rim:
  rim <- data.frame(
    x=c(-750:(-1)/1000,1:750/1000,750:1/1000,-1:-750/1000),
    y=c(c(5.25+sqrt(0.75^2-c(-750:(-1)/1000,1:750/1000)^2)),c(5.25-sqrt(0.75^2-c(750:1/1000,-1:-750/1000)^2))),
    type = 'rim'
  )
  
  ###backboard:
  backboard <- data.frame(
    x=c(-3,3),
    y=c(4,4),
    type = 'backboard'
  )
  
  ###three-point line:
  threeP <- data.frame(
    x=c(-22,-22,-22000:(-1)/1000,1:22000/1000,22,22),
    y=c(0,169/12,5.25+sqrt(23.75^2-c(-22000:(-1)/1000,1:22000/1000)^2),169/12,0),
    type = 'threeP'
  )
  
  
  
  court <- list(outside_box     = outside_box,
                key             = key,
                box_inKey       = box_inKey,
                
                solid_FT        = solid_FT,
                restrictedArea  = restrictedArea,
                halfcourt_semic = halfcourt_semic,
                rim             = rim,
                threeP          = threeP,
                
                dashed_FT       = dashed_FT,
                backboard       = backboard
                
                )
  
  
  
  
  court
  
}

# -----------------------------------------------------------------------------

# Plot_court

plot_court <- function(title){
  
  court    <- construct_court()
  
  plot <- ggplot(data=data.frame(x=1,y=1),aes(x,y))+ ggtitle(title)+ theme(plot.title = element_text(size = 14, hjust = 0.5, face= 'bold'))+
    
    #Draw court
    ## Half-court adapted from (Edward Kupfer) https://gist.github.com/edkupfer/6354404
    
    #boxes
    
    geom_path(data= court$outside_box                   , colour = 'black')+
    geom_path(data= court$key                           , colour = 'black')+
    geom_path(data= court$box_inKey                     , colour = 'black')+
    
    #circles
    geom_path(data = court$solid_FT        ,aes(x=x,y=y), colour = 'black')+
    geom_path(data = court$restrictedArea  ,aes(x=x,y=y), colour = 'black')+
    geom_path(data = court$halfcourt_semic ,aes(x=x,y=y), colour = 'black')+
    geom_path(data = court$rim             ,aes(x=x,y=y), colour = 'black')+
    geom_path(data = court$threeP          ,aes(x=x,y=y), colour = 'black')+
    
    #special lines
    geom_path(data= court$dashed_FT ,aes(x=x,y=y),linetype='dashed', colour = 'black')+
    geom_path(data= court$backboard ,lineend='butt', colour = 'black')+
    
    ###fix aspect ratio to 1:1
    coord_fixed()
  
  plot
  
}"""
    st.code(code2, language='R')

st.write("""And finally get the different visualisations with the following code""")

with st.expander('See Code (main.R)'):
    code3 = """#If one of the following packages is not installed uncomment the corresponding line

#install.packages("ggplot2")
#install.packages("tidyverse")
#install.packages("devtools")
#remotes::install_github("tylermorganwall/rayshader")


# Call libraries

library(ggplot2)
library(tidyverse)
library(rayshader)
source("create_court.R")
source("compute_stats.R")

## IMPORT DATA
shotsData <- read.csv("shots_data.csv")
shotsDataframe <- data.frame(shotsData)

#Change of coordinates: 
#         - In our plot the y axis is centered at the baseline not at the center of the rim)
#         - So to represent the shots we need to adjust the y axis adding 5.25 feets
#         - Because the center of the rim is 13.75 feets from the free throw line, 
#           that is 5.25 feets from the baseline

shotsDataframe['plot_y'] = shotsDataframe['y'] + 5.25
shotsDataframe$fgmadeLogic <- as.logical(shotsDataframe$fgmade)


# COMPUTE ZONE STATS

#Define shot zones
shotsDataframe <- divide_shots_by_zone(shotsDataframe)

#Compute shot stats
shooting_tables <- create_shot_stats(shotsDataframe)
shotsAttemted   <- shooting_tables$attempted
shotsMade       <- shooting_tables$made
stats           <- shooting_tables$stats


# VISUALIZE ZONE STATS
shots_and_stats <- shots_add_stats(shotsDataframe, stats)


# 2D Visualization
teams_shotchart <- plot_court('HOW THE TEAMS SHOT (By Zone)\n') + 
  geom_point(data = shots_and_stats, aes(x = x, y = plot_y, size = usage, color = efg, fill = efg), alpha = 0.8)+

  
  scale_color_gradient(low = "#033270", high = "#65010C", name = 'eFG%')+
  scale_fill_gradient(low = "#033270", high = "#65010C", name = 'eFG%')+
  labs(fill = 'eFG%', size = 'shot%')+
  #guides(size = "none")+
  facet_wrap(~ team)

teams_shotchart



# 3D Visualization
teams_shotchart <- teams_shotchart + guides(size = "none")
  
plot_gg(teams_shotchart, multicore = TRUE, width = 6, height = 5.5, height_aes = "color", scale = 300, 
        background = "#afceff",shadowcolor = "#3a4f70")


colnames(shotsAttemted) <- c('team','C3','NC3', 'PT2', 'total')
colnames(shotsMade) <- c('team','C3','NC3', 'PT2', 'total')

stats <- subset(stats, select = -c(team) )

stats <- stats /100


stats$team = c('Team A', 'Team B')
print(shotsAttemted)
print(shotsMade)
print(stats)"""

    st.code(code3, language='R')

st.write("""OUTPUT""")
st.write('Stats Computed')
st.image(Image.open(current_dir / "Projects" / "Project  1" / "output" / "print.jpg"))

st.write('2D Shotchart')
st.image(Image.open(current_dir / "Projects" / "Project  1" / "output" / "df.jpeg"))

'''st.write('3D Shotchart')
video = open(current_dir / "Projects" / "Project  1" / "output" / "3d plot demo.mp4",'rb')
st.video(video, format="video/mp4", start_time=0)'''


st.write('\n')
st.subheader("Project 2: Application of classification in Marketing and Sales")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/MACHINE_LEARNING/blob/main/Application_of_classification_in_Marketing_and_Sales_.ipynb'})")


st.write('\n')
st.subheader("Project 3: ACB Web Scrapping of players information")
st.write("The code that you can see below iterates over each team roster in ACB")
st.image(Image.open(current_dir / "Projects" / "Project 2" / "1.jpg"))
st.write("Gets the information of each player")
st.image(Image.open(current_dir / "Projects" / "Project 2" / "2.jpg"))
st.write("And stores them in  MYSQL Table")
st.image(Image.open(current_dir / "Projects" / "Project 2" / "3.jpg"))
st.write('To use this code, you only need to write here the password of yor MYSQL Server')
st.image(Image.open(current_dir / "Projects" / "Project 2" / "4.jpg"))
st.write(f"[Link to github repo](https://github.com/mariomunooz/ACB-scrapper)")
