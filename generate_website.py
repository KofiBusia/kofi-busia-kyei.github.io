from jinja2 import Environment, FileSystemLoader

# Personal Details
personal_details = {
    'email': 'kyeikofi@gmail.com',
    'phone': '0244208667',
    'linkedin': 'https://linkedin.com/in/kofi-busia-kyei-24a6661b8'
}

# Professional Summary
professional_summary = """
Seasoned finance professional with over a decade of experience in investment management, wealth management, and stockbroking. Proven expertise in pension fund oversight, portfolio optimization, and strategic leadership. Adept at leveraging advanced technologies, including Artificial Intelligence, to deliver innovative solutions in financial services. A recognized thought leader with multiple published works and a track record of achieving outstanding investment returns and forging impactful industry partnerships.
"""

# Employment Experience
employment_experience = [
    {
        'title': 'Head, Pension Funds & Institutional Funds Management',
        'company': 'Merban Capital Ltd (formerly UMB Investment Holdings Limited)',
        'period': 'Sep 2022 - Present',
        'description': """
        - Oversee and direct all aspects of managing pension funds and institutional investment portfolios.
        - Provide leadership, strategic oversight, and asset management for client portfolios.
        - Develop and implement tailored investment strategies for institutional clients, ensuring alignment with long-term goals.
        - Monitor and assess financial markets to identify risks and opportunities for fund performance.
        - Coordinate with regulatory bodies to ensure compliance and uphold fiduciary responsibilities.
        """
    },
    {
        'title': 'Deputy Manager, Wealth Management',
        'company': 'Merban Capital Ltd',
        'period': 'Sep 2019 - Aug 2022',
        'description': """
        - Supported Wealth Management team in managing high-net-worth clients’ portfolios.
        - Delivered exceptional client relationship management and financial advisory services.
        """
    },
    {
        'title': 'Acting Head',
        'company': 'UMB Stockbrokers Limited',
        'period': 'May 2016 - Apr 2018',
        'description': """
        - Managed operations of the stockbroking division, including research, advisory services, and trading.
        - Directed brokerage services, ensuring effective execution of client transactions.
        """
    },
    {
        'title': 'Head, Trading & Settlement',
        'company': 'UMB Stockbrokers Ltd',
        'period': 'Apr 2015 - May 2016',
        'description': """
        - Oversaw trading and settlement operations, ensuring efficiency in financial market transactions.
        """
    },
    {
        'title': 'Research & Relationship Manager',
        'company': 'UMB Stockbrokers Limited',
        'period': 'Jun 2012 - Apr 2015',
        'description': """
        - Built strong client relationships while providing research-based investment insights.
        """
    },
    {
        'title': 'Banking Officer',
        'company': 'Universal Merchant Bank',
        'period': 'Feb 2009 - Jun 2012',
        'description': """
        - Delivered essential banking services, regulatory compliance, and excellent customer experience.
        """
    },
    {
        'title': 'National Service Person',
        'company': 'Universal Merchant Bank',
        'period': 'Oct 2007 - Aug 2008',
        'description': """
        - Provided support in banking operations, gaining valuable industry experience.
        """
    }
]

# Publications
publications = [
    {'title': 'CEDI FACES PRESSURE AMID US DEBT CEILING NEGOTIATIONS', 'source': 'Business & Financial Times', 'date': 'May 30, 2023'},
    {'title': 'Green Bonds: A Model of Transparency and Accountability in Sustainable Investments', 'source': 'Business & Financial Times', 'date': 'July 22, 2024'},
    {'title': 'Formalizing Businesses: The Key to Attracting Investors and Affordable Capital', 'source': 'Business & Financial Times', 'date': 'Sept 14, 2023'},
    {'title': 'Investments on the Ghana Stock Exchange: Has the Foreign Investor Benefited?', 'source': 'CITI Newsroom', 'date': 'Sept 2018'},
    {'title': 'DDEP Coupon Payments: Key to Financial Markets Recovery', 'source': 'Business & Financial Times', 'date': 'Sept 22, 2023'},
    {'title': 'Unlisted Multinational Companies in Ghana: A Reason for the Depreciation of the Ghanaian Cedi', 'source': 'Business & Financial Times', 'date': 'Sept 19, 2023'},
    {'title': 'BITCOINS, ALTCOINS, PONZI SCHEMES', 'source': 'Business & Financial Times', 'date': 'Feb 18, 2018'}
]

# Projects
projects = [
    {'name': 'Stock Trading Platform', 'description': 'Built an automated trading solution using Python for enhanced trading accuracy and efficiency'},
    {'name': 'Investment Portfolio Manager', 'description': 'Designed a portfolio management system'},
    {'name': 'HR Management WebApp', 'description': 'Developed cleanvisionhr.com to streamline HR processes for businesses'},
    {'name': 'Investment Calculator WebApp', 'description': 'Built younginvestorcalculator.com to assist users in financial planning'}
]

# Technical Skills & Certifications
skills_certifications = [
    'AI Tools & Certifications: Certified in DALLE-E, ChatGPT, DeepSeek, Jasper AI, and MidJourney',
    'Programming & Data Analysis: Proficient in Python for financial modeling, automation, and AI-driven solutions',
    'Prompt Engineering: Skilled in designing optimized prompts for AI tools such as ChatGPT and Jasper AI',
    'Portfolio Management: Expertise in managing diverse investment portfolios for institutional and individual clients',
    'Financial Market Analysis: Strong analytical skills for evaluating market trends and risks',
    'Pension Fund Management: Specialized in strategies for maximizing long-term fund growth'
]

# Education
education = [
    {'degree': 'MBA Finance', 'institution': 'Wisconsin International University', 'period': '2012 - 2014'},
    {'degree': 'BA Sociology & English', 'institution': 'University of Ghana', 'period': '2003 - 2007'}
]

# Render Template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

data = {
    'personal_details': personal_details,
    'professional_summary': professional_summary,
    'employment_experience': employment_experience,
    'publications': publications,
    'projects': projects,
    'skills_certifications': skills_certifications,
    'education': education
}

html = template.render(data)

with open('index.html', 'w') as f:
    f.write(html)

print("Website generated successfully!")