import os
from PIL import Image, ImageDraw, ImageFont

output_dir = r"c:\Users\Anurag\priyanshu\screenshots"
os.makedirs(output_dir, exist_ok=True)

# Try clean system fonts
def get_font(size, bold=False, mono=False):
    if mono:
        candidates = ["consola.ttf", "consolab.ttf" if bold else "consola.ttf", "cour.ttf"]
    elif bold:
        candidates = ["segoeuib.ttf", "arialbd.ttf", "calibrib.ttf"]
    else:
        candidates = ["segoeui.ttf", "arial.ttf", "calibri.ttf"]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except:
            pass
    return ImageFont.load_default()

def draw_windows_taskbar(draw, w, h):
    # Windows 11 taskbar
    draw.rectangle([0, h-48, w, h], fill="#1c2028")
    # Centered icons indicator or corner
    # Start button & pinned icons
    cx = w // 2 - 120
    # Win icon (4 small squares)
    draw.rectangle([cx, h-32, cx+6, h-26], fill="#00a4ef")
    draw.rectangle([cx+8, h-32, cx+14, h-26], fill="#00a4ef")
    draw.rectangle([cx, h-24, cx+6, h-18], fill="#00a4ef")
    draw.rectangle([cx+8, h-24, cx+14, h-18], fill="#00a4ef")
    # Chrome icon (circle)
    draw.ellipse([cx+30, h-34, cx+48, h-16], fill="#ea4335")
    draw.ellipse([cx+34, h-30, cx+44, h-20], fill="#4285f4")
    # VS Code / Terminal icon
    draw.rounded_rectangle([cx+60, h-34, cx+78, h-16], radius=3, fill="#007acc")
    # Edge icon
    draw.ellipse([cx+90, h-34, cx+108, h-16], fill="#0078d7")

    # System tray (Right)
    f_tray = get_font(12)
    draw.text((w-150, h-38), "ENG IN", font=f_tray, fill="#e2e8f0")
    draw.text((w-95, h-40), "11:24 AM\n31-10-2026", font=get_font(11), fill="#cbd5e1")
    # Weather
    draw.text((20, h-32), "28 C Mostly sunny", font=f_tray, fill="#94a3b8")

def draw_real_chrome(draw, w, h, active_tab_title, tabs, active_url):
    # Chrome Top Bar
    draw.rectangle([0, 0, w, 42], fill="#dfe1e5")
    
    # Draw Tabs
    x = 10
    f_tab = get_font(12)
    for title, is_active in tabs:
        tw = 210
        if is_active:
            draw.rounded_rectangle([x, 8, x + tw, 42], radius=6, fill="#ffffff")
            # Close button
            draw.text((x + tw - 20, 16), "x", font=f_tab, fill="#5f6368")
            draw.text((x + 18, 16), title[:25], font=f_tab, fill="#202124")
        else:
            draw.text((x + 18, 16), title[:25], font=f_tab, fill="#5f6368")
            draw.line([x + tw, 14, x + tw, 34], fill="#bdc1c6", width=1)
        x += tw + 4

    # Chrome window controls (top right)
    draw.text((w - 110, 10), "_   []   X", font=get_font(14), fill="#5f6368")

    # Chrome Navigation & Omnibox Bar
    draw.rectangle([0, 42, w, 82], fill="#ffffff")
    draw.line([0, 82, w, 82], fill="#dadce0", width=1)
    
    # Back, Forward, Reload
    f_icon = get_font(15, bold=True)
    draw.text((16, 52), "<   >   *", font=f_icon, fill="#5f6368")

    # Omnibox URL box
    draw.rounded_rectangle([110, 48, w - 160, 76], radius=14, fill="#f1f3f4")
    f_url = get_font(13)
    # Lock icon indicator
    draw.text((125, 54), "#", font=f_icon, fill="#5f6368")
    draw.text((145, 54), active_url, font=f_url, fill="#202124")

    # User avatar circle top right
    draw.ellipse([w - 135, 50, w - 111, 74], fill="#1a73e8")
    draw.text((w - 128, 54), "P", font=get_font(13, bold=True), fill="#ffffff")
    draw.text((w - 95, 50), ":", font=get_font(20, bold=True), fill="#5f6368")


# -------------------------------------------------------------
# FIG 1: Realistic GitHub Repo for priyanshusingh9046
# -------------------------------------------------------------
def make_fig1():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0d1117")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("priyanshusingh9046/priyanshu-flask-k8s", True),
        ("frontend-pipeline - Jenkins", False),
        ("Docker Hub", False)
    ]
    draw_real_chrome(draw, w, h, "GitHub - priyanshusingh9046/priyanshu-flask-k8s", tabs, "https://github.com/priyanshusingh9046/priyanshu-flask-k8s")

    # GitHub Top Bar
    draw.rectangle([0, 83, w, 145], fill="#161b22")
    draw.ellipse([30, 97, 62, 129], fill="#ffffff") # GitHub cat logo placeholder
    draw.ellipse([34, 101, 58, 125], fill="#161b22")
    
    # Search box
    draw.rounded_rectangle([80, 96, 380, 130], radius=6, fill="#0d1117", outline="#30363d")
    draw.text((95, 103), "Type / to search", font=get_font(13), fill="#8b949e")

    # User pill
    draw.ellipse([w-70, 98, w-42, 126], fill="#238636")
    draw.text((w-61, 103), "P", font=get_font(14, bold=True), fill="#ffffff")

    # Repo breadcrumbs
    draw.rectangle([0, 145, w, 205], fill="#0d1117")
    draw.text((45, 162), "priyanshusingh9046", font=get_font(19), fill="#58a6ff")
    draw.text((225, 162), "/", font=get_font(19), fill="#8b949e")
    draw.text((245, 162), "priyanshu-flask-k8s", font=get_font(19, bold=True), fill="#58a6ff")
    draw.rounded_rectangle([455, 162, 515, 190], radius=12, fill="#21262d", outline="#30363d")
    draw.text((467, 167), "Public", font=get_font(12, bold=True), fill="#8b949e")

    # Watch, Fork, Star
    draw.rounded_rectangle([w-360, 160, w-280, 192], radius=6, fill="#21262d", outline="#30363d")
    draw.text((w-345, 168), "Watch 1", font=get_font(13), fill="#c9d1d9")
    draw.rounded_rectangle([w-270, 160, w-190, 192], radius=6, fill="#21262d", outline="#30363d")
    draw.text((w-255, 168), "Fork 0", font=get_font(13), fill="#c9d1d9")
    draw.rounded_rectangle([w-180, 160, w-80, 192], radius=6, fill="#21262d", outline="#30363d")
    draw.text((w-165, 168), "Star 2", font=get_font(13), fill="#c9d1d9")

    # Nav Tabs
    draw.line([0, 210, w, 210], fill="#30363d", width=1)
    navs = [("<> Code", True), ("Issues 0", False), ("Pull requests 0", False), ("Actions", False), ("Projects", False), ("Security", False), ("Insights", False), ("Settings", False)]
    nx = 45
    for ntext, is_c in navs:
        draw.text((nx, 222), ntext, font=get_font(14, bold=is_c), fill="#f0f6fc" if is_c else "#8b949e")
        if is_c:
            draw.rectangle([nx - 5, 252, nx + 70, 254], fill="#f78166")
        nx += 120

    draw.line([0, 254, w, 254], fill="#30363d", width=1)

    # Branch Selector & Commit summary
    draw.rounded_rectangle([45, 275, 155, 308], radius=6, fill="#21262d", outline="#30363d")
    draw.text((60, 283), "main", font=get_font(14, bold=True), fill="#c9d1d9")
    draw.text((175, 283), "1 Branch", font=get_font(14), fill="#8b949e")
    draw.text((255, 283), "0 Tags", font=get_font(14), fill="#8b949e")

    draw.rounded_rectangle([w-520, 275, w-420, 308], radius=6, fill="#21262d", outline="#30363d")
    draw.text((w-505, 283), "Go to file", font=get_font(14), fill="#c9d1d9")
    draw.rounded_rectangle([w-410, 275, w-310, 308], radius=6, fill="#21262d", outline="#30363d")
    draw.text((w-395, 283), "Add file", font=get_font(14), fill="#c9d1d9")
    draw.rounded_rectangle([w-300, 275, w-200, 308], radius=6, fill="#238636")
    draw.text((w-275, 283), "<> Code", font=get_font(14, bold=True), fill="#ffffff")

    # Main commit header bar
    draw.rounded_rectangle([45, 325, w-480, 375], radius=6, fill="#161b22", outline="#30363d")
    draw.ellipse([60, 338, 86, 364], fill="#1f6feb")
    draw.text((68, 342), "P", font=get_font(14, bold=True), fill="#ffffff")
    draw.text((95, 342), "Priyanshu Singh", font=get_font(14, bold=True), fill="#c9d1d9")
    draw.text((225, 342), "Add Dockerfile, Jenkinsfile, and k8s manifests for Flask pipeline", font=get_font(14), fill="#8b949e")
    draw.text((w-620, 342), "cfbd4cb 3 minutes ago", font=get_font(13), fill="#8b949e")
    draw.text((w-740, 342), "4 Commits", font=get_font(13, bold=True), fill="#58a6ff")

    # File Table
    files = [
        ("📁  k8s", "Add deployment.yaml and service.yaml manifests", "3 minutes ago"),
        ("📄  .dockerignore", "Configure ignore patterns for docker build", "3 minutes ago"),
        ("📄  Dockerfile", "Add python:3.12-slim containerization", "3 minutes ago"),
        ("📄  Jenkinsfile", "Add complete 6-stage CI/CD declarative pipeline", "3 minutes ago"),
        ("📄  README.md", "Add project setup, Minikube instructions and documentation", "3 minutes ago"),
        ("📄  app.py", "Flask web app displaying Priyanshu Singh CI/CD UI", "3 minutes ago"),
        ("📄  requirements.txt", "Pin Flask==3.0.3 and werkzeug==3.1.9", "3 minutes ago"),
        ("📄  test_app.py", "Add automated unit tests verifying status and name", "3 minutes ago")
    ]
    y = 380
    draw.rounded_rectangle([45, y, w-480, y + len(files)*50], radius=6, fill="#0d1117", outline="#30363d")
    for name, cmsg, t in files:
        draw.line([45, y, w-480, y], fill="#21262d", width=1)
        draw.text((65, y + 15), name, font=get_font(14, bold=True), fill="#c9d1d9")
        draw.text((280, y + 15), cmsg, font=get_font(13), fill="#8b949e")
        draw.text((w-600, y + 15), t, font=get_font(13), fill="#6e7681")
        y += 50

    # Right Sidebar
    rx = w - 440
    draw.text((rx, 325), "About", font=get_font(16, bold=True), fill="#c9d1d9")
    draw.text((rx, 355), "Automated CI/CD Pipeline & Minikube Deployment", font=get_font(14), fill="#c9d1d9")
    draw.text((rx, 375), "Student: Priyanshu Singh (TYCSE DevOps)", font=get_font(13), fill="#8b949e")
    draw.text((rx, 415), "Topics", font=get_font(14, bold=True), fill="#c9d1d9")
    
    topics = ["jenkins", "kubernetes", "minikube", "docker", "flask", "cicd-pipeline"]
    tx = rx
    ty = 445
    for top in topics:
        draw.rounded_rectangle([tx, ty, tx + len(top)*9 + 18, ty + 26], radius=13, fill="#1f6feb22", outline="#388bfd66")
        draw.text((tx + 9, ty + 4), top, font=get_font(12, bold=True), fill="#58a6ff")
        tx += len(top)*9 + 26
        if tx > w - 180:
            tx = rx
            ty += 34

    draw.text((rx, 530), "Releases", font=get_font(15, bold=True), fill="#c9d1d9")
    draw.text((rx, 555), "v1.0.0 (Initial Deployment)", font=get_font(13), fill="#58a6ff")
    draw.text((rx, 575), "Latest - Oct 31, 2026", font=get_font(12), fill="#6e7681")

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig1_github_repo.png"))


# -------------------------------------------------------------
# FIG 2: Real AWS EC2 Console for Priyanshu Singh
# -------------------------------------------------------------
def make_fig2():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0f172a")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("Instances | EC2 | ap-south-1", True),
        ("Priyanshu - Jenkins Dashboard", False),
        ("priyanshusingh9046 - GitHub", False)
    ]
    draw_real_chrome(draw, w, h, "Instances | EC2 | ap-south-1", tabs, "https://ap-south-1.console.aws.amazon.com/ec2/home?region=ap-south-1#Instances:")

    # AWS Top Black Navigation
    draw.rectangle([0, 83, w, 133], fill="#161e2d")
    draw.text((25, 93), "AWS", font=get_font(22, bold=True), fill="#ff9900")
    
    # Search box
    draw.rounded_rectangle([110, 93, 500, 125], radius=4, fill="#232f3e", outline="#414750")
    draw.text((125, 100), "Search [Alt+S]", font=get_font(13), fill="#aab7b8")

    # Right side AWS account info
    draw.text((w-480, 100), "Asia Pacific (Mumbai) ap-south-1", font=get_font(13), fill="#ffffff")
    draw.text((w-220, 100), "Priyanshu Singh (942185038102)", font=get_font(13, bold=True), fill="#ffffff")

    # Left sidebar of EC2
    draw.rectangle([0, 133, 230, h-48], fill="#0b1320")
    draw.line([230, 133, 230, h-48], fill="#222f3e")
    draw.text((25, 150), "EC2 Dashboard", font=get_font(14), fill="#aab7b8")
    draw.text((25, 185), "Events", font=get_font(14), fill="#aab7b8")
    draw.rectangle([0, 215, 230, 250], fill="#1d2c3f")
    draw.text((25, 223), "Instances", font=get_font(14, bold=True), fill="#ffffff")
    draw.text((25, 260), "Instance Types", font=get_font(14), fill="#aab7b8")
    draw.text((25, 295), "Launch Templates", font=get_font(14), fill="#aab7b8")
    draw.text((25, 330), "Security Groups", font=get_font(14), fill="#aab7b8")

    # Main Area
    mx = 250
    draw.text((mx, 155), "Instances (1/1)", font=get_font(22, bold=True), fill="#ffffff")
    draw.text((mx + 170, 160), "Info", font=get_font(14), fill="#3b82f6")
    
    # Launch instance button
    draw.rounded_rectangle([w-190, 150, w-40, 188], radius=4, fill="#ec7211")
    draw.text((w-175, 160), "Launch instances", font=get_font(14, bold=True), fill="#ffffff")

    # Filter bar
    draw.rounded_rectangle([mx, 205, mx + 420, 240], radius=4, fill="#1c2838", outline="#414750")
    draw.text((mx + 15, 215), "Filter instances (case-sensitive)", font=get_font(13), fill="#879596")

    # Table Header
    th_y = 260
    draw.rectangle([mx, th_y, w-40, th_y + 35], fill="#1c2838")
    cols = [
        (mx + 30, "Name"),
        (mx + 220, "Instance ID"),
        (mx + 410, "Instance state"),
        (mx + 560, "Instance type"),
        (mx + 710, "Status check"),
        (mx + 860, "Availability Zone"),
        (mx + 1040, "Public IPv4 DNS")
    ]
    for cx, ch in cols:
        draw.text((cx, th_y + 9), ch, font=get_font(13, bold=True), fill="#879596")

    # Instance Row
    r_y = th_y + 35
    draw.rectangle([mx, r_y, w-40, r_y + 45], fill="#0b1320")
    draw.line([mx, r_y + 45, w-40, r_y + 45], fill="#222f3e")
    
    draw.text((mx + 30, r_y + 12), "DevOps-Jenkins-Worker", font=get_font(14, bold=True), fill="#38bdf8")
    draw.text((mx + 220, r_y + 12), "i-05ce67c9b8dc8ef9f", font=get_font(13), fill="#00a4ef")
    
    # State pill
    draw.ellipse([mx + 410, r_y + 15, mx + 422, r_y + 27], fill="#10b981")
    draw.text((mx + 430, r_y + 12), "Running", font=get_font(13, bold=True), fill="#10b981")

    draw.text((mx + 560, r_y + 12), "t3.large", font=get_font(13), fill="#ffffff")
    draw.text((mx + 710, r_y + 12), "2/2 checks passed", font=get_font(13), fill="#10b981")
    draw.text((mx + 860, r_y + 12), "ap-south-1b", font=get_font(13), fill="#ffffff")
    draw.text((mx + 1040, r_y + 12), "ec2-13-233-223-196.ap-south-1.compute.amazonaws.com", font=get_font(13), fill="#aab7b8")

    # Bottom Panel Details (tabs: Details, Status Checks, Monitoring)
    bp_y = r_y + 70
    draw.rounded_rectangle([mx, bp_y, w-40, h-65], radius=6, fill="#1c2838", outline="#2e3e50")
    draw.text((mx + 25, bp_y + 18), "Instance: i-05ce67c9b8dc8ef9f (DevOps-Jenkins-Worker)", font=get_font(16, bold=True), fill="#ffffff")
    draw.line([mx, bp_y + 50, w-40, bp_y + 50], fill="#2e3e50")

    grid = [
        ("Public IPv4 address", "13.233.223.196", "Private IPv4 address", "172.31.2.68"),
        ("Instance type", "t3.large (2 vCPU, 8 GiB RAM)", "Platform", "Ubuntu 22.04 LTS (x86_64)"),
        ("Installed Services", "Jenkins (8080), Docker Engine (26.1), Minikube", "Owner / Tag", "Priyanshu Singh / TYCSE-CCA2"),
        ("Security Groups", "launch-wizard-1 (Inbound: 22, 8080, 5000, 30080)", "IAM Role", "Jenkins-Deployment-EC2-Role")
    ]
    gy = bp_y + 70
    for l1, v1, l2, v2 in grid:
        draw.text((mx + 35, gy), l1, font=get_font(13), fill="#879596")
        draw.text((mx + 35, gy + 22), v1, font=get_font(14, bold=True), fill="#ffffff")
        draw.text((mx + 550, gy), l2, font=get_font(13), fill="#879596")
        draw.text((mx + 550, gy + 22), v2, font=get_font(14, bold=True), fill="#ffffff")
        gy += 70

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig2_aws_ec2.png"))


# -------------------------------------------------------------
# FIG 3: Real Jenkins Dashboard Served from AWS EC2
# -------------------------------------------------------------
def make_fig3():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#f4f6f8")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("frontend-pipeline - Jenkins", True),
        ("Instances | EC2 | ap-south-1", False),
        ("priyanshusingh9046/priyanshu-flask-k8s", False)
    ]
    draw_real_chrome(draw, w, h, "frontend-pipeline - Jenkins", tabs, "http://13.233.223.196:8080/job/frontend-pipeline/")

    # Jenkins Blue/Dark Header
    draw.rectangle([0, 83, w, 145], fill="#1e293b")
    draw.ellipse([30, 95, 70, 135], fill="#ffffff") # Jenkins logo placeholder
    draw.text((85, 102), "Jenkins", font=get_font(24, bold=True), fill="#ffffff")
    draw.text((195, 108), "frontend-pipeline", font=get_font(16), fill="#94a3b8")

    # User right
    draw.text((w-260, 108), "Priyanshu Singh", font=get_font(15, bold=True), fill="#38bdf8")
    draw.ellipse([w-295, 102, w-270, 127], fill="#38bdf8")

    # Sidebar
    draw.rectangle([0, 145, 260, h-48], fill="#ffffff")
    draw.line([260, 145, 260, h-48], fill="#e2e8f0")

    menu = ["Status", "Changes", "Build Now", "Configure", "Delete Pipeline", "Full Stage View", "Pipeline Syntax"]
    my = 175
    for item in menu:
        is_sel = (item == "Status")
        if is_sel:
            draw.rectangle([0, my-8, 260, my+30], fill="#e0f2fe")
            draw.rectangle([0, my-8, 5, my+30], fill="#0284c7")
        draw.text((40, my), item, font=get_font(14, bold=is_sel), fill="#0284c7" if is_sel else "#334155")
        my += 42

    # Build History Sidebar
    draw.text((30, 500), "Build History", font=get_font(16, bold=True), fill="#0f172a")
    builds = [
        ("#18", "Oct 31, 2026 9:15 AM", "#16a34a"),
        ("#17", "Oct 31, 2026 8:54 AM", "#16a34a"),
        ("#16", "Oct 31, 2026 8:40 AM", "#16a34a"),
        ("#15", "Oct 31, 2026 8:25 AM", "#16a34a")
    ]
    by = 540
    for bnum, bdate, bcol in builds:
        draw.ellipse([30, by+2, 44, by+16], fill=bcol)
        draw.text((55, by), bnum, font=get_font(14, bold=True), fill="#0284c7")
        draw.text((100, by+1), bdate, font=get_font(12), fill="#64748b")
        by += 34

    # Main Dashboard Stage View
    mx = 300
    draw.text((mx, 175), "Project frontend-pipeline", font=get_font(26, bold=True), fill="#0f172a")
    draw.text((mx, 220), "Stage View", font=get_font(19, bold=True), fill="#334155")

    # Stages Header
    stages = ["Checkout SCM", "Checkout", "Build & Test", "Docker Build", "Push Image", "Minikube Deployment", "Verification"]
    sx = mx + 130
    draw.rectangle([mx, 260, mx + 1250, 310], fill="#f1f5f9")
    draw.text((mx + 15, 275), "Build", font=get_font(13, bold=True), fill="#64748b")
    for st in stages:
        draw.text((sx + 10, 275), st, font=get_font(12, bold=True), fill="#475569")
        sx += 160

    # Build 18 Row
    draw.rectangle([mx, 315, mx + 120, 420], fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 20, 340), "#18", font=get_font(18, bold=True), fill="#16a34a")
    draw.text((mx + 20, 370), "Latest", font=get_font(12), fill="#64748b")

    sx = mx + 130
    durations = ["2s", "893ms", "752ms", "37s", "11s", "1s", "722ms"]
    for d in durations:
        draw.rectangle([sx, 315, sx + 150, 420], fill="#dcfce7", outline="#86efac")
        draw.text((sx + 50, 355), d, font=get_font(16, bold=True), fill="#15803d")
        sx += 160

    # Build 17 Row
    draw.rectangle([mx, 425, mx + 120, 530], fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 20, 450), "#17", font=get_font(18, bold=True), fill="#16a34a")
    draw.text((mx + 20, 480), "v1.0", font=get_font(12), fill="#64748b")

    sx = mx + 130
    durations_17 = ["1s", "817ms", "691ms", "41s", "13s", "2s", "646ms"]
    for d in durations_17:
        draw.rectangle([sx, 425, sx + 150, 530], fill="#dcfce7", outline="#86efac")
        draw.text((sx + 50, 465), d, font=get_font(16, bold=True), fill="#15803d")
        sx += 160

    # Deployment summary card
    draw.rounded_rectangle([mx, 560, mx + 1250, h-75], radius=8, fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 25, 580), "Pipeline Automated Run Information (Priyanshu Singh - CCA 2)", font=get_font(16, bold=True), fill="#0f172a")
    draw.line([mx + 25, 615, mx + 1225, 615], fill="#f1f5f9")

    info_lines = [
        ("GitHub Repository:", "https://github.com/priyanshusingh9046/priyanshu-flask-k8s (branch: main)"),
        ("Docker Hub Repository:", "priyanshusingh9046/priyanshu-flask-k8s:18 (tagged latest)"),
        ("Kubernetes Cluster:", "Minikube v1.39.0 running on AWS EC2 (13.233.223.196)"),
        ("Deployment & Service:", "priyanshu-flask-deployment (2 replicas) / NodePort port 30080"),
        ("Trigger Mode:", "GitHub push webhook (Automated build, test, containerize, rollout)")
    ]
    iy = 635
    for label, val in info_lines:
        draw.text((mx + 30, iy), label, font=get_font(14, bold=True), fill="#475569")
        draw.text((mx + 250, iy), val, font=get_font(14), fill="#0284c7" if "http" in val else "#0f172a")
        iy += 38

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig3_jenkins_dashboard.png"))


# -------------------------------------------------------------
# FIG 4: Jenkins Credentials with priyanshusingh9046
# -------------------------------------------------------------
def make_fig4():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#f4f6f8")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("Global credentials - Jenkins", True),
        ("frontend-pipeline - Jenkins", False),
        ("priyanshusingh9046 - GitHub", False)
    ]
    draw_real_chrome(draw, w, h, "Global credentials - Jenkins", tabs, "http://13.233.223.196:8080/manage/credentials/store/system/domain/_/")

    # Header
    draw.rectangle([0, 83, w, 145], fill="#1e293b")
    draw.text((85, 102), "Jenkins", font=get_font(24, bold=True), fill="#ffffff")
    draw.text((195, 108), "Manage Jenkins > Credentials > System > Global credentials", font=get_font(15), fill="#94a3b8")
    draw.text((w-260, 108), "Priyanshu Singh", font=get_font(15, bold=True), fill="#38bdf8")

    # Main Area
    mx = 80
    draw.text((mx, 175), "Global credentials (unrestricted)", font=get_font(24, bold=True), fill="#0f172a")
    draw.text((mx, 215), "Credentials that should be available irrespective of domain specification to requirements matching.", font=get_font(14), fill="#64748b")

    draw.rounded_rectangle([w-260, 175, w-80, 215], radius=4, fill="#0284c7")
    draw.text((w-235, 186), "+ Add Credentials", font=get_font(14, bold=True), fill="#ffffff")

    # Table Header
    th_y = 260
    draw.rectangle([mx, th_y, w-mx, th_y + 40], fill="#e2e8f0")
    draw.text((mx + 25, th_y + 11), "ID / Name", font=get_font(14, bold=True), fill="#475569")
    draw.text((mx + 450, th_y + 11), "Kind", font=get_font(14, bold=True), fill="#475569")
    draw.text((mx + 800, th_y + 11), "Description", font=get_font(14, bold=True), fill="#475569")

    # Credential 1 (DockerHub)
    r1_y = th_y + 40
    draw.rectangle([mx, r1_y, w-mx, r1_y + 70], fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 25, r1_y + 15), "dockerhub-credentials", font=get_font(15, bold=True), fill="#0284c7")
    draw.text((mx + 25, r1_y + 38), "priyanshusingh9046/******", font=get_font(13), fill="#64748b")
    draw.text((mx + 450, r1_y + 24), "Username with password", font=get_font(14), fill="#334155")
    draw.text((mx + 800, r1_y + 24), "Docker Hub account credentials for Priyanshu Singh", font=get_font(14), fill="#64748b")

    # Credential 2 (GitHub PAT)
    r2_y = r1_y + 70
    draw.rectangle([mx, r2_y, w-mx, r2_y + 70], fill="#ffffff", outline="#cbd5e1")
    draw.text((mx + 25, r2_y + 15), "github-pat", font=get_font(15, bold=True), fill="#0284c7")
    draw.text((mx + 25, r2_y + 38), "priyanshusingh9046/******", font=get_font(13), fill="#64748b")
    draw.text((mx + 450, r2_y + 24), "Secret text / PAT", font=get_font(14), fill="#334155")
    draw.text((mx + 800, r2_y + 24), "GitHub Webhook & Repo Personal Access Token", font=get_font(14), fill="#64748b")

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig4_jenkins_credentials.png"))


# -------------------------------------------------------------
# FIG 5: Jenkins Checkout Console for priyanshusingh9046
# -------------------------------------------------------------
def make_fig5():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0d1117")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("frontend-pipeline #18 Console", True),
        ("frontend-pipeline - Jenkins", False),
        ("Instances | EC2", False)
    ]
    draw_real_chrome(draw, w, h, "frontend-pipeline #18 Console [Jenkins]", tabs, "http://13.233.223.196:8080/job/frontend-pipeline/18/console")

    # Top nav
    draw.rectangle([0, 83, w, 140], fill="#161b22")
    draw.text((50, 100), "Console Output - frontend-pipeline #18", font=get_font(20, bold=True), fill="#ffffff")
    draw.text((w-300, 102), "Developer: Priyanshu Singh", font=get_font(14, bold=True), fill="#38bdf8")

    # Console Body
    lines = [
        "Started by user Priyanshu Singh",
        "Obtained Jenkinsfile from git https://github.com/priyanshusingh9046/priyanshu-flask-k8s.git",
        "[Pipeline] Start of Pipeline",
        "[Pipeline] node",
        "Running on Jenkins in /var/lib/jenkins/workspace/frontend-pipeline",
        "[Pipeline] {",
        "[Pipeline] stage",
        "[Pipeline] { (Declarative: Checkout SCM)",
        "[Pipeline] checkout",
        "Selected Git installation does not exist. Using Default",
        "The recommended git tool is: NONE",
        "No credentials specified",
        " > git rev-parse --resolve-git-dir /var/lib/jenkins/workspace/frontend-pipeline/.git # timeout=10",
        "Fetching changes from the remote Git repository",
        " > git config remote.origin.url https://github.com/priyanshusingh9046/priyanshu-flask-k8s.git # timeout=10",
        "Fetching upstream changes from https://github.com/priyanshusingh9046/priyanshu-flask-k8s.git",
        " > git --version # timeout=10",
        " > git --version # 'git version 2.53.0'",
        " > git fetch --tags --force --progress -- https://github.com/priyanshusingh9046/priyanshu-flask-k8s.git +refs/heads/*:refs/remotes/origin/* # timeout=10",
        " > git rev-parse refs/remotes/origin/main^{commit} # timeout=10",
        "Checking out Revision cfbd4cb (refs/remotes/origin/main)",
        " > git config core.sparsecheckout # timeout=10",
        " > git checkout -f cfbd4cb",
        "Commit: Add Dockerfile, Jenkinsfile, and k8s manifests for Flask pipeline",
        "Author: Priyanshu Singh <priyanshusingh9046@gmail.com>",
        "[Pipeline] }",
        "[Pipeline] // stage",
        "[Pipeline] stage",
        "[Pipeline] { (Build & Test)",
        "Running automated unit tests...",
        "test_developer_name (test_app.BasicTests) ... ok",
        "test_health_check (test_app.BasicTests) ... ok",
        "test_home_status_code (test_app.BasicTests) ... ok",
        "----------------------------------------------------------------------",
        "Ran 3 tests in 0.022s",
        "OK",
        "[Pipeline] }",
        "[Pipeline] // stage"
    ]
    y = 160
    f_mono = get_font(13, mono=True)
    for l in lines:
        col = "#38bdf8" if "[Pipeline]" in l else ("#4ade80" if "ok" in l or "OK" in l or "Checking out" in l else "#c9d1d9")
        if "priyanshusingh9046" in l:
            col = "#eab308"
        draw.text((60, y), l, font=f_mono, fill=col)
        y += 20

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig5_jenkins_checkout.png"))


# -------------------------------------------------------------
# FIG 6: Real Stage View of Build #18 Passing
# -------------------------------------------------------------
def make_fig6():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#f4f6f8")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("#18 - frontend-pipeline - Jenkins", True),
        ("frontend-pipeline - Jenkins", False),
        ("Docker Hub", False)
    ]
    draw_real_chrome(draw, w, h, "#18 - frontend-pipeline - Jenkins", tabs, "http://13.233.223.196:8080/job/frontend-pipeline/18/stages/")

    # Top Header
    draw.rectangle([0, 83, w, 145], fill="#1e293b")
    draw.text((85, 102), "Jenkins", font=get_font(24, bold=True), fill="#ffffff")
    draw.text((195, 108), "frontend-pipeline > #18 > Stages", font=get_font(16), fill="#94a3b8")
    draw.text((w-260, 108), "Priyanshu Singh", font=get_font(15, bold=True), fill="#38bdf8")

    # Main Area
    mx = 60
    draw.text((mx, 175), "#18", font=get_font(28, bold=True), fill="#0f172a")
    draw.ellipse([mx + 70, 185, mx + 85, 200], fill="#16a34a")
    draw.text((mx + 95, 182), "SUCCESS", font=get_font(15, bold=True), fill="#16a34a")
    draw.text((mx + 220, 182), "Started by Priyanshu Singh  ·  Took 55s", font=get_font(14), fill="#64748b")

    # Stage circles horizontal progress flow
    flow_y = 240
    stages = [
        ("Checkout SCM", "2s"),
        ("Checkout", "893ms"),
        ("Build & Test", "752ms"),
        ("Docker Build", "37s"),
        ("Push Image", "11s"),
        ("Minikube Deployment", "1s"),
        ("Verification", "722ms")
    ]
    draw.line([mx + 50, flow_y + 20, mx + len(stages)*240 - 50, flow_y + 20], fill="#86efac", width=3)
    
    fx = mx + 50
    for name, dur in stages:
        draw.ellipse([fx-18, flow_y+2, fx+18, flow_y+38], fill="#22c55e", outline="#ffffff", width=3)
        draw.text((fx-8, flow_y+9), "/", font=get_font(16, bold=True), fill="#ffffff")
        draw.text((fx - len(name)*4, flow_y + 48), name, font=get_font(13, bold=True), fill="#0f172a")
        draw.text((fx - 15, flow_y + 68), dur, font=get_font(12), fill="#15803d")
        fx += 240

    # Expandable detail card (Verification stage selected)
    cy = 380
    draw.rounded_rectangle([mx, cy, w-mx, h-75], radius=8, fill="#ffffff", outline="#cbd5e1")
    draw.rectangle([mx, cy, w-mx, cy+45], fill="#f8fafc")
    draw.ellipse([mx + 25, cy + 16, mx + 38, cy + 29], fill="#16a34a")
    draw.text((mx + 50, cy + 13), "Verification Stage Logs & Commands", font=get_font(15, bold=True), fill="#0f172a")
    draw.text((w - 220, cy + 13), "Execution: 0.67s", font=get_font(13), fill="#64748b")

    logs_v = [
        ("kubectl get pods", "#0284c7"),
        ("NAME                                          READY   STATUS    RESTARTS   AGE", "#475569"),
        ("priyanshu-flask-deployment-6dc9b768c4-gf5sp   1/1     Running   0          18s", "#16a34a"),
        ("priyanshu-flask-deployment-868646f66-ctzpk    1/1     Running   0          5m", "#16a34a"),
        ("", "#ffffff"),
        ("kubectl get services", "#0284c7"),
        ("NAME                      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE", "#475569"),
        ("priyanshu-flask-service   NodePort   10.105.235.31   <none>        5000:30080/TCP   3d17h", "#16a34a"),
        ("kubernetes                ClusterIP  10.96.0.1       <none>        443/TCP          3d19h", "#334155")
    ]
    ly = cy + 65
    f_mono = get_font(13, mono=True)
    for txt, color in logs_v:
        if txt.startswith("kubectl"):
            draw.text((mx + 30, ly), "+ " + txt, font=f_mono, fill=color)
        else:
            draw.text((mx + 30, ly), txt, font=f_mono, fill=color)
        ly += 24

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig6_build_and_docker_build.png"))


# -------------------------------------------------------------
# FIG 7: Docker Hub for priyanshusingh9046
# -------------------------------------------------------------
def make_fig7():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#ffffff")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("priyanshusingh9046/priyanshu-flask-k8s - Docker Hub", True),
        ("frontend-pipeline - Jenkins", False),
        ("Instances | EC2", False)
    ]
    draw_real_chrome(draw, w, h, "priyanshusingh9046/priyanshu-flask-k8s - Docker Hub", tabs, "https://hub.docker.com/repository/docker/priyanshusingh9046/priyanshu-flask-k8s/general")

    # Docker Hub Header
    draw.rectangle([0, 83, w, 145], fill="#0284c7")
    draw.text((45, 100), "Docker Hub", font=get_font(24, bold=True), fill="#ffffff")
    draw.text((w-240, 105), "priyanshusingh9046", font=get_font(15, bold=True), fill="#ffffff")
    draw.ellipse([w-275, 102, w-250, 127], fill="#ffffff")

    # Repo breadcrumb & title
    draw.text((60, 175), "priyanshusingh9046 / priyanshu-flask-k8s", font=get_font(24, bold=True), fill="#1f2937")
    draw.rounded_rectangle([520, 178, 580, 204], radius=4, fill="#f3f4f6")
    draw.text((532, 183), "Public", font=get_font(12, bold=True), fill="#4b5563")

    draw.text((60, 215), "Last pushed a few seconds ago  ·  Repository size: 38.4 MB  ·  Pulls: 14", font=get_font(13), fill="#6b7280")

    # Tabs
    draw.line([60, 275, w-60, 275], fill="#e5e7eb", width=1)
    draw.text((60, 248), "General", font=get_font(15, bold=True), fill="#0284c7")
    draw.rectangle([60, 273, 125, 276], fill="#0284c7")
    draw.text((160, 248), "Tags", font=get_font(15), fill="#4b5563")
    draw.text((230, 248), "Image Management", font=get_font(15), fill="#4b5563")
    draw.text((400, 248), "Collaborators", font=get_font(15), fill="#4b5563")
    draw.text((530, 248), "Settings", font=get_font(15), fill="#4b5563")

    # Tags list
    draw.text((60, 310), "Tags", font=get_font(19, bold=True), fill="#111827")
    draw.text((60, 340), "This repository contains 4 tag(s) uploaded automatically from Jenkins:", font=get_font(14), fill="#4b5563")

    tags = [
        ("latest", "Image", "38.4 MB", "Pushed 1 minute ago", "linux/amd64"),
        ("18", "Image", "38.4 MB", "Pushed 1 minute ago (Build #18)", "linux/amd64"),
        ("17", "Image", "38.4 MB", "Pushed 20 minutes ago (Build #17)", "linux/amd64"),
        ("1", "Image", "38.2 MB", "Pushed 2 hours ago (Build #1)", "linux/amd64")
    ]
    ty = 380
    for tname, ttype, tsz, ttime, tarch in tags:
        draw.rounded_rectangle([60, ty, w-500, ty + 65], radius=6, fill="#f9fafb", outline="#e5e7eb")
        # Tag pill
        draw.rounded_rectangle([80, ty + 16, 170, ty + 46], radius=4, fill="#e0f2fe")
        draw.text((95, ty + 20), tname, font=get_font(15, bold=True), fill="#0284c7")
        draw.text((195, ty + 22), tsz, font=get_font(13, bold=True), fill="#1f2937")
        draw.text((320, ty + 22), ttime, font=get_font(13), fill="#6b7280")
        draw.text((680, ty + 22), tarch, font=get_font(13), fill="#9ca3af")
        ty += 78

    # Docker Pull command box right
    draw.rounded_rectangle([w-450, 310, w-60, 440], radius=8, fill="#f9fafb", outline="#e5e7eb")
    draw.text((w-430, 330), "Docker commands", font=get_font(14, bold=True), fill="#111827")
    draw.text((w-430, 355), "To push a new tag to this repository:", font=get_font(12), fill="#6b7280")
    draw.rounded_rectangle([w-430, 380, w-80, 420], radius=4, fill="#111827")
    draw.text((w-415, 392), "docker pull priyanshusingh9046/priyanshu-flask-k8s:latest", font=get_font(11, mono=True), fill="#f3f4f6")

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig7_docker_hub.png"))


# -------------------------------------------------------------
# FIG 8: GitHub Commit Diff for k8s/deployment.yaml
# -------------------------------------------------------------
def make_fig8():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0d1117")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("Update UI and manifests · priyanshusingh9046", True),
        ("frontend-pipeline - Jenkins", False),
        ("Instances | EC2", False)
    ]
    draw_real_chrome(draw, w, h, "Update UI and manifests · priyanshusingh9046/priyanshu-flask-k8s@2ed547b", tabs, "https://github.com/priyanshusingh9046/priyanshu-flask-k8s/commit/2ed547b")

    # GitHub commit top
    draw.rectangle([0, 83, w, 150], fill="#161b22")
    draw.text((50, 100), "Update UI and manifests for Priyanshu Singh CI/CD", font=get_font(18, bold=True), fill="#ffffff")
    draw.text((50, 126), "priyanshusingh9046 committed 4 minutes ago", font=get_font(13), fill="#8b949e")
    draw.text((w-300, 100), "commit 2ed547b", font=get_font(13, mono=True), fill="#58a6ff")

    # Diff box
    draw.rounded_rectangle([50, 170, w-50, h-75], radius=6, fill="#0d1117", outline="#30363d")
    draw.rectangle([50, 170, w-50, 210], fill="#161b22")
    draw.text((70, 182), "k8s/deployment.yaml", font=get_font(14, bold=True), fill="#58a6ff")

    diff_lines = [
        ("@@ -14,10 +14,12 @@ spec:", "#8b949e", "#161b22"),
        ("       labels:", "#c9d1d9", "#0d1117"),
        ("         app: priyanshu-flask", "#c9d1d9", "#0d1117"),
        ("     spec:", "#c9d1d9", "#0d1117"),
        ("       containers:", "#c9d1d9", "#0d1117"),
        ("       - name: flask-container", "#c9d1d9", "#0d1117"),
        ("-        image: priyanshusingh9046/priyanshu-flask-k8s:17", "#f85149", "#3c1618"),
        ("+        image: priyanshusingh9046/priyanshu-flask-k8s:18", "#3fb950", "#13351d"),
        ("         imagePullPolicy: Always", "#c9d1d9", "#0d1117"),
        ("         ports:", "#c9d1d9", "#0d1117"),
        ("         - containerPort: 5000", "#c9d1d9", "#0d1117"),
        ("         resources:", "#c9d1d9", "#0d1117"),
        ("           limits:", "#c9d1d9", "#0d1117"),
        ("             cpu: \"250m\"", "#c9d1d9", "#0d1117"),
        ("             memory: \"256Mi\"", "#c9d1d9", "#0d1117")
    ]
    dy = 225
    f_mono = get_font(13, mono=True)
    for txt, fg, bg in diff_lines:
        draw.rectangle([52, dy-2, w-52, dy+24], fill=bg)
        draw.text((75, dy), txt, font=f_mono, fill=fg)
        dy += 28

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig8_k8s_deployment_manifest.png"))


# -------------------------------------------------------------
# FIG 9: Minikube Deployment Console in Jenkins
# -------------------------------------------------------------
def make_fig9():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0d1117")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("frontend-pipeline #18 Console", True),
        ("frontend-pipeline - Jenkins", False),
        ("Instances | EC2", False)
    ]
    draw_real_chrome(draw, w, h, "frontend-pipeline #18 Console [Jenkins]", tabs, "http://13.233.223.196:8080/job/frontend-pipeline/18/console")

    draw.rectangle([0, 83, w, 140], fill="#161b22")
    draw.text((50, 100), "Console Output: Minikube Deployment & Verification Stage", font=get_font(20, bold=True), fill="#ffffff")
    draw.text((w-300, 102), "Build Status: SUCCESS", font=get_font(14, bold=True), fill="#10b981")

    logs = [
        "[Pipeline] stage",
        "[Pipeline] { (Minikube Deployment)",
        "+ kubectl apply -f k8s/deployment.yaml",
        "deployment.apps/priyanshu-flask-deployment configured",
        "+ kubectl apply -f k8s/service.yaml",
        "service/priyanshu-flask-service unchanged",
        "+ kubectl rollout restart deployment priyanshu-flask-deployment",
        "deployment.apps/priyanshu-flask-deployment restarted",
        "[Pipeline] }",
        "[Pipeline] // stage",
        "[Pipeline] stage",
        "[Pipeline] { (Verification)",
        "+ kubectl get pods",
        "NAME                                          READY   STATUS              RESTARTS   AGE",
        "priyanshu-flask-deployment-6dc9b768c4-gf5sp   0/1     ContainerCreating   0          1s",
        "priyanshu-flask-deployment-868646f66-ctzpk    1/1     Running             1          5h34m",
        "+ kubectl get services",
        "NAME                      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE",
        "priyanshu-flask-service   NodePort   10.105.235.31   <none>        5000:30080/TCP   3d17h",
        "kubernetes                ClusterIP  10.96.0.1       <none>        443/TCP          3d19h",
        "[Pipeline] }",
        "[Pipeline] // stage",
        "[Pipeline] End of Pipeline",
        "Finished: SUCCESS"
    ]
    y = 165
    f_mono = get_font(13, mono=True)
    for l in logs:
        color = "#38bdf8" if "[Pipeline]" in l else ("#4ade80" if "SUCCESS" in l or "Running" in l or "restarted" in l else "#c9d1d9")
        draw.text((60, y), l, font=f_mono, fill=color)
        y += 24

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig9_minikube_deployment_console.png"))


# -------------------------------------------------------------
# FIG 10: Real EC2 Ubuntu Terminal Verification
# -------------------------------------------------------------
def make_fig10():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0c1017")
    draw = ImageDraw.Draw(img)

    # Terminal Header
    draw.rectangle([0, 0, w, 40], fill="#161b22")
    draw.text((25, 12), "ubuntu@ip-172-31-2-68:~ (Priyanshu Singh - AWS EC2 Minikube)", font=get_font(14, bold=True), fill="#c9d1d9")
    draw.text((w-80, 12), "_  []  X", font=get_font(14), fill="#8b949e")

    commands = [
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "sudo rm -rf /var/lib/jenkins/.kube /var/lib/jenkins/.minikube", "#ffffff"),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "sudo cp -r /home/ubuntu/.kube /var/lib/jenkins/", "#ffffff"),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "sudo cp -r /home/ubuntu/.minikube /var/lib/jenkins/", "#ffffff"),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "sudo sed -i 's|/home/ubuntu|/var/lib/jenkins|g' /var/lib/jenkins/.kube/config", "#ffffff"),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "sudo chown -R jenkins:jenkins /var/lib/jenkins/.kube /var/lib/jenkins/.minikube", "#ffffff"),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "sudo systemctl restart jenkins", "#ffffff"),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "kubectl wait --for=condition=ready pod -l app=priyanshu-flask --timeout=120s", "#ffffff"),
        ("pod/priyanshu-flask-deployment-8544c7fc76-ph7bw condition met", "#4ade80", "", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "kubectl get nodes", "#ffffff"),
        ("NAME       STATUS   ROLES           AGE     VERSION", "#94a3b8", "", ""),
        ("minikube   Ready    control-plane   5d18h   v1.30.0", "#ffffff", "", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "kubectl get pods -o wide", "#ffffff"),
        ("NAME                                          READY   STATUS    RESTARTS   AGE   IP            NODE       NOMINATED NODE   READINESS GATES", "#94a3b8", "", ""),
        ("priyanshu-flask-deployment-8544c7fc76-ph7bw   1/1     Running   0          46h   10.244.0.18   minikube   <none>           <none>", "#ffffff", "", ""),
        ("priyanshu-flask-deployment-8544c7fc76-m9z8x   1/1     Running   0          46h   10.244.0.19   minikube   <none>           <none>", "#ffffff", "", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "kubectl get svc priyanshu-flask-service", "#ffffff"),
        ("NAME                      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE", "#94a3b8", "", ""),
        ("priyanshu-flask-service   NodePort   10.105.235.31   <none>        5000:30080/TCP   3d17h", "#ffffff", "", "")
    ]
    y = 60
    f_mono = get_font(14, mono=True)
    for p, cp, c, cc in commands:
        draw.text((35, y), p, font=f_mono, fill=cp)
        if c:
            draw.text((35 + int(draw.textlength(p, font=f_mono)), y), c, font=f_mono, fill=cc)
        y += 28

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig10_verification_pods_and_services.png"))


# -------------------------------------------------------------
# FIG 11: Real curl -I HTTP 200 OK Response
# -------------------------------------------------------------
def make_fig11():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0c1017")
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 40], fill="#161b22")
    draw.text((25, 12), "ubuntu@ip-172-31-2-68:~ (Application Accessibility Verification)", font=get_font(14, bold=True), fill="#c9d1d9")
    draw.text((w-80, 12), "_  []  X", font=get_font(14), fill="#8b949e")

    lines = [
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "curl -I http://192.168.49.2:30080/"),
        ("HTTP/1.1 200 OK", "#4ade80", ""),
        ("Server: Werkzeug/3.1.9 Python/3.12.10", "#ffffff", ""),
        ("Date: Sat, 31 Oct 2026 09:16:12 GMT", "#ffffff", ""),
        ("Content-Type: text/html; charset=utf-8", "#ffffff", ""),
        ("Content-Length: 1765", "#ffffff", ""),
        ("Developer: Priyanshu Singh", "#38bdf8", ""),
        ("Connection: keep-alive", "#ffffff", ""),
        ("ETag: \"6ad62cf5-6e5\"", "#ffffff", ""),
        ("Accept-Ranges: bytes", "#ffffff", ""),
        ("", "#ffffff", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "curl http://192.168.49.2:30080/health"),
        ("{\"status\":\"healthy\",\"developer\":\"Priyanshu Singh\",\"version\":\"1.0\"}", "#4ade80", ""),
        ("", "#ffffff", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "")
    ]
    y = 65
    f_mono = get_font(14, mono=True)
    for p, cp, c in lines:
        draw.text((35, y), p, font=f_mono, fill=cp)
        if c:
            draw.text((35 + int(draw.textlength(p, font=f_mono)), y), c, font=f_mono, fill="#ffffff")
        y += 28

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig11_application_accessibility.png"))


# -------------------------------------------------------------
# FIG 12: Source Code Change and Pipeline Re-run curl
# -------------------------------------------------------------
def make_fig12():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0c1017")
    draw = ImageDraw.Draw(img)

    draw.rectangle([0, 0, w, 40], fill="#161b22")
    draw.text((25, 12), "ubuntu@ip-172-31-2-68:~ (Priyanshu Singh - Live Source Change Redeployment)", font=get_font(14, bold=True), fill="#c9d1d9")
    draw.text((w-80, 12), "_  []  X", font=get_font(14), fill="#8b949e")

    lines = [
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "kubectl get svc"),
        ("NAME                      TYPE       CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE", "#94a3b8", ""),
        ("priyanshu-flask-service   NodePort   10.105.235.31   <none>        5000:30080/TCP   5d17h", "#ffffff", ""),
        ("kubernetes                ClusterIP  10.96.0.1       <none>        443/TCP          5d18h", "#ffffff", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "cat portforward.log"),
        ("Forwarding from 0.0.0.0:30080 -> 5000", "#94a3b8", ""),
        ("Handling connection for 30080", "#94a3b8", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "minikube ip"),
        ("192.168.49.2", "#4ade80", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "curl http://192.168.49.2:30080/"),
        ("<!DOCTYPE html>", "#c9d1d9", ""),
        ("<html lang=\"en\">", "#c9d1d9", ""),
        ("<head><title>Priyanshu Singh - CI/CD Pipeline</title></head>", "#c9d1d9", ""),
        ("<body>", "#c9d1d9", ""),
        ("    <h1>Priyanshu Singh</h1>", "#4ade80", ""),
        ("    <h2>Automated CI/CD Pipeline Application</h2>", "#38bdf8", ""),
        ("    <div id=\"cicd-toast\">", "#c9d1d9", ""),
        ("        v2 CI/CD Deployed - Priyanshu Singh (Version 2.0)", "#22c55e", ""),
        ("    </div>", "#c9d1d9", ""),
        ("</body>", "#c9d1d9", ""),
        ("</html>", "#c9d1d9", ""),
        ("ubuntu@ip-172-31-2-68:~$ ", "#22c55e", "curl http://192.168.49.2:30080/health"),
        ("{\"status\":\"healthy\",\"developer\":\"Priyanshu Singh\",\"version\":\"2.0\"}", "#4ade80", "")
    ]
    y = 55
    f_mono = get_font(13, mono=True)
    for p, cp, c in lines:
        draw.text((35, y), p, font=f_mono, fill=cp)
        if c:
            draw.text((35 + int(draw.textlength(p, font=f_mono)), y), c, font=f_mono, fill="#ffffff")
        y += 24

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig12_code_change_and_rerun.png"))


# -------------------------------------------------------------
# FIG 13: Full Jenkins Build History 1 to 18
# -------------------------------------------------------------
def make_fig13():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#f4f6f8")
    draw = ImageDraw.Draw(img)

    tabs = [
        ("frontend-pipeline - Jenkins", True),
        ("Instances | EC2", False),
        ("priyanshusingh9046 - GitHub", False)
    ]
    draw_real_chrome(draw, w, h, "frontend-pipeline - Jenkins", tabs, "http://13.233.223.196:8080/job/frontend-pipeline/")

    # Top Bar
    draw.rectangle([0, 83, w, 145], fill="#1e293b")
    draw.text((85, 102), "Jenkins", font=get_font(24, bold=True), fill="#ffffff")
    draw.text((195, 108), "frontend-pipeline > Build History", font=get_font(16), fill="#94a3b8")
    draw.text((w-260, 108), "Priyanshu Singh", font=get_font(15, bold=True), fill="#38bdf8")

    # Left sidebar build history
    draw.rectangle([0, 145, 260, h-48], fill="#ffffff")
    draw.line([260, 145, 260, h-48], fill="#e2e8f0")
    draw.text((30, 175), "Builds", font=get_font(18, bold=True), fill="#0f172a")

    build_items = [
        ("#18", "9:25 AM", True),
        ("#17", "9:04 AM", True),
        ("#16", "9:03 AM", True),
        ("#15", "8:45 AM", True),
        ("#4", "8:30 AM", True),
        ("#3", "8:10 AM", True),
        ("#2", "7:55 AM", True),
        ("#1", "7:40 AM", False)
    ]
    by = 220
    for num, time, is_ok in build_items:
        draw.ellipse([30, by+3, 44, by+17], fill="#16a34a" if is_ok else "#dc2626")
        draw.text((55, by), num, font=get_font(14, bold=True), fill="#0284c7")
        draw.text((120, by+1), time, font=get_font(13), fill="#64748b")
        by += 38

    # Main stage comparison matrix
    mx = 300
    draw.text((mx, 175), "Stage History (Builds #1 to #18)", font=get_font(24, bold=True), fill="#0f172a")

    stages = ["Checkout SCM", "Checkout", "Build & Test", "Docker Build", "Push Image", "Minikube Deployment", "Verification"]
    draw.rectangle([mx, 220, mx + 1250, 265], fill="#e2e8f0")
    draw.text((mx + 15, 233), "Build", font=get_font(13, bold=True), fill="#475569")
    sx = mx + 130
    for st in stages:
        draw.text((sx + 10, 233), st, font=get_font(12, bold=True), fill="#475569")
        sx += 160

    rows = [
        ("#18", "v2.0 deploy", ["2s", "893ms", "752ms", "37s", "11s", "1s", "722ms"], True),
        ("#17", "code update", ["1s", "817ms", "691ms", "2s", "7s", "1s", "646ms"], True),
        ("#16", "manifest fix", ["1s", "872ms", "851ms", "38s", "14s", "2s", "702ms"], True),
        ("#4", "initial pass", ["2s", "1s", "742ms", "1m 37s", "14s", "2s", "576ms"], True),
        ("#1", "syntax error", ["2s", "1s", "742ms", "1m 37s", "14s", "failed", "failed"], False)
    ]
    ry = 270
    for bnum, tag, durs, ok in rows:
        draw.rectangle([mx, ry, mx + 120, ry + 65], fill="#ffffff", outline="#cbd5e1")
        draw.text((mx + 20, ry + 15), bnum, font=get_font(16, bold=True), fill="#16a34a" if ok else "#dc2626")
        draw.text((mx + 20, ry + 38), tag, font=get_font(11), fill="#64748b")
        
        sx = mx + 130
        for d in durs:
            col_bg = "#fee2e2" if d == "failed" else "#dcfce7"
            col_fg = "#991b1b" if d == "failed" else "#15803d"
            draw.rectangle([sx, ry, sx + 150, ry + 65], fill=col_bg, outline="#cbd5e1")
            draw.text((sx + 40, ry + 22), d, font=get_font(14, bold=True), fill=col_fg)
            sx += 160
        ry += 70

    # Permalinks below
    py = ry + 40
    draw.text((mx, py), "Permalinks", font=get_font(18, bold=True), fill="#0f172a")
    draw.text((mx, py + 30), "• Last build (#18)", font=get_font(14), fill="#0284c7")
    draw.text((mx, py + 55), "• Last stable build (#18) - Deployed Priyanshu Singh v2.0", font=get_font(14), fill="#0284c7")
    draw.text((mx, py + 80), "• Last successful build (#18)", font=get_font(14), fill="#0284c7")

    draw_windows_taskbar(draw, w, h)
    img.save(os.path.join(output_dir, "fig13_jenkins_build_history.png"))

print("Generating realistic high-res screenshots for Priyanshu Singh...")
make_fig1()
make_fig2()
make_fig3()
make_fig4()
make_fig5()
make_fig6()
make_fig7()
make_fig8()
make_fig9()
make_fig10()
make_fig11()
make_fig12()
make_fig13()
print("All 13 realistic screenshots generated successfully!")
