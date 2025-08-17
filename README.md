# ChatbotProject
# 🤖 Intelligent Terminal Chatbot with Ollama Integration

A sophisticated terminal-based AI chatbot built with Ollama, capable of engaging conversations in both Turkish and English on history, arts, and cinema topics.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Ollama](https://img.shields.io/badge/ollama-v0.11+-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- *🔍 Smart Language Detection*: Automatically detects input language and responds accordingly
- *📚 Multi-Domain Expertise*: Specialized in history, arts, and cinema topics
- *🛡 Robust Error Handling*: Advanced error catching and recovery system
- *🎨 User-Friendly Interface*: Clean and intuitive terminal interface
- *🏠 Offline AI*: Runs completely offline without internet dependency
- *⚡ Fast Response*: Optimized for quick local AI inference

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Ollama installed on your system

### Installation

1. *Clone the repository:*
bash
git clone https://github.com/username/terminal-chatbot-ollama.git
cd terminal-chatbot-ollama


2. *Install Ollama:*
bash
# Windows
winget install Ollama.Ollama

# macOS  
brew install ollama

# Linux
curl -fsSL https://ollama.com/install.sh | sh


3. *Download the AI model:*
bash
ollama pull gemma:2b


4. *Run the chatbot:*
bash
python chatbot.py


## 💬 Usage Examples

### English Conversation

You: Who was Van Gogh?
Bot: Vincent van Gogh was a Dutch post-impressionist painter from the 19th century, known for his vibrant colors and emotional brushwork...

You: What is the Mona Lisa painting about?
Bot: The Mona Lisa is a portrait painting by Leonardo da Vinci, famous for the subject's enigmatic smile...


### Turkish Conversation

You: Van Gogh kimdir?
Bot: Van Gogh, 19. yüzyıldan kalma Hollandalı post-empresyonist bir ressam olup, canlı renkleri ve duygusal fırça darbeleriyle tanınır...

You: Mona Lisa tablosu nedir?
Bot: Mona Lisa, Leonardo da Vinci'nin yaptığı bir portre resmidir ve öznenin gizemli gülümsemesiyle ünlüdür...


### Exiting the Program

You: quit
Bot: Goodbye! 👋


## 🛠 Technical Architecture

### Language Detection Algorithm
The chatbot implements an intelligent language detection system:

python
def detect_language(message):
    # Turkish character detection
    turkish_chars = ['ç', 'ğ', 'ı', 'ş', 'ü', 'ö']
    # Turkish question words
    turkish_words = ['ne', 'nedir', 'kimdir', 'nasıl', 'nerede', 'ne zaman']
    
    is_turkish = (
        any(char in message.lower() for char in turkish_chars) or
        any(word in message.lower() for word in turkish_words)
    )
    
    return "turkish" if is_turkish else "english"


### Core Components

- *Connection Handler*: Tests and maintains Ollama connectivity
- *Language Processor*: Detects input language and formats prompts
- *Response Manager*: Handles AI model responses and error recovery
- *Interface Controller*: Manages user interaction and terminal display

### AI Model Specifications
- *Model*: Google Gemma 2B
- *Size*: ~1.7GB
- *Performance*: 3-8 seconds response time
- *Memory Usage*: ~2GB RAM
- *Offline Capability*: Full offline operation

## 🔧 Development Journey

This project evolved through several iterations, addressing key technical challenges:

### Challenge 1: Unicode Encoding Issues
*Problem*: Windows charset incompatibility with UTF-8 characters
python
UnicodeDecodeError: 'charmap' codec can't decode byte 0x8f in position 332

*Solution*: Implemented comprehensive encoding handling
python
result = subprocess.run(
    [...],
    encoding='utf-8',
    errors='ignore'
)
# Windows charset configuration
os.system('chcp 65001 >nul 2>&1')


### Challenge 2: Subprocess Timeout Management
*Problem*: AI model occasionally freezing without response
*Solution*: Added timeout protection and graceful degradation
python
result = subprocess.run([...], timeout=30)


### Challenge 3: Inconsistent Language Responses
*Problem*: Mixed language responses despite clear input language
*Solution*: Developed smart language detection and prompt engineering

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| Cold Start Time | ~2 seconds |
| Average Response Time | 3-8 seconds |
| Memory Footprint | ~2GB (including model) |
| CPU Usage | Moderate during inference |
| Supported Languages | Turkish, English |
| Topics Covered | History, Arts, Cinema |

## 🧪 Testing

### Automated Tests
bash
# Run basic functionality tests
python -m pytest tests/

# Test language detection
python tests/test_language_detection.py

# Performance benchmarks
python tests/benchmark.py


### Manual Testing Scenarios
- Turkish questions with special characters
- English questions with complex grammar
- Mixed language conversations
- Error recovery scenarios
- Timeout handling

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. *Fork the repository*
2. *Create a feature branch*
   bash
   git checkout -b feature/amazing-feature
   
3. *Commit your changes*
   bash
   git commit -m 'Add amazing feature'
   
4. *Push to the branch*
   bash
   git push origin feature/amazing-feature
   
5. *Open a Pull Request*

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comprehensive docstrings
- Include unit tests for new features
- Update documentation as needed

## 🗺 Roadmap

- [ ] *GUI Interface*: Desktop application with modern UI
- [ ] *Conversation Memory*: Persistent chat history
- [ ] *Multi-Model Support*: Integration with additional AI models
- [ ] *Web API*: RESTful API for external integrations
- [ ] *Docker Support*: Containerized deployment
- [ ] *Plugin System*: Extensible architecture for custom features
- [ ] *Voice Integration*: Speech-to-text and text-to-speech capabilities

## 📋 System Requirements

### Minimum Requirements
- *OS*: Windows 10, macOS 10.14, or Linux (Ubuntu 18.04+)
- *RAM*: 4GB (8GB recommended)
- *Storage*: 3GB free space
- *Python*: 3.8+

### Recommended Requirements
- *RAM*: 8GB or more
- *CPU*: Multi-core processor
- *Storage*: SSD for faster model loading

## 🔒 Security Considerations

- *Local Processing*: All data processed locally, no external API calls
- *No Data Collection*: Conversations are not stored or transmitted
- *Sandboxed Execution*: AI model runs in isolated environment
- *Input Sanitization*: User inputs are validated and sanitized

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎯 Use Cases

- *Educational Tool*: Interactive learning for history and arts
- *Research Assistant*: Quick fact-checking and information retrieval
- *Language Practice*: Bilingual conversation practice
- *Offline AI Demo*: Showcasing local AI capabilities

## 🙏 Acknowledgments

- *[Ollama Team](https://ollama.com/)* - For the excellent local AI platform
- *[Google AI](https://ai.google.dev/gemma)* - For the Gemma model
- *Python Community* - For the robust ecosystem
- *Contributors* - For their valuable contributions

## 📞 Support

Having issues? Here are some resources:

- *Documentation*: Check our [Wiki](https://github.com/username/terminal-chatbot-ollama/wiki)
- *Issues*: Report bugs in [Issues](https://github.com/username/terminal-chatbot-ollama/issues)
- *Discussions*: Join [Discussions](https://github.com/username/terminal-chatbot-ollama/discussions)

## 📈 Stats

![GitHub stars](https://img.shields.io/github/stars/username/terminal-chatbot-ollama?style=social)
![GitHub forks](https://img.shields.io/github/forks/username/terminal-chatbot-ollama?style=social)
![GitHub issues](https://img.shields.io/github/issues/username/terminal-chatbot-ollama)
![GitHub pull requests](https://img.shields.io/github/issues-pr/username/terminal-chatbot-ollama)

---

⭐ *Star this repository if you found it helpful!*

Made with ❤ by developers who believe in the power of local AI.
