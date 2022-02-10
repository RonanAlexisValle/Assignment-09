import json

hatdog = [
    {
        'name': "Dolores T. Madrigal",
        'place': "Philippines",
        'phone_number': "+(63) 912 345 6789",
        'mail': "youredawan@gmail.com",
        'account': "linkedin.com\in\youredawan",
        'nino': 'Skills: ',
        'skills':[
            {
            'skill_01':" - Layout Artist",
            'skill_02':" - Proficient in Python Coding",
            'skill_03':" - Proficient with Microsoft Office",
            'skill_04':" - Proficient in Adobe Photoshop",
            'skill_05':" - Proficient in HTML Coding",
            'skill_06':" - Skills in Website Troubleshooting",
            'skill_07':" - Skilled in Digital Design and Software Development",
            'skill_08':" - Strong Analytical Skills"
            }
            ],
        'pixelrei': "Experiences: ",   
        'exp':[
            {
                'top': "Software Engineer",
                'company': "CirroStratus Inc.",
                'dates': "2016-2020",
                'ronan': "     - Engineered modern applications with Java, JavaScript, SQL Server, and SQL.",
                'alexis': "     - Built innovative microservices and Web Services",
                'timola': "     - Utilized Cloud Foundry for efficient building on top of Kubernetes.",
                'valle': "     - Efficiently deployed and integrated software engineered by team.",
                'next': "Kell Tech",
                'king': "September 2015 to May 2016",
                'nay': "    - Completed maintenance on existing programs",
                'justin': "    - Supported Kell Technicals testing and engineering processes."
            }
        ],
        'educ': "Educational Attainment: ",
        'school': [
            {
                'ter': "Tertiary: ",
                'univ': "Polytechnic University of the Philippines",
                'year': "2010-2014"
            }
        ]
    }
]

onin = json.dumps(hatdog, indent = 4)  
with open('Resume.json', 'w') as f:
    f.write(onin)
    f.close()  