from flask import Flask, render_template, request, redirect, url_for, session
import json, os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'harish_portfolio_secret_2024_dev')

ADMIN_PASSWORD = "harish123"
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

def load_data():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def next_id(items):
    return max((i["id"] for i in items), default=0) + 1

def admin_logged_in():
    return session.get("admin") is True

# PUBLIC
@app.route("/")
def index():
    data = load_data()
    return render_template("index.html", data=data)

# ADMIN
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form.get("password") == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("admin_dashboard"))
        return render_template("login.html", error="Wrong password!")
    if admin_logged_in():
        return redirect(url_for("admin_dashboard"))
    return render_template("login.html", error=None)

@app.route("/admin/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("index"))

@app.route("/admin/dashboard")
def admin_dashboard():
    if not admin_logged_in():
        return redirect(url_for("admin"))
    data = load_data()
    return render_template("admin.html", data=data)

# ABOUT
@app.route("/admin/about/update", methods=["POST"])
def update_about():
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    for field in ["name","title","tagline","bio","email","linkedin","github"]:
        data["about"][field] = request.form.get(field, "")
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#about")

# PROJECTS
@app.route("/admin/project/add", methods=["POST"])
def add_project():
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    tools = [t.strip() for t in request.form.get("tools","").split(",") if t.strip()]
    data["projects"].append({
        "id": next_id(data["projects"]),
        "title": request.form.get("title",""),
        "description": request.form.get("description",""),
        "tools": tools,
        "github": request.form.get("github",""),
        "live": request.form.get("live",""),
        "image": request.form.get("image","")
    })
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#projects")

@app.route("/admin/project/update/<int:pid>", methods=["POST"])
def update_project(pid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    tools = [t.strip() for t in request.form.get("tools","").split(",") if t.strip()]
    for p in data["projects"]:
        if p["id"] == pid:
            p.update({"title": request.form.get("title",""), "description": request.form.get("description",""),
                      "tools": tools, "github": request.form.get("github",""),
                      "live": request.form.get("live",""), "image": request.form.get("image","")})
            break
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#projects")

@app.route("/admin/project/delete/<int:pid>")
def delete_project(pid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["projects"] = [p for p in data["projects"] if p["id"] != pid]
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#projects")

# SKILLS
@app.route("/admin/skill/add", methods=["POST"])
def add_skill():
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["skills"].append({"id": next_id(data["skills"]),
        "name": request.form.get("name",""), "level": int(request.form.get("level",50)),
        "category": request.form.get("category","")})
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#skills")

@app.route("/admin/skill/update/<int:sid>", methods=["POST"])
def update_skill(sid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    for s in data["skills"]:
        if s["id"] == sid:
            s.update({"name": request.form.get("name",""), "level": int(request.form.get("level",50)),
                      "category": request.form.get("category","")})
            break
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#skills")

@app.route("/admin/skill/delete/<int:sid>")
def delete_skill(sid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["skills"] = [s for s in data["skills"] if s["id"] != sid]
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#skills")

# CERTIFICATIONS
@app.route("/admin/cert/add", methods=["POST"])
def add_cert():
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["certifications"].append({"id": next_id(data["certifications"]),
        "name": request.form.get("name",""), "issuer": request.form.get("issuer",""),
        "year": request.form.get("year",""), "link": request.form.get("link",""), "file_path": request.form.get("file_path","")})
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#certs")

@app.route("/admin/cert/update/<int:cid>", methods=["POST"])
def update_cert(cid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    for c in data["certifications"]:
        if c["id"] == cid:
            c.update({"name": request.form.get("name",""), "issuer": request.form.get("issuer",""),
                      "year": request.form.get("year",""), "link": request.form.get("link",""), "file_path": request.form.get("file_path","")})
            break
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#certs")

@app.route("/admin/cert/delete/<int:cid>")
def delete_cert(cid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["certifications"] = [c for c in data["certifications"] if c["id"] != cid]
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#certs")

# EDUCATION
@app.route("/admin/edu/add", methods=["POST"])
def add_edu():
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["education"].append({"id": next_id(data["education"]),
        "education": request.form.get("education",""), "institution": request.form.get("institution",""),
        "year": request.form.get("year",""), "grade": request.form.get("grade","")})
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#education")

@app.route("/admin/edu/update/<int:eid>", methods=["POST"])
def update_edu(eid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    for e in data["education"]:
        if e["id"] == eid:
            e.update({"education": request.form.get("education",""), "institution": request.form.get("institution",""),
                      "year": request.form.get("year",""), "grade": request.form.get("grade","")})
            break
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#education")

@app.route("/admin/edu/delete/<int:eid>")
def delete_edu(eid):
    if not admin_logged_in(): return redirect(url_for("admin"))
    data = load_data()
    data["education"] = [e for e in data["education"] if e["id"] != eid]
    save_data(data)
    return redirect(url_for("admin_dashboard") + "#education")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
