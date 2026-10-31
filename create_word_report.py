import os
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

doc = Document()

# Set standard margins (0.75 in)
for section in doc.sections:
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.75)
    section.right_margin = Inches(0.75)

# Styling Helper
def set_cell_background(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), hex_color)
    tcPr.append(shd)

# Title
title_p = doc.add_paragraph()
title_p.paragraph_format.space_before = Pt(0)
title_p.paragraph_format.space_after = Pt(2)
run_title = title_p.add_run("CCA 2")
run_title.font.name = "Calibri"
run_title.font.size = Pt(20)
run_title.font.bold = True
run_title.font.color.rgb = RGBColor(17, 24, 39)

sub_p = doc.add_paragraph()
sub_p.paragraph_format.space_before = Pt(0)
sub_p.paragraph_format.space_after = Pt(12)
run_sub = sub_p.add_run("CI/CD Pipeline Implementation and Deployment of an Existing Project")
run_sub.font.name = "Calibri"
run_sub.font.size = Pt(13)
run_sub.font.bold = True
run_sub.font.color.rgb = RGBColor(55, 65, 81)

# Student Info Table
info_data = [
    ("Student", "Priyanshu Singh"),
    ("PRN / Division", "1262240182 / G"),
    ("Course", "TYCSE: Cloud Computing and DevOps"),
    ("Project", "Automated Flask CI/CD Web Application"),
    ("GitHub repository URL", "https://github.com/priyanshusingh9046/priyanshu-flask-k8s"),
    ("Branch", "main"),
    ("Jenkins job", "frontend-pipeline"),
    ("Container registry", "Docker Hub: priyanshusingh9046/priyanshu-flask-k8s"),
    ("Deployment", "Minikube on AWS EC2 (Ubuntu 22.04 LTS, Mumbai ap-south-1)")
]

t1 = doc.add_table(rows=len(info_data), cols=2)
t1.alignment = WD_TABLE_ALIGNMENT.CENTER
t1.autofit = False

for i, (k, v) in enumerate(info_data):
    row = t1.rows[i]
    cell_k, cell_v = row.cells[0], row.cells[1]
    cell_k.width = Inches(2.3)
    cell_v.width = Inches(4.7)
    
    pk = cell_k.paragraphs[0]
    pk.paragraph_format.space_after = Pt(2)
    pk.paragraph_format.space_before = Pt(2)
    rk = pk.add_run(k)
    rk.font.name = "Calibri"
    rk.font.size = Pt(10)
    rk.font.bold = True
    
    pv = cell_v.paragraphs[0]
    pv.paragraph_format.space_after = Pt(2)
    pv.paragraph_format.space_before = Pt(2)
    rv = pv.add_run(v)
    rv.font.name = "Calibri"
    rv.font.size = Pt(10)
    if k == "Student":
        rv.font.bold = True

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Section: Pipeline Overview
h_po = doc.add_paragraph()
h_po.paragraph_format.space_before = Pt(8)
h_po.paragraph_format.space_after = Pt(4)
r_po = h_po.add_run("Pipeline Overview")
r_po.font.name = "Calibri"
r_po.font.size = Pt(14)
r_po.font.bold = True

desc_po = doc.add_paragraph()
desc_po.paragraph_format.space_after = Pt(6)
r_dpo = desc_po.add_run(
    "The Flask application is built, tested, packaged, and deployed automatically. Jenkins, Docker, and Minikube "
    "run on one AWS EC2 server. The table below lists the pipeline stages from CCA 2 and the figure that shows each one."
)
r_dpo.font.name = "Calibri"
r_dpo.font.size = Pt(10.5)

# Pipeline Stages Table
stages_data = [
    ("Stage", "What happens", "Evidence"),
    ("Source Code", "Project, Dockerfile, Jenkinsfile and k8s files are stored in GitHub", "Fig. 1"),
    ("Jenkins Checkout", "Jenkins pulls the latest code from the repository", "Fig. 5"),
    ("Build and Test", "Automated unit tests in test_app.py run and verified", "Fig. 6"),
    ("Docker Build", "Image built from Dockerfile and tagged with the build number", "Fig. 6"),
    ("Push Image", "Image pushed to Docker Hub using credentials stored in Jenkins", "Fig. 4, Fig. 7"),
    ("Minikube Deployment", "Deployment and Service from k8s/ applied, new image rolled out", "Fig. 8, Fig. 9"),
    ("Verification", "Pods, deployment and service checked; application opened", "Fig. 10, Fig. 11"),
    ("Code change re-run", "Source changed, pushed and pipeline run again", "Fig. 12, Fig. 13")
]

t2 = doc.add_table(rows=len(stages_data), cols=3)
t2.alignment = WD_TABLE_ALIGNMENT.CENTER

for i, (c1, c2, c3) in enumerate(stages_data):
    row = t2.rows[i]
    cell1, cell2, cell3 = row.cells[0], row.cells[1], row.cells[2]
    cell1.width = Inches(1.8)
    cell2.width = Inches(4.2)
    cell3.width = Inches(1.0)
    
    is_head = (i == 0)
    for idx, (cell, val) in enumerate([(cell1, c1), (cell2, c2), (cell3, c3)]):
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.space_before = Pt(3)
        r = p.add_run(val)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        if is_head:
            r.font.bold = True
            set_cell_background(cell, "F3F4F6")

doc.add_paragraph().paragraph_format.space_after = Pt(4)

# Files in Repository Section
h_files = doc.add_paragraph()
h_files.paragraph_format.space_before = Pt(8)
h_files.paragraph_format.space_after = Pt(2)
r_hf = h_files.add_run("Files in the Repository")
r_hf.font.name = "Calibri"
r_hf.font.size = Pt(13)
r_hf.font.bold = True

p_files = doc.add_paragraph()
p_files.paragraph_format.space_after = Pt(12)
r_pf = p_files.add_run("Jenkinsfile (repository root), Dockerfile, app.py, test_app.py, requirements.txt, k8s/deployment.yaml, k8s/service.yaml and README.md. All are on the main branch.")
r_pf.font.name = "Calibri"
r_pf.font.size = Pt(10.5)

# Figures List
figures = [
    (1, "Source Code on GitHub", "fig1_github_repo.png", 
     "Fig. 1: Repository priyanshu-flask-k8s on the main branch for priyanshusingh9046, with project source, Dockerfile, Jenkinsfile, and k8s/ folder."),
    
    (2, "AWS Infrastructure", "fig2_aws_ec2.png", 
     "Fig. 2: EC2 instance DevOps-Jenkins-Worker (t3.large, ap-south-1) running with 2/2 status checks passed for Priyanshu Singh. It hosts Jenkins, Docker and Minikube."),
    
    (3, "Jenkins Running on AWS", "fig3_jenkins_dashboard.png", 
     "Fig. 3: Jenkins dashboard served from the EC2 server (port 8080) with the pipeline job frontend-pipeline and its latest successful build."),
    
    (4, "Jenkins Credentials", "fig4_jenkins_credentials.png", 
     "Fig. 4: Jenkins global credentials configured securely for Docker Hub (dockerhub-credentials / priyanshusingh9046) and GitHub token."),
    
    (5, "Pipeline Stage: Jenkins Checkout", "fig5_jenkins_checkout.png", 
     "Fig. 5: Build #18 console. Jenkins obtains the Jenkinsfile from GitHub repository priyanshusingh9046/priyanshu-flask-k8s and checks out the repository."),
    
    (6, "Build, Test and Docker Build Stages", "fig6_build_and_docker_build.png", 
     "Fig. 6: Stage view of build #18. Checkout, Build and Test, Docker Build, Push Image, Minikube Deployment and Verification all passed."),
    
    (7, "Push Image to Docker Hub", "fig7_docker_hub.png", 
     "Fig. 7: Docker Hub repository priyanshusingh9046/priyanshu-flask-k8s with the latest tag and the build-number tags pushed by the pipeline."),
    
    (8, "Kubernetes Deployment Manifest", "fig8_k8s_deployment_manifest.png", 
     "Fig. 8: k8s/deployment.yaml (image from Docker Hub, 2 replicas, container port 5000) committed and pushed to the main branch."),
    
    (9, "Minikube Deployment", "fig9_minikube_deployment_console.png", 
     "Fig. 9: Build #18 console. The Minikube Deployment and Verification stages ran (kubectl get svc shows frontend-pipeline) and the build finished with SUCCESS."),
    
    (10, "Verification: Pods, Deployment and Service", "fig10_verification_pods_and_services.png", 
     "Fig. 10: Pods Running (1/1), deployment available, and the priyanshu-flask-service NodePort service active on port 30080."),
    
    (11, "Application Accessibility", "fig11_application_accessibility.png", 
     "Fig. 11: The application is accessible through the Kubernetes NodePort service at port 30080, serving the web application successfully with HTTP 200 OK."),
    
    (12, "Source Code Change and Pipeline Re-run", "fig12_code_change_and_rerun.png", 
     "Fig. 12: Source code updated to Version 2.0, pushed to GitHub, and pipeline re-run verified via live curl."),
    
    (13, "Jenkins Build History", "fig13_jenkins_build_history.png", 
     "Fig. 13: Builds #1 to #18 of frontend-pipeline. Build #18 successfully deployed the version 2.0 change.")
]

for num, title, img_file, caption in figures:
    doc.add_page_break()
    
    # Heading
    hp = doc.add_paragraph()
    hp.paragraph_format.space_before = Pt(4)
    hp.paragraph_format.space_after = Pt(6)
    hr = hp.add_run(f"{num}. {title}")
    hr.font.name = "Calibri"
    hr.font.size = Pt(14)
    hr.font.bold = True
    hr.font.color.rgb = RGBColor(17, 24, 39)
    
    # Image Table Container (Centered single cell with border)
    img_path = os.path.join(r"c:\Users\Anurag\priyanshu\screenshots", img_file)
    if os.path.exists(img_path):
        t_img = doc.add_table(rows=1, cols=1)
        t_img.alignment = WD_TABLE_ALIGNMENT.CENTER
        c_img = t_img.rows[0].cells[0]
        c_img.width = Inches(7.0)
        p_img = c_img.paragraphs[0]
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(2)
        p_img.paragraph_format.space_after = Pt(2)
        
        # Add picture with 6.8 inch width
        p_img.add_run().add_picture(img_path, width=Inches(6.8))
        
        # Caption below table
        cp = doc.add_paragraph()
        cp.paragraph_format.space_before = Pt(4)
        cp.paragraph_format.space_after = Pt(14)
        cr = cp.add_run(caption)
        cr.font.name = "Calibri"
        cr.font.size = Pt(9.5)
        cr.font.italic = True
        cr.font.color.rgb = RGBColor(75, 85, 99)

# Result Section at the end
doc.add_page_break()
hr_p = doc.add_paragraph()
hr_p.paragraph_format.space_before = Pt(8)
hr_p.paragraph_format.space_after = Pt(6)
rr = hr_p.add_run("Result")
rr.font.name = "Calibri"
rr.font.size = Pt(16)
rr.font.bold = True
rr.font.color.rgb = RGBColor(17, 24, 39)

rp = doc.add_paragraph()
rp.paragraph_format.space_after = Pt(8)
rr_desc = rp.add_run(
    "A CI/CD pipeline was implemented for the Frontend-Pipeline using GitHub, Jenkins, Docker, Docker Hub, "
    "Kubernetes and Minikube on AWS EC2. Every push can be built, tested, packaged and deployed automatically, "
    "and the source-code change was verified as a new version running in Minikube."
)
rr_desc.font.name = "Calibri"
rr_desc.font.size = Pt(11)

out_docx = r"c:\Users\Anurag\priyanshu\CCA2_Submission_Priyanshu_Singh.docx"
doc.save(out_docx)
print(f"Successfully saved clean report to {out_docx}")
