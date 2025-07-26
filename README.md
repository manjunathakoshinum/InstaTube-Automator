
````markdown
# 🚀 InstaTube-Automator  
**Automated Instagram-to-YouTube Publishing with Precision, Intelligence & Zero Manual Work**

> _This project is my proof of belief. Built out of passion, not pressure. Automation is not just what I do — it’s how I think._

## 📚 Table of Contents

- [🧠 Why](#-why)
- [⚙️ How It Works](#️-how-it-works)
- [🛠️ What's Inside](#-whats-inside)
- [✨ Features](#-features)
- [📦 Tech Stack](#-tech-stack)
- [👨‍💻 Author's Note](#-authors-note)
- [📛 Legal & Disclaimer](#-legal--disclaimer)
- [📺 Demo Channel](#-demo-channel)
- [📩 Contact](#-contact)
- [📄 License](#-license)


## 🧠 Why

In a world overflowing with content, creators waste hours on repetitive tasks —  
downloading, renaming, uploading, rewriting descriptions, managing metadata... again and again.

I didn’t build this for a resume.  
I built it because I **couldn’t resist the challenge**.

I love automation. I love building systems that remove friction, save time, and scale like magic.  
That love drove me through **6+ months** of late nights, debugging, refactoring, and refining — not because someone asked me to, but because it felt right.

This isn’t just code.  
This is a **belief system**:

- That a solo developer can build tools as powerful as a team  
- That real engineering solves real-world chaos  
- That curiosity, when paired with structure, becomes pure power  

---



## ⚙️ How It Works

`InstaTube-Automator` is a **modular automation system** that connects Instagram and YouTube through intelligent workflows.

### 🔁 What it does:

- 📥 Downloads reels from Instagram (filtered by category, views, time)
- 🧠 Auto-generates **titles, descriptions, and tags** if missing
- 🚀 Uploads videos to YouTube using Selenium (title, thumbnail, age restriction, visibility, etc.)
- 🔄 Supports multiple YouTube channels with **upload limits**, history tracking, and rotation
- 📬 Sends **email notifications** with status updates
- 🧼 Avoids duplicates via hashed logs & session control
- 🧠 Handles metadata quality, browser sessions, and error fallback logic

---


## 🛠️ What's Inside

### 🧾 Major Folders and Responsibilities


```text
📁 cleanup/                    → Removes previously uploaded files
📁 download_upload/           → Downloads Instagram reels using smart configs
📁 preprocessing/             → Auto-generates metadata (title, tags, description)
📁 upload_to_youtube/         → Handles full YouTube upload via Selenium
📁 youtube_channels/          → Multi-channel management, configs, and logs
📄 main.py                    → Main orchestrator
📄 instagram_download.py      → Standalone downloader
📄 notification_via_mail.py   → Sends channel status via email
````


### 📂 Full Project Structure

```text
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
│   └── youtube_uploading.py
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
│   │       └── video_files_path.json
│   └── channel_selection.py
│       ├── check_upload_policy.py
│       └── copy_file_path.py
│
├── main.py
├── instagram_download.py
├── notification_via_mail.py
├── requirements.txt
├── LICENSE
└── README.md
```


---


## ✨ Features

* ✅ Intelligent, structured automation (not just scripting)
* ✅ Real-time email notifications
* ✅ Seamless multi-channel upload support
* ✅ Category-based video download filtering
* ✅ Metadata generation and validation pipeline
* ✅ History logs to prevent duplicates
* ✅ JSON-based configurations for flexibility
* ✅ Selenium-powered, human-like browser interaction

---


## 📦 Tech Stack

* **Python 3.x**
* **Selenium + Firefox + Geckodriver**
* **Instaloader**
* **Pillow, Requests, SMTP**
* **JSON-based state/config management**

---


## 👨‍💻 Author's Note

This isn’t just an automation tool.
It’s a reflection of **how I think**:

* I see a broken process → I fix it
* I see friction → I remove it
* I see repetition → I automate it

This project represents:

* 🧠 My belief in deep work
* 🔧 My love for thoughtful system design
* 🚀 My obsession with solving real inefficiencies

> I don’t just code to get a job.
> I code to express myself.
> I code to build things that **think**.





## 📛 Legal & Disclaimer

> ⚠️ This project is intended strictly for **educational, personal, and non-commercial** use.

**By using this code, you agree to the following:**

- 📌 This tool interacts with **Instagram and YouTube**, which have strict **Terms of Service** regarding automation, scraping, and bot usage.
- ❌ **Unauthorized automation may violate** their terms and can lead to **temporary/permanent bans** of user accounts or channels.
- ⚠️ **The author does NOT take responsibility** for:
  - Account suspension or termination
  - Data loss
  - API or browser changes that break functionality
  - Any **financial, reputational, or legal loss** caused by using or modifying this tool

🧪 This project was created solely to:
- Demonstrate technical ability in automation and systems design
- Practice ethical software engineering
- Learn from real-world browser interaction challenges

> 📚 Use this code **only at your own risk**, for learning and sandbox testing.  
> 🚫 Do **not** use it for spamming, scraping unauthorized content, or violating any platform’s policy.

---




## 📺 Demo Channel

Want to see the automation in action?

🎬 **[@disconum on YouTube](https://www.youtube.com/@disconum)**

> These are real videos uploaded using this system. For testing & proof-of-concept only.

---


## 📩 Contact

If you're a developer, recruiter, or creator who shares this mindset — I’d love to connect:

* 📧 Email: [manjunathakoshinum@gmail.com](mailto:manjunathakoshinum@gmail.com)
* 🌐 GitHub: [@manjunathakoshinum](https://github.com/manjunathakoshinum)
* 💼 LinkedIn: [https://www.linkedin.com/in/manjunathah/](https://www.linkedin.com/in/manjunathah/)

---


## 📄 License

Licensed under the [MIT License](LICENSE).

````
