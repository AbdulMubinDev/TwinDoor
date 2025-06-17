
---

# 🚪 TwinDoor – Ethical Windows 11 Backdoor for Red Teaming & Scammer Hunting

**TwinDoor** is a modular, Windows 11-compatible backdoor developed for **ethical red teaming, scammer hunting, CTF labs, malware behavior research, and detection engineering**. It enables security professionals and researchers to simulate real-world adversary techniques in a controlled environment — helping blue teams prepare, threat hunters detect, and reverse engineers learn from realistic adversarial behavior.

> ⚠️ **Disclaimer:**
> TwinDoor is strictly for educational, research, or lawful red team use. Do **not** deploy this on any machine you do not own or have explicit permission to test.

---

## 🎯 Purpose

TwinDoor was born from the real-world need to:

* Educate **junior analysts** on attacker behavior
* Train blue teams in detection and response
* Improve **SOC and EDR/YARA rule development**
* Enable ethical hackers to understand modern Windows backdoor techniques

---

## 🧱 Key Features

| Feature           | Description                                                       |
| ----------------- | ----------------------------------------------------------------- |
| ✅ Reverse Shell   | Connects back to attacker's server and executes commands remotely |
| 📁 File Transfer  | Upload/download files to/from victim machine                      |
| 🎹 Keylogger      | Stealth capture of keystrokes using `pynput`                      |
| 🔒 AES Encryption | Encrypted communication to bypass string scanners                 |
| 🔁 Persistence    | Survives reboot via Registry or Task Scheduler                    |
| 🎭 Anti-Analysis  | Optional obfuscation, hidden window, and self-deletion mode       |
| 🧩 Modular Design | Clean separation of logic for easy extension and customization    |

---

## 🖥️ Target Environment

| Attribute    | Details                                       |
| ------------ | --------------------------------------------- |
| OS           | Windows 11 (Tested on 22H2, also works on 10) |
| Architecture | x64 recommended (x86 compatible)              |
| Privileges   | Admin NOT required for core features          |

---

## 🔐 Ethical Use Cases

* 🧪 Simulate adversary behavior in research labs
* 🧠 Train SOC analysts and threat hunters
* 🔎 Build and test EDR/YARA/AV detection signatures
* 🛠 Red Team post-exploitation toolkit development
* ⚔️ Assist in **scammer detection and takedown** workflows

---

## 📁 Example Folder Structure

```
twindoor/
├── client/
│   ├── backdoor.py           # Main reverse shell & logic
│   ├── keylogger.py          # Keylogging module
│   ├── persistence.py        # Registry/Task Scheduler setup
│   ├── crypto.py             # AES/XOR encryption
├── server/
│   ├── control_panel.py      # Listener & command handler
├── utils/
│   ├── obfuscator.py         # Obfuscation, string encryption
├── README.md
├── LICENSE
```

---

## ⚙️ Technologies Used

* `Python 3.x`
* `socket`, `subprocess`, `threading`, `os`, `winreg`
* `pynput`, `cryptography`, `base64`
* Tools like `pyinstaller`, `nuitka`, `auto-py-to-exe` for `.exe` generation

---

## 🧪 Testing Recommendations

* Always test in:

  * 🧱 Isolated **VM environments** (VirtualBox/VMware)
  * 💻 Windows 11 (preferably clean snapshots)
  * 🔍 Monitoring tools: `ProcMon`, `Wireshark`, `Sysmon`, `Splunk`, etc.
* NEVER upload builds to public virus scanners

---

## 📜 Licensing & Contribution

> TwinDoor is an **educational open-source project**. Contributions to expand modules or improve stealth/opsec are welcome — as long as the intent aligns with ethical use cases like scammer defense, red teaming, and research.

---
