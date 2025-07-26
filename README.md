# 🚀 InstaTube-Automator  
**Automated Instagram-to-YouTube Publishing with Precision, Intelligence & Zero Manual Work**
 
> This project is my proof of belief. Love and passion for coding . Built because I had to.

---

## 🧠 Why

In a world overflowing with content, creators waste hours on repetitive tasks —  
downloading, renaming, uploading, rewriting descriptions, managing metadata... again and again.

I didn’t build this project for a resume or an interview.  
I built it because I **couldn’t resist the challenge**.

I love automation. I love thinking like a system and building tools that remove friction, save time, and scale like magic.  
That love drove me through **6 months** of late nights, debugging, refactoring, and versioning — not because someone asked me to, but because it felt right.

This isn’t just code.  
This is a **belief system**:

- That a solo developer can build tools as powerful as a team  
- That real engineering solves real-life chaos  
- That curiosity, when combined with structure, creates pure power  

This project is proof of that belief.

---

## ⚙️ How

`InstaTube-Automator` is a **modular automation system** that connects Instagram and YouTube through intelligent workflows.

### It:
- 📥 Downloads trending reels from Instagram (category-specific configs)
- 🧠 Auto-generates **titles, descriptions, and tags** if missing
- 🚀 Uploads videos to YouTube via **Selenium** (handles titles, age restriction, visibility, tags, thumbnails)
- 🔁 Switches across **multiple YouTube channels**, tracks daily limits and upload history
- 📬 Sends **email notifications** (success/failure/status)
- 🧼 Prevents duplicates using hashed logs and download state
- 🔐 Manages sessions, rate limits, and broken metadata gracefully

---

## 🛠️ What’s Inside

```text
📁 download_upload/            → Instagram reel downloads with config/session control  
📁 preprocessing/              → Smart metadata generation (title, tags, description)  
📁 upload_to_youtube/          → YouTube upload automation (via Selenium)  
📁 youtube_channels/           → Channel config, limits, logs, and selection  
📁 cleanup/                    → Cleanup logic for uploaded/processed videos  
📄 main.py                     → Automation orchestrator  
📄 notification_via_mail.py    → SMTP email notification system

📁 Repository Structure

automated-youtube-upload/
│
├── cleanup/
│   └── delete_uploaded_files.py
│
├── download_upload/
│   ├── categories.json
│   ├── instagram_download.py
│   ├── download_check.py
│   ├── move_video_files.py
│   ├── instaloader_session/
│
├── preprocessing/
│   ├── duration.py
│   ├── get_description.py
│   ├── get_tags.py
│   ├── get_title.py
│   ├── get_video_text_image_file.py
│   ├── preprocessing.py
│   └── title_description_tags.py
│
├── upload_to_youtube/
│   ├── youtube_details.py
│   ├── youtube_uploading.py
│
├── youtube_channels/
│   ├── categories/
│   │   ├── memes/
│   │   ├── nature/
│   │   └── ...
│   ├── channels/
│   │   └── channel_management/
│   │       ├── description.json
│   │       ├── hashtags.json
│   │       ├── download_config.json
│   │       ├── downloaded_links.json
│   │       ├── video_files_path.json
│   └── channel_selection.py
│       ├── check_upload_policy.py
│       ├── copy_file_path.py
│
├── main.py
├── instagram_download.py
├── notification_via_mail.py
├── requirements.txt
├── LICENSE
└── README.md

✨ Features
✅ Intelligent automation, not just scripting

✅ Real-time email updates

✅ Multi-channel YouTube management

✅ Category-based content filtering

✅ Full Selenium automation with session handling

✅ Configurable JSON logic

✅ Duplicate prevention with history logs

✅ Seamless scaling with modular design

📦 Stack
Python 3.x

Selenium + Firefox + Geckodriver

Instaloader

JSON-based state and config management

Pillow, Requests, SMTP (for email delivery)

👨‍💻 Author’s Note
This isn’t just an automation tool.
It’s a reflection of how I think:

I see a broken process → I fix it

I see friction → I remove it

I see repetition → I automate it

This project represents:

🧠 My belief in deep work

🔧 My love for system design

🚀 My obsession with solving real-life inefficiencies


I code to express myself.
I code to build things that think.

🔒 Disclaimer
⚠️ This project was built strictly for learning, personal testing, and technical skill development.

❌ Not made for making money

✅ Built to showcase deep automation and engineering practice

📹 Videos used were for testing/demo purposes only — not reused, republished, or monetized

✅ Uploads done ethically, following fair-use and automation constraints

⚠️ No copyrighted or commercial use

This is a passion project, not a product. A proof of concept, not a content farm.

📺 Demo Channel
You can see proof of the system’s output (videos uploaded through this project) on my test/demo YouTube channel:

🎬 @disconum on YouTube
https://www.youtube.com/@disconum/


📩 Contact
If you're a developer, recruiter, or creator who shares this passion — feel free to reach out.

📧 Email: manjunathakoshinum@gmail.com

🌐 GitHub: @manjunathakoshinum

💼 LinkedIn: https://www.linkedin.com/in/manjunathah/
