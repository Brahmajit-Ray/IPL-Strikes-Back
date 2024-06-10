import streamlit as st
import pickle
import pandas as pd

venues=['Ahmedabad', 'Abu Dhabi', 'Delhi', 'Indore', 'Chennai', 'Dubai',
       'Kolkata', 'Mumbai', 'Durban', 'Mohali', 'Jaipur', 'Centurion',
       'Bangalore', 'Port Elizabeth', 'Cape Town', 'Lucknow', 'Hyderabad',
       'Raipur', 'Johannesburg', 'Sharjah', 'Mullanpur', 'Nagpur', 'Pune',
       'Cuttack', 'Dharamsala', 'Bengaluru', 'Guwahati', 'Visakhapatnam',
       'Bloemfontein', 'Ranchi', 'East London', 'Kimberley']

teams=['Mumbai Indians',
 'Kolkata Knight Riders',
 'Royal Challengers Bengaluru',
 'Chennai Super Kings',
 'Punjab Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Rajasthan Royals',
 'Gujarat Titans',
 'Lucknow Super Giants']

batsman=['AC Gilchrist', 'Azhar Mahmood', 'M Vohra', 'Mandeep Singh',
       'DA Miller', 'RG Sharma', 'N Wadhera', 'C Green', 'SA Yadav',
       'Tilak Varma', 'Vishnu Vinod', 'TH David', 'CJ Jordan',
       'PP Chawla', 'K Kartikeya', 'JP Behrendorff', 'Q de Kock',
       'Ishan Kishan', 'SS Tiwary', 'KH Pandya', 'HH Pandya',
       'KA Pollard', 'G Gambhir', 'C de Grandhomme', 'RV Uthappa',
       'MK Pandey', 'YK Pathan', 'CR Woakes', 'SP Narine', 'PA Patel',
       'JC Buttler', 'N Rana', 'Washington Sundar', 'V Kohli',
       'RM Patidar', 'GJ Maxwell', 'AB de Villiers', 'Shahbaz Ahmed',
       'DT Christian', 'KA Jamieson', 'HV Patel', 'Mohammed Siraj',
       'DR Smith', 'BB McCullum', 'SK Raina', 'F du Plessis', 'MS Dhoni',
       'MS Bisla', 'DPMD Jayawardene', 'KC Sangakkara', 'Yuvraj Singh',
       'Shahid Afridi', 'HH Gibbs', 'SB Styris', 'Y Venugopal Rao',
       'DB Ravi Teja', 'RP Singh', 'PP Ojha', 'PM Sarvesh Kumar',
       'DP Vijaykumar', 'DM Bravo', 'SV Samson', 'KK Nair', 'JP Duminy',
       'RR Pant', 'CH Morris', 'P Negi', 'NJ Maddinson', 'S Dhawan',
       'SR Tendulkar', 'R Sathish', 'DJ Bravo', 'R McLaren', 'MK Tiwary',
       'SS Iyer', 'KM Jadhav', 'AD Mathews', 'JA Morkel', 'UBT Chand',
       'DA Warner', 'LRPL Taylor', 'NV Ojha', 'AD Russell', 'IK Pathan',
       'UT Yadav', 'BJ Hodge', 'SC Ganguly', 'WP Saha', 'OA Shah',
       'LR Shukla', 'RS Gavaskar', 'SE Bond', 'M Kartik', 'I Sharma',
       'SP Goswami', 'KS Williamson', 'PK Garg', 'JO Holder',
       'YV Takawale', 'AM Rahane', 'ST Jayasuriya', 'AM Nayar',
       'Harbhajan Singh', 'DS Kulkarni', 'C Nanda', 'SL Malinga',
       'V Sehwag', 'GJ Bailey', 'BR Dunk', 'CJ Anderson', 'AT Rayudu',
       'AP Tare', 'CM Gautam', 'Z Khan', 'LS Livingstone', 'SPD Smith',
       'AJ Turner', 'S Badrinath', 'RA Jadeja', 'KMDN Kulasekara',
       'R Ashwin', 'YBK Jaiswal', 'D Padikkal', 'SO Hetmyer', 'R Parag',
       'KL Rahul', 'CH Gayle', 'MA Agarwal', 'AJ Finch', 'AR Patel',
       'AJ Tye', 'BB Sran', 'MM Sharma', 'AA Bilakhia', 'TL Suman',
       'A Symonds', 'CA Lynn', 'SR Watson', 'BA Stokes', 'RD Gaikwad',
       'DP Conway', 'S Dube', 'P Kumar', 'JH Kallis', 'KP Pietersen',
       'R Dravid', 'R Bishnoi', 'R Vinay Kumar', 'DW Steyn', 'A Kumble',
       'Shakib Al Hasan', 'JD Ryder', 'GC Smith', 'AA Jhunjhunwala',
       'M Manhas', 'SB Wagh', 'R Sharma', 'RA Tripathi', 'RR Rossouw',
       'MA Starc', 'VR Aaron', 'AB Dinda', 'KS Bharat', 'JM Bairstow',
       'V Shankar', 'Mohammad Nabi', 'Abdul Samad', 'Rashid Khan',
       'Sandeep Sharma', 'B Kumar', 'D Brevis', 'Naman Dhir',
       'R Shepherd', 'JR Philippe', 'Navdeep Saini', 'YS Chahal',
       'TM Dilshan', 'A Mishra', 'MF Maharoof', 'VY Mahesh', 'PJ Sangwan',
       'Shubman Gill', 'B Sai Sudharsan', 'R Tewatia', 'M Vijay',
       'SE Marsh', 'R Dhawan', 'MG Johnson', 'Anureet Singh', 'SM Curran',
       'DJ Hussey', 'ML Hayden', 'A Flintoff', 'JDP Oram',
       'Joginder Sharma', 'T Thushara', 'Gurkeerat Singh', 'PR Shah',
       'RR Raje', 'JEC Franklin', 'IR Jaggi', 'B Chipli', 'KD Karthik',
       'JP Faulkner', 'MJ Lumb', 'FY Fazal', 'AC Voges', 'AS Raut',
       'AP Dole', 'LMP Simmons', 'MEK Hussey', 'Dhruv Jurel',
       'Rahmanullah Gurbaz', 'N Jagadeesan', 'VR Iyer', 'RK Singh',
       'SN Thakur', 'Karanveer Singh', 'PP Shaw', 'MP Stoinis',
       'Lalit Yadav', 'PC Valthaty', 'Bipul Sharma', 'RJ Harris',
       'BR Sharath', 'DG Nalkande', 'SH Johnson', 'Noor Ahmad',
       'LJ Wright', 'EJG Morgan', 'STR Binny', 'DR Sams', 'K Rabada',
       'LA Carseldine', 'LPC Silva', 'H Das', 'DNT Zoysa', 'KV Sharma',
       'AB Barath', 'RS Sodhi', 'RN ten Doeschate', 'MM Ali', 'DB Das',
       'R Bhatia', 'SMSM Senanayake', 'Azmatullah Omarzai',
       'M Shahrukh Khan', 'KK Ahmed', 'Shivam Mavi', 'Kuldeep Yadav',
       'J Suchith', 'R Ravindra', 'DJ Mitchell', 'R Sai Kishore',
       'A Ashish Reddy', 'DJG Sammy', 'GH Vihari', 'SB Dubey',
       'KK Cooper', 'VS Malik', 'DJM Short', 'M Kaif', 'Younis Khan',
       'Kamran Akmal', 'M Rawat', 'D Salunkhe', 'Pankaj Singh',
       'GHS Garton', 'MD Mishra', 'SP Jackson', 'AC Blizzard', 'MM Patel',
       'DL Chahar', 'MA Wood', 'Imran Tahir', 'SN Khan', 'D Wiese',
       'Abhishek Sharma', 'N Pooran', 'AK Markram', 'Umran Malik',
       'SE Rutherford', 'CA Ingram', 'AF Milne', 'S Badree', 'S Aravind',
       'E Lewis', 'GD Phillips', 'Anuj Rawat', 'DJ Willey',
       'PWH de Silva', 'RD Chahar', 'JJ Bumrah', 'TA Boult', 'S Sohal',
       'CL White', 'MJ McClenaghan', 'Atharva Taide', 'MW Short',
       'P Simran Singh', 'Harpreet Singh', 'JM Sharma', 'Harpreet Brar',
       'NT Ellis', 'MN Samuels', 'MR Marsh', 'RK Bhui', 'T Stubbs',
       'Abishek Porel', 'MJ Clarke', 'MK Lomror', 'K Gowtham',
       'JC Archer', 'JJ Roy', 'CV Varun', 'SM Katich', 'S Anirudha',
       'A Nehra', 'SW Billings', 'MC Henriques', 'DJ Hooda',
       'BCJ Cutting', 'JDS Neesham', 'R Shukla', 'Mohammed Shami',
       'Rasikh Salam', 'PBB Rajapaksa', 'Arshdeep Singh', 'S Kaul',
       'AB Agarkar', 'CK Langeveldt', 'AUK Pathan', 'CA Pujara',
       'JJ van der Wath', 'DL Vettori', 'Anmolpreet Singh', 'H Klaasen',
       'Sanvir Singh', 'M Jansen', 'M Markande', 'Fazalhaq Farooqi',
       'M Morkel', 'RS Bopara', 'Parvez Rasool', 'Shashank Singh',
       'SA Asnodkar', 'SK Warne', 'Sohail Tanvir', 'C Munro',
       'KW Richardson', 'AA Kulkarni', 'A Badoni', 'VG Arora', 'TM Head',
       'Nithish Kumar Reddy', 'S Chanderpaul', 'MV Boucher', 'B Akhil',
       'S Gopal', 'Kartik Tyagi', 'S Nadeem', 'R Sanjay Yadav',
       'Ramandeep Singh', 'J Botha', 'AL Menaria', 'I Udana',
       'KB Arun Karthik', 'A Mithun', 'PJ Cummins', 'RR Sarwan',
       'WG Jacks', 'Saurav Chauhan', 'Vijaykumar Vyshak', 'B Indrajith',
       'Sachin Baby', 'PV Tambe', 'SK Trivedi', 'K Goel', 'JR Hopes',
       'HM Amla', 'MD Shanaka', 'A Manohar', 'VRV Singh', 'U Kaul',
       'TG Southee', 'N Saini', 'SD Chitnis', 'B Lee', 'Iqbal Abdulla',
       'L Balaji', 'J Fraser-McGurk', 'SD Hope', 'TM Srivastava',
       'MC Juneja', 'T Kohler-Cadmore', 'R Powell', 'J Theron',
       'RJ Peterson', 'TD Paine', 'M Muralitharan', 'A Nortje',
       'Mukesh Kumar', 'AG Paunikar', 'RE van der Merwe', 'NS Naik',
       'VVS Laxman', 'Jaskaran Singh', 'LA Pomersbach', 'WA Mota',
       'RR Powar', 'MS Wade', 'AC Thomas', 'W Jaffer', 'RT Ponting',
       'T Shamsi', 'Abdul Basith', 'SD Lad', 'AS Joseph', 'KR Mayers',
       'JD Unadkat', 'Ravi Bishnoi', 'Avesh Khan', 'Y Nagar', 'M Ashwin',
       'RP Meredith', 'Sumit Kumar', 'FA Allen', 'TS Mills', 'AD Hales',
       'G Coetzee', 'SZ Mulani', 'MJ Santner', 'D Pretorius',
       'KC Cariappa', 'Mohammad Hafeez', 'KP Appanna', 'RJ Quiney',
       'PD Salt', 'RE Levi', 'SS Prabhudessai', 'WD Parnell',
       'Mohammad Asif', 'GD McGrath', 'M Klinger', 'DR Shorey', 'A Zampa',
       'DH Yagnik', 'CR Brathwaite', 'NLTC Perera', 'B Stanlake',
       'A Choudhary', 'DJ Harris', 'PA Reddy', 'J Arunkumar',
       'Misbah-ul-Haq', 'DT Patil', 'Abdur Razzak', 'D Ferreira',
       'SM Harwood', 'MS Gony', 'LE Plunkett', 'Harmeet Singh', 'P Awana',
       'AB McDonald', 'KS Sharma', 'Mohsin Khan', 'S Sriram', 'T Banton',
       'KL Nagarkoti', 'M Prasidh Krishna', 'LH Ferguson', 'PN Mankad',
       'WPUJC Vaas', 'Shoaib Ahmed', 'Tanush Kotian', 'KA Maharaj',
       'A Tomar', 'TR Birt', 'AD Mascarenhas', 'B Sumanth',
       'MG Bracewell', 'CRD Fernando', 'GC Viljoen', 'TL Seifert',
       'L Wood', 'B Laughlin', 'SP Fleming', 'S Vidyut', 'M Ntini',
       'TK Curran', 'AS Rajpoot', 'Mujeeb Ur Rahman', 'BJ Rohrer',
       'Mustafizur Rahman', 'UT Khawaja', 'Arjun Tendulkar',
       'Ashutosh Sharma', 'Sikandar Raza', 'AP Majumdar', 'CJ Ferguson',
       'AG Murtaza', 'P Chopra', 'P Dogra', 'A Uniyal', 'Yudhvir Singh',
       'P Parameswaran', 'JR Hazlewood', 'Ankit Sharma', 'Kumar Kushagra',
       'JA Richardson', 'J Syed Mohammad', 'R Rampaul', 'S Randiv',
       'DE Bollinger', 'BMAJ Mendis', 'AS Roy', 'Harshit Rana',
       'Anirudh Singh', 'AD Nath', 'Basil Thampi', 'Mukesh Choudhary',
       'SS Cottrell', 'SB Bangar', 'AS Yadav', 'AN Ahmed', 'F Behardien',
       'T Natarajan', 'RV Gomez', 'S Sreesanth', 'PVD Chameera',
       'IC Pandey', 'JE Root', 'KM Asif', 'L Ronchi', 'SM Pollock',
       'MA Khote', 'S Ladda', 'DP Nannes', 'BB Samantray',
       'Aman Hakim Khan', 'JM Kemp', 'RA Bawa', 'OF Smith', 'YV Dhull',
       'HC Brook', 'DJ Jacobs', 'MJ Guptill', 'Swapnil Singh',
       'Sunny Gupta', 'C Sakariya', 'Arshad Khan', 'Naveen-ul-Haq',
       'PD Collingwood', 'CK Kapugedera', 'SJ Srivastava', 'S Lamichhane',
       'NL McCullum', 'JE Taylor', 'Y Gnaneswara Rao', 'AA Noffke',
       'SB Joshi', 'AU Rashid', 'VS Yeligati', 'DS Lehmann', 'AA Chavan',
       'GB Hogg', 'Akash Deep', 'RV Patel', 'AT Carey', 'HR Shokeen',
       'UA Birla', 'K Upadhyay', 'NM Coulter-Nile', 'KMA Paul',
       'A Raghuvanshi', 'DJ Thornely', 'SA Abbott', 'BA Bhatt',
       'BAW Mendis', 'A Mukund', 'Sunny Singh', 'Yashpal Singh',
       'SS Shaikh', 'R Ninan', 'Mayank Dagar', 'RJW Topley', 'S Narwal',
       'SW Tait', 'Sameer Rizvi', 'HE van der Dussen', 'KR Sen',
       'Salman Butt', 'Umar Gul', 'TU Deshpande', 'MN van Wyk',
       'DAJ Bracewell', 'A Kamboj', 'Shoaib Malik', 'S Kaushik',
       'T Henderson', 'Kamran Khan', 'KAJ Roach', 'Virat Singh',
       'A Chopra', 'Simarjeet Singh', 'M Theekshana', 'L Ablish',
       'P Dubey', 'S Tyagi', 'AN Ghosh', 'P Ray Barman', 'BE Hendricks',
       'TP Sudhindra', 'C Ganapathy', 'DJ Muthuswami']

pipe = pickle.load(open('IPL_Model.pkl','rb'))
st.title('IPL Win Predictor 2024')

df=pd.read_csv("Strike_Rates1.csv")


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))

teams2=[option for option in teams if option!=batting_team]

with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams2))

selected_city = st.selectbox('Select host city',sorted(venues))

target = st.number_input('Target',min_value=0,step=1)

col6,col7=st.columns(2)

with col6:
       batter=st.selectbox("Select batsman1",sorted(batsman))

batsman2=[option for option in batsman if option!=batter]

with col7:
       non_striker=st.selectbox("Select batsman2",sorted(batsman2))

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score',min_value=0,step=1)
with col4:
    overs = st.number_input('Overs completed',min_value=0,step=1)
with col5:
    wickets = st.number_input('Wickets out',min_value=0,step=1)

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    strike_rate_x=df.loc[df["Batsman"]==batter]["Strike_Rate"].item()
    strike_rate_y=df.loc[df["Batsman"]==batter]["Strike_Rate"].item()

    input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team],
                             "target":[target],"balls_left":[balls_left],"wickets_left":[wickets],
                             "runs_left":[runs_left],"crr":[crr],"rrr":[rrr],"Venue":[selected_city],
                             "Strike_Rate_x":[strike_rate_x],"Strike_Rate_y":[strike_rate_y]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win * 100)) + "%")
    st.header(bowling_team + "- " + str(round(loss * 100)) + "%")
