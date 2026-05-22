# 📸 AI-Powered Image Database Search Engine (Simple Demo) 🚀

Hello there! 👋 Welcome to my personal project! ❤️ Welcome to this smart image database search engine. I'm so excited to share this with you! Check out how we can find images using just plain natural language! 🌟

---

## 📌 Project Overview & Disclaimer

This is a **personal project** designed to build a multimodal image search engine. 

> ⚠️ **Important Disclaimer:** > The AI model used in this project (`jinaai/jina-clip-v2`) is introduced from an **outside source** (Jina AI) and was **NOT made by me**. I did **NOT fine-tune** this model; it is directly used out-of-the-box to leverage its powerful pre-trained multimodal embedding capabilities. 

---

## 🛠️ Prerequisites & Installation

Before running the project, you need to set up your environment in your VS Code terminal.

### 1. 📂 Prepare Your Image Dataset
Please note that you **must prepare your own image sets**. 
* Create a folder named `images` in the root directory.
* Put all your target images inside the `images` folder.

### 2. 💻 Install Necessary Libraries
Open your VS Code terminal and run the following command to install all the required libraries (including `QdrantClient`, `SentenceTransformer`, `torch`, etc.):

```bash
pip install qdrant-client sentence-transformers torch pillow tqdm
```

# 📸 Demonstration
## 💡 Note: All the images used in the following demonstration below were taken by myself.

1️⃣ Step 1: Query Input
"animal"
Here is what it looks like when typing the search query in the command line terminal:
<img width="1169" height="122" alt="螢幕擷取畫面 2026-04-29 235825" src="https://github.com/user-attachments/assets/009aa948-af58-4bc7-a8d0-2a9ae1debb04" />

2️⃣ Step 2: Search Results
Based on the text query, the system instantly matches the most relevant photos from our database:

🥇 Top 1 Result:
A cow on the road

<img width="440" height="423" alt="iedemo1" src="https://github.com/user-attachments/assets/d8a38247-765e-44ab-b7af-d3b0fb005009" />

🥈 Top 2 Result:
A dog in the mall

<img width="396" height="422" alt="iedemo2" src="https://github.com/user-attachments/assets/8adf3f50-15c2-4e2b-aba7-3d9d5e857378" />

🥉 Top 3 Result:
Mud and rocks !? 😓 Alright, AI consider it as animal~ nvm

<img width="436" height="427" alt="iedemo3" src="https://github.com/user-attachments/assets/42a37fa1-71a1-4300-a407-0ab0829041b7" />

## 📝 License & Usage
🎓 This project is intended and should only be used for educational purposes. Feel free to clone, study, and play around with the code!
🌟 Remember: Keep learning, keep coding, and let's make things smarter every day! 😉
