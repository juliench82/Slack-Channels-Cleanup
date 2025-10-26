# Slack Channels Cleanup Tool 🧹

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![IT Automation](https://img.shields.io/badge/Category-IT%20Automation-orange.svg)](#)

> **Enterprise Slack workspace management tool for automated cleanup of deprecated channels**

A Python automation script designed for **IT administrators** and **Workspace managers** to efficiently manage large Slack workspaces by identifying and bulk-deleting inactive or deprecated channels (both private and public).

## 🎯 Business Value

- **Workspace Optimization**: Reduce clutter and improve workspace navigation
- **Storage Management**: Free up valuable storage space in enterprise Slack plans
- **Compliance**: Ensure inactive channels don't contain stale sensitive information
- **User Experience**: Improve channel discoverability for active teams
- **Administrative Efficiency**: Automate manual cleanup tasks that would take hours

## 🚀 Features

- ✅ **Bulk Channel Analysis**: Scan entire workspace for inactive channels
- ✅ **Smart Detection**: Identify channels based on activity thresholds and age
- ✅ **Flexible Filtering**: Support for both private and public channel cleanup
- ✅ **Safe Operations**: Dry-run mode to preview actions before execution
- ✅ **Detailed Logging**: Comprehensive audit trail for compliance requirements
- ✅ **API Integration**: Uses official Slack Web API for reliable operations

## 📋 Prerequisites

- Python 3.8 or higher
- Slack workspace admin privileges
- Slack Bot Token with appropriate scopes:
  - `channels:read`
  - `channels:manage`
  - `groups:read`
  - `groups:write`

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/juliench82/Slack-Channels-Cleanup.git
   cd Slack-Channels-Cleanup
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Slack API Token**
   ```bash
   export SLACK_BOT_TOKEN="xoxb-your-bot-token-here"
   ```

## 🔧 Usage

### Basic Usage
```bash
python slack-cleanup.py
```

### Advanced Options
```bash
# Dry run mode (preview only)
python slack-cleanup.py --dry-run

# Set inactivity threshold (days)
python slack-cleanup.py --inactive-days 90

# Target specific channel types
python slack-cleanup.py --channel-type public
```

## 📊 Sample Output
```
🔍 Scanning Slack workspace...
📈 Found 245 total channels
⚠️  Identified 23 inactive channels (>90 days)
🗂️  Public channels: 15
🔒 Private channels: 8

💾 Estimated storage savings: ~2.3 GB
⏱️  Manual cleanup time saved: ~4.5 hours
```

## 🛡️ Security & Best Practices

- **Token Security**: Store API tokens as environment variables, never in code
- **Permission Validation**: Script validates required permissions before execution
- **Backup Recommendations**: Consider exporting channel data before cleanup
- **Audit Logging**: All actions are logged with timestamps and user context

## 🏢 Enterprise Use Cases

- **Quarterly Workspace Maintenance**: Scheduled cleanup of inactive project channels
- **Compliance Preparation**: Remove channels containing outdated sensitive data
- **Onboarding/Offboarding**: Clean up channels when teams or projects conclude
- **Storage Optimization**: Proactive management of workspace storage limits

## 🤝 Contributing

Contributions are welcome! This tool is designed with enterprise IT needs in mind.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Author

**Julien Chevallier** - Senior IT Manager
- LinkedIn: [@julienc82](https://linkedin.com/in/julienc82)
- GitHub: [@juliench82](https://github.com/juliench82)
- Email: jchevallier82@gmail.com

## 🏆 Related Projects

Part of my **IT Automation & Management** portfolio demonstrating:
- Enterprise workspace management
- Python automation for IT operations
- API integration for business process optimization
- Compliance-focused administrative tools

---

⭐ **Give this repo a star if it helped streamline your Slack workspace management!**