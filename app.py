from pathlib import Path

import streamlit as st
from PIL import Image
import pandas as pd


def add_job_section(job_data):
    col1, col2 = st.columns([1, 5], gap="small")
    with col1:
        st.image(job_data['image'], width=100)

    with col2:
        st.write(job_data['title'])

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
Data Scientist, assisting enterprises by supporting data-driven decision-making.
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


for edu in range(len(pics_for_edu)):
    job_data = {'image': pics_for_edu[edu],
                'emoji': None,
                'title': edu_titles[edu],

                'description': ''}
    add_job_section(job_data)


# --- Projects & Accomplishments ---
# st.write('\n')
# st.subheader("Projects & Accomplishments")
# st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")



st.write('\n')
st.subheader("PROJECT PORTFOLIO")
st.write("---")

st.write('\n')
st.subheader("Project 1: 2D and 3D Shotchart Visualisation")

shots = pd.read_csv('https://raw.githubusercontent.com/mariomunooz/data/main/shots_data.csv')
st.write('INPUT DATA')
st.dataframe(data=shots)

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

st.write('3D Shotchart')
video = open(current_dir / "Projects" / "Project  1" / "output" / "3d plot demo.mp4",'rb')
st.video(video, format="video/mp4", start_time=0)


st.write('\n')
st.subheader("Project 2: Application of classification in Marketing and Sales")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/MACHINE_LEARNING/blob/main/Application_of_classification_in_Marketing_and_Sales_.ipynb'})")
st.write("""In this project, we will develop and apply different supervised classification tecnhiques. These methodologies are broadly used in business to multiple use cases as:

-   -Identify new customers in the market
-   -Identify customers in our internal Data Warehouse with more likely to buy a new product
-   -Identify unsatisfied customers and thus, likely to be churners
-   -Classify text into categories for spam identification or to process messages or emails from our customers

During this project we will follow the end-to-end Machine Learning process: from data gathering and cleaning, exploratory data analysis, feature engineering and finally, training and prediction. In particular, the main sections of this project are:

-    -Data understanding and preparation: exploration of the dataset and feature engineering (missing values, outlier identification, categorical variables management)
-    -Model Training: training the baseline SVM and Decision Trees. Analysis of metrics (recall, precision, confusion metrics) and improvement the classification through several techniques as undersampling to balance or ensemble of models
-    -Creating a Business opportunity with Machine Learning: selection of the best model and identification of the most important features

We will apply all these techniques to identify new customers to capture and improve sales in a marketing use case.""")


st.write('\n')
st.subheader("Project 3: Data Mining | Data Preparation")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_data_preparation.ipynb'})")
st.write("""Data scientists spend a big chunk of their time preparing data and this is one of the first steps in any data mining project. This step is normally called data preparation.

The processes of getting an initial understanding of a dataset and preparing it usually go hand-in-hand, and it is critical to perform them well to obtain valid results later. Plus, you can save time and effort by learning how to do proper data preparation.

In this session, we will assume you just received a new dataset and need to do some initial steps with it:

1. Exploratory Data Analysis

    - Calculate basis statistics as mean, median, variance, maximum and minimum
    - Look at distributions, identify outliers
    - Calculate correlations between variables

2. Feature engineering:

    - Deal with missing values
    - Standardize all numerical columns
    - Convert categorical columns to dummy binary variables
    - Date and period management
    - Feature generation
""")


st.write('\n')
st.subheader("Project 4: Data Mining | Find near-duplicates using shingling")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_Find_near_duplicates_using_shingling.ipynb'})")
st.write("""In this session we will take a large corpus of tweets and detect near-duplicates on this corpus using a technique known as shingling.

Two documents are considered near-duplicates if they share a large amount of ngrams. The ngrams of a phrase are overlapping sequences of words of length n. For instance, the phrase 'Never let them guess your next move.' has the following 3-grams:

    'never let them'
    'let them guess'
    'them guess your'
    'guess your next'
    'your next move'

To measure the similarity between two sets, we will use the Jaccard index, which is the size of the intersection of the two sets divided by their union. This values goes between 0.0 (meaning the documents have no ngrams in common) to 1.0 (meaning the documents have the same ngrams).

To speed up things, instead of comparing the set of shingles of two documents which can be large, we will derive a fixed-length signature or sketch for each document. This will be obtained by (1) applying a random permutation to the list of possible ngrams, and (2) pick the ngram that appears first in the permuted list. The Jaccard index between these signatures will be a good approximation of the Jaccard index between the original sets of ngrams.
""")

st.write('\n')
st.subheader("Project 5: Data Mining | Association Rules")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_association_rules.ipynb'})")
st.write("""Association rule mining techniques are useful to analyze datasets consisting of transactions, in which each transaction is a collection of items.

We will use a well-known dataset named Instacart containing more than 3 million orders of products through a grocery shopping app""")


st.write('\n')
st.subheader("Project 6: Data Mining | Recommendations engines (interactions-based)")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_Item_based_recsys.ipynb'})")
st.write("""For this assignment we will build and apply an item-based and model-based collaborative filtering recommenders for movies.""")

st.write('\n')
st.subheader("Project 7: Data Mining | Outlier Analysis")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/Data-Mining/blob/main/Data_mining_outlier_analysis.ipynb'})")
st.write("""The objective of this session is to practice finding outliers by implementing the Isolation Forest algorithm.""")

st.write('\n')
st.subheader("Project 8: Data Mining | Forecasting")
st.write(f"[Python Notebook link]({'https://github.com/mariomunooz/Data-Mining/blob/main/Data_Mining_forecasting.ipynb'})")
st.write("""In this session we will do some time series forecasting on a weather-related time series, which contains temperature, precipitation, and wind speed data for the Barcelona airport.""")







st.write('\n')
st.subheader("Project 9: ACB Web Scrapping of players information")
st.write("The code that you can see below iterates over each team roster in ACB")
st.image(Image.open(current_dir / "Projects" / "Project 2" / "1.jpg"))
st.write("Gets the information of each player")
st.image(Image.open(current_dir / "Projects" / "Project 2" / "2.jpg"))
st.write("And stores them in  MYSQL Table")
st.image(Image.open(current_dir / "Projects" / "Project 2" / "3.jpg"))
st.write('To use this code, you only need to write here the password of yor MYSQL Server')
st.image(Image.open(current_dir / "Projects" / "Project 2" / "4.jpg"))
st.write(f"[Link to github repo](https://github.com/mariomunooz/ACB-scrapper)")



