from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# =========================================================
# KCE KNOWLEDGE BASE
# =========================================================

college_info = {

    "about": """
Kings College of Engineering (KCE) is an autonomous engineering institution
located at Punalkulam, near Thanjavur, Gandarvakottai Taluk,
Pudukkottai District, Tamil Nadu.

KCE was founded in 2001 by Raj Educational Trust (RET), Chennai.
The institution focuses on providing technical education and is approved
by AICTE and affiliated to Anna University, Chennai.
KCE is also a NAAC accredited institution and has autonomous status.
""",

    "location": """
Kings College of Engineering is located at:

Punalkulam, Near Thanjavur,
Gandarvakottai Taluk,
Pudukkottai District – 613 303,
Tamil Nadu, India.

The campus is on the Thanjavur-Pudukkottai Highway.
""",

    "contact": """
📍 Kings College of Engineering
Punalkulam, Near Thanjavur,
Gandarvakottai Taluk,
Pudukkottai District – 613 303,
Tamil Nadu, India.

📞 Office / Admission: +91-6380989024
📧 Email: contact@kingsengg.edu.in
🌐 Website: www.kingsengg.edu.in
""",

    "ug": """
🎓 UG Programmes currently listed by KCE:

• B.E. Civil Engineering
• B.E. Computer Science and Engineering
• B.E. Electronics and Communication Engineering
• B.E. Electrical and Electronics Engineering
• B.E. Mechanical Engineering
• B.Tech Artificial Intelligence and Data Science
• B.Tech Information Technology
""",

    "pg": """
🎓 PG Programmes currently listed by KCE:

• M.E. VLSI Design
• M.E. Thermal Engineering
• M.E. Power Electronics and Drives
• M.E. Computer Science and Engineering
• M.B.A. Master of Business Administration
""",

    "phd": """
🔬 Ph.D. Programmes currently listed by KCE:

• Ph.D. Mechanical Engineering
• Ph.D. Electronics and Communication Engineering
""",

    "courses": """
KCE currently lists:

UG:
7 programmes

PG:
5 programmes

Ph.D:
2 programmes

The programmes include Civil Engineering, Computer Science and Engineering,
Electronics and Communication Engineering, Electrical and Electronics
Engineering, Mechanical Engineering, Artificial Intelligence and Data Science,
Information Technology, VLSI Design, Thermal Engineering,
Power Electronics and Drives, Computer Science and Engineering,
MBA and Ph.D. programmes.
""",

    "cse": """
💻 Department of Computer Science and Engineering

KCE offers B.E. Computer Science and Engineering.
The CSE programme was established in 2001 and the current listed intake
is 120 students.

The department focuses on computer science, programming,
software development, computing technologies and related areas.
""",

    "ece": """
📡 Department of Electronics and Communication Engineering

KCE offers B.E. Electronics and Communication Engineering.
The department was established in 2001 and the current listed intake
is 120 students.

The department is also associated with research activities at KCE.
""",

    "eee": """
⚡ Department of Electrical and Electronics Engineering

KCE offers B.E. Electrical and Electronics Engineering.
The department was established in 2001 and the current listed intake
is 60 students.
""",

    "civil": """
🏗️ Department of Civil Engineering

KCE offers B.E. Civil Engineering.
The department was established in 2010 and the current listed intake
is 30 students.
""",

    "mechanical": """
⚙️ Department of Mechanical Engineering

KCE offers B.E. Mechanical Engineering.
The department was established in 2006 and the current listed intake
is 60 students.

The department is also associated with research activities.
""",

    "it": """
🖥️ Information Technology

KCE currently lists B.Tech Information Technology.
The programme was established in 2024 and the current listed intake
is 30 students.
""",

    "aids": """
🤖 Artificial Intelligence and Data Science

KCE currently lists B.Tech Artificial Intelligence and Data Science.
The programme was established in 2023 and the current listed intake
is 60 students.
""",

    "facilities": """
🏫 KCE provides several campus facilities, including:

• Classrooms
• Laboratories
• Computer laboratories
• Library
• Seminar and conference facilities
• Auditorium
• Hostel facilities
• Cafeteria
• Health centre
• Sports facilities
• Indoor stadium
• Gym facilities
• Internet and IT infrastructure
• Drinking water facilities
""",

    "library": """
📚 KCE Library

The library provides books, journals and electronic resources.
The official library information currently lists more than 33,000 books
and resources including IEEE collections and e-resources.

The library also provides OPAC and access to learning resources.
""",

    "hostel": """
🏠 Hostel Facilities

KCE has separate hostel facilities for boys and girls.

Facilities listed by KCE include:

• Study facilities
• Reading rooms
• Recreation facilities
• Gym
• Sports facilities
• Medical facilities
• Purified drinking water
• Mess facilities
• 24-hour water supply
• Telephone facilities
• Canteen and other campus facilities
""",

    "placement": """
💼 Training and Placement

KCE has a Training and Placement Cell that works on career preparation,
industry interaction, soft-skill development, aptitude training,
career guidance and campus recruitment.

The official placement page also lists recent recruitment drives
and placement-related activities.
""",

    "admission": """
🎓 Admissions

For current admission information, eligibility, application procedures,
counselling information and available programmes, students should check
the official KCE website or contact the admission office.

📞 Admission Contact:
+91-6380989024

🌐 www.kingsengg.edu.in
""",

    "autonomous": """
KCE is an autonomous institution.

The official KCE website states that the institution is approved by AICTE,
affiliated to Anna University, NAAC accredited and has autonomous status.
""",

    "transport": """
🚌 For current transport-related information, routes and availability,
please contact the college directly or check the official KCE website.
""",
    "faculty": """
Department of Computer Science and Engineering HOD: DR.S.M.Uma M.E..,Ph.D.,
Department of Electrical and Electronics Engineering HOD : MR.R.Sundaramoorthi B.E.,M.E.,Ph.D.,
Department of Electronics and Communication Engineering HOD : Mrs.N.Mangaiyarkarasi B.E.,M.E.,(Ph.D).,
Department of Civil Engineering HOD : PROF.DR.R.Saravanan B.E.,M.E.,Ph.D.,
Department of Mechanical Engineering HOD : B.E.,M.E.,Ph.D.,
Department of Artificial Intelligence and Data Science HOD : DR.S.M.Uma M.E..,Ph.D.,
Department of Information Technology HOD : DR.S.M.Uma M.E..,Ph.D., .
""",

    "website": """
🌐 Official KCE Website:

www.kingsengg.edu.in

You can use the official website for announcements,
admissions, departments, facilities, placements and contact information.
"""
}


# =========================================================
# CHATBOT RESPONSE FUNCTION
# =========================================================

def chatbot_response(message):

    text = message.lower().strip()

    # Greetings
    if re.search(r"\b(hi|hello|hey|hii|good morning|good evening)\b", text):
        return (
            "Hello! 👋 I'm the KCE Chatbot. "
            "I can help you with courses, departments, admissions, "
            "facilities, placements, hostel, library and contact details."
        )

    # Thanks
    if any(word in text for word in ["thank you", "thanks", "thank"]):
        return "You're welcome! 😊 I'm happy to help with KCE information."

    # Location
    if any(word in text for word in [
        "where is", "location", "located", "address", "where college"
    ]):
        return college_info["location"]

    # Contact
    if any(word in text for word in [
        "contact", "phone", "mobile", "email", "mail", "number"
    ]):
        return college_info["contact"]

    # About
    if any(word in text for word in [
        "about kce", "about college", "history", "when founded",
        "established", "about kings"
    ]):
        return college_info["about"]

    # All courses
    if any(word in text for word in [
        "courses", "course", "programmes", "programs",
        "how many courses", "departments"
    ]):
        return college_info["courses"]

    # UG
    if any(word in text for word in [
        "ug", "undergraduate", "b.e", "btech", "b.tech"
    ]):
        return college_info["ug"]

    # PG
    if any(word in text for word in [
        "pg", "postgraduate", "m.e", "mba"
    ]):
        return college_info["pg"]

    # PhD
    if any(word in text for word in [
        "phd", "ph.d", "doctorate", "research"
    ]):
        return college_info["phd"]

    # CSE
    if any(word in text for word in [
        "cse", "computer science", "computer department"
    ]):
        return college_info["cse"]

    # ECE
    if any(word in text for word in [
        "ece", "electronics", "communication department"
    ]):
        return college_info["ece"]

    # EEE
    if any(word in text for word in [
        "eee", "electrical", "electrical department"
    ]):
        return college_info["eee"]

    # Civil
    if any(word in text for word in [
        "civil", "civil department"
    ]):
        return college_info["civil"]

    # Mechanical
    if any(word in text for word in [
        "mechanical", "mech", "mechanical department"
    ]):
        return college_info["mechanical"]

    # IT
    if any(word in text for word in [
        "information technology", "it department"
    ]):
        return college_info["it"]

    # AI & DS
    if any(word in text for word in [
        "artificial intelligence", "data science", "ai ds", "aids"
    ]):
        return college_info["aids"]

    # Facilities
    if any(word in text for word in [
        "facility", "facilities", "infrastructure",
        "campus", "lab", "laboratory", "sports"
    ]):
        return college_info["facilities"]

    # Library
    if any(word in text for word in [
        "library", "books", "book"
    ]):
        return college_info["library"]

    # Hostel
    if any(word in text for word in [
        "hostel", "accommodation", "stay"
    ]):
        return college_info["hostel"]

    # Placement
    if any(word in text for word in [
        "placement", "placements", "job", "recruitment",
        "training and placement"
    ]):
        return college_info["placement"]

    # Admission
    if any(word in text for word in [
        "admission", "apply", "application", "eligibility",
        "counselling", "counseling"
    ]):
        return college_info["admission"]

    # Autonomous
    if any(word in text for word in [
        "autonomous", "aicte", "anna university", "naac", "approval"
    ]):
        return college_info["autonomous"]

    #FACULTY
    if any(word in text for word in [
        "faculty", "HOD", "staff"
    ]):
        return college_info["faculty"]

    # Website
    if any(word in text for word in [
        "website", "official site", "web"
    ]):
        return college_info["website"]

    # Transport
    if any(word in text for word in [
        "transport", "bus", "bus route"
    ]):
        return college_info["transport"]

   # =========================================================
# FALLBACK
# =========================================================

    return (
        "I'm sorry, I don't have that information yet.🙂\n\n"
        "I can currently help you with courses, departments, "
        "admissions, facilities, hostel, library, placements, "
        "faculty, contact details and other KCE information.\n\n"

        "🌐 For further and updated information, "
        "please visit the official KCE website:\n"
        
        "https://www.kingsengg.edu.in/"
    )


# =========================================================
# FLASK ROUTES
# =========================================================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    response = chatbot_response(user_message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)