import os
from flask import Flask, render_template

# Get the absolute path to the directory where this script is located
basedir = os.path.abspath(os.path.dirname(__file__))
# Ensure the working directory is set to the script's location
os.chdir(basedir)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/skills")
def skills():
    skills_list = [
        "CI/CD", "Jenkins", "Docker", "Kubernetes", "AWS EC2",
        "HTML", "CSS", "JavaScript",
        "Python", "SQL", "Photoshop", "Lightroom", "Figma"
    ]
    return render_template("skills.html", skills=skills_list)

@app.route("/projects")
def projects():
    projects_data = [
        {
            "title": "Siddharth Assignment", 
            "desc": "UI/UX Design project on Figma.", 
            "link": "https://www.figma.com/file/FVWgtwVkiyFNgGoT14e8Wj/Siddharth-Assignment"
        },
        {
            "title": "Grab A Cab", 
            "desc": "Web application hosted on Netlify.", 
            "link": "https://grabacab.netlify.app/index.html"
        },
        {
            "title": "WeatheriFive", 
            "desc": "Weather forecast application.", 
            "link": "https://weatherifive.netlify.app/"
        },
        {"title": "AI Powered Chatbot", "desc": "AI chatbot implementation.", "link": "https://github.com/siddharthx29/AI-powered-Chatbot-"},
        {"title": "Java Classroom Programs", "desc": "Collection of Java programs.", "link": "https://github.com/siddharthx29/Java_Classroom_Programs"},
        {"title": "PL/SQL", "desc": "Procedural language SQL examples.", "link": "https://github.com/siddharthx29/PL-Sql"},
        {"title": "DSA in C Basics", "desc": "Data Structures and Algorithms in C.", "link": "https://github.com/siddharthx29/DSA-IN-C_Basics"},
        {"title": "Online Shopping", "desc": "Online shopping system codebase.", "link": "https://github.com/siddharthx29/online_shopping"},
        {"title": "Terraform", "desc": "Terraform infrastructure as code.", "link": "https://github.com/siddharthx29/terraform"},
        {"title": "Jenkins", "desc": "Jenkins CI/CD configurations.", "link": "https://github.com/siddharthx29/Jenkins"},
        {"title": "AWS EC2", "desc": "AWS EC2 instances setup.", "link": "https://github.com/siddharthx29/From-Aws-EC2"},
        {"title": "Docker", "desc": "Docker containerization setups.", "link": "https://github.com/siddharthx29/Docker"},
        {"title": "Node.js Express", "desc": "Backend API with Node.js and Express.", "link": "https://github.com/siddharthx29/Node.js-express"},
        {"title": "Arrays in C", "desc": "C programming practices with arrays.", "link": "https://github.com/siddharthx29/Arrays-in-C-"},
        {"title": "C Programs", "desc": "General C programming examples.", "link": "https://github.com/siddharthx29/C-Programs"},
        {"title": "APIs in Python", "desc": "Building APIs with Flask and Python.", "link": "https://github.com/siddharthx29/APIs"},
        {"title": "Goa Rentacab Source", "desc": "Source code for rental cab website.", "link": "https://github.com/siddharthx29/Goa-rentacab"},
        {"title": "Weather App Source", "desc": "Source code for weather application.", "link": "https://github.com/siddharthx29/Weather-app"}
    ]
    return render_template("projects.html", projects=projects_data)

@app.route("/certifications")
def certifications():
    certifications_data = [
        {"title": "DevOps Course", "issuer": "Tutedude", "date": "10/10/2025"},
        {"title": "UI/UX Course", "issuer": "Tutedude", "date": "23/09/2024"},
        {"title": "Data Analytics Essentials", "issuer": "Cisco Networking Academy", "date": "July 26, 2024"},
        {"title": "Web Development Course", "issuer": "Teachnook", "date": "Sept 23, 2022"},
        {"title": "Web Development Internship", "issuer": "Teachnook / Immensphere", "date": "Sept 23, 2022"},
        {"title": "Build a Full Website using WordPress", "issuer": "Coursera", "date": "Dec 20, 2023"}
    ]
    return render_template("certifications.html", certifications=certifications_data)

@app.route("/contact me")
def contact():
    return render_template("contact&about me.html")

if __name__ == "__main__":
    app.run(debug=True)
